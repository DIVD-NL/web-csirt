---
layout: post
title: SmarterTrack Full disclosure
author: Finn van der Knaap
researchers: 
    - Wietse Boonstra
    - Finn van der Knaap
excerpt: "Full disclosure of vulnerabilities we discovered in SmarterTrack"
---
On 27 October 2021 [Wietse Boonstra](https://www.divd.nl/team/Wietse%20Boonstra/) found several vulnerabilities in the latest version of SmarterTrack. There were [two](/CVE-2022-24384) [XSS](/CVE-2022-24386), an [unauthenticated download](/CVE-2022-24385) and an [upload / overwrite vulnerability](/CVE-2022-24387). The researcher [Wietse Boonstra](https://www.divd.nl/team/Wietse%20Boonstra/) and [Finn van der Knaap](https://www.divd.nl/team/Finn%20van%20der%20Knaap/), examined the vulnerability and made the proof of concept.

Today we are releasing case [DIVD-2021-00029](/DIVD-2021-00029) and are disclosing the details of the four CVEs.


## Reflective Cross-site Scripting (XSS)

- CVE: {% cve CVE-2022-24384 %}
- Case: {% divd DIVD-2021-00029 %}
- Discoverd by: Wietse Boonstra
- Credits: Discovered by [Wietse Boonstra](https://www.divd.nl/team/Wietse%20Boonstra/) of DIVD, Additional research by [Finn van der Knaap](https://www.divd.nl/team/Finn%20van%20der%20Knaap/) of DIVD
- Products: SmarterTools - SmarterTrack V100.0.8019.14010
- CVSS: 8.8
- Reference: case {% divd DIVD-2021-00029 %}, {% cve CVE-2022-24384 %}
- Solution: Upgrade to the latest version

POC: open the URL to the portal and simply add any type of script behind a URL with, for example, an error message. This is a working example script:
`{SMARTERTRACK_URL}/Main/Default.aspx?viewSurveyError=Unknown+survey"><img%20src=x%20onerror=alert(1)>`

Impact: When this attack is performed, the attacker can do any action that the user also can do. Fortunately, the attacker can't access any password from this attack since the credentials are protected. But the attacker can still see sensitive data and modify this.

![Screenshoot of reflective XSS in /Main/Default.aspx](/img/DIVD-2021-00029/poc1.png)

## Unauthenticated downloading of attachment

- CVE: {% cve CVE-2022-24385 %}
- Case: {% divd DIVD-2021-00029 %}
- Discoverd by: Wietse Boonstra
- Credits: Discovered by [Wietse Boonstra](https://www.divd.nl/team/Wietse%20Boonstra/) of DIVD, Additional research by [Finn van der Knaap](https://www.divd.nl/team/Finn%20van%20der%20Knaap/) of DIVD
- Products: SmarterTools - SmarterTrack V100.0.8019.14010
- CVSS: 6.5
- Reference: Case {% divd DIVD-2021-00029 %}, {% cve CVE-2022-24384 %}
- Solution: Upgrade to the latest version

Description: Direct Object Access vulnerability in SmarterTools SmarterTrack leads to information disclosure.

POC: Start a Private Browsing session to clear the sessions. Go to the following URL: `{SMARTERTRACK_URL}/Management/Tickets/frmAttachment.aspx?ticketID=1`
Now enumerate the ticketID and increment the 1. If the ticket has attachments, a zip file can be downloaded containing all the files.

Impact: When someone downloads the attachment without authorization, sensitive data can be exposed that was added to the ticket.


![Screenshot of Director Object Access](/img/DIVD-2021-00029/poc2.png)


## Stored Cross-site Scripting (XSS)

- CVE: {% cve CVE-2022-24386 %}
- Case: {% divd DIVD-2021-00029 %}
- Discoverd by: Wietse Boonstra
- Credits: Discovered by [Wietse Boonstra](https://www.divd.nl/team/Wietse%20Boonstra/) of DIVD, Additional research by [Finn van der Knaap](https://www.divd.nl/team/Finn%20van%20der%20Knaap/) of DIVD
- Products: SmarterTools - SmarterTrack V100.0.8019.14010
- CVSS: 8.8
- Reference: case {% divd DIVD-2021-00029 %}, {% cve CVE-2022-24384 %}
- Solution: Upgrade to the latest version

Description: Stored XSS in SmarterTools SmarterTrack. In SmarterTrack you can start a live chat to talk to a certain department. The problem with this is that you can change the values and execute an XSS when the operator opens the live chat.

PoC: Below is the PoC curl request, that starts a new chat containing the XSS;
The following POST parameters are vulnerable to the XSS:
* `CustomFields[0][DefaultValue]`
* `CustomFields[1][DefaultValue]`

Below is a Linux curl request where you need to change the “localhost” to the hostname of your SmarterTrack domain/IP.

```
curl -i -s -k -X $'POST' \
    -H $'Host: localhost:9996' -H $'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H $'Content-Length: 565' -H $'Origin: http://localhost:9996' -H $'Connection: close' \
    --data-binary $'ChatID=-1&InfoGuid=3c2f7485c3264143bfee29bdc2c4f95b&LastEventID=-1&UserLanguage=&UnsentMessageStandard=test&DepartmentID=3&Status=2&CustomFields%5B0%5D%5BID%5D=1&CustomFields%5B0%5D%5BDefaultValue%5D=<IMG+\"\"\"><SCRIPT>alert(1)</SCRIPT>\">&CustomFields%5B0%5D%5BSpecialMapping%5D=UserDisplayName&CustomFields%5B0%5D%5BDisplayName%5D=Display+Name&CustomFields%5B1%5D%5BID%5D=2&CustomFields%5B1%5D%5BDefaultValue%5D=i@a.a<IMG+\"\"\"><SCRIPT>alert(2)</SCRIPT>\">&CustomFields%5B1%5D%5BSpecialMapping%5D=UserEmailAddress&CustomFields%5B1%5D%5BDisplayName%5D=Email&VisitorGuid=' \
    $'http://localhost:9996/api/Chat/StartChat'
 ```

When a chat operator opens the live chat, the XSS will execute.

Impact: This vulnerability is worse than the first XSS. This is because this is stored in the ticket itself. Everyone that opens the ticket will be affected by it, unlike the reflected XSS.


![Screenshot of stored XSS](/img/DIVD-2021-00029/poc3a.png)
![Screenshot of stored XSS](/img/DIVD-2021-00029/poc3b.png)

## Path traversal - Uploading files

- CVE: {% cve CVE-2022-24387 %}
- Case: {% divd DIVD-2021-00029 %}
- Discoverd by: Wietse Boonstra
- Credits: Discovered by [Wietse Boonstra](https://www.divd.nl/team/Wietse%20Boonstra/) of DIVD, Additional research by [Finn van der Knaap](https://www.divd.nl/team/Finn%20van%20der%20Knaap/) of DIVD
- Products: SmarterTools - SmarterTrack V100.0.8019.14010
- CVSS: 9.1
- Reference: Case {% divd DIVD-2021-00029 %}, {% cve CVE-2022-24384 %}
- Solution: Upgrade to the latest version

Description: When authenticated as administrator or another operator, it is possible to upload files in the app data folder and perform a path traversal to overwrite the systemsetting.xml file located in the app_data/Config folder. Any other file within the app data folder is also possible to overwrite, resulting in a denial of service (DoS).

POC: Open the management interface and start a new ticket. Then add an attachment to the ticket and open BurpSuite (or any other man in the middle proxy). Go to the proxy and then HTTP history, here you can find the `POST /FileStorageUpload.ashx`. Send this to the repeater and go to line 20 where you can see the name of the file you uploaded. From here you can change the name and below that the content that is in the file. When you send it, it will appear in the App_data folder.

In other words, the POST parameter “name” is vulnerable to a path traversal attack. Because the SmarterTrack folder has no write privileges for the user, it is not possible to write outside the App_data folder. It is possible to write in c:\windows\temp\ confirming a path traversal.

Impact: This could have a big impact on the files within the SmarterTrack application since they could be overwritten and an attacker could change the content inside files. This could affect how SmarterTrack is running on the server.

![Screenshot of file overwrite vulnerability](/img/DIVD-2021-00029/poc4a.png)
![Screenshot of file overwrite vulnerability](/img/DIVD-2021-00029/poc4b.png)
