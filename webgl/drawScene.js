
	var zoomLevel = 0;
	var xRotation = 15;
	var yRotation = 15;
	var zRotation = 0;

    function drawScene()
	{
        gl.viewport(0, 0, gl.viewportWidth, gl.viewportHeight);
        gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);

        mat4.perspective(45, gl.viewportWidth / gl.viewportHeight, 0.1, 100.0, pMatrix);
        mat4.identity(mvMatrix);

		var zAdjustment = (-1 * zoomLevel / 10) - 16;
        mat4.translate(mvMatrix, [0.0, 0.0, zAdjustment]);

        mat4.translate(mvMatrix, [ 0.0, 0.0, -40.0]);

		mat4.rotate(mvMatrix, degToRad(xRotation), [1, 0, 0]);
		mat4.rotate(mvMatrix, degToRad(yRotation), [0, 1, 0]);
		mat4.rotate(mvMatrix, degToRad(zRotation), [0, 0, 1]);

		var offset = -8
        mat4.translate(mvMatrix, [offset, 0.0,offset]);

		var total = 5;
		var factor = 4;

		var pos = [0.0, 0.0, 0.0];

		for(i=0;i<total;i++)
		{
			for(j=0;j<total;j++)
			{
				pos = [i*factor, 0.0, j*factor];
				if(i==1 && j==2)
				{
					drawObject(buffers[1],pos,j);
				}
				else
				{
					drawObject(buffers[0],pos,j);
				}
			}
		}
    }

	function drawObject(myObj,pos,rot)
	{

		mvPushMatrix();

        gl.bindBuffer(gl.ARRAY_BUFFER, myObj.grootPos);
        gl.vertexAttribPointer(shaderProgram.vertexPositionAttribute, myObj.grootPos.itemSize, gl.FLOAT, false, 0, 0);
        gl.bindBuffer(gl.ARRAY_BUFFER, myObj.grootCol);
        gl.vertexAttribPointer(shaderProgram.vertexColorAttribute, myObj.grootCol.itemSize, gl.FLOAT, false, 0, 0);
		gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, myObj.grootIndex);

        mat4.translate(mvMatrix,pos);
		mat4.rotate(mvMatrix, degToRad(rot*5), [0, 0, 1]);
        setMatrixUniforms();

        gl.drawElements(gl.TRIANGLES, myBox.grootIndex.numItems, gl.UNSIGNED_SHORT, 0);

		mvPopMatrix();
	}
