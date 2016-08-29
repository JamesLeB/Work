<script src='jquery/jquery-1.11.1.js'></script>
<script src='jquery/jquery-ui.js'></script>
<link  href='jquery/jquery-ui.css' rel='stylesheet'/>
<script type="text/javascript" src="glMatrix.js"></script>
<script type="text/javascript" src="webgl-utils.js"></script>

<script src='utility.js'></script>
<script src='groot.js'></script>
<script src='drawScene.js'></script>
<script src='docReady.js'></script>

<script id="shader-fs" type="x-shader/x-fragment">

    precision mediump float;

	varying vec4 vColor;

    void main(void)
	{
        gl_FragColor = vColor;
    }

</script>

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


<canvas id="mainViewer" width="500" height="400"></canvas>
<div id='viewerControls'>
	<div>
		<div>
			<div id='slider1' class='slider'></div>
			<div id='slider4' class='slider'></div>
		</div>
		<div>
			<div id='slider2' class='slider'></div>
			<div id='slider5' class='slider'></div>
		</div>
		<div>
			<div id='slider3' class='slider'></div>
			<div id='slider6' class='slider'></div>
		</div>
	</div>
	<div>
		<div>
			<div>X Rot</div>
			<div>0</div>
			<div>Zoom</div>
			<div>0</div>
		</div>
		<div>
			<div>Y Rot</div>
			<div>0</div>
		</div>
		<div>
			<div>Z Rot</div>
			<div>0</div>
		</div>
	</div>
</div>
<style>
	#mainViewer
	{
		border: 5px ridge yellow;
		margin-left: 30px;
		margin-top: 20px;
	}
	#viewerControls
	{
		border: 5px ridge blue;
		float: right;
		height: 300px;
		width:  500px;
		background: lightBlue;
		margin-right: 30px;
		margin-top: 20px;
	}
	#viewerControls > div:nth-child(1) 
	{
		margin-left: 40px;
		margin-top: 20px;
	}
	#viewerControls > div:nth-child(1) > div
	{
		height: 40px;
	}
	#viewerControls > div:nth-child(1) > div > div
	{
		width: 180px;
		float: left;
	}
	#viewerControls > div:nth-child(1) > div > div:nth-child(2)
	{
		margin-left: 40px;
	}
	#viewerControls > div:nth-child(2)
	{
		border: 1px solid black;
		padding: 10px;
		border-radius: 10px;
		box-shadow: 1px 1px 1px 1px;
		width: 400px;
		margin-left: auto;
		margin-right: auto;
	}
	#viewerControls > div:nth-child(2) > div
	{
		height: 35px;
	}
	#viewerControls > div:nth-child(2) > div:nth-child(1)
	{
		margin-top: 15px;
	}
	#viewerControls > div:nth-child(2) > div > div
	{
		float: left;
	}
	#viewerControls > div:nth-child(2) > div > div:nth-child(1)
	{
		width: 60px;
		margin-left: 20px;
	}
	#viewerControls > div:nth-child(2) > div > div:nth-child(2)
	{
		width: 40px;
		text-align: right;
	}
	#viewerControls > div:nth-child(2) > div > div:nth-child(3)
	{
		width: 60px;
		margin-left: 50px;
	}
	#viewerControls > div:nth-child(2) > div > div:nth-child(4)
	{
		width: 40px;
		text-align: right;
	}
</style>
