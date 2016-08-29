
	function tick()
	{
		requestAnimFrame(tick);
		drawScene(myBox);
		//animate();
	}

	var myBox;

    function webGLStart()
	{
        var canvas = document.getElementById("mainViewer");
        initGL(canvas);
        initShaders();
        myBox = initBuffers();
        gl.clearColor(0.0, 0.0, 0.0, 1.0);
        gl.enable(gl.DEPTH_TEST);
		tick();
    }

	$(document).ready(function()
	{
		webGLStart();
		$('#slider1').slider({
			slide: function(event, ui){
				var val1 = ui.value;
				myBox.xCubeRot = Math.round(val1 * 360 * .01);
				$('#viewerControls > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)').html(myBox.xCubeRot);
			}
		});
		$('#slider2').slider({
			slide: function(event, ui){
				var val1 = ui.value;
				myBox.yCubeRot = Math.round(val1 * 360 * .01);
				$('#viewerControls > div:nth-child(2) > div:nth-child(2) > div:nth-child(2)').html(myBox.yCubeRot);
			}
		});
		$('#slider3').slider({
			slide: function(event, ui){
				var val1 = ui.value;
				myBox.zCubeRot = Math.round(val1 * 360 * .01);
				$('#viewerControls > div:nth-child(2) > div:nth-child(3) > div:nth-child(2)').html(myBox.zCubeRot);
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
