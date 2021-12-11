---
layout: post
title: Apache log4j2 remote code execution
author: Ralph Horn
excerpt: "Apache fixes actively exploited logging component remote code excution zero-day"
#jekyll-secinfo:
#  cve:
#    url: /cves/CVE-
---
We just opened case {% divd DIVD-2021-00038 %} to address a vulnerability known as {% cve CVE-2021-44228 %} in the Apache log4j project that allows for unauthenticated, remote code execution. Apache log4j is often used in Java applications for logging purposes.

In the coming days, we will be scanning worldwide to identify unpatched and thus vulnerable applications that use vulnerable Apache log4j and send notifications to our information-sharing partners and individual network administrators.