---
title: Report DIVD-2021-00010-vCenter Server Preauth RCE
date: February 19, 2022
author: Gerard Janssen
excerpt: On 25 May 2021, VMware published an advisory – a recommendation – to install updates for the vSphere Web Client. 

---

<header>
    <h2>Report DIVD-2021-00010– vCenter Server Preauth RCE</h2>
    <span>February 19th, 2022 by Gerard Janssen</span>
</header>
Case Lead: Victor Gevers<br>
Researchers: Lennaert Oudshoorn and Hidde Smit

VMware, Inc. is an American cloud computing and virtualization technology company with headquarters in California. vSphere Web Client is an interface that administrators use to access VMware hosts.
Researchers found a vulnerability in versions  7.0, 6.7, 6.5, 4.x, 3.x of vSphere Web Client, due to lack of input validation in the Virtual SAN Health Check plug-in, which is enabled by default in vCenter Server (CVE-2021-21985)

A malicious actor with network access to port 443 could exploit this vulnerability to execute commands with unrestricted privileges on the underlying operating system. Since May 31, volunteers of the DIVD performed various scans, looking for vulnerable systems on port 443. The scope of the scan is a combination of Shodan and BinaryEdge results. The DIVD sent notifications about the vCenter vulnerability to system owners. 

DIVD has used the following indicators to conclude if a system is vulnerable:<br>
* vCenter server version 7.0, 6.7, 6.5, 4.x or 3.x.
* build version (patched builds are: 17958471, 18010531, 17994927).
* Availability of API endpoint indicating the possibility to exploit.


## Timeline

| Date  | Description |
|:-----:|-------------|
| 25-05-2021 | VMWare publishes an advisory. |
| 31-05-2021 | DIVD starts a daily scan and  finds 1691 (exploitable) systems and another 1046 which are (likely) vulnerable. |
| 01-06-2021 | 1684 exploitable (and another 1091 likely vulnerable) systems.  |
| 02-06-2021 | 1666 exploitable (and 1084 likely vulnerable) systems. |
| 03-06-2021 | 1451 exploitable (and 1186 likely vulnerable) systems. |
| 27-07-2021 | 639 exploitable (and 1079 likely vulnerable) systems. |
| 23-11-2021 | 156 vulnerable/exploitable and 888 likely vulnerable systems. |
| 30-11-2021 | Case closed. |

## Links

[VMware Advisory](https://www.vmware.com/security/advisories/VMSA-2021-0010.html)
