"""Render an editorial second cut with continuous narration and source ambience."""
import json,subprocess,wave
from array import array
from pathlib import Path
ROOT=Path(__file__).parent/'day-materials'
PLAN=json.loads((ROOT/'day-v2-plan.json').read_text())
clips={c['id']:c for c in json.loads((ROOT/'selected.json').read_text())};clips[13]=json.loads((ROOT/'connector.json').read_text())
OUT=ROOT/'v2';OUT.mkdir(exist_ok=True)
def run(args):
 r=subprocess.run(args,capture_output=True,text=True,timeout=300)
 if r.returncode:raise RuntimeError(r.stderr[-2500:])
 return r.stdout
def probe(path):return json.loads(run(['ffprobe','-v','error','-show_format','-show_streams','-of','json',str(path)]))
def ts(t):return f'{int(t)//3600}:{int(t)//60%60:02}:{int(t)%60:02}.{int(t*100)%100:02}'
def escape(s):return s.replace('\\','').replace('{','').replace('}','').replace('\n',' ')
def wrap(s,width):
 parts=[]
 while len(s)>width:
  split=s.rfind(' ',0,width+1) if width>30 else width
  if split<8:split=width
  parts.append(s[:split]);s=s[split:].lstrip()
 return '\\N'.join(parts+[s])
shots=[]
for i,shot in enumerate(PLAN['shots']):
 source=ROOT/clips[shot['clip']]['file'];duration=shot['duration'];speed=(shot['end']-shot['start'])/duration
 if duration<=0 or shot['start']<0 or shot['end']>float(probe(source)['format']['duration'])+.01:raise ValueError('Invalid shot timing')
 audio=any(s['codec_type']=='audio' for s in probe(source)['streams'])
 dest=OUT/f'shot-{i}.mp4'
 args=['ffmpeg','-y','-v','error','-ss',str(shot['start']),'-t',str(shot['end']-shot['start']),'-i',str(source)]
 if not audio:args+=['-f','lavfi','-i','anullsrc=r=48000:cl=stereo']
 vf=f'setpts=(PTS-STARTPTS)/{speed},scale=1280:720:force_original_aspect_ratio=decrease,pad=1280:720:(ow-iw)/2:(oh-ih)/2,setsar=1,tpad=stop_mode=clone:stop_duration=1'
 af=f'aresample=48000,atempo={speed},apad,atrim=end_sample={round(duration*48000)},asetpts=N/SR/TB,volume=0.16,afade=t=in:d=0.05,afade=t=out:st={duration-.05}:d=0.05'
 args+=['-map','0:v:0','-map','0:a:0' if audio else '1:a:0','-vf',vf,'-af',af,'-t',str(duration),'-r','24','-c:v','libx264','-preset','veryfast','-crf','22','-pix_fmt','yuv420p','-c:a','aac','-ar','48000','-ac','2',str(dest)]
 run(args);shots.append(dest);print('Shot',i,'speed',round(speed,2),flush=True)
groups=[]
for name,indices in [('real-before',range(6)),('imagination',[6]),('real-after',[7,8])]:
 listing=OUT/f'{name}.txt';listing.write_text(''.join(f"file '{shots[i].resolve()}'\n" for i in indices))
 dest=OUT/f'{name}.mp4';run(['ffmpeg','-y','-v','error','-f','concat','-safe','0','-i',str(listing),'-c','copy',str(dest)]);groups.append(dest)
for lang in ['zh','en']:
 timings=[];sample_rate=48000;channels=2
 mixed=array('i',[0])*(35*sample_rate*channels)
 for i,cue in enumerate(PLAN['narration']):
  voice=ROOT/f'voice-v2-{lang}-{i}.aiff';length=float(probe(voice)['format']['duration']);window=cue['until']-cue['at']-.1;factor=max(1,length/window)
  if factor>1.6:raise ValueError('Narration too long for its scene')
  maximum=round(window*sample_rate)
  af=f'atempo={factor},loudnorm=I=-17:TP=-2:LRA=7,aresample=48000,atrim=end_sample={maximum},asetpts=N/SR/TB'
  result=subprocess.run(['ffmpeg','-v','error','-i',str(voice),'-af',af,'-t',str(window),'-f','s16le','-ac','2','-ar','48000','pipe:1'],capture_output=True,timeout=30)
  if result.returncode:raise RuntimeError(result.stderr.decode()[-1000:])
  if len(result.stdout)>maximum*channels*2+4:raise ValueError('Unexpected narration size')
  samples=array('h');samples.frombytes(result.stdout);offset=round(cue['at']*sample_rate)*channels
  for j,value in enumerate(samples):
   if offset+j<len(mixed):mixed[offset+j]+=value
  timings.append({'at':cue['at'],'end':cue['at']+len(samples)/(sample_rate*channels),'text':cue[lang]})
 pcm=array('h',(max(-32768,min(32767,x)) for x in mixed))
 voice_track=OUT/f'voice-{lang}.wav'
 with wave.open(str(voice_track),'wb') as out:
  out.setnchannels(channels);out.setsampwidth(2);out.setframerate(sample_rate);out.writeframes(pcm.tobytes())
 ass=OUT/f'captions-{lang}.ass'
 header='[Script Info]\nScriptType: v4.00+\nPlayResX: 1280\nPlayResY: 720\n[V4+ Styles]\nFormat: Name,Fontname,Fontsize,PrimaryColour,SecondaryColour,OutlineColour,BackColour,Bold,Italic,Underline,StrikeOut,ScaleX,ScaleY,Spacing,Angle,BorderStyle,Outline,Shadow,Alignment,MarginL,MarginR,MarginV,Encoding\n'
 header+='Style: Caption,Noto Sans CJK SC,39,&H00FFFFFF,&H00FFFFFF,&H00202020,&H90000000,1,0,0,0,100,100,0,0,3,2,0,2,70,70,45,1\nStyle: Label,Noto Sans CJK SC,18,&H00D5F582,&H00FFFFFF,&H00202020,&H90000000,0,0,0,0,100,100,0,0,3,1,0,7,25,25,20,1\nStyle: Chapter,Noto Sans CJK SC,25,&H00FFFFFF,&H00FFFFFF,&H00202020,&H90000000,1,0,0,0,100,100,0,0,3,1,0,7,25,25,52,1\n[Events]\nFormat: Layer,Start,End,Style,Name,MarginL,MarginR,MarginV,Effect,Text\n'
 notice='虚构日记 · 多来源素材 · 工作片段为仿真' if lang=='zh' else 'FICTIONAL DIARY · MULTIPLE SOURCES · SIMULATED WORK'
 header+=f'Dialogue: 0,0:00:00.00,0:00:35.00,Label,,0,0,0,,{notice}\n'
 for t in timings:header+=f'Dialogue: 0,{ts(t["at"])},{ts(min(35,t["end"]+.3))},Caption,,0,0,0,,{wrap(escape(t["text"]),25 if lang=="zh" else 48)}\n'
 chapters=[(0,6.5,'出发｜今天争取准时收工','The plan: finish on time'),(6.5,12.5,'换乘｜让四个轮子接力','An engine upgrade'),(12.5,18.7,'抵达｜打工模式启动','Employee mode: on'),(18.7,24.35,'脑内预演｜仿真工作画面','In my head: a simulated work rehearsal'),(24.35,35,'回到现实｜这次，不赶了','Back to reality. No rush.')]
 for a,b,zh,en in chapters:header+=f'Dialogue: 0,{ts(a)},{ts(b)},Chapter,,0,0,0,,{escape(zh if lang=="zh" else en)}\n'
 ass.write_text(header)
 fc='[0:v]settb=AVTB,setpts=PTS-STARTPTS[a];[1:v]settb=AVTB,setpts=PTS-STARTPTS[b];[2:v]settb=AVTB,setpts=PTS-STARTPTS[c];[a][b]xfade=transition=dissolve:duration=0.3:offset=18.7[ab];[ab][c]xfade=transition=dissolve:duration=0.3:offset=24.2,'+f'subtitles={ass},format=yuv420p[video];[0:a][1:a]acrossfade=d=0.3[abg];[abg][2:a]acrossfade=d=0.3[ambient];[ambient][3:a]amix=inputs=2:duration=longest:normalize=0,alimiter=limit=0.95[audio]'
 dest=ROOT/f'my-day-v2-{lang}.mp4'
 run(['ffmpeg','-y','-v','error','-filter_complex_threads','1','-i',str(groups[0]),'-i',str(groups[1]),'-i',str(groups[2]),'-i',str(voice_track),'-filter_complex',fc,'-map','[video]','-map','[audio]','-t','35','-r','24','-c:v','libx264','-preset','veryfast','-crf','22','-c:a','aac','-ar','48000','-ac','2','-movflags','+faststart',str(dest)])
 info=probe(dest);actual=float(info['format']['duration']);assert 34.9<=actual<=35.2
 (OUT/f'edit-{lang}.json').write_text(json.dumps({'title':PLAN['title_'+lang],'fictional':True,'plan':PLAN,'narration_timing':timings,'rendered_duration':actual,'source_provenance':[clips[s['clip']] for s in PLAN['shots']]},ensure_ascii=False,indent=2))
 print('FINISHED',lang,actual,flush=True)
