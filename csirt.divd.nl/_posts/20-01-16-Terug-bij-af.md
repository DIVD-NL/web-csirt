---
layout: post
title: Citrix mitigatie blijkt niet betrouwbaar / Citrix mitigation turns out to be unreliable
author: Frank Breedijk
excerpt: De mitigatie voorgesteld door Citrix lijk onbetrouwbaar. Terug bij af. 😢 / Citrix's mitigation is unreliable. We are back to square one 😢
---

Zojuist kwam het NCSC met [dit nieuwsbericht](https://www.ncsc.nl/actueel/nieuws/2020/januari/16/door-citrix-geadviseerde-mitigerende-maatregelen-niet-altijd-effectief). 

Onze interpretatie van dit bericht is dat het uitvoeren van de mitigatie niet voldoende (b)lijkt te zijn om de kwetsbaarheid van het systeem weg te nemen. Het is zeker dat de mitigatie niet gewerkt heeft op bepaalde versies van Citrix ADC en over alle andere versies is twijfel.

Aangezien de scan van het Security Meldpunt alleen kon vaststellen of de mitigatie op een systeem is uitgevoerd, betekent dit ook dat daarmee de scan onbetrouwbaar is geworden. We hebben daarom besloten het scannen en notificeren op te schorten tot het moment dat we weer een betrouwbare scan kunnen ontwikkelen.

We zijn terug bij af 😢

<hr>

### <a name="english"></a>English

Earlier this evening the Dutch NCSC released [this news article](https://www.ncsc.nl/actueel/nieuws/2020/januari/16/door-citrix-geadviseerde-mitigerende-maatregelen-niet-altijd-effectief) ([translation by google](https://translate.google.com/translate?hl=&sl=auto&tl=en&u=https%3A%2F%2Fwww.ncsc.nl%2Factueel%2Fnieuws%2F2020%2Fjanuari%2F16%2Fdoor-citrix-geadviseerde-mitigerende-maatregelen-niet-altijd-effectief). 

Our interpretation of this article is that implementing the mitigation suggested by Citrix seem to be/is not sufficient to remove the vulnerability from the system. It is certain that this mitigation was not effective on certain ADC versions and there is doubt about its effectiveness on other versions.

Since our scan only detects if the mitigations are installed or not, this is not a reliable indicator of the vulnerability of the system, the results of our scans are not reliable either. We have therefore determined to stop scanning for now and wait until we can develop a reliable scan again.

We are back to square one 😢
