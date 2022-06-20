---
title: Report DIVD-2020-00007 Citrix ShareFile
date: 31st June 2021
author: Jeroen van de Weerd
excerpt: On May 5, 2020, Citrix released a security advisory for the Citrix ShareFile product. The vulnerabilities allow an attacker to potentially compromise the storage zone controller and gain access to sensitive ShareFile documents and folders.
---
<header>
    <h2>Report DIVD-2020-00007 - Citrix ShareFile</h2>
    <span>31st of June by Jeroen van de Weerd</span>
</header>
Case lead Lennaert Oudshoorn
Researchers: Lennaert Oudshoorn

On May 5, 2020, Citrix released a security advisory for the Citrix ShareFile product. (https://support.citrix.com/article/CTX269106) The three vulnerabilities listed here allow an attacker to potentially compromise the storage zone controller and gain access to sensitive ShareFile documents and folders. The newly found vulnerabilities apply to Citrix ShareFile storage zone controllers that are on-premises and self-managed. The vulnerabilities have been assigned the following CVE numbers.

- CVE-2020-7473
- CVE-2020-8982
- CVE-2020-8983

The vulnerabilities are found in the following versions:
- ShareFile storage zones Controller 5.9.0, 5.8.0, 5.7.0, 5.6.0, 5.5.0
- All earlier versions of ShareFile StorageZones Controller

Citrix ShareFile is an enterprise file sharing solution that allows employees to securely exchange company-owned and sensitive corporate data with each other. You can also use the software to lock or completely erase potentially compromised mobile devices.

There is a mitigation available from Citrix, as just updating ShareFile to a non vulnerable version does not fix the vulnerability in previously created storage zones. To resolve this, Citrix has released another mitigation tool. Instructions on how to fix the vulnerabilities are in the Citrix article, however, a login is required here. https://support.citrix.com/article/CTX269341

There is a way to check for yourself if your system is vulnerable.
See: https://github.com/DimitriNL/CTX-CVE-2020-7473 for more information, with special thanks to @DimitriNL

On May 22, 2020, DIVD CSIRT researchers searched for ShareFile servers in the Netherlands via Shodan. A total of 27 organizations were found. On June 23, 2020, researchers contacted 20 organizations by mail. 7 organizations already fixed the vulnerability. After that the case was closed.

More information.
- https://thehackernews.com/2020/05/citrix-sharefile-vulnerability.html
