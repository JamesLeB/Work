function start()
{
	var p = {func:'start'};
	$.post('ticktock.php',p,function(d){
		var o = $.parseJSON(d);
		$('#myClock').html(o.clock);
		tick();
	});
}

function tick()
{
	payload = [];
	var p = {func:'run',payload:payload};
	$.post('ticktock.php',p,function(d){
		var o = $.parseJSON(d);
		$('#myClock').html(o.clock);
		tick();
	});
}
