/*
 * Functions for the donate page
 * whydonate.js from https://whydonate-production-api.appspot.com/api/v1/project/fundraising/local/?client=whydonate_production&slug=divd
 * Whydonate2 from   https://whydonate-production-api.appspot.com/api/v1/donation/orders/fundraising/local/?client=whydonate_production&id=15964&cursor=&limit=1000
 */

function update_donations(data) {
	//console.log(data);
	data.results.forEach(function(d) {
		txt = "<tr>"
		txt += "<td class='unbrakable'>"+$("<div>").text(d.created_at.split("T")[0]).html()+"</td>"
		txt += "<td class='right-align unbrakable'>&euro; "+$("<div>").text(d.amount).html()+"</td>"
		if( d.is_anonymous ) {
			txt += "<td>Anonymous</td>"
		} else { 
			txt += "<td>"+$("<div>").text(d.donor.full_name).html()+"</td>"
		}
		txt += "<td>"+$("<div>").text(d.donor.message).html()+"</td>"
		txt += "</tr>"
		$('#donations').append(txt)

	})
}

function update_fundraiser(data) {
	console.log(data);
	$('#title').text(data.title);
	$('#description').text(data.description);
	$('#amount').text(data.donation.amount);
	$('#count').text(data.donation.count);
	$('.donate_btn').on('click', function(evt) {
		window.location.href="https://www.whydonate.nl/fundraising/divd"
	});
}

function load_donations() {
	$.ajax({

	    url : '/data/whydonate2.json',
	    type : 'GET',
	    data : {},
	    dataType:'json',
	    success : function(data) {
	    	update_donations(data)   
	    },
	    error : function(request,error)
	    {
	    	console.error("C")
	        console.log("Request: "+JSON.stringify(request));
	    }
	});
};

function load_fundraiser() {
	$.ajax({

	    url : '/data/whydonate.json',
	    type : 'GET',
	    data : {},
	    dataType:'json',
	    success : function(data) {
	    	update_fundraiser(data.data)   
	    },
	    error : function(request,error)
	    {
	        console.log("Request: "+JSON.stringify(request));
	    }
	});
};


$( document ).ready(function() {
	load_donations();
	load_fundraiser();
})