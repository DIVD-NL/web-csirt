---
title: Report DIVD-2020-00012 - Scanning 49,577 Vulnerable Fortinet VPN Devices
date: 12 May 2021
author: Jeroen van de Weerd
excerpt: A total of 34,830 notifications were sent to companies and agencies with vulnerable Fortinet VPN devices. We received some positive responses.
---
<header>
    <h2>Report DIVD-2020-00012 - Scanning 49,577 Vulnerable Fortinet VPN Devices</h2>
    <span>12 May by Jeroen van de Weerd</span>
</header>
</BR>Case lead: Frank Breedijk

</BR>On November 19, 2020, a threat intelligence analyst found a list of 49,577 Fortinet VPN devices that appear to be vulnerable to [CVE-2018-13379](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-13379). This vulnerability allows an attacker, via a modified HTTP request, to retrieve system files to which they should not normally have access. By requesting the sslvpn_websession file, it is possible to steal users' login credentials. This is an older vulnerability, which has been warned about and brought to attention several times.

Fortinet VPN is a common VPN solution that companies and agencies use to gain remote access to their network. Vulnerabilities like these may be of interest to ransomware groups and APT’s. Therefore, a vulnerability present in this solution is highly undesirable and should be resolved immediately.

Researchers from DIVD CSIRT ran multiple global scans with nmap, a .nse script was used. The results were compared with the list of vulnerable Fortinet VPN devices. On 25 November 2020, the researchers started comparing the results. This way, they were able to verify that the systems on the list were indeed vulnerable.

A total of 34,830 notifications were sent to companies and agencies with vulnerable Fortinet VPN devices. We received some positive responses.

As there were no other responses the case is closed. By means of the [FortiGuard PSIRT Advisory](http://www.fortiguard.com/psirt/FG-IR-18-384) you can check if your Fortinet VPN device is vulnerable.
