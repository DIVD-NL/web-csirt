---
title: Cases
---
{% assign cvepages = site.cves |reverse %}
{% assign team = site.team | map: "name" %}
{% for p in cvepages %}
<div class="caseitem">
<h3>
{% if p.json %}
{% assign cve_title = p.json.description.description_data | where: "lang", "eng" %}
{% capture cve_title %}{{ cve_title[0].value }}{% endcapture %}
<a href='{{ p.url }}'>{{ p.json.CVE_data_meta.ID | escape }} - {{ cve_title | escape }}</a>
{% else %}
<a href="{{ p.url }}">{{ p.cve | escape }} - {{ p.title | escape }}</a><
{% endif %}
</h3>
</div>
<hr>
{% endfor %}