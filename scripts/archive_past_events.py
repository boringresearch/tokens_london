#!/usr/bin/env python3
"""Archive public event pages and project details; no login or submissions."""
import concurrent.futures, datetime, html, json, re, time, urllib.request
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'past-events'
BASE = 'https://tokensand.com'

class Content(HTMLParser):
    def __init__(self):
        super().__init__(); self.depth=0; self.skip=0; self.parts=[]; self.links=[]; self.href=None; self.label=[]; self.ld=[]; self.ldbuf=None
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='main': self.depth+=1
        if tag=='script' and a.get('type')=='application/ld+json': self.ldbuf=[]
        if tag in ('script','style'): self.skip+=1
        if not self.depth or self.skip:return
        if tag in ('p','div','section','article','li','h1','h2','h3','h4','br'):self.parts.append('\n')
        if tag=='a':self.href=a.get('href');self.label=[]
    def handle_endtag(self,tag):
        if tag=='script' and self.ldbuf is not None:
            try:self.ld.append(json.loads(''.join(self.ldbuf)))
            except ValueError:pass
            self.ldbuf=None
        if tag in ('script','style'):self.skip=max(0,self.skip-1);return
        if self.depth and not self.skip:
            if tag=='a' and self.href:
                self.links.append({'text':''.join(self.label).strip(),'url':urllib.parse.urljoin(BASE,self.href)});self.href=None
            if tag in ('p','div','section','article','li','h1','h2','h3','h4'):self.parts.append('\n')
        if tag=='main':self.depth=max(0,self.depth-1)
    def handle_data(self,data):
        if self.ldbuf is not None:self.ldbuf.append(data)
        if self.depth and not self.skip:
            self.parts.append(data)
            if self.href:self.label.append(data)
    def result(self):
        text='\n'.join(x.strip() for x in ''.join(self.parts).splitlines() if x.strip())
        return {'text':text,'links':self.links,'structured_data':self.ld}

def get(url):
    for attempt in range(3):
        try:
            req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 (public event archive)'})
            with urllib.request.urlopen(req,timeout=40) as r:return r.read().decode('utf-8')
        except Exception:
            if attempt==2:raise
            time.sleep(attempt+1)

def write_json(path,data):path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
def flight(s):
    stream=''
    for m in re.finditer(r'self\.__next_f\.push\((.*?)\)</script>',s):
        try:d=json.loads(m.group(1))
        except ValueError:continue
        if len(d)>1 and isinstance(d[1],str):stream+=d[1]
    records={}
    wire=stream.encode('utf-8');pos=0
    while pos<len(wire):
        if wire[pos:pos+1]==b'\n':pos+=1;continue
        header=re.match(rb'([0-9a-f]+):',wire[pos:])
        if not header:
            end=wire.find(b'\n',pos)
            if end<0:break
            pos=end+1;continue
        key=header[1].decode();pos+=header.end()
        text_header=re.match(rb'T([0-9a-f]+),',wire[pos:])
        if text_header:
            pos+=text_header.end();size=int(text_header[1],16)
            records[key]=wire[pos:pos+size].decode('utf-8');pos+=size
        else:
            end=wire.find(b'\n',pos)
            if end<0:end=len(wire)
            try:records[key]=json.loads(wire[pos:end])
            except ValueError:pass
            pos=end+1
    def resolve(v,seen=frozenset()):
        if isinstance(v,str) and re.fullmatch(r'\$L?[0-9a-f]+',v) and v[1:].removeprefix('L') in records and v not in seen:
            return resolve(records[v[1:].removeprefix('L')],seen|{v})
        if isinstance(v,list):return [resolve(x,seen) for x in v]
        if isinstance(v,dict):return {k:resolve(x,seen) for k,x in v.items()}
        return v
    return {k:resolve(v) for k,v in records.items()}

def extract(s):
    p=Content();p.feed(s);result=p.result()
    records=flight(s);mains=[];ld=[]
    def walk(v):
        if isinstance(v,list):
            if len(v)>3 and v[0]=='$' and v[1]=='main':mains.append(v)
            for x in v:walk(x)
        elif isinstance(v,dict):
            if '__html' in v:
                try:
                    d=json.loads(v['__html'])
                    if isinstance(d,dict) and d.get('@type')=='SoftwareSourceCode':ld.append(d)
                except (ValueError,TypeError):pass
            for x in v.values():walk(x)
    for v in records.values():walk(v)
    def render(v,links):
        if isinstance(v,str):return v if not v.startswith('$') else ''
        if isinstance(v,list):
            if len(v)>3 and v[0]=='$' and isinstance(v[3],dict):
                tag=v[1];props=v[3]
                if tag in ('script','style'):return ''
                t=render(props.get('children'),links)
                if props.get('href'):links.append({'text':t.strip(),'url':urllib.parse.urljoin(BASE,props['href'])})
                return '\n'+t+'\n' if tag in ('main','div','p','section','article','li','h1','h2','h3','h4') else t
            return ''.join(render(x,links) for x in v)
        return ''
    for main in mains + [v for v in records.values() if isinstance(v,list)]:
        links=[];t=render(main,links);t='\n'.join(x.strip() for x in t.splitlines() if x.strip())
        score=lambda x:(any(marker in x for marker in ('Project description','Review the project','Judging locked')),len(x))
        if score(t)>score(result['text']):result['text']=t;result['links']=links
    if ld:result['structured_data']=list({json.dumps(x,sort_keys=True):x for x in ld}.values())
    return result
def projects_from_html(s):
    for m in re.finditer(r'self\.__next_f\.push\((.*?)\)</script>',s):
        try:d=json.loads(m.group(1))
        except ValueError:continue
        if len(d)<2 or not isinstance(d[1],str):continue
        for hit in re.finditer(r'"projects":\[',d[1]):
            items,_=json.JSONDecoder().raw_decode(d[1][hit.end()-1:])
            if items and isinstance(items[0],dict) and 'slug' in items[0]:
                records=flight(s)
                def resolve(v):
                    if isinstance(v,str) and re.fullmatch(r'\$[0-9a-f]+',v):return records.get(v[1:],v)
                    if isinstance(v,list):return [resolve(x) for x in v]
                    if isinstance(v,dict):return {k:resolve(x) for k,x in v.items()}
                    return v
                return resolve(items)
    raise ValueError('No public project list found')

def archive_project(item):
    event,p=item;slug=p['slug'];folder=OUT/event/'projects';folder.mkdir(parents=True,exist_ok=True)
    url=BASE+'/p/'+slug
    try:
        raw_path=folder/(slug+'.html')
        raw=raw_path.read_text() if raw_path.exists() else get(url);raw_path.write_text(raw)
        data=extract(raw)
        for label,value in [('GitHub 仓库',p.get('repoUrl')),('项目网站',p.get('demoUrl')),('项目截图',p.get('imageUrl')),('演示视频',p.get('metadata',{}).get('hackathonSubmission',{}).get('demoVideoUrl'))]:
            if value and value not in {x['url'] for x in data['links']}:data['links'].append({'text':label,'url':value})
        if len(data['text'])<50:raise ValueError('Detail content not extracted')
        data.update(url=url,retrieved_at=datetime.datetime.now(datetime.timezone.utc).isoformat())
        write_json(folder/(slug+'.json'),data)
        chunks=[f"# {p['title']}",f"原始页面：{url}","所属活动："+event,"说明：以下为公开项目页面内容及作者自述，非独立验证结果；展示顺序不代表名次。","## 页面正文",data['text'],"## 公开链接"]
        seen=set()
        for l in data['links']:
            if l['url'] not in seen:
                chunks.append(f"- [{l['text'] or l['url']}]({l['url']})");seen.add(l['url'])
        for ld in data['structured_data']:
            if ld.get('@type')=='SoftwareSourceCode':
                parts=ld.get('hasPart',[])
                if parts:chunks.append('## 页面结构化补充资料')
                for part in parts:chunks.extend(['### '+part.get('name',''),part.get('description','')])
        (folder/(slug+'.md')).write_text('\n\n'.join(chunks)+'\n')
        return {'event':event,'slug':slug,'title':p['title'],'url':url,'ok':True}
    except Exception as e:return {'event':event,'slug':slug,'url':url,'ok':False,'error':str(e)}

def main():
    OUT.mkdir(exist_ok=True);todo=[];events={}
    for event,name in [('vastsf','旧金山 · 2026-10-02'),('vastnyc','纽约 · 2026-10-09')]:
        folder=OUT/event;folder.mkdir(exist_ok=True)
        for kind,url in [('event',BASE+'/'+event),('gallery',BASE+'/'+event+'/projects')]:
            raw=get(url);(folder/(kind+'.html')).write_text(raw)
            data=extract(raw);data['url']=url;write_json(folder/(kind+'.json'),data)
            (folder/(kind+'.txt')).write_text(url+'\n\n'+data['text'])
            if kind=='gallery':projects=projects_from_html(raw)
        write_json(folder/'project-list.json',projects);events[event]=(name,projects);todo.extend((event,p) for p in projects)
        print(event,len(projects),'projects',flush=True)
    results=[]
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        for i,r in enumerate(pool.map(archive_project,todo),1):
            results.append(r)
            if i%10==0 or not r['ok']:print(i,'/',len(todo),r['slug'],r['ok'],flush=True)
    manifest={'retrieved_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'results':results,'success':sum(r['ok'] for r in results),'failed':sum(not r['ok'] for r in results)}
    write_json(OUT/'manifest.json',manifest)
    index=['# 往期活动完整公开资料归档','抓取日期：2026-10-16。来源：tokensand.com 官方活动页面和公开项目详情。','本归档包含活动说明、两场完整项目列表、每项详情正文、页面结构化技术/运行/经验说明，以及代码仓库和演示链接。项目内容为作者自述，未复现，也不是获奖名单。','网页保存为 HTML，便于核对原文；离线阅读请优先使用 Markdown，原始动态网页不保证离线交互正常。视频、图片和代码仓库本体未下载，链接已保留。','## 抓取结果',f"共 {len(todo)} 条参赛项目记录，成功 {manifest['success']}，失败 {manifest['failed']}。详见 [manifest.json](manifest.json)。"]
    for event,(name,projects) in events.items():
        index.extend(['## '+name,f"共 {len(projects)} 项。[活动原文]({event}/event.txt) · [完整列表数据]({event}/project-list.json)",'| 项目 | 简介 |','| --- | --- |'])
        for p in projects:
            title=p['title'].replace('|','／');summary=(p.get('summary') or '').replace('|','／').replace('\n',' ')
            index.append(f"| [{title}]({event}/projects/{p['slug']}.md) | {summary} |")
    index.extend(['## 更新方式','在项目根目录运行 `python3 scripts/archive_past_events.py` 会更新活动列表、下载缺失的项目页，并重新解析已有网页缓存。生成结果会覆盖对应归档文件。','完整原文和机器可读数据保留于各活动目录；本次未登录任何账号或访问参赛团队的私人运行环境。'])
    text='\n\n'.join(index[:7])+'\n\n'+'\n'.join(index[7:])+'\n'
    text=re.sub(r'\n(## )',r'\n\n\1',text)
    text=re.sub(r'(## [^\n]+)\n(?!\n)',r'\1\n\n',text)
    text=text.replace('project-list.json)\n|','project-list.json)\n\n|')
    (OUT/'README.md').write_text(text)
    print(json.dumps({'success':manifest['success'],'failed':manifest['failed']}),flush=True)
if __name__=='__main__':main()
