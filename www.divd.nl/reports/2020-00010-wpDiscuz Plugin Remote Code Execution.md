---
title: Report DIVD-2020-00010 - wpDiscuz Plugin Remote Code
date: 12 May 2021
author: Jeroen van de Weerd
excerpt: DIVD researchers identified vulnerable wpDiscuz installations in the Netherlands and notified the system administrators.
---
<header>
    <h2>Report DIVD-2020-00010 - wpDiscuz Plugin Remote Code</h2>
    <span>12 May by Jeroen van de Weerd</span>
</header>
Case lead Frank Breedijk

On June 19, 2020, Wordfence's Threat Intelligence team alerted the authors of wpDiscuz on a critical vulnerability [CVE-2020-24186](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-24186). wpDiscuz is an interactive comment plugin for WordPress. This responsive comment system offers a real-time discussion function for visitors to post, share, and vote on comments. wpDiscuz has 90,000+ active installations.

The developer fixed the vulnerability in version 7.0.5 on July 27, 2020. The vulnerability allowed the webserver to be taken over by an error in the validation of uploads from the user, allowing PHP code to be executed. At the time of writing, wpDiscuz has version 7.2.1.

On June 30, 2020, DIVD CSIRT researchers checked a large number of .nl domain names for the presence of the wpDiscuz stylesheet on the main page. This allowed them to determine whether this plugin was installed. Through the readme file, they were able to determine the version number. Eventually, 41 installations were found in the Netherlands, of which 35 appeared to be vulnerable.

On August 4, 2020, a manual check was done, and on August 7, 2020, notifications were sent to abuse@, security@, and info@ email addresses of these domains.

On December 3, the case was closed.
