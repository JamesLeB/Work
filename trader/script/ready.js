
$(document).ready(function(){
	//alert('Document Ready');
	$('#tabs').tabs({active:0});
	$('#buttonStart').click(function(){start();});
	$('#buttonBook').click(function(){getBook();});
});
