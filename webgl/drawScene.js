

	var zoomLevel = 0;
	

    function drawScene(myObj)
	{
	
        gl.viewport(0, 0, gl.viewportWidth, gl.viewportHeight);
        gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);

        mat4.perspective(45, gl.viewportWidth / gl.viewportHeight, 0.1, 100.0, pMatrix);
        mat4.identity(mvMatrix);

		var zAdjustment = (-1 * zoomLevel / 10) - 6;
        mat4.translate(mvMatrix, [0.0, 0.0, zAdjustment]);

		drawObject(myObj);

    }

	function drawObject(myObj)
	{

		mvPushMatrix();

        gl.bindBuffer(gl.ARRAY_BUFFER, myObj.grootPos);
        gl.vertexAttribPointer(shaderProgram.vertexPositionAttribute, myObj.grootPos.itemSize, gl.FLOAT, false, 0, 0);
        gl.bindBuffer(gl.ARRAY_BUFFER, myObj.grootCol);
        gl.vertexAttribPointer(shaderProgram.vertexColorAttribute, myObj.grootCol.itemSize, gl.FLOAT, false, 0, 0);
		gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, myObj.grootIndex);

		mat4.rotate(mvMatrix, degToRad(myObj.xCubeRot), [1, 0, 0]);
		mat4.rotate(mvMatrix, degToRad(myObj.yCubeRot), [0, 1, 0]);
		mat4.rotate(mvMatrix, degToRad(myObj.zCubeRot), [0, 0, 1]);
        mat4.translate(mvMatrix, [0.0, 0.0, 0.0]);
        setMatrixUniforms();

        gl.drawElements(gl.TRIANGLES, myBox.grootIndex.numItems, gl.UNSIGNED_SHORT, 0);

		mvPopMatrix();
	}
