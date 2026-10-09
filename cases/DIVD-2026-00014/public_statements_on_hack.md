---
layout: page
title: Overview of public statements on our hack
excerpt: Page with an overview of public social media statements on our hack
redirect_from:  /DIVD-2026-00014/public_statements_on_hack/
---
### [Statement #1](https://www.linkedin.com/feed/update/urn:li:activity:7508986131779088384) — Thursday 24 September 2026
We got hacked. We noticed suspicious activity, investigated, and came to the inevitable conclusion that we got hacked. We went into full incident response
mode, blocked access to our infrastructure and started a forensics investigation with a third party incident response team. The modus operandi indicates an agentic AI powered attack, something we had not seen before. We informed the directly involved parties, reported the incident to the Autoriteit Persoonsgegevens and NCSC-NL and discussed our options with the police. Until proven otherwise, we handle this as a worst case scenario and assume breach.

### [Statement #2](https://www.linkedin.com/feed/update/urn:li:activity:7509723920586153984) — Saturday 26 September 2026
On our birthday, we share two redacted screenshots from the logs. They show the attacker's scripts contain notes where the agent justifies its own actions, explaining why what it's doing is okay and really not phishing, something a human attacker wouldn't bother with. It supports our assessment that this is an agentic AI powered attack. We can't share more for now without getting in the way of the investigation.

### [Statement #3](https://www.linkedin.com/feed/update/urn:li:activity:7510363579972206592)
We separate what we know from what we think and what we don't know yet. The attackers got in by exploiting a technical vulnerability, and it was not Citrix Netscaler. We see no link to any known public threat actor, and no facts so far point to our worst case scenario, in which an actor targeted us directly to get at our crown jewels, though we can't rule it out. The attack was loud and very messy, with the agent working automated and deciding each next step itself at speed on sloppy logic and its overexplaining comments have made our reverse engineering a lot easier.

### [Statement #4](https://www.linkedin.com/feed/update/urn:li:activity:7511092587848523778) — Tuesday 30 September 2026
We explain the attackers got in through two zero-days in Zammad that together allowed session hijacking, remote code execution and privilege escalation from the Zammad user to root, in seconds due to the agentic part of this hack. From there they could access other services and exfiltrate data. Thanks to proper network segmentation and the actions of our IT and Incident Response Team after detection, we were able to stop the attackers from going deeper into our systems and network. Unfortunately some of the damage was already done. We've found signs of compromise that we're still looking into, and until we can prove otherwise we assume breach. Still, stopping the attackers is a win and in a situation like this you take every win you can get. 
**We have assigned the CVE IDs {% cve cve-2026-102489 %} and {% cve cve-2026-102490 %} to these vulnerabilities and started case {% divd divd-2026-00015 %} to do target and victim notification for these two known exploited vulnerabilities.**

### [Statement #5](https://www.linkedin.com/feed/update/urn:li:activity:7511448012582387714) — Thursday 1 October 2026
We share the most painful and awkward part of being hacked, which data got out. We don't wait until we have every answer, because that doesn't make digital society any safer. What we know for sure is that volunteer data got out, such as DIVD email addresses and possibly contact details. Whose data and exactly which data is still being investigated, but it does mean it's now easier for someone to pose as a DIVD volunteer. If a message from someone at DIVD feels off, check with us first at communications@divd.nl. 

### [Statement #6](https://www.linkedin.com/feed/update/urn:li:activity:7511784574121594880) — Saturday 3 October 2026
We are contained. When we shut down our infrastructure on Tuesday 22 September, we hoped that would do the trick, and now we know for sure it did. That takes some of the pressure off, so we can focus fully on the investigation, working out the details and writing the reports people have asked for. We'll also give a spontaneous talk at the ONE Conference next Wednesday. It's a no-publicity talk on purpose, so we can be even more transparent there, and we'll speak to the press afterwards.

