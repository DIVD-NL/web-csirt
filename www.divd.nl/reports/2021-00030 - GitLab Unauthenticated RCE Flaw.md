---
title: Report DIVD-2021-00030 - GitLab Unauthenticated RCE Flaw
date: November 19, 2021
author: Jeroen van de Weerd
excerpt: We have received a list of GitLab servers running a vulnerable version of GitLab from security researchers at Censys.io. An issue has been discovered in GitLab CE/EE.
---
<header>
    <h2>Report DIVD-2021-00030 - GitLab Unauthenticated RCE Flaw</h2>
    <span>November 19, by Jeroen van de Weerd</span>
</header><BR>
Case lead: Victor Gevers<BR>
Researchers: Frank Breedijk, Victor Gevers, Lennaert Oudshoorn

<BR>November 7, Censys wrote a [blog](https://censys.io/blog/cve-2021-22205-it-was-a-gitlab-smash/) about a vulnerability in GitLab enterprise and community edition. A researcher named "vakzz" (William Bowling) found this vulnerability on May 7, 2021, and reported it via a bounty program.
It appeared that the application was not correctly checking uploaded images. Engineers at GitLab fixed the vulnerability almost immediately.
However, a few months later, a report came out on Twitter that a botnet of thousands of compromised GitLab servers was performing DDoS attacks.

GitLab is an open-source code repository system that brings development, operations, and security teams into a single application.  It is primarily used by large organizations to manage DevOps and other related software projects.

November 11, DIVD opened case [DIVD-2021-00030](https://csirt.divd.nl/cases/DIVD-2021-00030/). We received data from [Censys](https://censys.io/) containing vulnerable GitLab servers. We validated a subset of this data and added abuse mail addresses to all unique IP addresses.
On November 15, we sent around 8,000 notifications by email. We received multiple good responses and some of them some have said thank you. Some indicated that they had forgotten the update. A few indicated that traces of abuse had been found.
We did not send any other notifications and therefore, this case was closed.
  
More information can be found here:

* [GitLab Critical Security Release: 13.10.3, 13.9.6, and 13.8.8](https://about.gitlab.com/releases/2021/04/14/security-release-gitlab-13-10-3-released/)
* [GitLab servers are being exploited in DDoS attacks in excess of 1 ⦁ Tbps](https://therecord.media/gitlab-servers-are-being-exploited-in-ddos-attacks-in-excess-of-1-tbps/)
* [CVE-2021-22205: It Was A GitLab Smash](https://censys.io/blog/cve-2021-22205-it-was-a-gitlab-smash/)
* [CVE-2021-22205](https://attackerkb.com/topics/D41jRUXCiJ/cve-2021-22205/rapid7-analysis)
