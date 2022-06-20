---
title: Report DIVD-2020-00005– Apache Tomcat AJP
date: 14 July, 2021
author: Gerard Janssen
excerpt: A vulnerability was found in Apache Tomcat, nicknamed Ghostcat. The DIVD scanned the web for vulnerable systems and shared this information through non-public CERT channels.
---
<header>
    <h2>Report DIVD-2020-00005– Apache Tomcat AJP</h2>
    <span>14th July by Gerard Janssen</span>
</header>
Case lead Frank Breedijk


February 20, 2020, the China National Vulnerability Database published a security advisory for a vulnerability in Apache Tomcat (CNVD-2020-10487/CVE-2020-1938). The vulnerability was called Ghostcat, because it has remained invisible for over thirteen years. It can be exploited to read and write files.

Apache Tomcat is a popular open source servlet container, a web server that uses java to dynamically generate a webpage on the server side.

Chinese security firm Chaitin Tech found the vulnerability in the Tomcat AJP protocol. Tomcat listens on ports 8080 (http) and 8009 (AJP). AJP stands for Apache JServ Protocol and is enabled by default, if the AJP connector is enabled. A Proof of concept appeared on the same day

On February 20, DIVD immediately scanned and found 54,000 vulnerable systems worldwide, of which 773 in the Netherlands. This information has been shared with non-public CERT channels.

June 2021 a rescan was done. 25,000 of the 54,000 systems were still vulnerable. This list was again shared through the same channels.
