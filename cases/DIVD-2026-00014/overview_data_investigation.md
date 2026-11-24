---
layout: page
title: Overview of data investigation
excerpt: A complete and up-to-date overview of the status of our data investigation following the breach on 21 September 2026
redirect_from:  /DIVD-2026-00014/overview_data_investigation/
---
On Monday 21 September 2026, the servers in our data centre were compromised. We have contained the attack and are rebuilding our infrastructure. True to DIVD fashion, this incident got its own DIVD case number: {% divd DIVD-2026-00014 %}, with the title "When, not if..." Because let’s be honest: in security, it was never a question of if.

# TL;DR

This page contains the the status of our data based ont he final reports that we received from [Melron](https://merlon-security.eu/) and [NVISO](https://www.nviso.eu/) of which we will publish, redacted, versions soon. This should be out last update to this page. 

The attacker was able to get into our network by breaching our csirt (Zammad) ticket system and becoming root on this server. Because of the way the network is configured exfiltrating data took the attackers time and forced them to upload files to a place where they where served by the Zammad web server. This enabled the forensic team to get an almost complete picture of the data exfiltrated. As data exfiltration was difficult, the attacker had to be selective. 
Data only ends up in tickets when a party sends an email to csirt@divd.nl or an email address ending in @csirt.divd.nl. 

In accordance with our [leaked credential policy](/credentials), we never email unmasked passwords. A limited set of credentials belonging to specific organisations was leaked for the following cases:
* {% divd DIVD-2024-00019 %}
* {% divd DIVD-2024-00022 %}
* {% divd DIVD-2025-00031 %}
* {% divd DIVD-2025-00035 %}
* {% divd DIVD-2025-00041 %}
* {% divd DIVD-2026-00007 %}

From the exfiltrated data, we gathered all email addresses, phone numbers and street addresses. Using a combination of LLMs, scripts and human review, we filtered out spam, generic or group email addresses, non-personal phone numbers and non-residential street addresses. This gives us the following overview.

| Type             | Unfiltered  | Personal  |
|------------------|-------------|-----------|
| Email addresses  | 48,928      | 4,121     |
| Phone numbers    | 316         | 34        |
| Street addresses | 39          | 0         |

CVE records and the CNA process are kept in a separate environment from the one that was compromised, and we have found no indication that this part of the environment was accessed.
The same is true of our scanning signatures, non-weaponised exploits and zero-day research.

Using authentication tokens in the configuraiton of Zammad, they where able read our Google workspace directory. They also managed to het into our Jira and Confluence environment as application administrators.

* Email addresses: 207 email addresses (including aliases and functional addresses) of volunteers and former volunteers were leaked.
* Phone numbers: Two phone numbers of volunteers were leaked.
* Profile pictures: Identifiable profile pictures of seven volunteers were leaked.

No data was leaked from our other corporate system.

For more details, read on.

# No salami tactics here

We believe open and honest communication about hacks is vital for a resilient digital society. The GDPR (the AVG, for the Dutch among us) backs this up by requiring that people whose personal data has been leaked are notified "without undue delay". It doesn’t say "when the PR team feels ready". Too often, we see this kind of news emerge through the [salami tactic](https://en.wikipedia.org/wiki/Salami_slicing_tactics). Serving the whole sausage at once could cause a lot of worry and stomach aches, so organisations cut it into thin slices, hoping each one feels less painful, causes less reputational damage and is easier to digest.

This is not the way.

Below, you’ll find the types of data we hold, both personal (PII) and non-personal, along with an update on the investigation status. That includes the things we don't know yet. This page will be updated as soon as we know more.

# What data is listed here

It was quite a puzzle to figure out what data we should and shouldn't list here. We want this overview to be honest, but not overly long or complicated. 
The data listed below is information we believe needs to be investigated to determine whether it was compromised by the attacker. This includes data that may be valuable to the attacker or pose a risk to others if compromised.

Please note:
a) This is not an exhaustive list of all the data we hold.
b) The fact that data is listed here does NOT mean it has been compromised.

For each data category, we have included an Investigation Status, Preliminary Analysis and Final Assessment. These three columns indicate the progress of the investigation and the findings regarding the data.

A dash (-) means no input yet.

# Data about volunteers

Our volunteers are our favourite humans, which is why we start here. Without volunteers, DIVD would not be possible. We try to keep as little data about them as possible, but lots of little things still add up.

## Status

| Data | Description | Investigation status | Preliminary analysis | Final assessment |
|---|---|---|---|---|
| Our office environment in GSuite | - | Technical investigation and analysis complete. | n/a | No signs of data exfiltration. The OAuth tokens of the shared mailboxes csirt@divd.nl and report-abuse@divd.nl were obtained by the attacker and used to send test emails. No compromise of the data in these mailboxes was observed. |
| Our HR environment | - | Technical investigation and analysis complete. | No signs of compromise. | No signs of compromise.  |
| Our IT support systems including our helpdesk | - | Technical investigation and analysis complete. | Signs of (partial) data exfiltration found. | No signs of compromise. |
| Our project support environment, including Jira and Confluence | Project support, including Jira and Confluence. | Technical investigation and analysis complete. | Signs of (partial) data exfiltration found. | The attacker was mainly interested in credentials. All leaked credentials have been rotated. The email addresses of 207 volunteers were leaked, as were the phone numbers of two volunteers. Identifiable profile pictures of seven volunteers were also leaked. Pages marked TLP:Red and TLP:Amber were also leaked, but they contained no data that is still sensitive. |
| System data on IT systems that support our operations | - | Technical investigation and analysis complete. | Signs of (partial) data exfiltration found. | Only the system that hosted our CSIRT Zammad system was compromised at the system (root) level. |
| Source code in (hidden) repos in public GitHub and internal GitLab | Source code in GitHub and internal GitLab. | Technical investigation complete. | No signs of compromise. | No signs of compromise. One GitLab personal access token was compromised, but the attacker was unable to reach our internal GitLab. |
| Internal communication via Slack | - | Technical investigation and analysis complete. | No signs of compromise. | No signs of compromise. One Slack API key was compromised, but it had no read permissions. |

## Current picture

Our Jira and Confluence environment was compromised. 
* Email addresses: 207 email addresses (including aliases and functional addresses) of volunteers and former volunteers were leaked.
* Phone numbers: Two phone numbers of volunteers were leaked.
* Profile pictures: Identifiable profile pictures of seven volunteers were leaked.

Apart from credentials, which have been rotated, there is no evidence that other volunteer data leaked.

For DIVD volunteers (and others), this means that there is only a slightly elevated risk of social engineering. 

# Core business data

Volunteers may be our favourite humans, but DIVD is here to help everybody. “Everybody deserves a responsible disclosure.” This means we hold a lot of data about many entities, some of which is sensitive and not limited to PII.

## Status

| Data | Description | Investigation status | Preliminary analysis | Final assessment |
|---|---|---|---|---|
| CSIRT ticket system containing all conversations with csirt@divd.nl and *@csirt.divd.nl | - | Technical investigation and analysis complete. | Signs of (partial) data exfiltration found. | The titles of around 41,000 tickets and a limited set of older conversations have leaked. Some of these conversations were about leaked credentials that were already in the hands of criminals. All passwords in this dataset were masked in line with our [leaked credentials policy](/credentials/). The system contained email addresses, phone numbers and street addresses. See the overview below. |
| Lists of vulnerable systems | We are investigating which part of this information is in the CSIRT ticket system. | Technical investigation and analysis complete. | - | Correspondence with parties about small subsets of affected systems of the following case {% divd DIVD-2024-00013 %}<br>The database was searched for tickets with the keyword `deploy` for the following cases: <br>* {% divd DIVD-2024-00013 %}<br>* {% divd DIVD-2024-00014 %}<br>* {% divd DIVD-2024-00022 %}<br>The database was also searched for the keyword `wachtwoord` for the following cases:<br>* {% divd DIVD-2024-00019 %}<br>* {% divd DIVD-2024-00022 %}<br>* {% divd DIVD-2025-00031 %}<br>* {% divd DIVD-2025-00035 %}<br>* {% divd DIVD-2025-00041 %}<br>* {% divd DIVD-2026-00007 %} |
| Fingerprints to identify vulnerable systems | - | Technical investigation and analysis complete. | - | No indications of compromise found. |
| "De-weaponised" PoCs | - | Technical investigation and analysis complete. | - | No indications of compromise found. |
| Zero-day vulnerabilities | - | Technical investigation and analysis complete. | Data in Zammad may be compromised. Data stored elsewhere does not appear to have been impacted. | No indications of compromise found, apart from older CNA-related email chains in Zammad that are well past the 90-day disclosure limit. |
| Proof-of-concept attacks | - | Technical investigation and analysis complete. | - | No indications of compromise found. |
| Leaked credential dumps | - | Technical investigation and analysis complete. | - | No indications of compromise found. |
| Masked leaked credential dumps | - | Technical investigation and analysis complete. | - | Masked passwords for a small number of organisations leaked for cases:<br>* {% divd DIVD-2024-00019 %}<br>* {% divd DIVD-2024-00022 %}<br>* {% divd DIVD-2025-00031 %}<br>* {% divd DIVD-2025-00035 %}<br>* {% divd DIVD-2025-00041 %}<br>* {% divd DIVD-2026-00007 %}|
| Private communication between DIVD researchers and third parties via, for example, email (not via Zammad) | - | Technical investigation and analysis complete.  | Signs of partial or limited data exfiltration found. | No indications of compromise found. | 

## Current picture

The server and application hosting our CSIRT Zammad system were completely compromised. Because direct outbound traffic was not possible, we have a fairly complete picture of the data the attacker managed to extract. As data exfiltration was difficult, the attacker had to be selective. 
Data only ends up in tickets when a party sends an email to csirt@divd.nl or an email address ending in @csirt.divd.nl. 

In accordance with our [leaked credential policy](/credentials), we never email unmasked passwords. A limited set of credentials belonging to specific organisations was leaked for the following cases:
* {% divd DIVD-2024-00019 %}
* {% divd DIVD-2024-00022 %}
* {% divd DIVD-2025-00031 %}
* {% divd DIVD-2025-00035 %}
* {% divd DIVD-2025-00041 %}
* {% divd DIVD-2026-00007 %}

From the exfiltrated data, we gathered all email addresses, phone numbers and street addresses. Using a combination of LLMs, scripts and human review, we filtered out spam, generic or group email addresses, non-personal phone numbers and non-residential street addresses. This gives us the following overview.

| Type             | Unfiltered  | Personal  |
|------------------|-------------|-----------|
| Email addresses  | 48,928      | 4,121     |
| Phone numbers    | 316         | 34        |
| Street addresses | 39          | 0         |

CVE records and the CNA process are kept in a separate environment from the one that was compromised, and we have found no indication that this part of the environment was accessed.
The same is true of our scanning signatures, non-weaponised exploits and zero-day research.


# TCB: Taking care of business

Like any organisation, we have to pay the rent, answer the telephone, pay the occasional bill and keep ourselves organised. This includes the administration, accounting systems and bank account we need to run DIVD. 

## Status

| Data | Description | Investigation status | Preliminary analysis | Final assessment |
|---|---|---|---|---|
| Our administration in GSuite | - | Technical investigation and analysis complete. | - | No indications of compromise found. |
| Our accounting systems | Handled via an external party. | Not under investigation. | No signs of impact. | No signs of impact. |
| Our bank account | Handled via an external party. | Not under investigation. | No signs of impact. | No signs of impact. |

## Current picture
Our accounting systems and bank account are handled via an external party, and we have no indications of compromise there. Our administration in GSuite was not compromised.
