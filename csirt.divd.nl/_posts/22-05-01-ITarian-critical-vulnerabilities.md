---
layout: post
title: ITarian critical vulnerabilities
author: Frank Breedijk
excerpt: ITarian MSP platform and on-premise edition contain critical vulnerabilities, please consider not using it.
---
Today we are releasing data on a series of critical vulnerabilities we discovered in the ITarian All-in-one SaaS for MSP, the ITarian on-premise version, and the ITarian Endpoint Manager Communications Client for Windows, the client software used by both the SaaS and on-premise version.

In total, we have discovered five vulnerabilities. For the SaaS version, three of the vulnerabilities can be chained to take full control over all assets of a tenant, starting with an XSS attack.
In the on-premise platform, a valid user account is required (regardless of the privileges associated with the account), to achieve the same result.

In the past 100+ days since we informed ITarian about our findings, we have received no indication that our findings have been addressed or fixed. 

Given the lack of action from ITarian's side, we see no other option than to recommend all ITarian users to shield off and closely monitor on-premise installations of ITarian, stop using the ITarian SaaS platform, and uninstall the ITarian Endpoint Manager Communication Client from all Windows systems.

More details can be found in case [DIVD-2021-00037](/DIVD-2021-00037)

![ITarian logo](/assets/images/itarian.png)