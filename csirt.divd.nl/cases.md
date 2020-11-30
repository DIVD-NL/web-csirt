---
title: Cases
---
{% assign pages = site.pages |reverse %}
{% for p in pages %}
{% if p.url contains "/cases/" and p.url != page.url %}
<hr>
<div class="caseitem">
<h3><a href="{{ p.url }}">{{ p.title }}</a><em><a href='/handlers/{{ p.author | default: "anonymous" }}'>{{ p.author | default: "anonymous" }}</a></em>
</h3>
<p>
	Status: {{ p.status | default: "open" }}<br>
	{{ p.excerpt }}
</p>
<a href="{{ p.url }}">Lees meer</a>
</div>
{% endif %}
{% endfor %}
