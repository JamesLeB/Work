function getBook()
{
	payload = [];
	var p = {func:'getBook',payload:payload};
	$.post('controls.php',p,function(d){
		var o = $.parseJSON(d);
		$('#bookView').html(o.book);
	});
}
