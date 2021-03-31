/*
 * Functions for the donate page
 */

function update_display(data) {
	$('#name').text(data.name);
	$('#description').text(data.description);
	url = data.absoluteUrl;
	$(".donate_btn").attr("url",url);
	$('#amount').text(data.raised);
	if (data.goal > 0) {
		$('#goal').text("of €" + data.goal);
	} else { 
		$('#goal').text("");
	}
	data.donations.forEach(function(d) {
		txt = "<tr>"
		txt += "<td>"+$("<div>").text(d.created_at.split(" ")[0].split("-").reverse().join("-")).html()+"</td>"
		txt += "<td class='right-align'>&euro; "+$("<div>").text(d.amount).html()+"</td>"
		if( d.anonymous ) {
			txt += "<td>Anonymous</td>"
		} else { 
			txt += "<td>"+$("<div>").text(d.name).html()+"</td>"
		}
		txt += "<td>"+$("<div>").text(d.message).html()+"</td>"
		txt += "</tr>"
		$('#donations').prepend(txt)

	})
	$('.donate_btn').on('click', function(evt) {
		v=evt.target.value;
		if(v) {
			window.location.href=data.absoluteUrl+"/donate/"+v
		} else {
			window.location.href=data.absoluteUrl+"/donate"
		}
	});
}

function load_donations() {
	$.ajax({

	    url : '/data/supp.json',
	    type : 'GET',
	    data : {},
	    dataType:'json',
	    success : function(data) {
	    	update_display(data.data)   
	    },
	    error : function(request,error)
	    {
	    	console.error("Error: "+ error)
	        console.log("Request: "+JSON.stringify(request));
	    }
	});
};


$( document ).ready(function() {
	load_donations()
})