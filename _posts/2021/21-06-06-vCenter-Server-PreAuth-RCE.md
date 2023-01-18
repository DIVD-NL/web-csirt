---
layout: post
title: vCenter Server PreAuth RCE
author: Hidde Smit
excerpt: "
A critical vulnerability has been found in VMware vCenter Server versions 3.x, 4.x, 6.5, 6.7 and 7.0.
"

---

On 25 May 2021, VMware published an advisory [0] due to a critical vulnerability in vCenter server. The vulnerability can be exploited by unauthenticated malicious actors to gain remote code execution (RCE) through the abuse of a vulnerability in the Virtual SAN (vSAN) Health Check plug-in which is enabled by default. This vulnerability is present in the following versions: 7.0, 6.7, 6.5, 4.x, 3.x. Publicly available exploit code has been posted online on the 3rd of June 2021.

The Dutch Institute for Vulnerability Disclosure (DIVD) [2] is performing a daily scan since 31 May 2021. And will be sending notifications to system owners, for which it was analytically concluded that their system is most likely vulnerable.

For more information: [case DIVD-2021-00010](/DIVD-2021-00010/)
