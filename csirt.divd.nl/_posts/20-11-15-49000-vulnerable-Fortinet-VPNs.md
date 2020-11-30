---
layout: post
title: Lijst met 49 000 kwetsbare Fortinet VPNs / List of 49 000 vulnerable Fortinet VPNs
author: Lennaert Oudshoorn
excerpt: Er is een lijst online aangetroffen met 49 577 kwetsbare Fortinet VPN devices waarvan login credentials gestolen kunnen worden / A list was found online, with 49 577 vulnerable Fortinet VPN devices, potentially login credentials could be exposed

---

### Nederlands

Op 19 November is door een threat intelligence analyst een lijst met 49,577 kwetsbare Fortinet VPN devices aangetroffen. Het gaat hier om Fortinet devices die kwetsbaar zijn voor CVE-2018-13379, via deze kwetsbaarheid kan een aanvaller via een aangepast HTTP request systeem bestanden opvragen waartoe hij normaal gesproken geen toegang zou moeten hebben. Door het bestand sslvpn_websession op te vragen, is het mogelijk om de inlogggegeven van gebruikers te stelen.

Bleeping Computer heeft een [artikel gepubliceerd](https://www.bleepingcomputer.com/news/security/hacker-posts-exploits-for-over-49-000-vulnerable-fortinet-vpns/) over deze kwetsbaarheid.

Het DIVD Security Meldpunt gaat organisaties of netwerk beheerders waarschuwen, waarvan ze heeft kunnen vaststellen dat ze daadwerkelijk een kwetsbare versie van Fortinet VPN gebruiken of in hun netwerk hebben.

Voor meer informatie zie: [case DIVD-2020-00012](/DIVD-2020-00012/)

### English

On November 19th a threat intelligence analyst found a list with 49,577 vulnerable Fortinet VPN devices online. These devices are vulnerable to CVE-2018-13379, through this vulnerability an attacker can gain access to system files via crafted HTTP requests. Specificaly the system file sslvpn_websession can be acccess and used to retrieve user login credentials.

Bleeping Computer has [published an artical](https://www.bleepingcomputer.com/news/security/hacker-posts-exploits-for-over-49-000-vulnerable-fortinet-vpns/) about this vulnerability.

The DIVD Security Meldpunt will notify organisations or administrators of networks of which DIVD has determined that they are running a vulnerable version of Fortinet VPN.

For more information: [case DIVD-2020-00012](/DIVD-2020-00012/)
