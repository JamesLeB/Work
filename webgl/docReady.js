
	var buffers
    function webGLStart()
	{
        var canvas = document.getElementById("mainViewer");
        initGL(canvas);
        initShaders();
        buffers = initBuffers();
        gl.clearColor(0.0, 0.0, 0.0, 1.0);
        gl.enable(gl.DEPTH_TEST);
		tick();
    }
	function tick()
	{
		requestAnimFrame(tick);
		drawScene();
		//animate();
	}

	$(document).ready(function()
	{
		var p = {func: 'Start'};
		$.post('action.php',p,function(d){
			var o = $.parseJSON(d);
			$('#v5').html(o.mainView);
			$('#v8').html(o.mainControl);
			webGLStart();
			$('#slider1').slider({
				slide: function(event, ui){
					var val1 = ui.value;
					xRotation = Math.round(val1 * 360 * .01);
				}
			});
			$('#slider2').slider({
				slide: function(event, ui){
					var val1 = ui.value;
					yRotation = Math.round(val1 * 360 * .01);
				}
			});
			$('#main').css('visibility','visible');
		});

		$('#testCall').click(function(){
			var p = {func: 'Test'};
			$.post('action.php',p,function(d){
				var o = $.parseJSON(d);
				$('#v2').html(o.msg);
			});
		});
	});
