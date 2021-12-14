---
layout: post
title: Update Apache log4j2 remote code execution
author: Jeroen van de Weerd
excerpt: "Update Apache log4j2 remote code execution"
#jekyll-secinfo:
#  cve:
#    url: /cves/CVE-
---

On December 9th, a 0-day exploit in the popular Java logging library log4j (version 2) was reported by [LunaSec](https://www.lunasec.io/docs/blog/log4j-zero-day/) along with a [tweet ](https://web.archive.org/web/20211209143038/https://twitter.com/P0rZ9/status/1468949890571337731)of a Chinese researcher which linked to a Proof Of Concept (POC) posted on GitHub. The logging of a specially constructed string could result in remote code execution (RCE), giving an attacker complete control of a server.

Apache Log4j, a project of the Apache foundation, is an open-source software package used to log messages and is used in numerous software products and applications. Due to some properties of the Java ecosystem,  it can be challenging to know if an application uses log4j. It is like sugar: present in your meals, even when you didn't know. The vulnerability has been assigned  [CVE-2021-44228](https://nvd.nist.gov/vuln/detail/CVE-2021-44228) and is referred to as Log4Shell.

In this blog, we will take you through what has happened in the past few days and what the researchers of DIVD have done to help address this crisis.

On December 10th, several DIVD volunteers started developing methodologies to scan the internet for this vulnerability. These techniques are not perfect and don't guarantee that every vulnerable application is found, nor that every system detected as vulnerable to the injection is vulnerable to the entire RCE chain. Ever since, most have spent an average of 16 hours per day working on this very serious vulnerability (CVSS 10.0), [cooperating](https://fd.nl/tech-en-innovatie/1423175/nationale-cyberwaakhond-roept-beveiligers-bijeen-vanwege-wereldwijd-lek) with the Dutch [NCSC](https://www.ncsc.nl/) (National Cyber Security Center) and several security companies. During the work on this case, some level 1 researchers earned their spurs and were promoted to level 2 researchers.

Our first scan results showed several systems with either an .nl domain name or IP addresses registered by an organization in the Netherlands as vulnerable Apache Log4j systems.

On December 13th, various owners of vulnerable systems worldwide were notified by email regarding vulnerable Apache Log4j systems. Scanning for this vulnerability is not easy to automate. During a scan of thousands of IP addresses, the host the DIVD used was blocked, the account was locked, and the host was taken offline. Good work doesn't happen by itself.

We have shared curated data sets with the Dutch government and other parties. The cooperation with these parties is going well. Everyone has the same goal: to make the internet in the Netherlands and the world safer.

A common question is how to determine if exploitation of the Log4Shell has occurred or is in progress. Various IOCs (Indication of Compromise) are known and shared. For example, you can load these IOCs into an IDS (Intrusion Detection System). Several vulnerability scanners have also released updates or plugins to check if systems are vulnerable. Note that these scans do not provide a 100% guarantee that you do not have vulnerable systems.

Due to the high probability of widespread damage resulting from exploits, the NCSC is taking on the coordination role for the Netherlands. The questions below play a major role:

* Which software is vulnerable?
* Which scan tools are available?
* What are forms of mitigation available?
* What are forms of detection available?

The NCSC maintains a [list](https://github.com/NCSC-NL/log4shell/tree/main/software) of applications and devices that may be vulnerable. On this page (repository), you can also find software to scan your IT environment. There is also a list of different vulnerability scanners that can recognize and possibly stop the exploitation of the vulnerability. This list is very subject to change, so check it regularly.

The DIVD has built a [scanner](https://github.com/dtact/divd-2021-00038--log4j-scanner) together with [DTACT](https://dtact.com/), which is open-source and can quickly scan an internal network. This project gets improved daily, and new features are added. 

The DIVD uses a self-build scanner for scanning the internet, which will be made open-source shortly. We are creating a portal where we can share our tools with the infosec community. 

On December 12th, the first publicly confirmed ransomware attack appeared that involved exploitation of this vulnerability. 
Our national and international scans are still running. These scans also give our research team new insights and initiate further investigations into these products that have not yet been identified, like several Content Management Systems, project management software, and network storage devices. 

This blog post will be updated when more details become available.
