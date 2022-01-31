---
title: Report DIVD-2020-00014 - Solarwinds Orion 
date: 28 January, 2022
author: Gerard Janssen
excerpt: the DIVD scanned for vulnerable Solarwind Orion systems.
---
<header>
    <h2>REPORT DIVD-2020-00014 - SOLARWINDS ORION</h2>
    <span>28 January 2022 by Gerard Janssen</span>
</header>
Case lead: Barry van Kampen\
Researcher: Matthijs Koot


On December 8, 2020, FireEye announced that the company had fallen victim to a hack. FireEye is a privately held cybersecurity company headquartered in Milpitas, California. The company provides hardware, software, and services to investigate cybersecurity attacks, protect against malicious software, and analyze IT security risks. 

A few days later, it turned out that not only FireEye had been hit by the attack. The attack had been going on for months and had hit many other major companies, including Microsoft, Cisco, Intel, Nvidia, VMware, Deloitte, Malwarebytes, and various US government agencies. 

The attackers took advantage of a backdoor in Orion, a software package from the company Solarwinds. SolarWinds’ Orion system provides centralized monitoring across an organization’s entire IT stack. 

According to a statement by SolarWinds, the hackers already gained access to SolarWinds’ software development system in October 2019. They inserted a vulnerability in Orion software updates, dubbed SUNBURST, which was installed by customers in the spring of 2020. Solwarwind said it notified 33,000 customers, among them US government agencies, major private corporations, and Fortune 500 businesses. 

By analyzing the attack, security researchers from Symantec, Palo Alto Networks and Guidepoint found another backdoor, likely coming from a different threat actor (CVE-2020-10148), this vulnerability was also used by attackers to deliver malware, and was called Supernova.

The DIVD scanned for Supernova and found around 700 vulnerable Solarwinds Orion systems facing the internet, worldwide, including systems of foreign defense units and satellite communication. Eight of these systems used IP addresses from the Netherlands.

## Timeline

| Date | Description |
|:-----:|-------------|
|15-12-2020| GuidePoint Security posted an analysis of a web shell called Supernova |
|16-12-2020| Matthijs Koot found around 700 Solarwinds Orion systems facing the internet, worldwide.  |
|23-12-2020| Patches for this vulnerability released by SolarWinds |
|26-12-2020| Vulnerability publicly known |
|27-12-2020| 581 vulnerable systems still active |
|28-12-2020| 549 vulnerable systems were reported to NCSC-NL |

## Links

- [Solarwinds: Security Advisory](https://www.solarwinds.com/sa-overview/securityadvisory)
- [Fireye blog](https://www.fireeye.com/blog/products-and-services/2020/12/fireeye-shares-details-of-recent-cyber-attack-actions-to-protect-community.html)
- [Symantec blog](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/sunburst-supply-chain-attack-solarwinds)

