---
layout: post
title: Exchange Zero-day IoC detectie script / Exchange Zero-day detection script
author: Lennaert Oudshoorn
excerpt: Microsoft brengt detectie scripts uit voor IoC's, 40% van de exchange servers in NL nog kwetsbaar, kwetsbaarheden misbruikt sinds januari. / Microsoft releases IoC detection script, 40% of the exchange servers in NL remain vulnerable, vulnerability abused as early as January.

---
<p>
	<small><a href='{{ page.url }}#english'>English below</a></small>
</p>

### Nederlands

DIVD heeft rond de 46 duizend notificaties wereldwijd uitgestuurd van kwetsbare systemen, in het algemeen wordt er positief gereageerd en acties direct uitgezet. Herscans zijn op verzoek beschikbaar.

Microsoft heeft meerdere scripts gepubliceerd voor het detecteren van gecompromiteerde Exchange servers.
[Script voor het detecteren van webshells](https://github.com/cert-lv/exchange_webshell_detection)
[CSS-Exchange Github pagina](https://github.com/microsoft/CSS-Exchange/tree/main/Security) heeft het Test-ProxyLogon.ps1 script dat de commando's uit de eerdere [Hafnium blog post](https://www.microsoft.com/security/blog/2021/03/02/hafnium-targeting-exchange-servers/) automatiseerd.
De [Microsoft Safety Scanner](https://docs.microsoft.com/en-us/windows/security/threat-protection/intelligence/safety-scanner-download) en Microsoft Defender hebben een [update](https://msrc-blog.microsoft.com/2021/03/05/microsoft-exchange-server-vulnerabilities-mitigations-march-2021/) gehad voor het detecteren en verwijderen van de malware die via deze kwetsbaarheden verspreid is.

Het Nederlandse Nationaal Cyber Security Centrum  heeft het nieuws naar buiten gebracht dat, volgens eigen onderzoek, 40% van de Nederlandse Microsoft Exchange Servers nog kwetsbaar is. Zie het [geplaatste nieuws bericht](https://www.ncsc.nl/actueel/nieuws/2021/maart/8/40-nl-microsoft-exchange-servers-nog-steeds-kwetsbaar) voor meer informatie.

[Volexity](https://www.volexity.com/blog/2021/03/02/active-exploitation-of-microsoft-exchange-zero-day-vulnerabilities/) en [FireEye](https://www.fireeye.com/blog/threat-research/2021/03/detection-response-to-exploitation-of-microsoft-exchange-zero-day-vulnerabilities.html) rapporteren dat al sinds begin januari van deze kwetsbaarhedenmisbruik wordt gemaakt. Vandaar dat wij het belang willen benadrukken voor organisaties om na het patchen onderzoek te verrichten op de betrefende servers om vast te stellen of er misbruik van deze kwetsbaarheden is gemaakt.

Voor meer informatie zie: [case DIVD-2021-00001](/DIVD-2021-00001/)

### English

DIVD has sent about 46 thousand notifications of vulnerable systems, responses are positive, and fixes are implemented. Rescans are on request available.

Microsoft has published multiple scripts for the detection of compromised Exchange servers.
[Script for detection of webshells](https://github.com/cert-lv/exchange_webshell_detection)
[CSS-Exchange Github page](https://github.com/microsoft/CSS-Exchange/tree/main/Security) has the Test-ProxyLogon.ps1 script that automates the commands found in the earlier [Hafnium blog post](https://www.microsoft.com/security/blog/2021/03/02/hafnium-targeting-exchange-servers/).
The [Microsoft Safety Scanner](https://docs.microsoft.com/en-us/windows/security/threat-protection/intelligence/safety-scanner-download) and Microsoft Defender received an [update](https://msrc-blog.microsoft.com/2021/03/05/microsoft-exchange-server-vulnerabilities-mitigations-march-2021/) to detect and remove the malware that has been distributed using these vulnerabilities.

The Dutch Nationaal Cyber Security Centrum released the news that, according to their own research, 40% of the Dutch Microsoft Exchange Servers remain vulnerable. See [the news item](https://www.ncsc.nl/actueel/nieuws/2021/maart/8/40-nl-microsoft-exchange-servers-nog-steeds-kwetsbaar) for more information.

[Volexity](https://www.volexity.com/blog/2021/03/02/active-exploitation-of-microsoft-exchange-zero-day-vulnerabilities/) and [FireEye](https://www.fireeye.com/blog/threat-research/2021/03/detection-response-to-exploitation-of-microsoft-exchange-zero-day-vulnerabilities.html) report that these vulnerabilities have been abused since early January. With this in mind, we want to stress the importance for organisations to, after patching, perform an investigation to determine if these vulnerabilities have been exploited on their systems.

For more information: [case DIVD-2021-00001](/DIVD-2021-00001/)
