---
title: DIVD warns worldwide Confluence users of critical vulnerability
layout: news
author: Lucinda Sterk
---
It is again a race against time. Cyber criminals have been massively exploiting the critical vulnerability in Atlassian's Confluence for several days now. The voluntary researchers of the Dutch Institute for Vulnerability Disclosure (DIVD) are working diligently to alert as many Confluence users as possible to this vulnerability and the patch that is now in available. They’ve sent 15,000 mails and counting. In the Netherlands alone, there were at least 460 vulnerable systems.

On the 2nd of June, researchers at the American security company Volexity announced that they had discovered that an unknown (0-day) vulnerability in Confluence had been used against one of their customers' systems. At the time of discovery, this exploit was only used in a very targeted way. Later, at about the same time the patches were released, details of how to exploit the vulnerability came out, resulting in a massive spread of malware.

A few days later over 18,000 mails were sent and we kept updating the Digital Trust Center with our findings regarding the Netherlands. 

Confluence is used worldwide by governments, banks and critical infrastructure, among others. Confluence is a collaboration software for capturing (internal) documentation and supports direct integration with many other systems such as Google Drive, Draw.io. and more.

In the last few days, cybercriminals have been scanning for this vulnerability en masse. Greynoise.io found 350 unique IP addresses that were scanning for this vulnerability. 349 of these are marked 'malicious'. 

What can criminals achieve with an exploit?
---
By using Confluence servers, attackers can gain access to an organization's infrastructure. Within confluence the vulnerability allows attackers to create admin users and they can steal all internal data from the Confluence instance.

Since the exploit was announced, attackers have placed Crypto Miners, Mirai botnet agents and web shells on servers. It is also possible that attackers will scan internal systems, which can lead to major data breaches.


What does DIVD do?
---
DIVD's volunteer investigators identify vulnerable Confluence instances accessible over the Internet and alert their owners. We try to warn organizations to update their systems before criminals exploit the vulnerability and to facilitate speedy recovery if a system has already been taken over.

From our own scanning infrastructure [AS: 50559] we scan for Atlassian Confluence servers and filter out the versions that are not yet patched.

When we determine that a vulnerable Confluence instance is present, we send a notification to the organization via the internet service provider. In the case of Dutch system owners, we share our data with the Digital Trust Center and the Dutch Security Clearing House (Security Meldpunt). These organizations in turn share the information with the end users.

To contact the right ISPs we look up the correct contact details with use of WHOIS information. When we can see a clear owner by means of, for example, the domain name, we will look for a contact person or e-mail address to send a notification. With critical organizations such as governments, chemical industries, oil/gas production, manufacturers, transport and financial services, we often seek direct contact, via telephone or LinkedIn, if we do not yet have a liaison or contact person at these organizations.

What can organizations do?
---
Patch. If this is not possible, it might be in your best interest to take the environment off the public internet for the time being and/or use a WAF. Try to create an isolated environment that can only be accessed by IP addresses that need access.
Check that no additional users have been created by third parties.
Check the log files {installation directory}/logs/conf_access_log{date}.log for abuse.

If a malicious person was able to place a web shell, it is possible that the log file has been manipulated / cleaned afterwards. It is recommended to thoroughly investigate the server for any type of backdoors and to see if there has been any unusual activity from the server in question.

Observations
---

Our first global scan shows that Germany and the US were very late with patching the vulnerable systems. The US is in second place, but this is because cloud services such as Amazon are widely used.

| [![Caption to the table: Frequency of how often a country appears in the total set (from our first scan / mail round (03-05-22 to 04-05-22))](/images/news/confluence_graph.png)](/images/news/confluence_graph.png) |
|:--:|
| <small>Frequency of how often a country appears in the total set (from our first scan / mail round (03-05-22 to 04-05-22))</small> |



Where can I find more technical information?
---

* [DIVD case file](Https://csirt.divd.nl/DIVD-2022-00033)
* [Volexity blog post](https://www.volexity.com/blog/2022/06/02/zero-day-exploitation-of-atlassian-confluence/)
* [Rapid 7 blog post](https://www.rapid7.com/blog/post/2022/06/02/active-exploitation-of-confluence-cve-2022-26134/)
* [Atlassian advisory](https://confluence.atlassian.com/doc/confluence-security-advisory-2022-06-02-1130377146.html)
* [Definition of WAF (from Wikipedia)](https://en.wikipedia.org/wiki/Web_application_firewall)

