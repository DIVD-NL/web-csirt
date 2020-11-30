---
layout: post
title: GhostCat een kwetsbaarheid in Apache Tomcat AJP  / GhostCat an Apache Tomcat AJP vulnerability
author: Jeroen van de Weerd
excerpt: 773 Nederlandse IP adressen kwetsbaar voor Ghostcat - Apache Tomcat AJP File Read/Inclusion Vulnerability / 773 Dutch IP addresses vulnerable to Ghostcat - Apache Tomcat AJP File Read / Inclusion Vulnerability
---

### Nederlands

Deze kwetsbaarheid, GhostCat genaamd, werd ontdekt door onderzoekers van Chaitin Tech https://www.chaitin.cn/en/ghostcat en  op 3 januari aan Apache Software Foundation gemeld. Op 20 februari 2020 publiceerde de China National Vulnerability Database (CNVD) een beveiligingsadvies voor CNVD-2020-10487, een ernstige kwetsbaarheid in Apache Tomcat's Apache JServ Protocol (of AJP). De kwetsbaarheid heeft ook een CVE aanduiding gekregen, CVE-2020-1938.
Op dit moment heeft het [DIVD](https://www.divd.nl) 773 Nederlandse kwetsbare IP-adressen gevonden. Het Security Meldpunt gaat deze lijst verder onderzoeken en probeert de eigenaren op de hoogte te brengen.

De kwetsbaarheid heeft de naam Ghostcat gekregen omdat de kwetsbaarheid in alle versies (Tomcat 9/8/7/6 en ouder) van de Apache Tomcat AJP connector zit, deze connector staat standaard aan. Deze kwetsbaarheid is in staat geweest meer dan 10 jaar onzichtbaar te blijven, vandaar Ghostcat.

![Ghostcat](/assets/images/ghostcat-logo-small.png "Image copyright Chaitin Tech")

Op diverse Github pagina's zijn inmiddels Proof of Concept (PoC) programmas gedeeld die aantonen dat deze kwetsbaarheid te misbruiken is.
Op 20 februari heeft [@chybeta](https://twitter.com/chybeta/status/1230489154468732928) gepubliceerd dat het, onder bepaalde omstandigheden, is gelukt om code uit te voeren op het systeem via deze kwetsbaarheid. Dat betekent dat systemen, die aan deze voorwaarden voldoen, gemakkelijk over te nemen zijn.

Bij het uitbuiten van deze kwetsbaarheid kan de aanvaller de inhoud van alle configuratiebestanden en broncodebestanden van de webapps die op Tomcat zijn geïmplementeerd inzien. Als de applicatie het toestaat om bestanden te uploaden en deze binnen de root van de applicatie worden opgeslagen, kan een aanvaller een bestand met kwaadaardige JSP-scriptcode uploaden en deze hierna laten oppakken door de Ghostcat-kwetsbaarheid, dit kan uiteindelijk leiden tot uitvoering van externe code.
Apache heeft ondertussen al diverse updates uitgebracht om de kwetsbaarheid te verhelpen. De officieel versies 9.0.31, 8.5.51 en 7.0.100 zijn vrijgegeven om dit beveiligingslek te verhelpen.

Als de AJP Connector service niet wordt gebruikt dan raden wij aan om direct te updaten naar de nieuwe uitgegeven versies. Lukt het niet om te updaten, om welke reden dan ook, dan kunt u het beste de regel, "Connector port="8009" protocol="AJP/1.3" redirectPort=8443" in /conf/server.xml uit commentariëren. Let op, het poortnummer kan anders zijn dan in dit voorbeeld. U kunt ook firewall regels instellen om toegang tot de AJP connector verder te minimaliseren.

Als u de AJP Connector service wel gebruikt dan raden wij ook aan om direct te updaten naar de nieuwe uitgegeven versies. Onderzoekers van Chaitin Tech adviseren het "secret" kenmerk voor de AJP Connector in te stellen, hiermee wordt AJP-protocolverificatie actief.

Achtergrond en update info:
* [Vulnerability POC](https://twitter.com/chybeta/status/1230489154468732928)
* [Apache Tomcat Version 9.0.31](https://tomcat.apache.org/tomcat-9.0-doc/changelog.html)
* [Apache Tomcat Version 8.5.51](https://tomcat.apache.org/tomcat-8.5-doc/changelog.html)
* [Apache Tomcat Version 7.0.100](https://tomcat.apache.org/tomcat-7.0-doc/changelog.html)

Meer informatie en de laatste stand van zaken met betrekking tot deze case wordt aangelegd op [onze case pagina](/DIVD-2020-00005/)

<hr>

### English

This vulnerability, dubbed Ghostcat, was discovered by researchers at [Chaitin Tech](https://www.chaitin.cn/en/ghostcat) and reported to Apache Software Foundation on January 3. On February 20, 2020, the China National Vulnerability Database (CNVD) published a security advisory for CNVD-2020-10487, a serious vulnerability in Apache Tomcat's Apache JServ Protocol (or AJP). The vulnerability has also been given a CVE designation, CVE-2020-1938.
At the moment, the [DIVD](https://www.divd.nl) has found 773 vulnerable Dutch IP addresses. Security Meldpunt will further investigate this list and try to inform the owners.

It has been named Ghostcat because the vulnerability is present in all versions (Tomcat 9/8/7/6 and older) of the Apache Tomcat AJP connector and has been in it for more than 10 years without getting noticed, thats why it's called Ghostcat.

![Ghostcat](/assets/images/ghostcat-logo-small.png "Image copyright Chaitin Tech")

Proof of Concept (PoC) code is shared on various Github pages that demonstrate that this vulnerability can be exploited. On February 20, [@chybeta](https://twitter.com/chybeta/status/1230489154468732928) published that it was possible, under certain conditions, to execute code on the system through this vulnerability. This means that systems that meet these conditions are easy to take over.

When exploiting this vulnerability, the attacker can view the contents of all configuration files and source code files of the web apps implemented on Tomcat. If the website application allows files to be uploaded within the root of the web applicaitons, an attacker can upload a file with malicious JSP script code that can then be picked up by the Ghostcat vulnerability, which leads to remote code execution.
Apache has already released several updates to fix the vulnerability. The official versions 9.0.31, 8.5.51 and 7.0.100 have been released to address this vulnerability.

If the AJP Connector service is not used, we recommend that you immediately update to the newly issued versions. If it is not possible to update, for whatever reason, it is best to comment out the line, "Connector port="8009" protocol="AJP/1.3" redirectPort=8443" in /conf/server.xml. Please note, the port number may differ from this example. You can also set firewall rules to further minimize access to the AJP connector.

If you do use the AJP Connector service, we also recommend that you immediately update to the newly issued versions. Researchers from Chaitin Tech recommend setting the "secret" attribute for the AJP Connector, which makes AJP protocol verification active.

Background and update info:
* [Vulnerability POC](https://twitter.com/chybeta/status/1230489154468732928)
* [Apache Tomcat Version 9.0.31](https://tomcat.apache.org/tomcat-9.0-doc/changelog.html)
* [Apache Tomcat Version 8.5.51](https://tomcat.apache.org/tomcat-8.5-doc/changelog.html)
* [Apache Tomcat Version 7.0.100](https://tomcat.apache.org/tomcat-7.0-doc/changelog.html)

More information and the current status of this case can be found on [our case page](/DIVD-2020-00005/)
