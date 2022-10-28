var yearButtons = document.querySelectorAll('.yearBtn').forEach(function(b){
	b.onclick = function(e){
		yearButtonClick(e)
	}
});

function yearButtonClick(e) {
	y=e.target.innerHTML
	document.querySelectorAll('.yearBtn').forEach(function(b){
		b.className = "yearBtn"
	})
	e.target.className = "yearBtn active"
	document.querySelectorAll('.yearDiv').forEach(function(d){
		d.className = "yearDiv hidden"
	})
	document.querySelectorAll('#div'+y).forEach(function(d){
		d.className = "yearDiv"
	})

}
