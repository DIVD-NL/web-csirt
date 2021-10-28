---
title: Report DIVD-2021-00001– Microsoft Exchange Server ProxyLogon
date: August 26, 2021
author: Gerard Janssen
excerpt: In the beginning of 2021 various groups have been breaking into Microsoft Exchange servers using various zero-days, DIVD scanned for unpatched versions and warned more than 40,000 organizations.
---
<header>
    <h2>Report DIVD-2021-00001– Microsoft Exchange Server ProxyLogon</h2>
    <span>August 26, 2021 by Gerard Janssen</span>
</header>
Case lead Frank Breedijk  
Researchers: Matthijs Koot, Victor Gevers, Lennaert Oudshoorn

At the beginning of 2021, thousands of organizations were affected by vulnerabilities in Windows Exchange Server. Various groups have been breaking into Microsoft Exchange servers using various zero-days, unknown security holes.

March 2, 2021, Microsoft released a patch. DIVD scanned for unpatched versions and warned more than 40,000 organizations that use Windows Exchange worldwide.

In the fall of 2020, information security researchers at the Taiwanese company DevCore investigated the security of Microsoft Exchange Servers, Microsoft's collaboration platform, and the most popular mail server worldwide. They looked at incoming and outgoing emails, calendar invitations, and virtually anything accessed within Outlook through their Exchange server. One DevCore researcher discovered a pre-authentication proxy vulnerability, which was dubbed Proxylogon (CVE-2021-26855). Shortly afterward, they found a second vulnerability (CVE-2021-27065) that could be used in conjunction with the first to write or delete files without authentication. The vulnerabilities could be used to download entire mailboxes or create the first entry into a corporate network and continue from there.

January 5, 2021, DevCore warned Microsoft. A researcher, who goes by the name of "Orange Tsai" on Twitter, tweeted:

"Just reported a pre-auth RCE chain to the vendor. This might be the most serious RCE I have ever reported! Hope there is no bug collision or duplicate ".

At that time, the first attacks had already been carried out. On January 18, the Danish security company Dubex found suspicious activity on several Windows Exchange Servers. The American company Volexity also saw unusual activity on Windows Exchange Servers from two of their customers. Large amounts of data flowed to IP addresses that did not appear to belong to legitimate users.

Later analysis showed that the vulnerabilities had been exploited since January 3, 2021. Researchers discovered the China Chopper web shell. Microsoft linked the software to a hacker group that researchers from that company called Hafnium, which operates from China. Hafnium appears to target higher education institutions, military suppliers, think tanks, NGOs, and medical research institutions.

March 2, 2021, Microsoft published a blog and patches to plug the leak. This was a week earlier than the usual second Tuesday of the month - patch Tuesday - so DIVD researchers were alerted this patch must be vital.

This was the go-ahead for the DIVD to take action and scan for Dutch Exchange Servers, which were vulnerable. With a script by Kevin "GossiTheDog" Beaumont, they were able to determine which version number the exchange server had and whether it was vulnerable.

March 3, 2021, the DIVD found 42,193 vulnerable IP addresses during that first scan (over 2,000 in The Netherlands).

March 4, the DIVD sent this list to the National Management Organization for Internet Providers (NBIP).

Microsoft came up with the first tools to detect the so-called indicators of compromise, traces that show someone has broken into an exchange server and taken it over. Initially, that was only the set of the Hafnium collective (but on May 5, indicators from other groups were also added.)

March 7, DIVD sent more than 42,000 notifications to warn system administrators worldwide.

March 9, a new scan by DIVD showed that at least 23,000 systems were still vulnerable worldwide (688 in The Netherlands).

March 12, Cybersecurity firm Check Point Research saw that attacks doubled every two to three hours.

March 16 DIVD performed a new scan with better scanning methods. It turned out that there were still  23,000 to 30,000 vulnerable systems online.

March 18, Windows released an update of its antivirus software Defender, and the vulnerability was automatically mitigated to get the attackers off the system. At this time, it was plausible that an unpatched system likely would already be compromised.

March 23, a DIVD scan showed that vulnerable systems went down from 30,000 to 14,000 systems. April 6, the number further decreased to around 6,000.

April 13, new vulnerabilities (CVE 2021-248480, CVE-2021-28481) were reported to Microsoft by the NSA. The DIVD found 13,000 systems for which no patches are available for the newly discovered vulnerability.

April 21, there were still 5,100 vulnerable systems for the ‘old’ vulnerabilities and 9,700 for which no patch is available. Assuming these last victims are apparently not open to our warnings, DIVD stopped notifying them.

<img src="images/reports/00001_Exchange_graph.png" alt="Grafiek van gevonden kwetsbare Exchange systemen">
