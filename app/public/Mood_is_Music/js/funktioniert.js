function initialize(){
	socket = io.connect();
	var counter = 0;
	var counter_d = 0;

//Sendet RGBW Werte für Rot + Lumi-/Strobe-Slider Werte an Node, wenn auf Red-Button gedrückt wird
document.getElementById('red').addEventListener("click", function($){
	socket.emit('rgbw_send', {'r':255, 'g':0, 'b':0, 'w':0, 'l':document.getElementById('slider_1').value, 'str':document.getElementById('slider_2').value});
	console.log("Red on");
});

//Sendet RGBW Werte für Grün + Lumi-/Strobe-Slider Werte an Node, wenn auf Green-Button gedrückt wird
document.getElementById('green').addEventListener("click", function($){
	socket.emit('rgbw_send', {'r':0, 'g':255, 'b':0, 'w':0, 'l':document.getElementById('slider_1').value, 'str':document.getElementById('slider_2').value});
	console.log("Green on");
});

//Sendet RGBW Werte für Blau + Lumi-/Strobe-Slider Werte an Node, wenn auf Blue-Button gedrückt wird
document.getElementById('blue').addEventListener("click", function($){
	socket.emit('rgbw_send', {'r':0, 'g':0, 'b':255, 'w':0, 'l':document.getElementById('slider_1').value, 'str':document.getElementById('slider_2').value});
	console.log("Blue on");
});

//Sendet RGBW Werte für Weiß + Lumi-/Strobe-Slider Werte an Node, wenn auf White-Button gedrückt wird
document.getElementById('white').addEventListener("click", function($){
	socket.emit('rgbw_send', {'r':0, 'g':0, 'b':0, 'w':255, 'l':document.getElementById('slider_1').value, 'str':document.getElementById('slider_2').value});
	console.log("White on");
});

//Luminance Slider: Neben Slider wird Wert angezeigt und Wert wird an Node gesendet
document.getElementById('slider_1').addEventListener("change", function($){
	document.getElementById('slider_1_value').innerHTML=this.value;
	socket.emit('slider_1', {'l': document.getElementById('slider_1').value});
	console.log(this.value);
});

//Stroboscope Slider: Neben Slider wird Wert angezeigt und Wert wird an Node gesendet
document.getElementById('slider_2').addEventListener("change", function($){
	document.getElementById('slider_2_value').innerHTML=this.value;
		socket.emit('slider_2', {'str': document.getElementById('slider_2').value});
	console.log(this.value);
});

//Volume Slider: Neben Slider wird Wert angezeigt und Wert wird an Node gesendet
document.getElementById('slider_3').addEventListener("input", function($){
	document.getElementById('slider_3_value').innerHTML=this.value;
	socket.emit('volume', {'v': document.getElementById('slider_3').value});
	console.log(this.value);
});

//Bei jedem Klicken auf den Like-Button wird +1 gezählt und Wert neben dem Button angezeigt 
document.getElementById('like').addEventListener("click", function($){
	counter++;
	document.getElementById('like_count').innerHTML= counter;
});

//Bei jedem Klicken auf den Dislike-Button wird +1 gezählt und Wert neben dem Button angezeigt
document.getElementById('dislike').addEventListener("click", function($){
	counter_d++;
	document.getElementById('dislike_count').innerHTML= counter_d;
});

//Musik wird beim Betätigen des Play-Buttons von Vorne abgespielt
document.getElementById('play').addEventListener("click", function($){
	socket.emit('play_anything');
	console.log("play music");
});

//Musik wir beim BEtätigen des Pause-Button pausiert
document.getElementById('pause').addEventListener("click", function($){
	socket.emit('pause_anything');
	console.log("pause music");
});

socket.on('lumi',function(data){
document.getElementById('slider_1').value =data.l;
document.getElementById('slider_1_value').innerHTML =data.l;

});

socket.on('strobe',function(data){
document.getElementById('slider_2').value =data.str;
document.getElementById('slider_2_value').innerHTML =data.str;


});

socket.on('volume',function(data){
document.getElementById('slider_3').value =data.v;
document.getElementById('slider_3_value').innerHTML =data.v;


});


socket.on('alle_werte',function(alles){
console.log(alles);
document.getElementById('slider_1').value =alles.slider_1.l;
document.getElementById('slider_2').value =alles.slider_2.str;
document.getElementById('slider_3').value =alles.volume.v;

});

socket.on('rgbw_dmx',function(dmx){
console.log("getting dmx " +dmx);
color ='rgb('+dmx.r+','+dmx.g+','+dmx.b+')'
	console.log(color);
   document.body.style.backgroundColor = color;

});

$('.marquee').marquee();

}

//Zuletzt gedrückter Farb-Button bekommt einen gelben Rand
function activestate(id){
	jQuery('.colorbutton').each(function(obj){
		jQuery(this).removeClass('active');
			jQuery('#'+id).addClass("active");

});
};

function clickColor(hex, seltop, selleft, html5) {
    	farben=hexToRgb(hex);
	console.log('R: ' +farben.r);

	console.log('G: ' +farben.g);

	console.log('B: ' +farben.b);

	socket.emit('rgbw_send', {'r': farben.r, 'g': farben.g, 'b': farben.b, 'w': 0, 'l':document.getElementById('slider_1').value, 'str':document.getElementById('slider_2').value});
    
	
    if ((seltop+200)>-1 && selleft>-1) {
        document.getElementById("selectedhexagon").style.top=seltop + "px";
        document.getElementById("selectedhexagon").style.left=selleft + "px";
        document.getElementById("selectedhexagon").style.visibility="visible";
	} else {
        document.getElementById("divpreview").style.backgroundColor = str(hex);
        document.getElementById("selectedhexagon").style.visibility = "hidden";
	}
  
  
}
function hexToRgb(hex) {
    var result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
    return result ? {
        r: parseInt(result[1], 16),
        g: parseInt(result[2], 16),
        b: parseInt(result[3], 16)
    } : null;
}