"""Index all archive pages for the existing locations; download no videos."""
import concurrent.futures
import json
from app import api
from studio import ROOT,save

def collect(location):
    offset=0;rows={};total=None
    for _ in range(100):
        data=api('/videos/explore',params={'scope':'all','limit':100,'offset':offset,'location':location})
        chunks=data.get('chunks',[]);total=data.get('total',0)
        if not chunks:break
        for chunk in chunks:
            for segment in chunk.get('timeline',[]):
                if not segment.get('source'):continue
                rows[segment['source']]={'source':segment['source'],'original_video':chunk['original_video'],'location':location,'camera_id':chunk.get('camera_id'),'caption':segment.get('reasoning_content',''),'objects':segment.get('object_counts','{}'),'start':segment.get('segment_start_sec',0),'end':segment.get('segment_end_sec',5)}
        offset+=len(chunks)
        if offset>=total:break
    else:raise ValueError('Archive pagination did not finish')
    return {'location':location,'total_chunks':total,'segments':list(rows.values())}

if __name__=='__main__':
    old=json.loads((ROOT/'catalog.json').read_text())
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        results=list(pool.map(collect,[g['location'] for g in old]))
    # A partial refresh must not discard clips referenced by saved storyboards.
    previous={g['location']:g for g in old}
    for group in results:
        rows={r['source']:r for r in previous[group['location']]['segments']}
        rows.update({r['source']:r for r in group['segments']})
        group['segments']=list(rows.values())
    save(ROOT/'catalog-before-refresh.json',old)
    save(ROOT/'catalog.json',results)
    print(json.dumps({'clips_before':sum(len(g['segments']) for g in old),'clips_after':sum(len(g['segments']) for g in results),'locations':len(results)}))
