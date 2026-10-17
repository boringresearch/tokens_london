const fs=require('node:fs'),vm=require('node:vm'),assert=require('node:assert/strict');
const html=fs.readFileSync(__dirname+'/index.html','utf8');
const helpers=html.slice(html.indexOf('function stop(){'),html.indexOf('\nfunction el('));
function slot(visible=false){
 const s={dataset:{},visible,readyState:0,videoWidth:0,loads:0,pause(){},load(){this.loads++},setAttribute(){},addEventListener(name,cb){this[name]=cb}};
 s.classList={toggle(name,value){s.visible=value}};
 Object.defineProperty(s,'src',{set(value){assert.equal(s.visible,false,'must not replace the source of the visible video');this.source=value},get(){return this.source}});
 return s;
}
const a=slot(true),b=slot(false),nodes={};
const ctx=vm.createContext({videoSlots:[a,b],visibleVideo:a,v:b,session:7,beats:[{stream:'/first',director:'Hello',checker:''},{stream:'/next'}],raf:0,watchdog:0,synth:null,currentUtterance:null,cancelAnimationFrame(){},clearTimeout(){},startSpeech(){ctx.narrations++},narrations:0,$:id=>nodes[id]||(nodes[id]={})});
vm.runInContext(helpers,ctx);
ctx.prepareScene(b,0);ctx.prepareScene(b,0);assert.equal(b.loads,1,'reuse buffered scene');
ctx.waitForFrame(b,7,0);assert.equal(a.visible,true,'keep last frame while next clip has no frame');assert.equal(b.visible,false);
b.readyState=3;b.videoWidth=1280;b.loadeddata();
assert.equal(b.visible,true);assert.equal(a.visible,false);assert.equal(a.source,'/next','preload next scene only after old slot is hidden');assert.equal(ctx.narrations,1);
ctx.waitForFrame(a,6,1);assert.equal(b.visible,true,'stale scene callback cannot switch visible video');
console.log('Player checks passed: buffer reuse, last-frame hold, decoded-frame swap, next preload and stale callback protection.');
