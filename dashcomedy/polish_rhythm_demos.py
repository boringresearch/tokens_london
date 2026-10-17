"""Reviewed short dialogue for the existing demo sequences; do not alter scene speeds."""
import studio
from app import BACKEND, token
LINES={
('office','en'):[ '',"My commute has meetings. Of course it does.","Blue lights. Management has entered the chat.","His promotion moves faster than mine.","Even the hydrant has a permanent position.",'' ],
('nature','zh'):['通勤人开始追捕准时。','摩托先跑了，竞争真大。','消防栓不迁徙，也有领地。','','灯串都亮了，我还没开窍。','','红车占道，领地意识很强。','绕过去，生存全靠走位。','','物种活了，准时灭绝了。'],
('epic','zh'):['远征开始，红绿灯先审批。','','','绿灯放行，英雄也得排队。','','限速四十，野心没有上限。','前车都走了，我还在酝酿。','搅拌车拦路，史诗改期。']}
def main():
 library=studio.demo_library();pending=[]
 for (preset,lang),lines in LINES.items():
  entry=library[preset][lang];raw=studio.read_draft(entry['draft_id'])
  assert len(lines)==len(raw['shots'])
  for shot,line in zip(raw['shots'],lines):
   assert (shot['pace']=='travel')==(line=='')
   shot['narration']=line
  spoken=[s['narration'] for s in raw['shots'] if s['narration']]
  raw['story'].update(setup=spoken[0],escalation=spoken[len(spoken)//2],payoff=spoken[-1])
  d=studio.import_draft(raw);j=studio.submit(d['id'],d,BACKEND,token);pending.append((preset,lang,d,j))
 studio.POOL.shutdown(wait=True)
 for preset,lang,d,j in pending:
  done=studio.read_job(j['id'])
  if done['status']!='done':raise RuntimeError(done['message'])
  library[preset][lang].update(draft_id=d['id'],job_id=j['id'],fingerprint=studio.render_key(d))
  print(preset,lang,done['duration'],flush=True)
 studio.save(studio.STORE/'demo-library.json',library)
if __name__=='__main__':main()
