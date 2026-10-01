---
layout: page
title: Overview of data investigation
excerpt: A complete and up to date overview of the status of our data investigation after breach of 21-9-2026
redirect_from:  /DIVD-2026-00014/overview_data_investigation/
---
On Monday 21 September 2026, the servers in our data center got compromised. We are now in incident response mode. True to DIVD fashion this incident got its own DIVD case number: {% divd DIVD-2026-00014 %} with the title: When not if... Because let’s be honest, in security it was never a question of if.

# TL;DR

We'll update this page often, so to save you from reading this wall of text every time, here's the TL;DR.

We got hacked, and data was compromised and possibly exfiltrated. We don't have the full picture yet, because we're still in full investigation mode. We chose full transparency, which means that we also communicate about the things we don't know. Questions regarding data can be sent to [dpo@divd.nl](mailto:dpo@divd.nl?subject=Data%20status%20inquiry%20DIVD%20hack). All other questions can go to [communications@divd.nl](mailto:communications@divd.nl?subject=Quewstion%20about%20DIVD%20breach).

# No salami tactics here

We believe open and honest communication about hacks is vital for a resilient digital society. The GDPR (the AVG, for the Dutch among us) backs this up by requiring that people whose personal data has leaked are notified "without undue delay". It doesn't say "when the PR team feels ready". Too often we see this kind of news come out through the [salami tactic](https://en.wikipedia.org/wiki/Salami_slicing_tactics). Serving the whole sausage at once could raise a lot of worries and stomach aches, so organisations cut it into thin slices, hoping each one feels less painful, does less damage to their reputation and can easily be eaten up without stomach ache.

This is not the way.

Below you'll find every type of data we hold, personal (PII) and non-personal, with an update on the investigation status. That includes the things we don't know yet. This page will be updated as soon as we know more.

# What data is listed here

It was quite a puzzle to figure out what data we should and shouldn't list here. We want this overview to honest, but not overly long or complicated. 
The data listed below is data that we feel needs to be investigated to determine if it was compromised by our attacker. This means that this is data if valuable to them, or poses a risk to others if compromised.

Beware that:
a) This is not a definite list of all data we have
b) The fact that this data is listed alone here does NOT mean it is compromised

Per catagory of data we have listed a Investigation status, Preliminary Analysis and Final Assessment. There three columns indicate the status of the investigation and the status of the data.

A dash (-) means no input yet.

# Data about volunteers

Our volunteers are our favorite humans, that's why we start here. Without volunteers, DIVD would not be possible. We try to keep as little data about them as possible, but lots of little things still add up.

## Status

| Data | Description | Investigation status | Preliminary Analysis | Final assessment |
|---|---|---|---|---|
| Our office environment in GSuite | - | Ongoing | - | - |
| Our HR environment | - | Ongoing | - | - |
| Our IT support systems including our helpdesk | - | Ongoing | - | - |
| Our project support environment, including Jira and Confluence | Project support, including Jira and Confluence. | Ongoing | Signs of compromise of the system | - |
| System data on IT systems that support our operations | - | Ongoing | Signs of compromise of the system | - |
| Source code in (hidden) repos in public GitHub and internal GitLab | Source code in GitHub and internal GitLab. | Ongoing | - | - |
| Internal communication via Slack | - | Ongoing | - | - |

## Current picture

We know for sure that user data (DIVD email addresses) and possibly contact details of volunteers were exfiltrated, and we're still investigating exactly which data of which volunteers is affected. For DIVD volunteers (and others) this means a higher risk of social engineering, because this makes it easier for someone to pose as a DIVD'er.


# Core business data

Volunteers may be our favorite humans. But the DIVD is there to help everybody. “Everybody deserves a responsible disclosure”, but that means we do have a lot of data about a lot of entities, that is unfortunately sensitive in nature and that is not limited to PII.

## Status

| Data | Description | Investigation status | Preliminary Analysis | Final assessment |
|---|---|---|---|---|
| CSIRT tickets system with all conversations with csirt@divd.nl and *@csirt.divd.nl | - | Ongoing | Signs of compromise of the system | - |
| Lists of vulnerable systems | We are investigating which part of this information is in the CSIRT ticket system. | Ongoing | - | - |
| Fingerprints to identify vulnerable systems | - | Ongoing | - | - |
| "De-weaponised" PoCs | - | Ongoing | - | - |
| Zero day vulnerabilities | We are investigating which part of this information is in the CSIRT ticket system. | Ongoing | - | - |
| Proof of concept attacks | - | Ongoing | - | - |
| Leaked credential dumps | - | Ongoing | - | - |
| Masked leaked credential dumps | We are investigating which part of this information is in the CSIRT ticket system. | Ongoing | - | - |
| Private communication between DIVD researchers and third parties via e.g. mail | - | Ongoing | - | - |

## Current picture

We know for sure that the attackers got in through the ticketing system our CSIRT team uses. That system holds every email sent to the CSIRT mailbox and every reply, but not our initial notifications.
We know that the attackers had difficulties extracting information from this system and our environment, that makes that only a part of the information was extracted. If an organisation or individual has been emailing back and forth with our CSIRT team, assume the attackers may have that information. This could be follow-up requests on scan data (including IP addresses of vulnerable systems), vulnerabilities reported to us through the CSIRT mailbox and extracts of credential dumps with masked passwords.

We say 'assume' because our setup and security measures meant the attacker had to work for every bit of data they got out. We're still working out how far the exfiltration went, and that takes time.



# TCB: Taking care of business

Like any organisation we have to pay the rent, answer the telephone and pay an occasional bill and organise ourselves. This covers the administration, accounting and bank account we need to run DIVD. 

## Status

| Data | Description | Investigation status | Preliminary Analysis | Final assessment |
|---|---|---|---|---|
| Our administration in our GSuite | - | Ongoing | - | - |
| Our accounting systems | Handled via an external party. | Not under investigation | No signs found so far | - |
| Our bank account | Handled via an external party. | Not under investigation | No signs found so far | - |

## Current picture
Our accounting systems and bank account are handled via an external party, and we have no indications of compromise there. Our administration in GSuite is still under investigation.

