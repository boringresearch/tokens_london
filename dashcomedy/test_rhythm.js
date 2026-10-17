const assert=require('node:assert/strict');const R=require('./rhythm');
const beats=[{pace:'travel',speed:4,duration:5},{pace:'highlight',speed:1,duration:5},{pace:'detail',speed:.8,duration:5}];
assert.equal(R.duration(beats,1,false),15);
assert.equal(R.duration(beats),12.5);
assert.equal(R.speed(beats[0],1.5),6);
assert.equal(R.speed(beats[2],.6),.75);
assert.ok(R.duration(beats,1.5)<R.duration(beats,.6));
let r=4;for(let i=0;i<60;i++){const n=R.approach(r,1,1/60);assert.ok(n<=r&&n>=1);r=n}assert.ok(r<1.02);
console.log('Speed limits, timing, normal playback and smooth ramps passed.');
