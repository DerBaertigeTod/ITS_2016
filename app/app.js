var PORT = 3000;
var express = require('express');

var app = express();
var http = require('http')
var server = http.createServer(app);
var PythonShell = require('python-shell');
alle_werte ={ slider_1: { l: '180' },  slider_2: { str: '0' }, volume: { v: '20' },  dmx: { r: 255, g: 51, b: 0, w: 0, l: '180', str: '0' } };



app.use(express.static(__dirname + '/public/Mood_is_Music'));
server.listen(PORT);
var io = require('socket.io').listen(server);



//init Websockets
var socket = require('socket.io');
var io = socket.listen(server);
//Eventhandler socket
io.sockets.on("connection",function(socket){
	socket.emit('alle_werte',alle_werte);
	console.log("Someone connected");
	

	socket.on('rgbw_send',function(data){
		alle_werte.dmx = data;
		console.log("sollte rgbw senden : "+alle_werte);
		socket.broadcast.emit('rgbw_dmx',data);
		socket.emit('rgbw_dmx',data);
		socket.broadcast.emit('play_anything');
		});

	socket.on('slider_1',function(data){
		alle_werte.slider_1 = data;
		socket.broadcast.emit('lumi',data);
		});

	socket.on('slider_2',function(data){
		alle_werte.slider_2 = data;
		socket.broadcast.emit('strobe',data);
		});

	socket.on('play_anything',function(){
		socket.broadcast.emit('play_anything');
		});

	socket.on('pause_anything',function(){
		socket.broadcast.emit('pause_anything');
		});

	socket.on('volume',function(data){
		alle_werte.volume = data;
		socket.broadcast.emit('volume',data);
		});
	
	socket.on('lampe',function(data) {
			socket.broadcast.emit('lampe', data);
			console.log("checkbox: " + data.value);
		});

 	socket.on('disconnect', function () {
			console.log("Someone disconnected");
	
		});

 	socket.on('channels',function(channels){
 		socket.broadcast.emit('channels', channels);
 	})

 	socket.on('Interpret',function(data){
 		alle_werte.Interpret = data.Interpret;
 		alle_werte.Song = data.Song;
 		socket.broadcast.emit('Interpret', data);
 	})

 	socket.on('like', function(){
 		socket.broadcast.emit('like');
 	}
 
 	socket.on('dislike', function(){
 		socket.broadcast.emit('dislike');
 	}

setInterval( function(){
		socket.emit('get_channel_values');
	},250);

})



	

//RUN PYTHON scripts:
//	console.log('loading python client');
//	PythonShell.run('../Scripts/python/client.py', function (err) {
 // if (err) throw err;
  
 //}); 
