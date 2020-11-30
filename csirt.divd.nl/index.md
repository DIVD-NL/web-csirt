---
title: Cases
---
## Het Nederlands Security Meldpunt...

... is een groep vrijwilligers, onderdeel van het [Dutch Institute for Vulnerability Disclosure](https://divd.nl), die het zich tot taak heeft gesteld eigenaren van Nederlandse netwerkblokken en websites te informeren over (cyber) security zaken die bij het meldpunt gemeld worden.

### Wat kun je melden?

Wij richten ons specifiek op kwetsbaarheden die een groot aantal gebruikers treft zoals die in onze [Citrix ADC case](/DIVD-2020-00001/). In deze gevallen willen wij gericht de netwerk beheerders van netwerken met kwetsbare systemen op de hoogte brengen van het bestaan van deze systemen zodat zij de kwetsbaarheid kunnen (laten) verhelpen.

### Hoe kan ik melden?

Lees voor je gaat melden eerst onze [spelregels](/spelregels) en lees eventueel onze [veel gestelde vragen](/faq).

## Blog

Laatste 10 artikelen...

<ul>
{% for post in site.posts %}
	{% if forloop.index <= 10 %}
	    <li>
	        <a href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a>
	    </li>
	{% endif %}
{% endfor %}
</ul>

[Alle artikelen](/blog)
