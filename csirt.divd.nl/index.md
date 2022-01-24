---
title: DIVD CSIRT
layout : page
---
## The DIVD CSIRT...

... supports the [Dutch Institute for Vulnerability Disclosure](https://divd.nl), in its mission “…to make the digital world safer by reporting vulnerabilities we find in digital systems to the people who can fix them. We have a global reach, but do it Dutch style: open, honest, collaborative, and for free.”

The CSIRT handles the scanning for and disclosing of vulnerabilities, either discovered by DIVD researchers or third parties and warning people for leaked credentials.


## Our blog

Last 10 posts ...

<ul>
{% for post in site.posts %}
	{% if forloop.index <= 10 %}
	    <li>
	        <a href="{{ post.url | prepend: site.baseurl }}">{{ post.date | date: "%d-%m-%Y" }}  - {{ post.title }}</a>.
	    </li>
	{% endif %}
{% endfor %}
</ul>

[More posts](/blog/2)

{% include timeline_cases_open.html %}

## Open cases

<ul>
{% assign cases = site.cases |reverse %}
{% assign team = site.team | map: "name" %}
{% for p in cases %}
	{% if p.status == "Open" %}
		<li>
			<a href='{{ p.url }}'>{{ p.title }}</a>
		</li>
	{% endif %}
{% endfor %}
</ul>

## Some statistics

{% include stats.html %}