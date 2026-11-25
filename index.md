---
title: DIVD CSIRT
layout : page
---
## The DIVD CSIRT...

... supports the [Dutch Institute for Vulnerability Disclosure](https://divd.nl), in its mission “…to make the digital world safer by reporting vulnerabilities we find in digital systems to the people who can fix them. We have a global reach, but do it Dutch style: open, honest, collaborative, and for free.”

The CSIRT handles the scanning for and disclosing of vulnerabilities, either discovered by DIVD researchers or third parties and warning people for leaked credentials and operates our [CVE Numbering Authoristy (CNA) capability](/cna/).


## Our blog

Last 10 posts ...

<ul>
{%- for post in site.posts -%}
	{%- if forloop.index <= 10 -%}
	    <li>
	        <a href="{{ post.url | prepend: site.baseurl }}">{{ post.date | date: "%d-%m-%Y" }}  - {{ post.title }}</a>.
	    </li>
	{%- endif -%}
{%- endfor -%}
</ul>

[More posts](/blog/2)

{%- include timeline_cases_open.html -%}

## Recently closed cases

<ul>
{%- assign closed_cases = site.cases | where: "status", "Closed" | sort: "end" | reverse -%}
{%- for p in closed_cases limit: 10 -%}
	<li>
		{{ p.end | date: "%d-%m-%Y" }} - <a href='{{ p.url }}'>{{ p.title }}</a>.
	</li>
{%- endfor -%}
</ul>

[All cases](/cases/)

## Some statistics

{% include stats.html -%}