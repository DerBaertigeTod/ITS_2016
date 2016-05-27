function initialize(){
	var socket = io.connect();



	
	document.getElemtbyId('checkbox').addEventListener("click", function(){
		var slidervalue = document.getElementById('slider_1').value;
	if (checkbox.checked()){
	socket.emit('lampe',{'values':slidervalue});
	}
	else{
	socket.emit('lampe',{'values':0});
	}
	});



socket.on('get_channel_1',function(channels){
	var data = channels.all[0];
	document.getElementById('channel_l').innerHTML = value;
});
socket.on('get_channel_2',function(channels){
	var data = channels.all[1];
	document.getElementById('channel_2').innerHTML = value;
});

}


