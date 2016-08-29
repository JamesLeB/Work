
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
		webGLStart();
		$('#slider1').slider({
			slide: function(event, ui){
				var val1 = ui.value;
				xRotation = Math.round(val1 * 360 * .01);
				$('#viewerControls > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)').html(xRotation);
			}
		});
		$('#slider2').slider({
			slide: function(event, ui){
				var val1 = ui.value;
				yRotation = Math.round(val1 * 360 * .01);
				$('#viewerControls > div:nth-child(2) > div:nth-child(2) > div:nth-child(2)').html(yRotation);
			}
		});
		$('#slider3').slider({
			slide: function(event, ui){
				var val1 = ui.value;
				zRotation = Math.round(val1 * 360 * .01);
				$('#viewerControls > div:nth-child(2) > div:nth-child(3) > div:nth-child(2)').html(zRotation);
			}
		});
		$('#slider4').slider({
			slide: function(event, ui){
				var val1 = ui.value;
				zoomLevel = val1;
				$('#viewerControls > div:nth-child(2) > div:nth-child(1) > div:nth-child(4)').html(zoomLevel);
			}
		});
		$('#slider5').slider({});
		$('#slider6').slider({});
	});
