---
layout: case
title: "Zyxel - OS command injection "
author: Koen Schagen
lead: Koen Schagen
excerpt: "Two OS command injection vulnerabilities via quick.cgi file are found in QNAP QTS, QuTS hero and QuTScloud software/firmware versions"
researchers:
- Koen Schagen
cves:
- CVE-2024-29972
- CVE-2024-29973
- CVE-2024-29975
product:
- Zyxel NAS326
- Zyxel NAS542
versions: 
- NAS326 - V5.21(AAZF.16)C0 and earlier
- NAS542 - V5.21(ABAG.13)C0 and earlier
recommendation: "If you have a any of the vulnerable firmware/software version on your Zyxel NAS device, please update it to the latest version."
patch_status: Released
status : Open
start: 2024-06-24
end:
timeline:
- start: 2024-06-24
  end:
  event: "DIVD starts researching the vulnerabilities."
- start: 2024-06-27
  end:
  event: "DIVD found a way to fingerprint vulnerable devices"
- start: 2024-06-28
  end:
  event: "First version of this casefile"
- start: 2024-06-28
  end:
  event: "DIVD starts scanning the internet for vulnerable devices"

#ips: 0

---
## Summary
Two (OS) command injection vulnerabilities have been found in QNAP devices. When exploited it's possible for attackers with network/internet access to execute CLI commands on your NAS device as an admin user. QNAP has linked {% cwe CWE-78 %} to both CVE's. This is related to 'Improper Neutralization of Special Elements used in an OS Command ("OS Command Injection")'.

## Recommendations

Zyxel recommends to upgrade to the latest firmware version, to benefit from vulnerability fixes. On the versions below, the mentioned vulnerabilities have been fixed:

- NAS326 -> V5.21(AAZF.17)C0 (released May 10th 2024), [NAS326 Firmware link](https://download.zyxel.com/NAS326/firmware/NAS326_V5.21(AAZF.17)C0.zip)
- NAS542 -> V5.21(ABAG.14)C0 (released May 10th 2024), [NAS542 Firmware link](https://download.zyxel.com/NAS542/firmware/NAS542_V5.21(ABAG.14)C0.zip)

DIVD recommends that you do not have this device reachable from the internet unless it is absolutely nessecary. If this is the case, a firewall rule should be placed in front of the Zyxel NAS device so that it can only be accessed from trusted IP addresses.

## What we are doing

DIVD is currently working to identify vulnerable parties and notifying these. We do this by finding Zyxel NAS devices connected to the internet and verifying if the device is running the latest firmware version to be protected against the above described threats. The notifications will be sent to the party responsible for the ip address according to the whois database.

{% include timeline.html %}

## More information

* {% cve CVE-2024-29972 %}
* {% cve CVE-2024-29973 %}
* {% cve CVE-2024-29975 %}
* [Zyxel Security Advisory 06-04-2024](https://www.zyxel.com/global/en/support/security-advisories/zyxel-security-advisory-for-multiple-vulnerabilities-in-nas-products-06-04-2024)
