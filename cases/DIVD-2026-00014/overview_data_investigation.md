---
layout: page
title: Overview of data investigation
excerpt: A complete and up to date overview of the status of our data investigation after breach of 21-9-2026
redirect_from:  /DIVD-2026-00014/overview_data_investigation/
---
On Monday 21 September 2026, the servers in our data center got compromised. We have contained the attack and are rebuilding our infrastructure. True to DIVD fashion this incident got its own DIVD case number: {% divd DIVD-2026-00014 %} with the title: When not if... Because let’s be honest, in security it was never a question of if.

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
| Our office environment in GSuite | - | Technical investigation and analysis complete | n/a | The attackers got our internal directory. The email adddresses of all our volunteers leaked, the phone number of 34 volunteers leaked as well as 3 home addresses. 7 volunteers had identifiable profile pictures that leaked too.  |
| Our HR environment | - | Technical investigation and analysis complete. | No signs of compromise. | No signs of compromise.  |
| Our IT support systems including our helpdesk | - | Technical investigation and analysis complete. | Signs of (partial) data exfiltration found. | No signs of compromise. |
| Our project support environment, including Jira and Confluence | Project support, including Jira and Confluence. | Technical investigation and analysis complete. | Signs of (partial) data exfiltration found. | The attacker was mainly interested in credentials. All leaked credentials have been rotated. Pages that where marked TLP:Red and TLP:Amber where also leaked but contained on data that is currently still sensitive. |
| System data on IT systems that support our operations | - | Technical investigation and analysis complete. | Signs of (partial) data exfiltration found. | Only the system that hosted our CSIRT Zammad system was compromised on a system (root) level. |
| Source code in (hidden) repos in public GitHub and internal GitLab | Source code in GitHub and internal GitLab. | Technical investigation finished. | No signs of a compromise. | - |
| Internal communication via Slack | - | Technical investigation and analysis complete. | No signs of a compromise. | No signs of a compromise. |

## Current picture

Our Google directory was compromised. 
* Email addresses: 207 email addresses (including aliases and functional addresses) of volunteers and former volunteers where leaked
* Phone numbers: 34 phones numbers where stored and leaked.
* Home addresses: 3 home addresses where stored and leaked.
* Profile pictures: 7 volunteers had Google profile pictures that can be used to identify them, they where leaked.

There is no evidence that other volunteer data leaked.

For DIVD volunteers (and others) this means that there is only a slightly elevated risk of social engineering. 

# Core business data

Volunteers may be our favorite humans. But the DIVD is there to help everybody. “Everybody deserves a responsible disclosure”, but that means we do have a lot of data about a lot of entities, that is unfortunately sensitive in nature and that is not limited to PII.

## Status

| Data | Description | Investigation status | Preliminary Analysis | Final assessment |
|---|---|---|---|---|
| CSIRT tickets system with all conversations with csirt@divd.nl and *@csirt.divd.nl | - | Technical investigation and analysis complete. | Signs of (partial) data exfiltration found. | A limited set of data has leaked. Some of these conversations where about leaked credentials which where already in the hand of criminals. All of the passwords in this dataset where masked in line with our [leaked credentials policy](/credentials/). The system contained email addresses, phone numbers and street addresses. See the overview below. |
| Lists of vulnerable systems | We are investigating which part of this information is in the CSIRT ticket system. | Technical investigation and analysis complete. | - | Correspondence with parties about small subsets of effected systems of the following case {% divd DIVD-2024-00013 %}<br>The database was searched for tickets with the keyworks `deploy` for the following cases: <br>* {% divd DIVD-202400013 %}<br>* {% divd DIVD-2024-00014 %}<br>* {% divd DIVD-2024-00022 %}<br>And for the keyword `wachtwoord` for cases:<br>* {% divd DIVD-2024-00014 %}<br>* {% divd DIVD-2024-00022 %}<br>* {% divd DIVD-2025-00031 %}<br>* {% divd DIVD-2025-00035 %}<br>* {% divd DIVD-2025-00041 %}<br>* {% divd DIVD-2026-00007 %} |
| Fingerprints to identify vulnerable systems | - | Technical investigation and analysis complete. | - | No indications of compromise found. |
| "De-weaponised" PoCs | - | Technical investigation and analysis complete. | - | No indications of compromise found. |
| Zero day vulnerabilities | - | Technical investigation and analysis complete. | Data in Zammad may be compromised. Data in other places appears not to be impacted. | No indications of compromise found. |
| Proof of concept attacks | - | Technical investigation and analysis complete. | - | No indications of compromise found. |
| Leaked credential dumps | - | Technical investigation and analysis complete. | - | No indications of compromise found. |
| Masked leaked credential dumps | - | Technical investigation and analysis complete. | - | Masked passwords for a small number of organisations leaked for cases:<br>* {% divd DIVD-2024-00014 %}<br>* {% divd DIVD-2024-00022 %}<br>* {% divd DIVD-2025-00031 %}<br>* {% divd DIVD-2025-00035 %}<br>* {% divd DIVD-2025-00041 %}<br>* {% divd DIVD-2026-00007 %}|
| Private communication between DIVD researchers and third parties via e.g. mail (not via Zammad) | - | Technical investigation and analysis complete.  | Signs of (partial/limited) data exfiltration found. | No indications of compromise found. | 

## Current picture

THe server and applicaiton of our CSIRT Zammad system was completely compromised. Due to the fact that there was no direct outgoing traffic possible we have a fairly complete picture of all data that the attacker managed to extract. Because data exfiltration was difficult the attacker had to be selective. 
Data only ends up in tickets when a party sends an email to csirt@divd.nl or an email address ending in @csirt.divd.nl. 

As per out [leaked credential policy](/credentials), we never email unmasked password. A limited set of credentials of specific organisations leaked for the following cases:
* {% divd DIVD-2024-00014 %}
* {% divd DIVD-2024-00022 %}
* {% divd DIVD-2025-00031 %}
* {% divd DIVD-2025-00035 %}
* {% divd DIVD-2025-00041 %}
* {% divd DIVD-2026-00007 %}

From the exfiltrated data, we gathered all email addresses, phone numbers and street addresses. Using a combination of LLMs, scripts and humand review we filtered out all spam, generect or group email addresses, phone number and non-residential street addresss. This gives us the following overview.

| Type   | Unfiltered  | Personal  |
|--------|-------------|-----------|
| Email adresses | 48,928 | 4,121  |
| Phone numbers  | 316  | 34 |
| Street addresses | 39  | 3 |

CVE records and the CNA process are kept in a separate environment from the one that was compromised, and we have found no indication that this part of the environment was accessed.
The same is true of our scanning signatures and non-weaponized exploits and out 0-day research.


# TCB: Taking care of business

Like any organisation we have to pay the rent, answer the telephone and pay an occasional bill and organise ourselves. This covers the administration, accounting and bank account we need to run DIVD. 

## Status

| Data | Description | Investigation status | Preliminary Analysis | Final assessment |
|---|---|---|---|---|
| Our administration in our GSuite | - | Technical investigation and analysis complete. | - | No indications of compromise found. |
| Our accounting systems | Handled via an external party. | Not under investigation | No signs this is impacted. |No signs this is impacted. |
| Our bank account | Handled via an external party. | Not under investigation | No signs this is impacted. |No signs this is impacted. |

## Current picture
Our accounting systems and bank account are handled via an external party, and we have no indications of compromise there. Our administration in GSuite was not compromised.

