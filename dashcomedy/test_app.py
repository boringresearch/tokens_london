import os,unittest,json,tempfile
from pathlib import Path
os.environ.setdefault('INGRESS_URL','http://unused')
os.environ.setdefault('WANDB_API_KEY','unused')
from app import build_rhythm, generate
from unittest.mock import patch,Mock
class RhythmTests(unittest.TestCase):
    def setUp(self):
        self.segs=[dict(source='s3://bucket/'+str(i),caption='a cyclist',objects={},duration=5,chunk='ride.mp4',seg=i) for i in range(12)]
    def test_bridges_dedup_order_and_bounds(self):
        d=build_rhythm({'beats':[{'i':8,'pace':'detail'},{'i':3},{'i':3},{'i':999},{'i':'oops'}]},self.segs)
        self.assertEqual([b['i'] for b in d['beats']],[1,2,3,6,7,8])
        self.assertEqual([b['speed'] for b in d['beats']],[4,4,1,4,4,.8])
        self.assertTrue(d['beats'][3]['cut_before'])
        self.assertFalse(d['beats'][1]['cut_before'])
        self.assertEqual(d['beats'][0]['director'],'')
    def test_no_fabricated_sources(self):
        d=build_rhythm({'beats':[{'i':0,'stream':'http://evil','source':'fake'}]},self.segs)
        self.assertEqual(d['beats'][0]['source'],'s3://bucket/0')
    def test_no_valid_highlights(self):
        with self.assertRaises(ValueError):build_rhythm({'beats':[{'i':-1}]},self.segs)
    def test_english_generation_uses_english_prompt_and_bridge_labels(self):
        response=Mock()
        response.json.return_value={'choices':[{'message':{'content':'{"title":"Office Safari","beats":[{"i":3,"director":"Even the bus has better career direction."}]}'}}]}
        with patch('app.journey_segments',return_value=self.segs), patch('app.requests.post',return_value=response) as post:
            result=generate('trip','nature','Keep the bus','en')
        prompt=post.call_args.kwargs['json']['messages'][0]['content']
        self.assertIn('English',prompt)
        self.assertIn('Keep the bus',prompt)
        self.assertEqual(result['language'],'en')
        self.assertEqual(result['beats'][0]['reason'],'Fast-forward the real approach to the next highlight')
        self.assertEqual(result['title'],'Office Safari')
    def test_chinese_remains_default(self):
        result=build_rhythm({'beats':[{'i':2}]},self.segs)
        self.assertEqual(result['language'],'zh')
        self.assertIn('快进',result['beats'][0]['reason'])
    def test_day_demo_keeps_fictional_notice_without_new_model_call(self):
        with tempfile.TemporaryDirectory() as temp:
            story={'title':'A fictional day','language':'en','fictional':True,'notice':'Different sources','beats':[{'chapter':'bike'},{'chapter':'work','synthetic':True}]}
            (Path(temp)/'story-en.json').write_text(json.dumps(story))
            with patch('app.DAY_ROOT',Path(temp)),patch('app.requests.post') as post:
                result=generate('my-day-demo','worker',language='en')
            self.assertTrue(result['fictional'])
            self.assertEqual(result['notice'],'Different sources')
            self.assertTrue(result['beats'][1]['synthetic'])
            post.assert_not_called()
if __name__=='__main__':unittest.main()
