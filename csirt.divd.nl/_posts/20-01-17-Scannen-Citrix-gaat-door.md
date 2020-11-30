---
layout: post
title: We gaan weer door met scannen en melden ! / We have resumed scanning and notifying !
author: Frank Breedijk
excerpt: Ondanks de onzekerheid over de effectiviteit van de Citrix mitigatie gaan wij door met scannen en melden, lees hier waaarom. / Even tought the effectiveness of the mitigation is unknown we are continuing our Citrix scanning and notification efforts. Read why.
---

Gisteren [meldde ik](/2020/01/16/Terug-bij-af/) dat wij zouden stoppen met het scannen en melden van kwetsbare Citrix ADC's naar aanleiding van [dit bericht](https://www.ncsc.nl/actueel/nieuws/2020/januari/16/door-citrix-geadviseerde-mitigerende-maatregelen-niet-altijd-effectief) van het NCSC. Inmiddels hebben we, na overleg met mijn collega's van het meldpunt en het [DIVD](https://www.divd.nl) besloten toch door te gaan.

Waarom?
* Hoewel de mitigatie mogelijk niet voldoende bescherming biedt, is een systeem met mitigatie toch beter beschermd dan een systeem zonder.
* Een systeem waarop geen mitigatie is toegepast is een systeem wat niet "op de kaart staat", door onze melding komt dit systeem mogelijk wel in het zicht van de beheerder.

We willen nadrukkelijk melden aan iedereen die een bericht heeft gehad van een ongemitigeerd system, dat dit systeem waarschijnlijk al is overgenomen en dat het wenselijk is het system te onderzoeken (mogelijk met behulp van [deze informatie](/2020/01/15/How-to-check-your-Citrix-gateway/)).

We gaan weer aan de slag! 

<hr>

### <a name="english"></a>English

Yesterday [I reported](/2020/01/16/Terug-bij-af/) that we would stop scanning for vulnerable Citrix ADC's. [This article](https://www.ncsc.nl/actueel/nieuws/2020/januari/16/door-citrix-geadviseerde-mitigerende-maatregelen-niet-altijd-effectief) by the Dutch NCSC was at the basis of this discussion ([translation by google](https://translate.google.com/translate?hl=&sl=auto&tl=en&u=https%3A%2F%2Fwww.ncsc.nl%2Factueel%2Fnieuws%2F2020%2Fjanuari%2F16%2Fdoor-citrix-geadviseerde-mitigerende-maatregelen-niet-altijd-effectief)). 

After discussion with my colleagues at the Security Hotline and [DIVD](https://www.divd.nl) we decided to go on with scanning and notifying.

Why?
* While the mitigation may not be 100% effective, a system with this mitigation is still less vulnerable then a system without.
* A system that does not have the mitigations by now is likely "forgotten", by sending out notifications we hope to bring those systems under the attention of those that can "fix" them.

We want to explicitly report everyone that has received a notification from us about an unmitigated system that unmitigated systems at this point are likely already compromised. It is advisable to check the system (possibly with the help of [this information](/2020/01/15/How-to-check-your-Citrix-gateway/)).

We are back at it again!
