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
  response=Mock();story={k:'One optimistic commuter meets reality.' for k in ('premise','running_joke','setup','escalation','payoff')};response.json.side_effect=[{'choices':[{'message':{'content':json.dumps(doc)}}]} for doc in (story,self.raw,{'narration':['My bicycle has wheels, unlike my career.','Four wheels, and still no promotion in sight.']})]
  with patch('studio.requests.post',return_value=response),patch.object(studio.POOL,'submit') as pool:
   result=studio.draft('A funny commute','en',35)
  self.assertTrue((studio.STORE/'drafts'/f'{result["id"]}.json').exists());self.assertEqual(result['story'],story);self.assertEqual(result['estimated_seconds'],9.75);pool.assert_not_called()
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
 def test_single_theme_shortlist_keeps_neighboring_footage_together(self):
  rows=[{'id':f'{trip}{i}','source':f'{trip}/segment_{i:03}.mp4','original_video':f'{trip}_chunk_0001.mp4','location':trip,'camera_id':'bike','activity':'cycling'} for trip in ('ride_a','ride_b') for i in range(40)]
  ranked=[dict(rows[20],recent_uses=0),dict(rows[55],recent_uses=0)]
  with patch.object(studio,'assets',return_value=rows),patch.object(studio,'candidate_assets',return_value=ranked):
   chosen=studio.continuous_candidates('A funny bicycle commute')
  self.assertEqual({a['location'] for a in chosen},{'ride_a'})
  indices=[a['sequence_index'] for a in chosen]
  self.assertEqual(indices,list(range(indices[0],indices[0]+len(indices))))
 def test_explicit_speed_controls_duration_and_rejects_invalid_values(self):
  raw=copy.deepcopy(self.raw);raw['shots'][0].update(speed=3,duration=99)
  result=studio.validate(raw)
  self.assertAlmostEqual(result['shots'][0]['duration'],5/3)
  raw['shots'][0]['speed']=.5
  self.assertEqual(studio.validate(raw)['shots'][0]['duration'],10)
  for value in (0,float('nan'),9):
   raw['shots'][0]['speed']=value
   with self.assertRaises(ValueError):studio.validate(raw)
 def test_ten_shots_can_exceed_reference_length_with_mixed_speeds(self):
  raw=copy.deepcopy(self.raw);raw['target_seconds']=35
  raw['shots']=[dict(self.raw['shots'][i%2],speed=.625 if i<6 else 2.5,transition='cut') for i in range(10)]
  result=studio.validate(raw)
  self.assertEqual(len(result['shots']),10)
  self.assertEqual(result['estimated_seconds'],56)
  self.assertEqual([s['duration'] for s in result['shots']],[8]*6+[2]*4)
 def test_dialogue_polish_only_receives_spoken_shots(self):
  raw=copy.deepcopy(self.raw)
  raw['shots']=[dict(self.raw['shots'][i%2],speed=.625 if i<6 else 3,transition='cut',narration='A full joke about my imaginary office promotion.' if i<6 else None) for i in range(10)]
  story={k:'One optimistic commuter meets reality.' for k in ('premise','running_joke','setup','escalation','payoff')}
  dialogue={'narration':['My bicycle has wheels, unlike my office career.']*6}
  with patch.object(studio,'model_json',side_effect=[story,raw,dialogue]) as model:
   result=studio.draft('A funny commute','en',35)
  self.assertEqual(model.call_args.args[1]['expected_lines'],6)
  self.assertEqual(len(result['shots']),10)
  self.assertTrue(result['narration_polished'])
  self.assertTrue(all(not s['narration'] for s in result['shots'][6:]))
  self.assertGreater(result['estimated_seconds'],35)
 def install_demo(self):
  template=studio.import_draft(self.raw);jid='1'*32;folder=studio.job_path(jid);folder.mkdir(parents=True)
  (folder/'film.mp4').write_bytes(b'cached film');(folder/'demo.html').write_text('cached html')
  studio.save(folder/'status.json',{'status':'done','duration':9.75})
  studio.save(studio.STORE/'demo-library.json',{'office':{'en':{'label':'Office satire','draft_id':template['id'],'job_id':jid,'fingerprint':studio.render_key(template)}}})
  return template,jid
 def test_cached_demo_returns_fresh_editable_draft_and_reuses_film(self):
  template,original_job=self.install_demo()
  with patch.object(studio,'model_json') as model:
   draft=studio.demo_draft('office','en','My funny commute')
  model.assert_not_called();self.assertNotEqual(draft['id'],template['id']);self.assertEqual(draft['cache']['kind'],'reviewed_demo')
  auth=Mock()
  with patch.object(studio.POOL,'submit') as pool:job=studio.submit(draft['id'],draft,'http://unused',auth)
  pool.assert_not_called();auth.assert_not_called();self.assertTrue(job['cached']);self.assertNotEqual(job['id'],original_job)
  self.assertEqual((studio.job_path(job['id'])/'film.mp4').read_bytes(),b'cached film')
  snapshot=json.loads((studio.job_path(job['id'])/'edit.json').read_text());self.assertEqual(snapshot['brief'],'My funny commute')
 def test_edits_invalidate_cached_film(self):
  self.install_demo()
  for field,value in [('narration','A different joke.'),('speed',2)]:
   draft=studio.demo_draft('office');draft['shots'][0][field]=value
   with patch.object(studio.POOL,'submit') as pool:job=studio.submit(draft['id'],draft,'http://unused','secret')
   pool.assert_called_once();self.assertEqual(job['status'],'queued')
if __name__=='__main__':unittest.main()
