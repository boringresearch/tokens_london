"""Read existing team footage; create a clearly labelled demo without ingesting anything."""
import json,os,uuid,requests
from app import DATA,save,work,probe,ROOT
base=os.environ['INGRESS_URL'].rstrip('/')
r=requests.post(base+'/api/v1/auth/login',json={'username':os.environ['USERNAME'],'password':os.environ['PASSWORD']},timeout=30);r.raise_for_status()
token=r.json()['access_token']; headers={'Authorization':'Bearer '+token}
r=requests.get(base+'/api/v1/videos/explore',params={'scope':'all','limit':3,'offset':0,'location':'new_york'},headers=headers,timeout=60);r.raise_for_status()
chunks=r.json()['chunks']; jid=uuid.uuid4().hex;p=DATA/jid;p.mkdir();items=[]
for i,c in enumerate(chunks):
    source=c['preview_source']; path=p/f'input-{i}.mp4'
    r=requests.get(base+'/api/v1/videos/stream',params={'source':source,'token':token},timeout=90);r.raise_for_status();path.write_bytes(r.content)
    items.append({'file':path.name,'name':f'NYC ride — moment {i+1}.mp4','duration':probe(path)})
save(p,{'id':jid,'status':'working','message':'Analyzing real demo footage','progress':2,'files':items,'style':'Dry observational comedy about an urban bike ride','language':'English','target':24,'narration':True,'instruction':'Make this a funny urban cycling diary. This is demo footage, do not imply it belongs to the viewer.','version':0,'demo':True})
(ROOT/'static'/'demo.json').write_text(json.dumps({'id':jid}))
print('DEMO',jid,flush=True);work(jid)
d=json.loads((p/'state.json').read_text());print(json.dumps({k:d.get(k) for k in ['id','status','message','output','plan']},ensure_ascii=False),flush=True)
