---
layout: post
title: Axiell Iguana CMS full disclosure
author: Victor Pasman
researchers:
    - Amr Al Hallak
    - Frank Breedijk
    - Max van der Horst
excerpt: "Full disclosure of multiple injection vulnerabilities discovered in Axiell Iguana CMS"
---
DIVD received a vulnerability report from external researcher Amr Al Hallak about multiple injection vulnerabilities in the Axiell Iguana CMS, a content management system used by libraries. The vulnerabilities range from reflected cross-site scripting to a critical local file inclusion and can be leveraged to compromise a website running the affected software.

DIVD is a CVE Numbering Authority (CNA) and has used these rights to assign the following CVEs to the vulnerabilities included in the write-up below:
- {% cve CVE-2022-45049 %}
- {% cve CVE-2022-45050 %}
- {% cve CVE-2022-45051 %}
- {% cve CVE-2022-45052 %}

All four vulnerabilities were reported to the vendor and fixed in Iguana 4.5.02, released on 2022-11-03. The case ({% divd DIVD-2022-00064 %}) has since been closed. The rest of this post contains the full technical write-up of each vulnerability.

## Reflected XSS via the `url` parameter on `novelist.php` - CVE-2022-45049

- CVE: {% cve CVE-2022-45049 %}
- Case: {% divd DIVD-2022-00064 %}
- Discovered by: Amr Al Hallak
- Credits: Reported to DIVD by researcher Amr Al Hallak.
- Products: Axiell Iguana CMS (Windows, Linux)
- Affected versions: All versions prior to 4.5.02
- CVSS: 6.1 (MEDIUM) — `CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:L/I:L/A:N`
- CWE: CWE-79 Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')
- Reference: Case {% divd DIVD-2022-00064 %}, {% cve CVE-2022-45049 %}
- Solution: Upgrade to Iguana 4.5.02 or higher.

A reflected XSS vulnerability was found in Axiell Iguana CMS. The `url` parameter on the `novelist.php` endpoint does not properly neutralise user input before it is reflected back into the page, allowing an attacker to execute arbitrary JavaScript in a victim's browser in the context of the vulnerable site.

Proof of concept as reported against the researcher's test host:

```
https://<host>/iguana/php/novelist.php?url=%3Cscript%3Ealert(1)%3C/script%3E
```

The decoded payload is `<script>alert(1)</script>`, a benign marker used only to demonstrate script execution.

**Suggested actions**

Upgrade to the latest version of Iguana CMS.

## Reflected XSS via the `title` parameter on `twitter.php` - CVE-2022-45050

- CVE: {% cve CVE-2022-45050 %}
- Case: {% divd DIVD-2022-00064 %}
- Discovered by: Amr Al Hallak
- Credits: Reported to DIVD by researcher Amr Al Hallak.
- Products: Axiell Iguana CMS (Windows, Linux)
- Affected versions: All versions prior to 4.5.02
- CVSS: 6.1 (MEDIUM) — `CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:L/I:L/A:N`
- CWE: CWE-79 Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')
- Reference: Case {% divd DIVD-2022-00064 %}, {% cve CVE-2022-45050 %}
- Solution: Upgrade to Iguana 4.5.02 or higher.

A reflected XSS vulnerability was found in Axiell Iguana CMS. The `title` parameter on the `twitter.php` endpoint does not properly neutralise user input, resulting in arbitrary JavaScript execution in a victim's browser.

Proof of concept as reported against the researcher's test host:

```
https://<host>/iguana/php/twitter.php?title=%3Cscript%3Ealert(1)%3C/script%3E
```

**Suggested actions**

Upgrade to the latest version of Iguana CMS.

## Reflected POST XSS via the `module` parameter on `Service.Template.cls` - CVE-2022-45051

- CVE: {% cve CVE-2022-45051 %}
- Case: {% divd DIVD-2022-00064 %}
- Discovered by: Amr Al Hallak
- Credits: Reported to DIVD by researcher Amr Al Hallak.
- Products: Axiell Iguana CMS (Windows, Linux)
- Affected versions: All versions prior to 4.5.02
- CVSS: 6.1 (MEDIUM) — `CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:L/I:L/A:N`
- CWE: CWE-79 Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')
- Reference: Case {% divd DIVD-2022-00064 %}, {% cve CVE-2022-45051 %}
- Solution: Upgrade to Iguana 4.5.02 or higher.

A reflected XSS vulnerability was found in Axiell Iguana CMS that is triggered through a POST request. The `module` parameter on the `Service.Template.cls` endpoint does not properly neutralise user input, resulting in arbitrary JavaScript execution in a victim's browser.

Because the injection point is in a POST parameter, exploitation requires the victim to submit a request carrying the malicious `module` value — for example via an attacker-hosted page containing an auto-submitting form that targets the vulnerable endpoint. The researcher demonstrated this with a self-hosted proof-of-concept HTML page.

**Suggested actions**

Upgrade to the latest version of Iguana CMS.

## Local File Inclusion via the `url` parameter on the image proxy endpoint - CVE-2022-45052

- CVE: {% cve CVE-2022-45052 %}
- Case: {% divd DIVD-2022-00064 %}
- Discovered by: Amr Al Hallak
- Credits: Reported to DIVD by researcher Amr Al Hallak.
- Products: Axiell Iguana CMS (Windows, Linux)
- Affected versions: All versions prior to 4.5.02
- CVSS: 9.8 (CRITICAL) — `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`
- CWE: CWE-552 Files or Directories Accessible to External Parties
- Reference: Case {% divd DIVD-2022-00064 %}, {% cve CVE-2022-45052 %}
- Solution: Upgrade to Iguana 4.5.02 or higher.

A Local File Inclusion vulnerability was found in Axiell Iguana CMS. Due to insufficient neutralisation of user input on the `url` parameter of the image proxy endpoint (`imageProxy.type.php`), an unauthenticated external attacker can traverse the file system and read files on the server. As this requires no privileges and no user interaction while exposing confidentiality, integrity and availability, it carries a critical CVSS score.

Proof of concept as reported against the researcher's test host (path-traversal to a Windows system file):

```
https://<host>/iguana/php/imageProxy.type.php?url=../../../../../../../../../../../../../../windows/win.ini
```

**Suggested actions**

Upgrade to the latest version of Iguana CMS.

## Timeline

| Date | Event |
| --- | --- |
| 2022-09-08 | First four vulnerabilities (reflected XSS, POST XSS, LFI) reported to DIVD; evaluation and reporting process starts. |
| 2022-11-03 | First contact between Axiell and DIVD. Axiell releases Iguana 4.5.02, fixing CVE-2022-45049, CVE-2022-45050, CVE-2022-45051 and CVE-2022-45052. |
| 2022-11-17 | Researcher and DIVD confirm the four vulnerabilities are remediated by the patch. |
| 2022-11-21 | Researcher reports two additional vulnerabilities (SSRF and reflected XSS); DIVD contacts Axiell. |
| 2023-01-03 | Limited disclosure for the four CVEs. |
| 2024-07-22 | Case closed. |

## Summary

Multiple injection vulnerabilities were identified in Axiell Iguana CMS. Leveraging these vulnerabilities could allow an attacker to compromise a website running the affected software. All affected users should upgrade to Iguana 4.5.02 or higher.
