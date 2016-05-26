jQuery('#vol').change(function(){
	console.log("müll");
	var s = document.createElement('style'), 
    r = document.querySelector('#vol'), 
    prefs = ['webkit-slider-runnable', 'moz-range'];

document.body.appendChild(s);

var getTrackStyleStr = function(el, val) {
  var str = '', len = prefs.length;
  
  for(var i = 0; i < len; i++) {
    str += '.js input[type=range]::-' + prefs[i] + 
      '-track{background-size:' + val + '}';
  }
    
  return str;
};

var getValStr = function(el, p) {
  var min = el.min || 0, 
      p = p || el.value, 
      perc = (el.max) ? ~~(100*(p - min)/(el.max - min)) : p, 
      val = perc + '% 100%,100% 100%,100% 100%';
  
  return val;
};

r.addEventListener('input', function() {
  s.textContent = getTrackStyleStr(this, getValStr(this));
}, false);
});