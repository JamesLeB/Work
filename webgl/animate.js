

	var lastTime = 0;

	function animate()
	{
		var timeNow = new Date().getTime();
		if(lastTime != 0)
		{
			var elapsed = timeNow - lastTime;
			rCube += (75 * elapsed) / 1000;
		}
		lastTime = timeNow;
	}
