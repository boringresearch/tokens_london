/* Pure timing functions shared by the player and Node tests. */
(function(root){
  const clamp=(x,a,b)=>Math.max(a,Math.min(b,x));
  function speed(beat,tempo=1,enabled=true){
    if(!enabled)return 1;
    const base=Number(beat.speed)||({travel:4,detail:.8,highlight:1}[beat.pace]||1);
    // Keep important moments watchable even when the overall pace increases.
    return clamp(base*(beat.pace==='travel'?tempo:Math.sqrt(tempo)),.75,6);
  }
  function approach(current,target,seconds){
    return current+(target-current)*(1-Math.exp(-Math.max(0,seconds)/.18));
  }
  function duration(beats,tempo=1,enabled=true){
    return beats.reduce((total,b)=>total+(Number(b.duration)||5)/speed(b,tempo,enabled),0);
  }
  const api={speed,approach,duration};
  if(typeof module!=='undefined')module.exports=api;else root.Rhythm=api;
})(typeof window!=='undefined'?window:globalThis);
