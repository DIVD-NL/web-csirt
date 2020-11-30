---
layout: post
title: Wederom Citrix meldingen / Citrix notifications again
author: Frank Breedijk
excerpt: Op nog 70 systemen ontbreekt elke vorm van mitigatie, we gaan weer waarschuwen / We have identified 70 systems that still don't have any mitigation in place, we are notifying again
---

### Nederlands

Op 70 van de 546 initieel door ons geïdentificeerde kwetsbare systemen is nog steeds geen enkele vorm van mitigatie toegepast. Van deze systemen kan met zekerheid worden aangenomen dat ze reeds door kwaadwillende zijn overgenomen. Wij gaan contact proberen op te nemen met eigenaren/gebruikersorganisaties van de systemen en beheerders van de netwerken waarin deze systemen staan met de volgende boodschap:

```
L.S.,

(English below)

SecurityMeldpunt.nl (onderdeel van divd.nl) houdt op dit moment actief bij op welke 
Citrix Application Delivery Controllers in Nederland, de door Citrix op 17 december 
aangeraden mitigatie mbt CVE-2019-19781 nog niet is aangebracht.

Hieronder vind u een lijst van Citrix servers die horen bij uw organisatie of 
waarvan is vastgesteld dat ze staan opgesteld in een netwerk waarvoor u verantwoordelijk 
bent.

Van deze kwetsbaarheid wordt door kwaadwillenden (computercriminelen) op grote schaal 
geautomatiseerd misbruik gemaakt. Het is bekend dat zij dit lek gebruiken om gevoelige 
informatie (persoonsgegevens, concurrentiegevoelige informatie, intellectueel eigendom, 
bedrijfgeheimen, etc) te stelen, cryptomunten te minen en het netwerk verder binnen 
te dringen om daar onder andere gijzelsoftware te installeren. 
(https://www.zdnet.com/article/hackers-target-unpatched-citrix-servers-to-deploy-ransomware/)

Op basis van wat wij nu zien is het zeker dat de onderstaande systemen:
* Nog steeds kwetsbaar zijn;
* Hierop zelfs de eerste basismaatregelen zoals deze door CItirx zijn voorgeschreven op 
  17-12 nog niet (succesvol) zijn uitgevoerd.

U kunt ervan uit gaan dat deze systemen reeds zijn overgenomen door een hacker. We raden 
u dan ook aan om:
* Deze systemen onmiddellijk offline te halen;
* Een onderzoek in te stellen om vast te stellen of de aanvallers het achterliggende netwerk 
  (het bedrijfsnetwerk) zijn binnengedrongen;
* Melding te maken van een datalek bij de voor u geldende autoriteiten (in Nederland de 
  Autoriteit persoonsgegevens).

Wij doen een dringend beroep op netwerkbeheerders om toegang van en naar deze systemen te 
blokkeren omdat zij een gevaar voor uw netwerk en de algemene veiligheid van het internet 
vormen.

Op onze case pagina staat een actueel overzicht van de stand van zaken: 
https://www.securitymeldpunt.nl/cases/DIVD-2020-00001/
 
Met vriendelijke groet,
securitymeldpunt.nl
Onderdeel van DIVD.nl
meldpunt@divd.nl

``` 

De [case pagina](/DIVD-2020-00002) geeft een overzicht van de situatie.

![Grafiek met aantal ongemitigeerde systemen](/assets/images/CitrixADC_graph.png "Ongemitigeerde systemen")

<hr>

### English

We have identified that mitigations are still missing on 70 of the 546 systems we initially identified as vulnerable. It can be assumed with certainty that these systems have already been compromised by now. We are going to contract the organisations that use these systems and the administrators responsible for the network they are in with the following message:


```
L.S.,

SecurityMeldpunt.nl (part of divd.nl) is currently actively tracking Citrix Application 
Delivery Controllers in The Netherlands for which the mitigations recommended by Citrix 
against vulnerability CVE-2019-19781 have not been implemented yet.

Attached you will find a list of Citrix servers that either belong to your organisation 
or are located in a network for which you are responsible. 

Bad actors (cyber criminals) are actively and automatically abusing this vulnerbility 
to penetrate systems. After penetration they use the Citrix systems to steal sensitive 
information (personal identifiable information, intellectual property, company secrets, 
etc), mine cryptocurrency, and penetrate the corporate network e.g. to install 
ransomware. 
(https://www.zdnet.com/article/hackers-target-unpatched-citrix-servers-to-deploy-ransomware/)

Based on our latest scans we are sure of the following:
* The systems listed below are still vulnerable;
* Even the first basic mitigation steps as described by Citrix on the 17th of December 
  have not been (successfully) taken.

You will have to assume that these systems have been succesfully compromised. We 
recommend you to:
* Take these systems offline;
* Start an investigation to determine if the attached (corporate) networks have been 
  compromised;
* Inform the proper authorities of a data leak (for The Netherlands: inform the Autoriteit 
  Persoonsgegevens).

We are urgently requesting network administrators to block access to and from these systems, 
because they are a threat to the safety/security of your network and the internet as a whole.

On our case page you can find the current state of affairs with regards to this vulnerability: 
https://www.securitymeldpunt.nl/cases/DIVD-2020-00001/ 

Kind regards,
securitymeldpunt.nl
Part of DIVD.nl
meldpunt@divd.nl

``` 

The [case page](/DIVD-2020-00002) has on overview.

![Graph of unmitigated systems](/assets/images/CitrixADC_graph.png "Unmitigated systems")
