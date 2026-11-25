/*
	Colour theme switcher: auto (follow the system), light or dark.

	Loaded synchronously in <head> so the data-theme attribute is set
	before first paint; the toggle button lives in the site header.
*/
(function () {
	var KEY = 'divd-theme';
	var root = document.documentElement;
	var modes = ['auto', 'light', 'dark'];
	var icons = { auto: 'fa-adjust', light: 'fa-sun-o', dark: 'fa-moon-o' };

	function stored() {
		try {
			return localStorage.getItem(KEY);
		} catch (e) {
			return null;
		}
	}

	function apply(mode) {
		if (mode === 'light' || mode === 'dark') {
			root.setAttribute('data-theme', mode);
		} else {
			root.removeAttribute('data-theme');
			mode = 'auto';
		}
		var btn = document.getElementById('theme-toggle');
		if (btn) {
			btn.innerHTML = '<i class="fa ' + icons[mode] + '" aria-hidden="true"></i>';
			btn.title = 'Theme: ' + mode;
			btn.setAttribute('aria-label', 'Colour theme: ' + mode + '. Click to switch.');
		}
	}

	var mode = modes.indexOf(stored()) > 0 ? stored() : 'auto';
	apply(mode);

	document.addEventListener('DOMContentLoaded', function () {
		var btn = document.getElementById('theme-toggle');
		if (!btn) {
			return;
		}
		btn.hidden = false;
		apply(mode);
		btn.addEventListener('click', function () {
			mode = modes[(modes.indexOf(mode) + 1) % modes.length];
			try {
				localStorage.setItem(KEY, mode);
			} catch (e) {}
			apply(mode);
		});
	});
})();
