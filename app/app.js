var PORT = 3000;
var express = require('express');
 
var app = express();
var http = require('http')
var server = http.createServer(app);
var PythonShell = require('python-shell');




app.use(express.static(__dirname + '/public'));
server.listen(PORT);
var io = require('socket.io').listen(server);




//init Websockets
var socket = require('socket.io');
var io = socket.listen(server);
//Eventhandler socket
io.sockets.on("connection",function(socket){
	console.log("Someone connected");
	

	socket.on('slider_1',function(data){
		value= data.slidervalue;
		socket.broadcast.emit('broadcast',data);

		});

	
	socket.on('checkbox',function(data) {
			socket.broadcast.emit("checkbox", data);
			console.log("checkbox: " + data.value);
		});

 	socket.on('disconnect', function () {
			console.log("Someone disconnected");
	
		});


 })

setInterval( function(){
		socket.emit('get_channel_values');
	},1500);


	

//RUN PYTHON scripts:
console.log('loading python client');
PythonShell.run('../Scripts/python/client.py', function (err) {
  if (err) throw err;
  
}); 