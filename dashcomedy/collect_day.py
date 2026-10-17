"""Read-only corpus discovery for a clearly labelled fictional day montage."""
import concurrent.futures,json
from pathlib import Path
from app import api
ROOT=Path(__file__).parent/'day-materials'; ROOT.mkdir(exist_ok=True)
LOCATIONS=['new_york','toronto','indoor','warehouse3','san_francisco','neighborhood','nashville']
def collect(location):
    d=api('/videos/explore',params={'scope':'all','limit':10,'offset':0,'location':location})
    rows=[]
    for chunk in d.get('chunks',[]):
        for seg in chunk.get('timeline',[]):
            if not seg.get('source'):continue
            rows.append({'source':seg['source'],'original_video':chunk['original_video'],'location':location,'camera_id':chunk.get('camera_id'),'caption':seg.get('reasoning_content',''),'objects':seg.get('object_counts','{}'),'start':seg.get('segment_start_sec',0),'end':seg.get('segment_end_sec',5)})
    return {'location':location,'total_chunks':d.get('total'),'segments':rows}
results=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
    jobs={pool.submit(collect,loc):loc for loc in LOCATIONS}
    for future in concurrent.futures.as_completed(jobs):
        try:
            result=future.result();results.append(result);print(result['location'],len(result['segments']),flush=True)
        except Exception as e:print(jobs[future],type(e).__name__,flush=True)
(ROOT/'catalog.json').write_text(json.dumps(results,ensure_ascii=False,indent=2))
for result in results:
    print('\nLOCATION',result['location'])
    for row in result['segments'][::max(1,len(result['segments'])//8)][:8]:print(row['source'].split('/')[-1],row['caption'][:550])
