<?php
	session_start();
	$func = $_POST['func'];
	$rtn = array();
	switch($func)
	{
		case 'start':
			$_SESSION['clock'] = 1;
			$rtn['clock'] = $_SESSION['clock'];
			break;
		case 'run':
			$_SESSION['clock']++;
			$rtn['clock'] = $_SESSION['clock'];
			break;
	}
	echo json_encode($rtn);
?>
