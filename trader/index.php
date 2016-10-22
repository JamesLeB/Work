<?php
	$tab1 = file_get_contents('views/tab1.html');
	$tab2 = file_get_contents('views/tab2.html');
?>
<!DOCTYPE html>
<html>
<head>
	<title>Trader</title>

	<script src='jquery.js'></script>
	<script src='jquery/jquery-ui.js'></script>
	<link  href='jquery/jquery-ui.css' rel='stylesheet'/>

	<script src='script/ready.js'></script>
	<script src='script/ticktock.js'></script>
	<script src='script/controls.js'></script>
	<link  href='css/style.css' rel='stylesheet'/>

</head>
<body>
	<div id='wrapper'>
		<!-- HEADER --!>
		<div id='pageHead'>
			<div id='myClock'>0</div>
			<button id='buttonStart'>Start</button>
			<button id='buttonBook'>Book</button>
			<button>Button3</button>
		</div>
		<!-- BODY --!>
		<div>
			<div id='tabs'>
				<ul>
					<li><a href='#tab1'>Tab1</a></li>
					<li><a href='#tab2'>Tab2</a></li>
				</ul>
				<div id='tab1'><?php echo $tab1; ?></div>
				<div id='tab2'><?php echo $tab2; ?></div>
			</div>
		</div>
		<!-- FOOTER --!>
		<div></div>
	</div>
</body>
</html>
