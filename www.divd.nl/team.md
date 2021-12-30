---
layout: default
title: team
header: our team
---
<header>
    <h2>Researchers</h2>
</header>

We represent a team of highly skilled security researchers who seek and report vulnerabilities as a voluntary service next to their jobs. DIVD sees to it they follow our [Code of Conduct](https://divd.nl/divd-nl/code/) while we provide them a fire wall for journalists, lawyers and recruiters. Meanwhile, their research also serves as an empirical base to discover trends in security, stimulate security awareness and develop new methodologies in vulnerability research and disclosure. So, although you will probably never meet our researchers, you may hope they are checking your systems right now, before the bad guys do...

<hr>

### Team (in order of appearence)
{% assign sorted = site.team | where_exp: "x", "x.supervision != true" | sort: "appearance" %}
{%- for member in sorted -%}
- [{{ member.name }}]({{ member.url }}): {{ member.role }}
{% endfor %}

<hr>

### Department
#### Academy
{% assign sorted = site.team | where: "dept", "Academy" | sort: "appearance" %}
{%- for member in sorted -%}
[{{ member.name }}]({{ member.url }})
{% endfor %}

#### CSIRT
{% assign sorted = site.team | where: "dept", "CSIRT" | sort: "appearance" %}
{%- for member in sorted -%}
[{{ member.name }}]({{ member.url }})
{% endfor %}

#### Institute
{% assign sorted = site.team | where: "dept", "Institute" | sort: "appearance" %}
{%- for member in sorted -%}
[{{ member.name }}]({{ member.url }})
{% endfor %}

<hr>

### Board
{% assign board = site.team | where_exp: "x", "x.board == true" | sort: "appearance" %}
{%- for member in board -%}
	{% if member.active == true %}
- [{{ member.name }}]({{ member.url }}): {{ member.content }}
	{%- endif -%}
{% endfor %}

<hr>
### Supervisory Board
Hacker initiatives like these, tend to have their own dynamics: sparks lead to flames, which die out or lead to wildfires, wasting energy along the way. To keep our minds focused on our goal to make the digital world a safer place and provide helpful hackers a solid platform, we installed a Supervisory Board of cyber security heavyweights. Each board member also represents a sector we try to get along in reaching our goals, i.e.: law enforcement, intelligence services, cyber security companies and academia.

{% assign supers = site.team | where_exp: "x", "x.supervision == true" | sort: "appearance" %}
{%- for member in supers -%}
- [{{ member.name }}]({{ member.url }}): {{ member.content }}
{% endfor %}

