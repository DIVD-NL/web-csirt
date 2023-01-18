---
layout: post
title: Additionele exchange scan script/additional exchange scan script
author: Frank Breedijk
excerpt: We have rescanned all servers with a new script and found more vulnerable servers / We hebben opnieuw gescand met een additioneel script en nieuwe kwetsbare servers gevonden

---
<p>
	<small><a href='{{ page.url }}#english'>English below</a></small>
</p>

### Nederlands

Vandaag hebben onderzoekers van het DIVD opnieuw alle eerder gescande ssystemen gescanned. Ditmaal is naast het bestaande script wat werkt op basis van het versienummer van OWA ook gescanned met een script van Microsoft wat daadwerkelijk vaststeld of {% cve CVE-2021-26855 %} kan worden misbruikt. 

Op basis van het gecombineerde resultaat van deze twee scripts zijn duizenden extra kwetsbare systemen gevonden. De beheerders van deze kwetsbare systemen worden door ons op de hoogte gesteld.

Beheerders die nu nog niet hebben gepatched moeten er vanuit gaan dat hun systeem reeds is overgenomen, dat er meegelezen wordt met de interne en externe communicatie en dat het systeem mogelijk binnenkort wordt geinfecteerd door ransomware.

Voor meer informatie zie: [case DIVD-2021-00001](/DIVD-2021-00001/)

![Graph of notification sent](/assets/images/DIVD-2021-00001-stats.png "Notifications sent over time")


### English

Today researchers of the DIVD rescanned all previously scanned systems. This time also utilizing a new script that tests if {% cve CVE-2021-26855 %} can actually be exploited in addition to the script that reports based on the version number of OWA. 

Based on the combined result of these two scripts we have found thousands of new vulnerable servers.

Administrators of unpatched systems are advised to assume compromise. It is likely that internal and external email communication is being read and that the system will soon be infected with ransomware.

For more information: [case DIVD-2021-00001](/DIVD-2021-00001/)
