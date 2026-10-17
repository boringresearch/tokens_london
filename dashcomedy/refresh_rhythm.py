"""Rejudge existing demo sequences, render replacements, then atomically publish the library."""
import copy, json, sys, time
import studio
from app import BACKEND, token

def main():
 library=studio.demo_library();replacement=copy.deepcopy(library);pending=[]
 for preset,versions in library.items():
  for lang,entry in versions.items():
   raw=studio.read_draft(entry['draft_id'])
   if '--reuse' in sys.argv:
    for attempt in range(60):
     candidates=[json.loads(p.read_text()) for p in sorted((studio.STORE/'drafts').glob('*.json'),key=lambda p:p.stat().st_mtime,reverse=True)]
     revised=next((d for d in candidates if d.get('title')==raw['title'] and d.get('language')==lang and all(s.get('pace_mode')=='auto' for s in d['shots'])),None)
     if revised:break
     time.sleep(10)
    if not revised:raise RuntimeError('No existing scene-paced draft: '+preset+'/'+lang)
   else:revised=studio.rejudge_scene_rhythm(raw)
   draft=studio.import_draft(revised)
   job=studio.submit(draft['id'],draft,BACKEND,token)
   pending.append((preset,lang,draft,job))
   print('PACING',preset,lang,[(s['pace'],round(s['speed'],2),s['pace_reason'],s['narration']) for s in draft['shots']],flush=True)
 studio.POOL.shutdown(wait=True)
 for preset,lang,draft,job in pending:
  done=studio.read_job(job['id'])
  if done['status']!='done':raise RuntimeError(f'{preset}/{lang}: {done.get("message")}')
  replacement[preset][lang].update(draft_id=draft['id'],job_id=job['id'],fingerprint=studio.render_key(draft))
  print('READY',preset,lang,done['duration'],flush=True)
 studio.save(studio.STORE/'demo-library.json',replacement)
if __name__=='__main__':main()
