var PORT = 3000;
var express = require('express');
 
var app = express();
var http = require('http')
var server = http.createServer(app);
var PythonShell = require('python-shell');

//RUN PYTHON scripts:
console.log('loading python client');
PythonShell.run('../scripts/python/client.py', function (err) {
  if (err) throw err;
  
});


app.use(express.static(__dirname + '/public'));
server.listen(PORT);

var io = require('socket.io').listen(server);
io.sockets.on('connection', function (socket) {
	socket.on('checkbox',function(data) {
		socket.broadcast.emit("checkbox", data);
		console.log("checkbox: " + data.value);
	});

	socket.on('disconnect', function () {
		console.log("Someone disconnected");
	});
});
 