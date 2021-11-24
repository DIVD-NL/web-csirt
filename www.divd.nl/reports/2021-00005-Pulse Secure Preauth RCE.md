---
title: Report DIVD-2021-00005-Pulse Secure Preauth RCE
date: 23 November, 2021
author: Gerard Janssen
excerpt: Pulse Secure published an advisory in response to recently discovered critical vulnerabilities in the (VPN) product Pulse Connect Secure (PCS), version 9.0R3 and higher
---
<header>
    <h2>Report DIVD-2021-00005– Pulse Secure Preauth RCE</h2>
    <span>August 25th, 2021 by Gerard Janssen</span>
</header>
Case Lead: Matthijs Koot

Researchers: Lennaert Oudshoorn and Victor Gevers

Pulse Secure VPN is the market leader in online security solutions for enterprises. With Pulse Connect Secure (PCS), enterprises ‘can enable Zero Trust secure access to hybrid IT resources for an increasingly mobile workforce.’ Pulse VPN is widely used at universities, hospitals, energy companies, and banks. The company behind this software is Pulse Secure LLC, located in San Jose, California. (December 2020 Pulse Secure was acquired by the company Ivanti)

On April 20, 2021, Pulse Secure published an advisory in response to recently discovered critical vulnerabilities in the (VPN) product Pulse Connect Secure (PCS), version 9.0R3 and higher. Those vulnerabilities were discovered because they were exploited by foreign state actors. Security firm Mandiant (FireEye) investigated intrusions at defense, government, and financial organizations worldwide. Mandiant observed UNC2630 harvesting credentials from Pulse Secure login flows. With these credentials, an attacker can gain access to the internal networks and move laterally through the compromised networks. Mandiant already found 16 malware families exclusively designed to infect Pulse Secure VPN devices.

Based on an analysis by Pulse Secure (Avanti), it is suspected that some intrusions were due to the exploitation of previously disclosed Pulse Secure Vulnerabilities from 2019 (see also https://csirt.divd.nl/cases/DIVD-2020-00009/). Other intrusions were due to the exploitation of a previously unknown authentication bypass vulnerability that was discovered in April 2021 (CVE-2021-22893).

Since April 21, DIVD has been investigating all the Netherlands-linked Pulse Connect Secure systems that could be found in Shodan and BinaryEdge on that same day. On this basis, DIVD sent out notifications after the (security) update of Pulse Secure.

## Timeline

| Date  | Description |
|:-----:|-------------|
| 20-04-2021 | Pulse Secure (Ivanti) publishes a temporary measure (workaround). |
| 20-04-2021 | FireEye publishes extensive technical details. |
| 20-04-2021 | NCSC publishes the initial version of security advisory NCSC-2021-0345. |
| 21-04-2021 | DIVD starts investigation. |
| 21-04-2021 | Upon request, DIVD will share an initial (unevaluated) list of ~650 Netherlands-linked PCS systems on which the temporary measure is not yet active with the Dutch CERT community. |
| 03-05-2021 | Pulse Secure (Ivanti) makes a new PCS version available to all PCS customers. |
| 10-05-2021 | DIVD sends out first targeted notifications about systems on which a vulnerable PCS version is active without the temporary measure. |
| 06-06-2021 | Second round notifications sent by DIVD CSIRT. |
| 16-06-2021 | DIVD shares data with the Digital Trust Center of the Ministry of Economic Affairs so that they can approach companies that still use these vulnerable systems. |
| 15-07-2021 | DIVD shares data about the last vulnerable systems with a Pulse software reseller in the Netherlands, hoping that they can still reach some stragglers. |
| 01-08-2021 | After four notification attempts through different channels, the case is closed. |

https://www.fireeye.com/blog/threat-research/2021/04/suspected-apt-actors-leverage-bypass-techniques-pulse-secure-zero-day.html
