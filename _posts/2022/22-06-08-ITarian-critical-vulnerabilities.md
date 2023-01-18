---
layout: post
title: ITarian critical vulnerabilities
author: Frank Breedijk
excerpt: ITarian MSP platform and on-premise edition contain critical vulnerabilities. SaaS is patched, on-premise cannot be patched.
---
Today we are releasing data on a series of critical vulnerabilities we discovered in the ITarian All-in-one SaaS for MSP, the ITarian on-premise version, and the ITarian Endpoint Manager Communications Client for Windows, the client software used by both the SaaS and on-premise version.

In total, we have discovered four vulnerabilities. For the SaaS version, three of the vulnerabilities could also be chained to take full control over all assets of a tenant, starting with an XSS attack.
In the on-premise platform, a valid user account is required (regardless of the privileges associated with the account), to achieve the same result.

The disclosure process with ITarian was challenging, but the vulnerabilities in the SaaS version and Agent have been patched. The On-Premise version has been end-of-live for over two years and will not be patched. 

More details can be found in case [DIVD-2021-00037](/DIVD-2021-00037)

![ITarian logo](/assets/images/itarian.png)