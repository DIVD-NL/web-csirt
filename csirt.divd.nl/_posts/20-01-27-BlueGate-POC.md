---
layout: post
title: POC Exploit Microsoft Remote Dekstop Gateway RCE vulnerability
author: Barry van Kampen
excerpt: Het Security Meldpunt adviseerd dringend patches uit te rollen en gaat actief beheerders benaderen / The Security Hotline is advising urgently to patch systems and notify owners of vulnerable systems
---

### Nederlands

Op 14 januari bracht Microsoft twee zeer kritieke updates uit met een [CVSS score van .8](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?calculator&version=3&vector=(CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H/E:P/RL:O/RC:C)) voor de Windows 2012, 2012R2, 2016 en 2019 Server platformen. 

Deze patches verhelpen een kwetsbaarheid in Windows Remote Desktop Gateway (RD Gateway), een concurrent van Citrix. Misbruik van de kwetsbaarheid kan leiden tot onbeschikbaarheid (DoS, Denial of Service) en de mogelijkheid om willekeurige code op het systeem uit te voeren (RCE, Remote Command Execution).

Deze kwetsbaarheden zijn verholpen na het uitvoeren van de updates van Patchtuesday van januari 2020. 

Vandaag is door [@layle_ctf](https://twitter.com/layle_ctf/status/1221514332049113095) gepubliceerd dat het is gelukt om code uit te voeren op het systeem via deze kwetsbaarheid. Dat betekent dat systemen gemakkelijk over te nemen zijn.

Op dit moment heeft het [DIVD](https://www.divd.nl) zo'n 16 duizend kwetsbare systemen op het internet gevonden, waaronder ca. 1130 Nederlandse systemen.
Het Security Meldpunt gaat netwerk beheerders van de netwerken waar deze systemen gevonden zijn actief waarschuwen.

De kwetsbaarheid van deze systemen is vastgesteld met behulp van de door [ollypwn op GitHub](https://github.com/ollypwn/BlueGate) gepubliceerde code.

Achtergrond en update info:
* [CVE-2020-0609](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-0609) 
* [CVE-2020-0610](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-0610)
* [Vulnerability test en Denial of Service POC](https://github.com/ollypwn/BlueGate)

Meer informatie en de laatste stand van zaken met betrekking tot deze case wordt aangelegd op [onze case pagina](/DIVD-2020-00003/)

![A picture of a a blue and red gate in the sea](/assets/images/bluegate_small.png "Image copyright Scopio")

<hr>

### English

On January 14th Microsoft released patches for two critical vulnerabilities found in Windows Server 2012, 2012R2, 2016 and 2019 with a [CVSS score off 9.8](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?calculator&version=3&vector=(CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H/E:P/RL:O/RC:C))

Impact is both DOS (Denial Of Service) and RCE (Remote Command Execution), a functional impact can be a complete takeover of the system and it's information. Patches of January 2020 are effective and highly recommended to deploy asap.

Today a working POC of the RCE was announced by @layle_ctf (https://twitter.com/layle_ctf/status/1221514332049113095)

At the time of writing [DIVD](https://www.divd.nl) researchers determined that there are more than 16 thousand systems vulnerable, approximately 1140 of these are Dutch servers.

We are going to notify administrators of the vulnerable systems.

The vulnerability of the systems has been determined using [ollypwn's GitHub code](https://github.com/ollypwn/BlueGate)

Background and patch info:
* [CVE-2020-0609](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-0609) 
* [CVE-2020-0610](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-0610)
* [Vulnerability test en Denial of Service POC](https://github.com/ollypwn/BlueGate)

More information and the current status of this case can be found on [our case page](/DIVD-2020-00003/)
