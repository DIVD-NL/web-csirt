---
layout: post
title: SmarterTrack Full disclosure
author: Finn van der Knaap
excerpt: "Full disclosure of vulnerabilities we discovered in SmarterTrack"
---
On 27 October 2021 [Wietse Boonstra](https://www.divd.nl/Wietse%20Boonstra) found several vulnerabilities in the latest version of SmarterTrack. There were [two](/CVE-2022-24384) [XSS](/CVE-2022-24386), an [unauthenticated download](/CVE-2022-24385) and an [upload / overwrite vulnerability](/CVE-2022-24387).

Today we are releasing case [DIVD-2021-00029](/DIVD-2021-00029) and are disclosing the details of the four CVEs.

CVE: CVE-2022-24384
Case: DIVD-2021-00029
Discoverd by: Wietse Boonstra
Credits: Discovered by Wietse Boonstra of DIVD
Products: SmarterTools - SmarterTrack V100.0.8019.14010
CVSS: X
Reference: https://csirt.divd.nl/cases/DIVD-2021-00029/, https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24384, https://csirt.divd.nl/cves/CVE-2022-24384/
Solution: Upgrade to latest version

Description: Cross-site Scripting (XSS) vulnerability in SmarterTools SmarterTrack 

POC: open the URL to the portal and simply add any type of script behind a URL with, for example, an error message. This is a working example script:
{SMARTERTRACK_URL}/Main/Default.aspx?viewSurveyError=Unknown+survey"><img%20src=x%20onerror=alert(1)>

Impact: When this attack is performed, the attacker can do any action that the user also can do. Fortunately, the attacker can't access any password from this attack since the credentials are protected. But the attacker can still see sensitive data and modify this.

*image 1*

