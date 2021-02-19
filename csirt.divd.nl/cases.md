---
title: Cases
---
{% assign pages = site.pages |reverse %}
{% assign team = site.team | map: "name" %}
{% for p in pages %}
	{% if p.url contains "/cases/" and p.url != page.url %}
		{% assign case_author = p.author | default: "anonymous" %}
<div class="caseitem">
<h3><a href="{{ p.url }}">{{ p.title }}</a><em>
		{% if team contains case_author %}
<a href='https://www.divd.nl/team/{{ case_author }}.md'>{{ case_author }}</a>
		{% else %}
{{ case_author }}
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