import tempfile,unittest
from pathlib import Path
from unittest.mock import patch
import app as m
class AppTests(unittest.TestCase):
    def test_no_upload(self):
        r=m.app.test_client().post('/api/projects'); self.assertEqual(r.status_code,400)
    def test_traversal(self):
        with self.assertRaises(ValueError): m.folder('../config')
    def test_selection_rejects_unknown_duplicate_and_preserves_order(self):
        candidates=[dict(id=i,file=f'input-{i}.mp4',name=str(i),start=0,duration=5,order=i,observation='car',interest=5) for i in range(3)]
        with patch.object(m,'llm',return_value={'clips':[{'id':2,'caption':'last'},{'id':999},{'id':0,'caption':'first'},{'id':2}]}):
            d=m.plan(None,{'style':'funny','language':'English','target':40},candidates)
        self.assertEqual([c['id'] for c in d['clips']],[0,2])
    def test_busy_project_cannot_enqueue_twice(self):
        with tempfile.TemporaryDirectory() as tmp,patch.object(m,'DATA',Path(tmp)):
            jid='a'*32;p=Path(tmp)/jid;p.mkdir();m.save(p,{'status':'working'})
            r=m.app.test_client().post('/api/projects/'+jid+'/remix',json={'instruction':'funny'})
            self.assertEqual(r.status_code,409)
if __name__=='__main__': unittest.main()
