<?php
	$func = $_POST['func'];
	$rtn = array();
	switch($func)
	{
		case 'Start':
			$rtn['mainView'] = file_get_contents('mainViewer.html');
			$rtn['mainControl'] = file_get_contents('mainControl.html');
			break;
		case 'Test':
			$rtn['msg'] = 'Test message';
			break;
	} # end master switch

	echo json_encode($rtn);
?>
