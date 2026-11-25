/*
	Industrious by TEMPLATED
	templated.co @templatedco
	Released for free under the Creative Commons Attribution 3.0 license (templated.co/license)
*/
(function($) {
	var	$window = $(window),
		$banner = $('#banner'),
		$body = $('body');

	// Breakpoints.
		breakpoints({
			default:   ['1681px',   null       ],
			xlarge:    ['1281px',   '1680px'   ],
			large:     ['981px',    '1280px'   ],
			medium:    ['737px',    '980px'    ],
			small:     ['481px',    '736px'    ],
			xsmall:    ['361px',    '480px'    ],
			xxsmall:   [null,       '360px'    ]
		});

	// Play initial animations on page load.
		$window.on('load', function() {
			window.setTimeout(function() {
				$body.removeClass('is-preload');
			}, 100);
		});

	// Menu.
		$('#menu')
			.append('<a href="#menu" class="close"></a>')
			.appendTo($body)
			.panel({
				target: $body,
				visibleClass: 'is-menu-visible',
				delay: 500,
				hideOnClick: true,
				hideOnSwipe: true,
				resetScroll: true,
				resetForms: true,
				side: 'right'
			});
})(jQuery);

/* Toggle the "responsive" class on the menu when the user clicks on the menu button */
document.getElementById("menuBtn").addEventListener("click", function(){
	document.getElementById("nav_menu").classList.toggle("responsive");
});

/* Position the case timeline bars and axis labels. The CSP forbids inline
   style attributes, so the includes pass percentages via data attributes
   and we apply them through the CSSOM here. */
document.querySelectorAll(".ctl-axis span, .ctl-bar, .ctl-today").forEach(function(el) {
	if (el.dataset.left) { el.style.left = el.dataset.left + "%"; }
	if (el.dataset.width) { el.style.width = el.dataset.width + "%"; }
});
