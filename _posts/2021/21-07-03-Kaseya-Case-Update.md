---
layout: post
title: Kaseya Case Update
author: Lennaert Oudshoorn
excerpt: "Yesterday an attack on Kaseya VSA led to a large ransomware spree, because DIVD was already investigating this kind of product and we were able to react quickly."
---

On the night of 7-3 (CET), the DIVD CSIRT did a mass scan for online exposed Kaseya VSA instances due to an [alarming statement](https://helpdesk.kaseya.com/hc/en-gb/articles/4403440684689-Important-Notice-July-2nd-2021) from Kaseya. Kaseya turned off their SaaS services and advised all on-premise customers to turn off Kaseya VSA because it was being used to spread ransomware to various MSPs.

We were able to react very swiftly because we were already running a broad investigation into backup and system administration tooling and their vulnerabilities. One of the products we have been investigating is Kaseya VSA. We discovered severe vulnerabilities in Kaseya VSA and reported them to Kaseya, with whom we have been in regular contact since then. Additionally, we have, in confidence, also reported these vulnerabilities to our trusted partners.

Last night we reported all Kaseya VSA instances to the abuse addresses of the networks they are located in and provided the lists to the Dutch National Certs and partners. We are working with Kaseya as well to identify these customers and contact them directly. Over the past few days, we have seen a drastic drop in the number of online instances, which indicates that Kaseya’s customers are responding positively to Kaseya’s advice and contact.

At this time, we cannot disclose a lot of details to prevent copy-cat behavior. As more details become available, we will report them on our [blog](https://csirt.divd.nl/blog/) and [case file](https://csirt.divd.nl/DIVD-2021-00002/).

![Graph with number of vulnerable hosts over time](/assets/images/DIVD-2021-00002-stats.png)
