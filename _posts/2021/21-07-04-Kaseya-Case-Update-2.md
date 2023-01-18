---
layout: post
title: Kaseya Case Update 2
author: Victor Gevers
excerpt: "During the last 48 hours, the number of Kaseya VSA instances that are reachable from the internet has dropped from over 2.200 to less than 140 in our last scan today. And, by working closely with our trusted partners and national CERTs, the number of servers in The Netherlands has dropped to zero. A good demonstration of how a cooperative network of security-minded organizations can be very effective during a nasty crisis."
---

During the last 48 hours, the number of Kaseya VSA instances that are reachable from the internet has dropped from over 2.200 to less than 140 in our last scan today. And, by working closely with our trusted partners and national CERTs, the number of servers in The Netherlands has dropped to zero. A good demonstration of how a cooperative network of security-minded organizations can be very effective during a nasty crisis.

By now, it is time to be a bit more clear on our role in this incident. First things first, yes, Wietse Boonstra, a DIVD researcher, has previously identified a number of the zero-day vulnerabilities [CVE-2021-30116] which are currently being used in the ransomware attacks. And yes, we have reported these vulnerabilities to Kaseya under responsible disclosure guidelines (aka coordinated vulnerability disclosure).

Our research into these vulnerabilities is part of a larger project in which we investigate vulnerabilities in tools for system administration, specifically the administrative interfaces of these applications.

These are products like [Vembu BDR](https://csirt.divd.nl/cases/DIVD-2020-00011/), [Pulse VPN](https://csirt.divd.nl/cases/DIVD-2021-00005/), [Fortinet VPN](https://csirt.divd.nl/cases/DIVD-2020-00012/), to name a few. We are focusing on these types of products because we spotted a trend where more and more of the products that are used to keep networks safe and secure are showing structural weaknesses.

After this crisis, there will be the question of who is to blame. From our side, we would like to mention Kaseya has been very cooperative. Once Kaseya was aware of our reported vulnerabilities, we have been in constant contact and cooperation with them. When items in our report were unclear, they asked the right questions. Also, partial patches were shared with us to validate their effectiveness. During the entire process, Kaseya has shown that they were willing to put in the maximum effort and initiative into this case both to get this issue fixed and their customers patched. They showed a genuine commitment to do the right thing. Unfortunately, we were beaten by REvil in the final sprint, as they could exploit the vulnerabilities before customers could even patch.

After the first reports of ransomware occurred, we kept working with Kaseya, giving our input on what happened and helping them cope with it. This included giving them lists of IP addresses and customer IDs of customers that had not responded yet, which they promptly contacted by phone.

So, in summary: DIVD has been in a Coordinated Vulnerability Disclosure process with Kaseya, who was working on a patch. Some of these vulnerabilities were used in this attack. Kaseya and DIVD collaborated to limit the damage wherever possible.

As more details become available, we will report them on our [blog](https://csirt.divd.nl/blog/) and [case file](https://csirt.divd.nl/DIVD-2021-00002/).

Updated statistics:
![Graph with number of vulnerable hosts over time](/assets/images/DIVD-2021-00002-stats-2.png)
