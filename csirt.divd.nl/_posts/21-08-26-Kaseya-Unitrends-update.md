---
layout: post
title: Kaseya Unitrends update
author: Frank Breedijk
excerpt: "Server has been patched, mitigations for Unitrends client published"
#jekyll-secinfo:
#  cve:
#    url: /cves/CVE-
---
Mid July 2021 we opened case {% divd DIVD-2021-00014 %} tracking multiple vulnerabilities in Kaseya Unitrends. 

These vulnerabilities consited of:
*  An authenticated remote code execution vulnerability on the server,
* a privilege escaltion vulnerability from read-only user to admin on the server and
* a (yet) undisclosed vulnerability on the client

On 12 August 2021 Kaseya released version 10.5.5-2 of Unitrends that patches the the server side vulnerabilities. 

The client side vulnerability is current unpatched, but Kaseya urges users to mitigate these vulnerabilities via firewal wall rules as per their [best prectices and firewall requirements](https://support.unitrends.com/hc/en-us/articles/360013264518). In addition to that they have released a [knowledge base article](https://support.unitrends.com/hc/en-us/articles/4404684084369-RCE-KB) with steps to mitigate the vulnerability.

Kaseya has reached out to Unitrends customers with the advice to patch servers and to apply these mitigations for clients.

We have updated our case file {% divd DIVD-2021-00014 %} to reflect this update.