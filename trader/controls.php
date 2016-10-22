<?php
	session_start();
	$func = $_POST['func'];
	$rtn = array();
	switch($func)
	{
		case 'getBook':
			$rtn['book'] = 'Load and return book';
			break;
		case 'other':
			$rtn['other'] = 'other';
			break;
	}
	echo json_encode($rtn);
?>
