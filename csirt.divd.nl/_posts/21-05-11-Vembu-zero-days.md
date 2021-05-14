---
layout: post
title: Vembu Zero Days
author: Gerard Janssen
excerpt: "
	DIVD-researcher Wietse Boonstra vond vier zerodays in de Vembu BDR en gerelateeerde software / 
	DIVD reseacher Wietse Boonstra has found four zero day vulnerabilities in Vembu BDR and related software
"
---


### Nederlands

DIVD researcher Wietse Boonstra vond vier zero-day kwetsbaarheden in Vembu BDR Suite, software die bedrijven helpt bij het maken van backups en 'disaster recovery'. Via een of meerdere van deze kwetsbaarheden kan een aanvaller een kwetsbaar Vembu BDR systeem overnemen en toegang krijgen tot de opgeslagen data. Geen van de kwetsbaarheden was eerder gepubliceerd.
 
Tijdens een pentest in januari vond Boonstra vier lekken. Via commando's in de webbrowser lukte het om in te breken op het Vembu-systeem van een van Boonstra's klanten. Een kwetsbaarheid in dit soort software is ernstig. Backup en recovery-software grijpt per definitie diep in op het systeem van gebruikers van van Vembu. Volgens de eigen Vembu-site maken NASA, Samsung, Fujitsu en Epic Games gebruik van Vembu BDR Suite. De DIVD zal beheerders van netwerken waarin kwetsbare installaties staan de komende dagen waarschuwen.

Boonstra vond vier kwetsbaarheden. Drie daarvan zijn remote code execution (RCE) kwetsbaarheden, die vaak beschouwd worden als de ernstigste kwetsbaarheden. De vierde kwetsbaarheid is een Server-side request forgery (SSRF), die het mogelijk maakt om de toegangscontrole tot een systeem te omzeilen.

Boonstra meldde de lekken bij Vembu, maar kreeg aanvankelijk geen respons. Via andere kanalen lukte het de DIVD half februari wel contact te krijgen met Vembu. Vembu antwoordde dat de kwetsbaarheden al bekend waren en opgelost in de laatste versies van de software. Klanten kregen echter alleen een update als ze er actief om vroegen. Na enig aandringen van de DIVD is de gepatchte versie in april toch online gekomen. 

Nader onderzoek leert dat de kwetsbaarheden mogelijk ook in andere door Vembu gemaakte, producten voorkomt en dat de Server Side Request Forgery kwetsbaarheid zelfs in veel van deze producten voorkomt.


Zie ook: [case DIVD-2020-00011](/DIVD-2020-00011/)


### English

DIVD researcher Wietse Boonstra found four zero-day vulnerabilities in Vembu BDR Suite, software that helps companies make backups and 'disaster recovery'. An attacker can take over a vulnerable Vembu BDR system and gain access to the stored data via one or more of these vulnerabilities. None of the vulnerabilities had been previously published.
 
During a pentest in January, Boonstra found four leaks. Via commands in the web browser it was possible to break into the Vembu system of one of Boonstra's customers. A vulnerability in this type of software is serious. This kind of backup and recovery software by definition has a deep impact on the system. Vembu's customers are both small companies and large organizations. According to its own Vembu site, NASA, Samsung, Fujitsu, and Epic Games are using Vembu BDR Suite. The DIVD will warn administrators of networks containing vulnerable installations in the coming days.

Boonstra found four vulnerabilities. Three of these are remote code execution (RCE) vulnerabilities, which are often considered the most serious vulnerabilities. The fourth vulnerability is a Server-side request forgery (SSRF), which makes it possible to bypass access control to a system.

Boonstra reported the leaks at Vembu, but initially received no response. The DIVD did manage to get in touch with Vembu through other channels in mid-February. Vembu replied that the vulnerabilities were already known and fixed in the latest versions of the software. However, customers only got an update when they actively asked for it. After some urging from the DIVD, the patched version came online in April.

Further research has showed that these vulnerabilities are also present in other products created by Vembu. The Server Side Request FOrgery is even present in a lot of their products.


For more information: [case DIVD-2020-00011](/DIVD-2020-00011/)
