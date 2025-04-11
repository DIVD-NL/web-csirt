---
layout: post
title: SicommNet Basec product warning
author: DIVD
excerpt: "There are three serious vulnerabilities in the Basec tool hosted by SicommNet that allow attackers to bypass all security measures in the tool. Theses vulnerabilities have been present since at least 14 December 2021."
---
DIVD researcher Jesse Meijer has identified three critical vulnerabilities in the SicommNet BASEC e-procurement system. These vulnerabilities were discovered on the 14th of December 2021. With these vulnerabilities an attacker can bypass all security measures in the tool and access and alter the database of the tool and all data for any customer of SicommNet BASEC.

Bespite several attempts over the years, neither Jesse Meijer, DIVD CSIRT nor CISA has been able to sollicit a meaningful response of from SicommNet. In line with our [CNA policy](/cna) we are now issuing this product warning.

## Product warning

If you are currently using or in the past have used SicommNet BASEC, we urge you to:
* Stop using the tool
* Consider all data in the tool compromised:
	- Do not trust any data in the tool, because it might have been altered by a malicious actor
	- Consider all data in the tool as leaked
	- Inform any person of which personal identifiable data (PII) is stored in the tool that their PII has leaked
	- Inform any overseeing bodies of a data leak (if applicable)

Our case file [DIVD-2025-00001](/DIVD-2025-00001) contains the full details of the vulnerabilities found.

The vulnerabilities are:
* {% cve CVE-2025-22371 %} - SQL-injection in admin_login_handler allows unauthenticated user to log in as an administrator in SicommNet BASEC
* {% cve CVE-2025-22372 %} - Insecure password storage in SicommNet BASEC
* {% cve CVE-2025-22373 %} - XSS, HTML and Style injection on login page of SicommNet BASEC