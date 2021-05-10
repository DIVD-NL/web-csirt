---
layout: post
title: Vembu Zero Days
author: Gerard Janssen
excerpt: DIVD-researcher Wietse Boonstra vond vier zerodays in de Vembu back up software
---

Het probleem
============

DIVD researcher Wietse Boonstra heeft vier zero-day kwetsbaarheden gevonden in Vembu BDR Suite. Twee daarvan maken het voor aanvallers mogelijk om op afstand code te implementeren, die daarmee een systeem kunnen de overnemen of saboteren. Geen van de kwetsbaarheden was eerder beschreven.

Tijdens een pentest in januari vond Boonstra vier lekken in de software die bedrijven helpt bij het maken van backups en 'disaster recovery'. De software is gemaakt voor zowel kleine bedrijven als grote organisaties. Volgens de eigen Vembu-site maken NASA, Samsung, Fujitsu en Epic Games gebruik van Vembu BDR Suite. Dit soort backup en recovery-software grijpt per definitie diep in op het systeem. Een kwetsbaarheid in dit soort software is ernstig. Via een paar eenvoudige commando's in de browser is het voor iedereen mogelijk om in te breken op het systeem. De DIVD zal beheerders van netwerken waarin kwetsbare installaties staan de komende dagen waarschuwen.

Boonstra vond vier kwetsbaarheden. Twee daarvan zijn zijn remote code execution (RCE) kwetsbaarheden, die vaak beschouwd worden als de ernstigste kwetsbaarheden. De derde kwetsbaarheid is een Server-side request forgery (SSRF), die het mogelijk maakt om de toegangscontrole tot een systeem te omzeilen. De vierde kwetsbaarheid maakt het mogelijk om zonder in te loggen files te uploaden.

Boonstra probeerde de lekken te melden bij Vembu, maar vond aanvankelijk geen gehoor. Via andere kanalen lukte het half februari wel contact te krijgen met Vembu. Vembu antwoordde dat de kwetsbaarheden al bekend waren en opgelost in de laatste versies van de software. Klanten kregen echter alleen een update als ze er actief om vroegen. Na enig aandringen van de DIVD is de gepatchte versie in april toch online gekomen. 


### English

DIVD researcher Wietse Boonstra has found four zero-day vulnerabilities in Vembu BDR Suite. Two of these make it possible for attackers to implement code remotely, which can take over or sabotage a system.

During a pentest in January, Boonstra found four leaks in the software that helps companies make backups and 'disaster recovery'. The software is made for both small companies and large organizations. According to its own Vembu site, NASA, Samsung, Fujitsu and Epic Games are using Vembu BDR Suite. This kind of backup and recovery software, by definition, has a deep impact on the system. A vulnerability in this type of software is serious. With a few simple commands in the browser it is possible for anyone to break into the system. A first scan of DIVD found 1079 vulnerable systems.

Boonstra found four vulnerabilities. Two of these are remote code execution (RCE) vulnerabilities, which are often considered the most serious vulnerabilities. The third vulnerability is a Server-side request forgery (SSRF), which makes it possible to bypass access control to a system. The fourth vulnerability makes it possible to upload files without logging in.

Boonstra tried to report the leaks to Vembu, but initially found no response. Via other channels it was possible to get in touch with Vembu in mid-February. Vembu replied that the vulnerabilities were already known and fixed in the latest versions of the software. However, customers only got an update when they actively requested it. After some urging from the DIVD, the patched version came online in April.