"""Prepare reviewed bilingual comedy presets and render them once for instant playback."""
import json
import studio
from app import BACKEND,token

SCRIPTS={
'office':{
'en':('This Commute Could Have Been an Email',[
"I'm definitely on time. My imaginary spreadsheet says so.",
"First, a sidewalk meeting. Naturally, it could've been an email.",
"Blue lights. Even my commute has a surprise management audit.",
"That motorcyclist's moving up. I'm still waiting for my promotion.",
"The hydrant has a permanent position. I'm still on probation.",
"I'm definitely on time. I've just rebranded late as flexible."]),
'zh':('这次通勤，本来可以发封邮件',[
'我今天绝不迟到。我的脑内表格已经批准了。',
'先在路边开个会。很好，又是一个本可以发邮件的会。',
'蓝灯一闪。连通勤都逃不过领导突击检查。',
'摩托车已经升职了。我还在等流程审批。',
'连消防栓都有固定岗位。我居然还在试用期。',
'我没有迟到。我只是把迟到，重新命名为弹性工作。'])},
'nature':{
'en':('The Commuter: An Endangered Schedule',[
'Here we observe the commuter, hunting an increasingly endangered arrival time.',
'The creature displays confidence. Scientists have yet to locate supporting evidence.',
'A brief burst of speed. Evolution calls this being late.',
'It conserves energy by blaming the habitat. A highly adaptive strategy.',
'Its greatest discovery is a wonderfully flexible definition of punctuality.',
'In conclusion, the species survives. The schedule, sadly, does not.']),
'zh':('动物世界：濒危的准时',[
'现在观察一只通勤人，正在追捕濒危物种：准时。',
'它表现得十分自信。科学家暂时没有找到证据。',
'突然加速。在进化论里，这通常叫快迟到了。',
'它通过埋怨环境节省体力。这是一种高级生存策略。',
'经过漫长迁徙，它终于发现：准时的定义可以很灵活。',
'最终，物种活了下来。时间表就没有这么幸运了。'])},
'epic':{
'en':('The Fellowship of the Commute',[
'A thousand legends begin with destiny. Mine begins with a calendar notification.',
'My noble steed has horsepower. My confidence is powered entirely by denial.',
'The road offers many paths. Somehow, all lead to another meeting.',
"I summon ancient courage: the ability to say, 'Sorry, running slightly late.'",
'History will remember this journey. My manager will remember the timestamp.',
'I have not conquered time. I have merely requested an extension.']),
'zh':('通勤远征：迟到之王',[
'传奇始于命运。而我的史诗，始于一条会议提醒。',
'我的坐骑靠马力前进。我的信心，全靠嘴硬。',
'道路通向四面八方。不知为何，终点都是开会。',
'我召唤远古的勇气：不好意思，我可能稍微晚一点。',
'历史会铭记这段旅程。领导只会铭记打卡时间。',
'我没有战胜时间。我只是向命运，申请了延期。'])}}

LABELS={'office':{'en':'Office satire','zh':'打工人吐槽'},'nature':{'en':'Nature documentary','zh':'动物世界'},'epic':{'en':'Epic commute','zh':'史诗通勤'}}

def main():
 library=studio.demo_library();pending=[]
 office=json.loads(studio.media('4d32a5c5cc9e4725981b45e3b6f1da08','edit.json').read_text())
 nature=json.loads(studio.media('9ef11703d9274a07add18cce43f3bacc','edit.json').read_text())
 car=studio.continuous_candidates('driving a car')[:8]
 epic={'shots':[{'asset_id':a['id'],'chapter':'The heroic commute','start':0,'end':min(5,a['duration']),'speed':3 if i in (2,5) else .65,'narration':'' if i in (2,5) else 'placeholder','transition':'cut'} for i,a in enumerate(car)]}
 for key,base in [('office',office),('nature',nature),('epic',epic)]:
  for lang,(title,lines) in SCRIPTS[key].items():
   raw=json.loads(json.dumps(base));raw.update(title=title,language=lang,narration_enabled=True,brief=f'Reviewed {key} comedy demo',logline='One continuous journey. One increasingly ridiculous narrator.' if lang=='en' else '一段连贯旅程，一位越来越离谱的旁白。',target_seconds=35)
   raw['story']={'premise':title,'running_joke':LABELS[key][lang],'setup':lines[0],'escalation':lines[2],'payoff':lines[-1]}
   spoken=[s for s in raw['shots'] if s.get('narration')]
   assert len(spoken)==len(lines)
   for s,line in zip(spoken,lines):s['narration']=line
   # Chinese speech gets slightly more breathing room while silent bridges stay fast.
   if lang=='zh':
    for s in spoken:s['speed']=.6
   d=studio.import_draft(raw);j=studio.submit(d['id'],d,BACKEND,token())
   pending.append((key,lang,d,j))
   print('Preparing',key,lang,j['id'],flush=True)
 studio.POOL.shutdown(wait=True)
 for key,lang,d,j in pending:
  done=studio.read_job(j['id'])
  if done['status']!='done':raise RuntimeError(f'{key}/{lang}: '+done['message'])
  library.setdefault(key,{})[lang]={'label':LABELS[key][lang],'draft_id':d['id'],'job_id':j['id'],'fingerprint':studio.render_key(d)}
  print('Ready',key,lang,done['duration'],flush=True)
 studio.save(studio.STORE/'demo-library.json',library)
if __name__=='__main__':main()
