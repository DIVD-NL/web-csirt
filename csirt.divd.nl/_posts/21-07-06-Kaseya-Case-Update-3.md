---
layout: post
title: Kaseya Case Update 3
author: Lennaert Oudshoorn
excerpt: "Since the start of the incident last Friday, the number of Kaseya VSA instances that are reachable from the internet has dropped from over 2.200 to less than 70 in our last scan today."
---

Since the first signs of an incident last Friday evening the DIVD has continued to monitor the internet for instances of Kaseya VSA that remained online. We are happy to report a steady decrease in the number of online servers.

The Dutch Institute for Vulnerability Disclosure (DIVD) performs a daily scan to detect vulnerable Kaseya VSA servers and notify the owners directly or via the known abuse channels, Gov-CERTs, and other trusted channels. After our initial incident response started Friday 2 of Jul 2021.
We have identified this server by downloading the paths ‘/’, ‘/api/v1.5/cw/environment’ and ‘/install/kaseyalatestversion.xml’ and matching patterns in these files.
The result of our latest scan worldwide:
![Graph with number of vulnerable hosts over time worldwide](/assets/images/DIVD-2021-00002-stats-3.png)

We are especially proud that we’ve successfully managed to reduce the number of instances in the Netherlands to zero:

![Graph with number of vulnerable hosts over time in the Netherlands](/assets/images/DIVD-2021-00002-stats-nl.png)

We feel at this point in time we can share more detailed numbers about the amount of systems that were discovered in our scans:

| Scan | Suspected instances | Delta | NL | Delta NL |
|:-------------:|-----|-----|-----|-----|
| baseline scan 1 | 2238 | - | 84 | - |
| baseline scan 2 | 2254 | +16 | 72 | -12 |
| 3-7 night | 591 | -1663 | 28 | -44 |
| 3-7 day | 197 | -394 | 3 | -25 |
| 4-7 | 138 | -59 | 0 | -3 |
| 5-7 | 88 | -50 | 0 | 0 |
| 6-7 | 68 | -20 | 0 | 0 |

## Continued advice
All on-premises VSA Servers should continue to remain offline until further instructions from Kaseya about when it is safe to restore operations.  A patch will be required to be installed prior to restarting the VSA and a set of recommendations on how to increase your security posture.


As this incident has taught us, having solid basics in terms of security is extremely important and will help prevent incidents like this. Some advise that is not specific to this case:
* Use MFA where available
* Remove admin interfaces from the public internet, for instance by placing them behind a VPN
* If something has to be on the internet work with an allow list for authorized addresses

##  Detection and incident response advice
Kaseya has released a [Detection tool](https://kaseya.app.box.com/s/0ysvgss7w48nxh8k1xt7fqhbcjxhas40) tool help determine if a system has been compromised.

Cado Security has made a github repository with [Resources for DFIR Professionals Responding to the REvil Ransomware Kaseya Supply Chain Attack](https://github.com/cado-security/DFIR_Resources_REvil_Kaseya/).

We recommend that any Kaseya server is carefully checked for signs of compromise before taking it back into service, including, but not limited to, the IoCs published by Kaseya.

## Resources with more information
[Important Notice July 5th, 2021](https://helpdesk.kaseya.com/hc/en-gb/articles/4403440684689-Important-Notice-July-3rd-2021)

[CISA-FBI Guidance for MSPs and their Customers Affected by the Kaseya VSA Supply-Chain Ransomware Attack](https://us-cert.cisa.gov/ncas/current-activity/2021/07/04/cisa-fbi-guidance-msps-and-their-customers-affected-kaseya-vsa)

As more details become available, we will report them on our [blog](https://csirt.divd.nl/blog/) and [case file](https://csirt.divd.nl/DIVD-2021-00002/).
