---
layout: post
title: Closing GeyNoise Ukraine Only case
author: Frank Breedijk
excerpt: We are closing DIVD-2022-00014 because GeryNoise is no longer updating the data
---
[GreyNoise](https://greynoise.io/) published a "free, public, unauthenticated, self-updating feed of all IPs that are exclusively targeting devices geographically located in Ukraine's IP space with scans, exploits, etc." We first became aware of it via a [tweet](https://twitter.com/Andrew___Morris/status/1496923547872206852?s=20&t=Y5vBKAso8TRrwief4KpbLg) from GreyNoise founder Andrew Morris. We feel that in these times, network administrators should be aware of these IP addresses even if they are unaware of the services of GreyNoise.

GreyNoise siltently stopped updating the API after 1 Aug 2022. THerefore we closed this case on 15 Aug 2022.

Overall we set 5698 notifications to owners of the IP addresses that appeared on this list. We have plotted them by the date they first hit the honeypots in the graph below.

![Graph of IP addresses, colored by provider, that execusively his GreyNoise honeypots in Ukraine.](/img/DIVD-2022-00014/GreyNoiseUkrainOnlyGraph.png)

You can also interact with [this graph on Google Data Studio](https://datastudio.google.com/u/1/reporting/5902c6e9-addf-405e-8d58-8853d1b41a7b/page/LHtnC)

All the case details can be found on {% divd DIVD-2022-00014 %}