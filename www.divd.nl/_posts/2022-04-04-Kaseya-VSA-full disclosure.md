---
title: DIVD gives full disclosure in Kaseya case
layout: news
author: Lucinda Sterk
---
Say Kaseya VSA and any IT specialist will know what you’re talking about. It was one of the most high-profile incidents of 2021. Almost a year later, the researchers of the Dutch Institute for Vulnerability Disclosure (DIVD) provide full disclosure in [release the full technical details of the bugs they found](https://csirt.divd.nl/2022/04/04/Kaseya-VSA-Full-Disclosure/)

It is now safe to fully explain what exactly was vulnerable and how it could be abused, says [Frank Breedijk](/team/Frank%20Breedijk), Manager CSIRT at DIVD. “If you haven't patched by now, you're a pancake.”

In the podcast [episode #6 of The Ransomware Files podcast](https://www.bankinfosecurity.com/interviews/ransomware-files-episode-6-kaseya-revil-i-5045) he and DIVD leader [Victor Gevers](/team/Victor%20Gevers) talk extensively about this case.

How it started
---
In April 2021, DIVD researcher Wietse Boonstra discovered several previously undiscovered vulnerabilities, zero days, in Kaseya VSA software. The vulnerabilities were reported and the volunteer specialists worked together with Kaseya for weeks on a patch. Only just before the finish did REvil's cybercriminals overtake them with all the consequences that entailed. Until now only [limited details](https://csirt.divd.nl/2021/07/07/Kaseya-Limited-Disclosure/) have been released

What we are disclosing
----------------------
The details released in the full disclosure indicate that the ransomware attack is due to a serious design flaw when it comes to how Kaseya's VSA client authenticated to the server. In addition, there was a lot of technical debt. The full disclosure also reveals the details of [CVE-2021-30118](https://csirt.divd.nl/CVE-2021-30118), which would have allowed REvil to execute its attack even more efficiently and effectively. REvil infected more than 1,500 organizations worldwide with ransomware through the Kaseya vulnerabilities.

A peek behind the scenes
------------------------
When the Kaseya VSA crisis happened, [Gerard Janssen](/team/Gerard%20Janssen/), was writing his book [Hackers](https://www.thomasrap.nl/boek/hackers/) and he wrote an entire chapter on this case of which a [translation is available as background report on this site](/reports/2021-00002-Kaseya%20VSA%20behind%20the%20scenes/).
