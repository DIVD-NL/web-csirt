---
layout: post
title: Kaseya Full Disclosure
author: Fank Breedijk
excerpt: We are disclosing the full details of the vulnerabilities we found in Kaseya VSA in June of 2021
---
In honor of our appearance on the [Ransomware Files podcast episode #5](https://www.bankinfosecurity.com/interviews/ransomware-files-episode-6-kaseya-revil-i-5045) we are releasing the full details of the vulnerabilities we found during our research into Kaseya VSA of which some were used by REvil to attack Kaseya's customers.

The details can be found in our CVE entries:
* [CVE-2021-30116](/CVE-2021-30116/) - Unauthenticated credentials leak via client download page
* [CVE-2021-30117](/CVE-2021-30117/) -  SQL injection in Kaseya VSA Unified Remote Monitoring & Management (RMM)
* [CVE-2021-30118](/CVE-2021-30118/) - Unauthenticated Arbitrary File Upload with Web server rights
* [CVE-2021-30119](/CVE-2021-30119/) - Authenticated reflective XSS
* [CVE-2021-30120](/CVE-2021-30120/) - Bypass 2FA
* [CVE-2021-30121](/CVE-2021-30121/) - Semi-authenticated local file inclusion
* [CVE-2021-30201](/CVE-2021-30201/) - Unauthenticated XML Entity Attack (XXE)

In addition, we have published a [translation of the chapter on Kaseya VSA](https://www.divd.nl/reports/2021-00002-Kaseya%20VSA%20behind%20the%20scenes/) from Gerard Jansssen's book [Hackers](https://www.thomasrap.nl/boek/hackers/) which gives a behind the scenes look at what happened at the time.