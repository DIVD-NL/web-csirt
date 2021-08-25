---
layout: post
title: SolarWinds Orion API authentication bypass
author: Lennaert Oudshoorn
excerpt: Een authenticatie bypass kan aanvallers de mogelijkeheid geven om API commando's uit te voeren, hierdoor kan het systeem gecompromiteerd worden. / An authentication bypass could allow attackers to execute API commands which may result in a compromise of the system.

---
<p>
	<small><a href='{{ page.url }}#english'>English below</a></small>
</p>

### Nederlands

Er is een nieuwe zero-day kwetsbaarheid gevonden in SolarWinds Orion, bekend als {% cve CVE-2020-10148 %}, met deze kwetsbaarheid kan een aanvaller zonder authenticatie API commando's uitvoeren en zo het systeem compromiteren. Onderzoekers van het DIVD hebben gescanned op kwetsbare systemen. Aan de hand van deze scan resultaten zullen wij de beheerders van deze systemen op de hoogte proberen te stellen.

Voor meer informatie zie: [case DIVD-2020-00014](/DIVD-2020-00014/)

### English

A new zero-day vulnerability was found in SolarWinds Orion, known as {% cve CVE-2020-10148 %}, this vulnerability allows a remote attacker to bypass authentication and execute API commandos, possibly compromising the system. DIVD researchers have scanned for vulnerable systems. Based on these scan results we try to notify administrators of vulnerable systems.

For more information: [case DIVD-2020-00014](/DIVD-2020-00014/)
