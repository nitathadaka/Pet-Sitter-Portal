//gallery

function seeMoreFunction(){
	var show = document.getElementById("seeMoreDiv");
		if(document.getElementById("seeMoreDiv").style.visibility==="hidden"){
		show.style.visibility="visible";
		document.getElementById("lowerDiv").style.marginTop="0px";
	}
	else if(document.getElementById("seeMoreDiv").style.visibility==="visible"){
		//test if invisible. If it is, make it visible
		show.style.visibility="hidden";
		//show.style.marginTop = "-200px";  
		document.getElementById("lowerDiv").style.marginTop="-400px";
	}
}

//eventCalendar
		function dateFunction(){
			//we are getting the date from the textbox
			var theDate=document.getElementById("datePicker").value;
			
			//the value from the textbox is a date. it needs to be changed into string to be converted
			//the line below cast(convert) date to string
			var theConvertedDate=theDate.toString();
			
			
			//yyyy-mm-dd
			//this array will store the dates on which events were held
			var eventDatesArray=["2017-07-10","2017-09-15","2017-07-29","2017-08-15"];
			
			//eventDatesArray[2]
			//this one will store the description of the event
			
			var eventDescriptionArray=["her birthday","his birthday","our anniversary","our first date"];
			
			//this i is a counter, used in the loop
			var i;
			
			var theResultEvent="no event found";
			
			//this loop is used for searching matching dates and corresponding event
			for(i=0;i<eventDatesArray.length;i++){
				if(theDate==eventDatesArray[i]){
					//alert(eventDescriptionArray[i]);
					theResultEvent=eventDescriptionArray[i];
					//document.getElementById("eventDescriptionDiv").innerHTML=eventDescriptionArray[i];
				}
				else{
					//whenever the comparison returns false, nothing happens,
					//the default value 'no event found' is valid
				}
			}
			
			//once the searching is done, it's time to write the value in the <p>
			document.getElementById("eventDescriptionDiv").innerHTML=theResultEvent;
			
		}

