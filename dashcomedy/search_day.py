import concurrent.futures,json,requests
from pathlib import Path
from app import BACKEND,token
QUERIES=['A person opens a car door and gets into a car','A person working at a desk with a computer in an office','People eating lunch or drinking coffee','People walking into a building entrance','A person handling boxes or working with equipment in a warehouse','A person arrives home and opens a front door']
headers={'Authorization':'Bearer '+token()}
def search(q):
 r=requests.post(BACKEND+'/api/v1/search',headers=headers,json={'query':q,'top_k':5,'llm_top_n':1,'min_similarity':0.15},timeout=90)
 if not r.ok:return {'query':q,'error':r.status_code,'detail':r.text[:100]}
 return {'query':q,'results':r.json().get('results',[])}
rows=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
 for result in pool.map(search,QUERIES):
  rows.append(result);print(result['query'],result.get('error','OK'),flush=True)
  for s in result.get('results',[]):print(s.get('source'),str(s.get('reasoning_content',''))[:450],flush=True)
p=Path(__file__).parent/'day-materials';p.mkdir(exist_ok=True);(p/'searches.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
