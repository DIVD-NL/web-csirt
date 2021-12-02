---
title: Cases
---
{% assign cases = site.cases |reverse %}
{% assign team = site.team | map: "name" %}
{% for p in cases %}
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
<a href='https://www.divd.nl/team/{{ case_author | uri_escape }}'>{{ case_author }}</a>
				{% else %}
{{ case_author }}
				{% endif %}
			{% endfor %}
    	{% else %}
			{% assign case_author = p.author | default: "anonymous" %}
			{% if team contains case_author %}
<a href='https://www.divd.nl/team/{{ case_author | uri_escape }}'>{{ case_author }}</a>
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
{% endfor %}
