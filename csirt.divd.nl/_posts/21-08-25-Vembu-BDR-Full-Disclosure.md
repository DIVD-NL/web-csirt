---
layout: post
title: Vembu BDR Full Disclosure
author: Frank Breedijk
excerpt: "Full Disclosure on Vembu BDR vulnerabilities CVE-2021-26471, CVE-2021-26472 and CVE-2021-26473"
jekyll-secinfo:
  cve:
    url: /cves/CVE-

---

## Context

On 15 May 2021 we published case {% divd DIVD-2020-00011 %}, which dealt with four vulnerabilities in Vembu BDR and related products. These four vulnerabilities here confidentially reported to Vembu in November 2020 and again in Februari 2021.

## Current status

From recent scan data we know that the three most damaging vulnerabilities have practically seized to be present on the internet, therefore we have decided to release the full technical details on these vulnerabilities.

When we notified Vembu in March of this year we identified over a 1000 instanaces of Vembu BDR and related products with a least one vulnerability. Of these instances nearly 90 where also vulnerable to a Remote Code Execution vunerability (RCE). A rescan on the first of July showed a dramatic drop, only 55 vulnerable instances remained online of which only a hand full still cotained the RCE. A rescan in August confirmed that these number remain low and we now deam it save to release the full details on the vulnerabilities we foun, except for {% cve-2021-26474 %} is still present on over 50 internet facing system.

![Graph of found instances](/assets/images/vembu_graph.png)

## Technical details

The details of the disclosed vulnerabilities can be found in the links below:
* {% cve CVE-2021-26471 %} - unauthenticated RCE
* {% cve CVE-2021-26472 %} - unauthenticated RCE with SYSTEM privileges
* {% cve CVE-2021-26473 %} - unauthenticated arbitrary file upload and RCE
