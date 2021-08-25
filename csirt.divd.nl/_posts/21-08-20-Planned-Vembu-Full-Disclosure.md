---
layout: post
title: Planned Vembu Full Disclosure
author: Frank Breedijk
excerpt: "The full details of 3 of the 4 Vembu vulnerabilities will be disclosed on 25 August 2021"
jekyll-secinfo:
  cve:
    url: /cves/CVE-
---

If you are using Vembu BDR version 3.7.0, 3.9.1 Update 1, 4.2.0 or 4.2.0.1 and have your instances exposed to public internet, you are strongly advices to upgrade to Vembu BDR v4.2.0.2.

On the 25th of August we plan to release the full details of the following CVEs:
* {% cve cve-2021-26471 %},
* {% cve cve-2021-26472 %}, and 
* {% cve cve-2021-26473 %}

All of these vulnerabilities are unauthenticated remote code execution vulnerabilities.