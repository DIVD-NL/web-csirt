---
layout: post
title: Ernstige lek in Citrix ShareFile storage server / Critical vulnerability in Citrix ShareFile storage server
author: Frank Breedijk
excerpt:  Citrix ShareFile servers bevatten een ernstig lek waarmee een aanvaller gevoelige informatie kan achterhalen / Citrix ShareFile servers contain a vulnerability that allows an attacker to obtain sensitive information.
---

### Nederlands

Op 5 mei heeft Citrix klanten die gebruik maken van de Citrix ShareFile oplossing gewaarschuwd over drie kwetsbaarheden in dit product en hiervoor patches en een mitigatie [beschikbaar](https://support.citrix.com/article/CTX269341) gesteld. 

Citrix heeft geen technisch inhoudelijke mededelingen gedaan over de verholpen kwetsbaarheden, maar onderzoek van [Dimitri van de Giessen](https://twitter.com/DimitriNL) wijst erop dat een van de kwetsbaarheden is ontstaan omdat Citrix gebruik gemaak heeft van een oude Ajax component met een kwetsbaarheid die het een aanvaller mogelijk maakt vertrouwelijke bestanden te lezen.

Opvallend is dat de het uitvoeren van de patch er slechts voor zorgt dat de kwetsbaarheid niet meer voorkomt in nieuwe "storage zones" die aangemaakt worden na het patchen. Om de kwetsbaarheid ook te verwijderen in eerder gecreëerde "storage zones" is het nodige mitigerende acties uit te voeren op alle storage servers in het cluster.

Onderzoekers van [DIVD](https://www.divd.nl) hebben via een scan een aantal nog kwetsbare, Nederlandse, Citrix ShareFile systemen geconden. Het Security Meldpunt heeft gaat de beheerders van deze systemen waarschuwen.

Voor meer en actuele informatie en advies zie onze [case pagina](/DIVD-2020-00007/).

### English

On May 5th Citrix has informed customers that use the Citrix ShareFile solution of three vulnerabilities in this product and has made patches and mitigation tools [available](https://support.citrix.com/article/CTX269341) to adress them. 

Citrix has not disclosed technical details about these vulnerabilities, but reseacher [Dimitri van de Giessen](https://twitter.com/DimitriNL) has published that at least one of the vulnerabilities is the result of the use of an outdated Ajax component with a vulnerability that allow an attacker to access confidential files.

Please take note that applying the patches only resolves this vulnerabilty for "storage zones" that are newly created after the patch has been applied. To resolve the vulnerability for pre-existing "storage zones", a mitigation tool must be applied to all storage servers in the cluster.

[DIVD](https://www.divd.nl) researchers have scanned for vulnerable, Dutch, ShareFile server. [The Security Hotline](https://www.securitymeldpunt.nl) will contact the administrators of these servers.

For more and up to date information and advice, please look at our [case page](/DIVD-2020-00007/).
