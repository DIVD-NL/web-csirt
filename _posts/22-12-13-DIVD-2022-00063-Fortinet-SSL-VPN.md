---
layout: post
title: Fortinet SSL VPN Vulnerability
author: Ralph Horn
excerpt: FortiOS SSL VPN is contains a critical vulnerability. Patch to the latest version.
---

We are aware of {% cve CVE-2022-42475 %} in FortiOS sslvpnd and have opened case {% divd DIVD-2022-00063 %}.

This vulnerability is a unauthenticated remote code execution vulnerability with a CVSS base score of 9.8. Patches are available.
We are currently working to find a method to remotely identify either the version of the device, or another safe way to identify if the device is vulnerable. If we succeed, we plan to scan worldwide to identify unpatched and thus vulnerable FortiOS SSL VPN instances and send notifications to our information sharing partners and individual network administrators.


More details can be found in case [DIVD-2022-00063](/DIVD-2021-00063)