function start()
{
	var p = {func:'start'};
	$.post('ticktock.php',p,function(d){
		tick();
	});
}

function tick()
{
	payload = [];
	var p = {func:'run',payload:payload};
	$.post('ticktock.php',p,function(d){
		var o = $.parseJSON(d);
	});
}
