/*
 * Functions for the donate page: 
 * - Fetch the data
 * - Render the html.
 */

/**
 * Anti-XSS condom
 */
function condom(unsafe) { 
	return $("<div>").text(unsafe).html(); 
}

/**
 * Iterate donations in reverse (to render the latest ones first and then:
 * - fix the date format and breaking on '-' in the table by replacing it with &#8209;
 * - Parse the name, or flag as anonymous
 * - html-safe render the name and donation comment.
 * - add the referal data to the donate link
 */
function renderDonations(data) {  
    
    let rows = data.donations.reverse().map(function(donation) {
        let created = donation.created_at.split(" ")[0].split("-").reverse().join("&#8209;");
        let name = donation.anonymous ? "Anonymous" :  `${donation.first_name ?? ''} ${donation.last_name_prefix ?? ''} ${donation.last_name ?? ''}`;
        
        return `<tr><td>${created}</td>
                    <td class='right-align'>&euro; ${donation.amount}</td>
                    <td>${condom(name)}</td>
                    <td>${condom(donation.message)}</td>
        </tr>`;
    });
    
    $("#donations").html(rows.join(''));

    $('.donate_btn').on('click', function(evt) {
	let addition = evt.target.value ? "/v=${evt.target.value}" : '';
	window.location.href = data.absoluteUrl+"/donate${addition}";
    });

};

$(document).ready(function() {
	$.getJSON('/data/supp.json').then((result)=>renderDonations(result.data));
});
