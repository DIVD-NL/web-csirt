---
layout: post
title:  SolarWinds N-able N-central
author: Thomas van Voorst
excerpt: "DIVD scanning for vulnerable N-able servers"

#jekyll-secinfo:
#  cve:
#    url: /cves/CVE-
---
Earlier this year, DIVD case {% divd DIVD-2021-00017 %} was opened. This case dealt with two vulnerabilities in N-able N-central software prior to 2021.HF6.

These vulnerabilities enable authenticated users the following:

* Agent takeover in a multi-tenant environment (NCCF-16663)
* Downloading and installing agents in a multi-tenant environment (NCCF-16662)

In the coming days we will be scanning worldwide to identify unpatched and thus vulnerable N-able/N-central software and send notifications to our information sharing partners and individual network administrators.
