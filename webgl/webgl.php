<!DOCTYPE html>
<html>
	<head>
		<!-- LOAD JQUERY --!>
		<script src='jquery/jquery-1.11.1.js'></script>
		<script src='jquery/jquery-ui.js'></script>
		<link  href='jquery/jquery-ui.css' rel='stylesheet'/>

		<!-- LOAD WEBGL TOOLS --!>
		<script type="text/javascript" src="glMatrix.js"></script>
		<script type="text/javascript" src="webgl-utils.js"></script>
		
		<!-- LOAD MY JS CODE --!>
		<script src='utility.js'></script>
		<script src='initBuffers.js'></script>
		<script src='groot.js'></script>
		<script src='cub.js'></script>
		<script src='drawScene.js'></script>
		<script src='docReady.js'></script>
		<!--
		--!>

		<!-- LOAD MY STYLE SHEET --!>
		<link  href='style.css' rel='stylesheet'/>

		<!-- FRAGMENT SHADER --!>
		<script id="shader-fs" type="x-shader/x-fragment">
		    precision mediump float;
			varying vec4 vColor;
		    void main(void)
			{
		        gl_FragColor = vColor;
		    }
		</script>
		
		<!-- VERTEX SHADER --!>
		<script id="shader-vs" type="x-shader/x-vertex">
		    attribute vec3 aVertexPosition;
		    attribute vec4 aVertexColor;
		    uniform mat4 uMVMatrix;
		    uniform mat4 uPMatrix;
			varying vec4 vColor;
		    void main(void)
			{
		        gl_Position = uPMatrix * uMVMatrix * vec4(aVertexPosition, 1.0);
				vColor = aVertexColor;
		    }
		</script>

		<!-- LOAD HTML --!>
		<?php
			#$main = file_get_contents('main.html');
			$main = file_get_contents('temp.html');
		?>

	</head>
	<body>
		<?php echo $main ?>
	</body>
</html>

