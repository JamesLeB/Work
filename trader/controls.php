<?php
	session_start();
	$func = $_POST['func'];
	$rtn = array();
	switch($func)
	{
		case 'getBook':
			#file_put_contents('data/kara.txt','kara is outside');
			$b = file_get_contents('data/book');
			$rtn['book'] = $b;
			break;
		case 'other':
			$rtn['other'] = 'other';
			break;
	}
	echo json_encode($rtn);
?>
