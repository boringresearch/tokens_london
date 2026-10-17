import concurrent.futures,json,subprocess,requests
from pathlib import Path
from app import BACKEND,token
ROOT=Path(__file__).parent/'day-materials';catalog=json.loads((ROOT/'catalog.json').read_text());by={g['location']:g['segments'] for g in catalog}
# Editorial order, not an assertion of shared identity, place, or capture time.
specs=[('bike','出门骑一段','On two wheels','new_york',0),('bike','出门骑一段','On two wheels','new_york',3),('drive','换成四个轮子','Switching wheels','toronto',14),('drive','换成四个轮子','Switching wheels','toronto',0),('arrive','抵达工作现场','Arriving at work','san_francisco',0),('work','开始干活','On the job','indoor',28),('work','开始干活','On the job','indoor',0),('work','开始干活','On the job','warehouse3',6),('break','出去透口气','A breath of fresh air','san_francisco',14),('break','出去透口气','A breath of fresh air','san_francisco',21),('return','收工，再骑一段','Back on the bike','new_york',42),('return','收工，再骑一段','Back on the bike','new_york',54)]
clips=[]
for i,(chapter,zh,en,loc,index) in enumerate(specs):
 row=dict(by[loc][index]);row.update(id=i,chapter=chapter,chapter_zh=zh,chapter_en=en,file=f'clip-{i:02}.mp4',synthetic=loc in ['indoor','warehouse3']);clips.append(row)
searches=json.loads((ROOT/'searches.json').read_text())
exit_scene=next(r for q in searches for r in q.get('results',[]) if 'rear passenger door open' in r.get('reasoning_content',''))
clips.insert(4,{'source':exit_scene['source'],'original_video':exit_scene.get('original_video',''),'caption':exit_scene['reasoning_content'],'objects':exit_scene.get('object_counts','{}'),'start':0,'end':5,'location':'san_francisco','camera_id':'sf_streets_cam-1','chapter':'arrive','chapter_zh':'下车，去上班','chapter_en':'Out of the car','synthetic':False})
for i,c in enumerate(clips):c.update(id=i,file=f'day-clip-{i:02}.mp4')
headers={'Authorization':'Bearer '+token()}
def download(c):
 p=ROOT/c['file']
 if not p.exists():
  r=requests.get(BACKEND+'/api/v1/videos/stream',params={'source':c['source'],'token':headers['Authorization'][7:]},timeout=90);r.raise_for_status();p.write_bytes(r.content)
 probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','json',str(p)]))
 c['duration']=float(probe['format']['duration'])
 subprocess.run(['ffmpeg','-y','-v','error','-ss','1','-i',str(p),'-frames:v','1','-vf','scale=480:270:force_original_aspect_ratio=decrease,pad=480:270:(ow-iw)/2:(oh-ih)/2',str(ROOT/f"thumb-{c['id']:02}.jpg")],check=True)
 print(c['id'],c['chapter'],c['duration'],c['caption'][:150],flush=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:list(pool.map(download,clips))
(ROOT/'selected.json').write_text(json.dumps(clips,ensure_ascii=False,indent=2))
print('SAVED',len(clips),flush=True)
