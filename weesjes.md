---
layout: none
---
{% assign team = site.team | map: "name" -%}
{% assign people = '' %}
{% for p in site.posts %}
  {% capture people %}{{ p.author }}|{{ people }}{% endcapture%}
{% endfor %}

{% for c in site.cases %}
  {% capture people %}{{ c.author | join: '|' }}|{{ c.lead }}|{{ c.researchers | join: '|' }}|{{ people }}{% endcapture%}
{% endfor %}

{% for p in site.csirt_posts %}
  {% capture people %}{{ p.author | join: '|' }}|{{ people }}{% endcapture%}
{% endfor %}

{% for c in site.cves %}
  {% capture people %}{{ c.author | join: '|' }}|{{ c.discovered_by | join: '|' }}|{{ c.researchers | join: '|' }}|{{ people }}{% endcapture%}
{% endfor %}
{% assign people = people | split: '|' | sort | uniq %}

{% for p in people %}
  {%- if team contains p -%}
  {%- else -%}
    {%- if p != "" -%}
Wees: {{ p }}<br>
    {% endif %}
  {%- endif -%}
{% endfor %}