import copy,json,os,tempfile,unittest
from pathlib import Path
from unittest.mock import patch,Mock
os.environ.setdefault('WANDB_API_KEY','test')
import studio
class StudioTests(unittest.TestCase):
 def setUp(self):
  self.temp=tempfile.TemporaryDirectory();self.root=Path(self.temp.name);self.patch1=patch.object(studio,'ROOT',self.root);self.patch2=patch.object(studio,'STORE',self.root/'studio');self.patch1.start();self.patch2.start()
  catalog=[{'location':'street','segments':[{'source':'s3://team/a.mp4','caption':'A cyclist stops beside a bicycle.','duration':5,'location':'street'},{'source':'s3://team/b.mp4','caption':'A car drives down a street.','duration':5,'location':'street'}]}]
  (self.root/'catalog.json').write_text(json.dumps(catalog));ids=[a['id'] for a in studio.assets()]
  self.raw={'title':'My trip','brief':'A funny commute','language':'en','target_seconds':15,'shots':[{'asset_id':ids[0],'start':0,'end':5,'duration':5,'chapter':'Ride','narration':'Two wheels.','transition':'cut'},{'asset_id':ids[1],'start':0,'end':5,'duration':5,'chapter':'Drive','narration':'Four wheels.','transition':'dissolve'}]}
 def tearDown(self):self.patch1.stop();self.patch2.stop();self.temp.cleanup()
 def test_unknown_source_and_nonfinite_timing_rejected(self):
  bad=copy.deepcopy(self.raw);bad['shots'][0]['asset_id']='file:///etc/passwd'
  with self.assertRaises(ValueError):studio.validate(bad)
  bad=copy.deepcopy(self.raw);bad['shots'][0]['duration']=float('nan')
  with self.assertRaises(ValueError):studio.validate(bad)
 def test_source_bounds_and_playback_rate(self):
  for key,value in [('end',6),('start',5),('duration',12)]:
   bad=copy.deepcopy(self.raw);bad['shots'][0][key]=value
   with self.assertRaises(ValueError):studio.validate(bad)
 def test_duration_accounts_for_transition(self):
  result=studio.validate(self.raw);self.assertAlmostEqual(result['estimated_seconds'],9.75);self.assertTrue(result['fictional'])
 def test_render_uses_immutable_reviewed_snapshot(self):
  d=studio.import_draft(self.raw)
  with patch.object(studio.POOL,'submit') as submit:
   job=studio.submit(d['id'],self.raw,'http://backend','secret-token')
  self.raw['title']='A later edit'
  snapshot=json.loads((studio.job_path(job['id'])/'edit.json').read_text())
  self.assertEqual(snapshot['title'],'My trip');self.assertNotIn('secret-token',json.dumps(snapshot));self.assertEqual(submit.call_args.args[2]['title'],'My trip')
 def test_html_export_is_self_contained_and_escapes_text(self):
  folder=self.root/'job';folder.mkdir();(folder/'film.mp4').write_bytes(b'demo-video');edit=studio.validate(self.raw);edit['title']='<script>alert(1)</script>'
  studio.export_html(folder,edit);doc=(folder/'demo.html').read_text()
  self.assertIn('data:video/mp4;base64,',doc);self.assertNotIn('<script>alert',doc);self.assertIn('&lt;script&gt;',doc)
 def test_model_draft_requires_review_before_any_render(self):
  response=Mock();response.json.return_value={'choices':[{'message':{'content':json.dumps(self.raw)}}]}
  with patch('studio.requests.post',return_value=response),patch.object(studio.POOL,'submit') as pool:
   result=studio.draft('A funny commute','en',35)
  self.assertTrue((studio.STORE/'drafts'/f'{result["id"]}.json').exists());pool.assert_not_called()
 def test_chinese_brief_ranks_matching_footage_without_download_bonus(self):
  rows=[{'id':str(i),'description':'Trees beside a quiet road.','activity':'street_activity','location':'same','original_video':str(i),'local_file':'cached.mp4'} for i in range(100)]
  rows.append({'id':'driving','description':'Driving a car down the road.','activity':'driving','location':'same','original_video':'car'})
  with patch.object(studio,'assets',return_value=rows):
   chosen=studio.candidate_assets('我想开车的一天',seed=1)
  self.assertEqual(chosen[0]['id'],'driving')
 def test_recently_used_clip_does_not_displace_equivalent_fresh_clip(self):
  rows=[{'id':str(i),'description':'A car driving.','activity':'driving','location':'same','original_video':str(i)} for i in range(100)]
  studio.save(studio.STORE/'drafts'/'previous.json',{'shots':[{'asset_id':'0'}]})
  with patch.object(studio,'assets',return_value=rows):
   chosen=studio.candidate_assets('A car driving',seed=1)
  self.assertNotIn('0',[a['id'] for a in chosen])
if __name__=='__main__':unittest.main()
