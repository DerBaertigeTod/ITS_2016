function initialize(){
	// Initialisiert socket.io
	var socket = io.connect();
	
	// set event handler for checkbox click
	var checkbox = document.getElementById("checkbox");
	function clickHandler(){
		if (this.checked){
			socket.emit("checkbox", {"value": 1});
		}
		else{
			socket.emit("checkbox", {"value": 0});
		}
		console.log(this.checked);
	}
	checkbox.addEventListener("click", clickHandler);
	
	// set event handler that dispatches incoming  messages
	function onCheckboxChanged(data){
		if (data.value == 1){
			checkbox.checked = true;
		}
		else {
			checkbox.checked = false;
		}
	}
	socket.on("checkbox",onCheckboxChanged);
}