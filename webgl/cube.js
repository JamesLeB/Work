

	function primative_cube()
	{
	    var grootPos;
   		var grootCol;
    	var grootIndex;
/*
	Basic cube parameters
	8 points
	6 colors
*/

        grootPos = gl.createBuffer();
        gl.bindBuffer(gl.ARRAY_BUFFER, grootPos);
        var vertices = [
			//Front face
            -1.0, -1.0,  1.0,
             1.0, -1.0,  1.0,
             1.0,  1.0,  1.0,
            -1.0,  1.0,  1.0,
			//Back face
            -1.0, -1.0, -1.0,
            -1.0,  1.0, -1.0,
             1.0,  1.0, -1.0,
             1.0, -1.0, -1.0,
			//Top face
            -1.0,  1.0, -1.0,
            -1.0,  1.0,  1.0,
             1.0,  1.0,  1.0,
             1.0,  1.0, -1.0,
			//Bottom face
            -1.0, -1.0, -1.0,
             1.0, -1.0, -1.0,
             1.0, -1.0,  1.0,
            -1.0, -1.0,  1.0,
			//Right face
             1.0, -1.0, -1.0,
             1.0,  1.0, -1.0,
             1.0,  1.0,  1.0,
             1.0, -1.0,  1.0,
			//Left face
            -1.0, -1.0, -1.0,
            -1.0, -1.0,  1.0,
            -1.0,  1.0,  1.0,
            -1.0,  1.0, -1.0,
        ];
        gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(vertices), gl.STATIC_DRAW);
        grootPos.itemSize = 3;
        grootPos.numItems = 24;

        grootCol = gl.createBuffer();
        gl.bindBuffer(gl.ARRAY_BUFFER, grootCol);

		var c1 = [1.0, 0.7, 0.9, 1.0];
		var c2 = [1.0, 0.7, 0.9, 1.0];
		var c3 = [1.0, 0.0, 0.9, 1.0];
		var c4 = [1.0, 0.0, 0.9, 1.0];
		var c5 = [1.0, 0.3, 0.9, 1.0];
		var c6 = [1.0, 0.3, 0.9, 1.0];

        var colors = [];
		colors.push(c1);
		colors.push(c2);
		colors.push(c3);
		colors.push(c4);
		colors.push(c5);
		colors.push(c6);

		var unpackedColors = [];
		for (var i in colors)
		{
			var color = colors[i];
			for(var j=0; j < 4; j++)
			{
				unpackedColors = unpackedColors.concat(color);
			}
		}

        gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(unpackedColors), gl.STATIC_DRAW);
        grootCol.itemSize = 4;
        grootCol.numItems = 24;

        grootIndex = gl.createBuffer();
        gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, grootIndex);
        indexes = [
			 0,  1,  2,    0,  2,  3,  // Front
			 4,  5,  6,    4,  6,  7,  // Back
			 8,  9, 10,    8, 10, 11,  // Top
			12, 13, 14,   12, 14, 15,  // Bottom
			16, 17, 18,   16, 18, 19,  // Right
			20, 21, 22,   20, 22, 23,  // Left
        ];
        gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, new Uint16Array(indexes), gl.STATIC_DRAW);
        grootIndex.itemSize = 1;
        grootIndex.numItems = 36;

		myBox = {};
	    myBox.grootPos = grootPos;
   		myBox.grootCol = grootCol;
    	myBox.grootIndex = grootIndex;
/*
		myBox.xCubeRot = 15;
		myBox.yCubeRot = 15;
		myBox.zCubeRot = 0;
*/
		return myBox;
    }
