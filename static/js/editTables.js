function activateSliders() {


		var rangeTableHeight = document.getElementById("rangeTableHeight");
		var outputRangeTableHeight = document.getElementById("tableHeight");
		outputRangeTableHeight.innerHTML = rangeTableHeight.value;

		rangeTableHeight.oninput = function() {
			if (currentTable) {
		  		if (pureNumber(currentTable.style.top) + (+this.value) <=100) {
		  			currentTable.style.height = this.value +"%";
		  		} else {
		  			currentTable.style.height = 100 - pureNumber(currentTable.style.top) +"%";
		  		}
		  		currentTableData.height = currentTable.style.height;
		  		currentTableData.pos_Y = (pureNumber(currentTable.style.top) + pureNumber(currentTable.style.height)/2) +"%";	
		  		outputPosY.innerHTML = (pureNumber(currentTable.style.top) + pureNumber(currentTable.style.height)/2) +"%";
		  		outputRangeTableHeight.innerHTML = currentTable.style.height;
		  	}
		  	
		}

		var rangeTableWidth = document.getElementById("rangeTableWidth");
		var outputRangeTableWidth = document.getElementById("tableWidth");
		outputRangeTableWidth.innerHTML = rangeTableWidth.value;

		rangeTableWidth.oninput = function() {
		    if (currentTable) {
		  		if (pureNumber(currentTable.style.left) + (+this.value) <=100) {
		  			currentTable.style.width = this.value +"%";
		  		} else {
		  			currentTable.style.width = 100 - pureNumber(currentTable.style.left) + "%";
		  		}
		  		currentTableData.width = currentTable.style.width;	
			    currentTableData.pos_X = (pureNumber(currentTable.style.left) + pureNumber(currentTable.style.width)/2) +"%";	
			    outputRangeTableWidth.innerHTML = currentTable.style.width;
			  	outputPosX.innerHTML = (pureNumber(currentTable.style.left) + pureNumber(currentTable.style.width)/2) +"%";	
		    }
		    
		}


		var sliderHorizontal = document.getElementById("rangePosX");
		var outputPosX = document.getElementById("posX");
		outputPosX.innerHTML = sliderHorizontal.value;

		sliderHorizontal.oninput = function() {
			if (currentTable) {
			  	if (pureNumber(currentTable.style.width) + (+this.value) <= 100) {
			  		currentTable.style.left = this.value +"%";
			  	} else {
			  			currentTable.style.left = 100 - pureNumber(currentTable.style.width) + "%";
			  	}
			  	currentTableData.pos_X = (pureNumber(currentTable.style.left) + pureNumber(currentTable.style.width)/2) +"%";
			  	outputPosX.innerHTML = (pureNumber(currentTable.style.left) + pureNumber(currentTable.style.width)/2) +"%";
			}	
		  
		}
		

		var sliderVertical = document.getElementById("rangePosY");
		var outputPosY = document.getElementById("posY");
		outputPosY.innerHTML = sliderVertical.value;

		sliderVertical.oninput = function() {
			if (currentTable) {
			  	if (pureNumber(currentTable.style.height) + (100 - this.value) <= 100) {
			  		currentTable.style.top = 100 - this.value +"%";
			  	} else {
			  		currentTable.style.top = 100 - pureNumber(currentTable.style.height) + "%";
			  	}
			  	currentTableData.pos_Y = (pureNumber(currentTable.style.top) + pureNumber(currentTable.style.height)/2) +"%";	
			  	outputPosY.innerHTML = (pureNumber(currentTable.style.top) + pureNumber(currentTable.style.height)/2) +"%";
			  }	
			  
			}

		}