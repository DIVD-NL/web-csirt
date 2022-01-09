---
title: Why did you scan me?
---
{{ page.title }}
===========

When you landed on this page, it is probably because you whitnessed one of our scanners in you logs. We operate the following scanners:
{% for s in site.data.scanners -%}
* {{ s.name }} - {{ s.description }}
{% endfor %}

**Don't Panic**

You have been scanned by the non-profit Dutch Institute for Vulnerability Disclosure ([DIVD](https://www.divd.nl); Twitter: [@divdnl](https://twitter.com/divdnl)). We scan the internet to detect systems that potentially contain vulnerabilities to inform system owners. All to support our mission:

<div class="center">
We aim to make the digital world safer by reporting vulnerabilities we find in digital systems to the people who can fix them. We have a global reach, but do it Dutch style: open, honest, collaborative, and for free.
</div>

<br>
We only test systems if our tests pass the criteria of proportionality and subsidiarity, which means that our tests are non-intrusive and as light-weight as possible and that there are no other ways to reach the same effect.

Additionally, all our research and our researchers are bound by our [code of conduct](https://www.divd.nl/code/).

DIVD does not operate on an opt-in or opt-out basis, but you can block the scanners above, although we highly recommend against it.

We currently have the following cases open, so the scan you observed is likely related to one of them:
{% assign cases = site.cases |reverse -%}
{% assign team = site.team | map: "name" -%}
{% for p in cases -%}
{%- if p.status == "Open" -%}
* [{{ p.title }}]({{ p.url }})
{% endif -%}
{% endfor %}
