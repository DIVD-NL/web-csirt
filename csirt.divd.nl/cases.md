---
title: Cases
---
{% assign pages = site.pages |reverse %}
{% assign team = site.team | map: "name" %}
{% for p in pages %}
	{% if p.url contains "/cases/" and p.url != page.url %}
<div class="caseitem">
<h3><a href="{{ p.url }}">{{ p.title }}</a><em>
    	{% if p.author[0] %}
    		{% assign first = true %}
    		{% for case_author in p.author %}
    			{% if first %}
    				{% assign first = false %}
    			{% else %}
    				,
    			{% endif %}
				{% if team contains case_author %}
<a href='https://www.divd.nl/team/{{ case_author }}'>{{ case_author }}</a>
				{% else %}
{{ case_author }}
				{% endif %}
			{% endfor %}
    	{% else %}
			{% assign case_author = p.author | default: "anonymous" %}
			{% if team contains case_author %}
<a href='https://www.divd.nl/team/{{ case_author }}'>{{ case_author }}</a>
			{% else %}
{{ case_author }}
			{% endif %}
		{% endif %}
</em>
</h3>
<p>
	Status: {{ p.status | default: "open" }}<br>
	{{ p.excerpt }}
</p>
<a href="{{ p.url }}">Lees meer</a>
</div>
<hr>
	{% endif %}
{% endfor %}
