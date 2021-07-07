---
layout: post
title: Kaseya VSA Limited Disclosure
author: Frank Breedijk
excerpt: "A short retrospective on DIVD-2021-00002 - Kaseya VSA case"
---

## Why we are only disclosing limited details on the Kaseya vulnerabilities
Last weekend we found ourselves in the middle of a storm. A storm created by the ransomware attacks executed via Kaseya VSA, using a vulnerability which we confidentially disclosed to Kaseya, together with six other vulnerabilities.

Ever since we released the news that we indeed notified Kaseya of a vulnerability used in the ransomware attack, we have been getting requests to release details about these vulnerabilities and the disclosure timeline. In line with the guidelines for [Coordinated Vulnerability Disclosure](https://english.ncsc.nl/publications/publications/2019/juni/01/coordinated-vulnerability-disclosure-the-guideline) we have not disclosed any details so far. And, while we feel it is time to be more open about this process and our decisions regarding this matter, we will still not release the full details.

## Why the secrecy?
As the ransomware attack using Kaseya VSA software has shown, the effects of a malicious actor knowing the full details of a vulnerability can be devastating. This immediately poses a dilemma to anybody that discovers a critical vulnerability in a critical piece of software, do we disclose the details or not?

Let’s use an analogy. Say a security researcher discovers a vulnerability in a high-end car. When you kick the left rear bumper in just the right way, the car doors open, and the engine starts. What should the researcher do? Tell everybody, tell all the owners of this type of car, or inform the manufacturer so he can recall and fix the car?

If the full details are made public, it is evident that many cars will get stolen very soon. If you inform the owners, this will likely happen too. The chances of the details remaining secret are slim if you inform a broad audience. Even if you limit the details to ‘a security issue involving the bumper’, you might tip off the wrong people. Telling the manufacturer there is a good chance that he comes up with a fix before large-scale car thefts are happening, and consider if you need to tell the owners to keep their car behind closed doors in the meantime.

## How does this relate to Kaseya VSA?
When we discovered the vulnerabilities in early April, it was evident to us that we could not let these vulnerabilities fall into the wrong hands. After some deliberation, we decided that informing the vendor and awaiting the delivery of a patch was the right thing to do. We hypothesized that, in the wrong hands, these vulnerabilities could lead to the compromise of large numbers of computers managed by Kaseya VSA.

As we stated before, Kaseya’s response to our disclosure has been on point and timely; unlike other vendors, we have previously disclosed vulnerabilities to. They listened to our findings, and addressed some of them by releasing a [patch](https://helpdesk.kaseya.com/hc/en-gb/articles/360019054377-9-5-5-Feature-Release-10-April-2021) resolving a number of these vulnerabilities. Followed by a [second patch](https://helpdesk.kaseya.com/hc/en-gb/articles/360019966738-9-5-6-Feature-Release-8-May-2021) resolving even more. We’ve been in contact with Kaseya ahead of the release of both these patches, allowing us to validate that these vulnerabilities had indeed been resolved by the patch in development.

Unfortunately, the worst-case scenario came true on Friday the 2nd of July. Kaseya VSA was used in an attack to spread ransomware, and Kaseya was compelled to use the nuclear option: shutting down their Kaseya Cloud and advising customers to turn off their on-premise Kaseya VSA servers. A message that unfortunately arrived too late for some of their customers.

We later learned that one of the two vulnerabilities used in the attack was one we previously disclosed to Kasya VSA.

## What can we tell?
In this blogpost and DIVD case [DIVD-2021-00011](https://csirt.divd.nl/DIVD-2021-00011/) we publish the timeline and limited details of the vulnerabilities we notified Kaseya of.

## Full disclosure?
Given the serious nature of these vulnerabilities and the obvious consequences of abuse of Kaseya VSA we will not disclose the full details of the vulnerabilities until such time that Kaseya has released a patch and this patch has been installed on a sufficient number of systems, something for which we have the monitoring scripts. In the past few days we have been working with Kaseya to make sure customers turn off their systems, by tipping them off about customers that still have systems online, and hope to be able to continue to work together to ensure that their patch is installed everywhere. We have no indication that Kaseya is hesitant to release a patch. Instead they are still working hard to make sure that after their patch the system is as secure as possible, to avoid a repeat of this scenario. Therefore we do not feel the need to lay down any kind of deadline for full disclosure at this point in time. A properly patched and secure Kaseya VSA is in the best interest of security of Kaseya customers and the internet at large.

## The vulnerabilities
We notified Kaseya of the following vulnerabilities:
* [CVE-2021-30116](https://csirt.divd.nl/cves/CVE-2021-30116) - A credentials leak and business logic flaw, to be included in 9.5.7
* [CVE-2021-30117](https://csirt.divd.nl/cves/CVE-2021-30117) - An SQL injection vulnerability, resolved in May 8th patch.
* [CVE-2021-30118](https://csirt.divd.nl/cves/CVE-2021-30118) - A Remote Code Execution vulnerability, resolved in April 10th patch. (v9.5.6)
* [CVE-2021-30119](https://csirt.divd.nl/cves/CVE-2021-30119) -  A Cross Site Scripting vulnerability, to be included in 9.5.7
* [CVE-2021-30120](https://csirt.divd.nl/cves/CVE-2021-30120) - 2FA bypass, to be resolved in v9.5.7
* [CVE-2021-30121](https://csirt.divd.nl/cves/CVE-2021-30121) - A Local File Inclusion vulnerability, resolved in May 8th patch.
* [CVE-2021-30201](https://csirt.divd.nl/cves/CVE-2021-30201) - A XML External Entity vulnerability, resolved in May 8th patch.

## Timeline

| Date | Description |
|:-------------:|-----|
| 01 Apr 2021 | Research start |
| 02 Apr 2021 | DIVD starts scanning internet-facing implementations. |
| 04 Apr 2020 | Start of the identification of possible victims (with internet-facing systems). |
| 06 Apr 2021 | Kaseya informed. |
| 10 Apr 2021 | Vendor starts issuing  [patches v9.5.5](https://helpdesk.kaseya.com/hc/en-gb/articles/360019054377-9-5-5-Feature-Release-10-April-2021). Resolving CVE-2021-30118. |
| 8 May 2021 | Vendor issues another [patch v9.5.6](https://helpdesk.kaseya.com/hc/en-gb/articles/360019966738-9-5-6-Feature-Release-8-May-2021). Resolving CVE-2021-30117, CVE-2021-30121, CVE-2021-30201. |
| 04 Jun 2021 | DIVD CSIRT hands over a list of identified Kaseya VSA hosts to Kaseya. |
| 26 Jun 2021 |  [9.5.7 on SaaS](https://helpdesk.kaseya.com/hc/en-gb/articles/4403021283217-9-5-7-Feature-Release-26-June-2021-) Resolving CVE-2021-30116 and CVE-2021-30119. |
| 02 Jul 2021 | DIVD responds to the ransomware, by scanning for Kaseya VSA instances reachable via the Internet and sends out notifications to network owners |
| 07 Jul 2021 | Limited publication (after 3 months). |
