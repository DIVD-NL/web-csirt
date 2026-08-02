---
layout: post
title: CyberAuditWeb and videx-legacy-ssl full disclosure
author: Victor Pasman
case: DIVD-2024-00043
researchers:
    - Hidde Smit (Reseacher)
    - Wietse Boonstra (Researcher)
    - Max van der Horst (Analyst)
excerpt: "Full disclosure of multiple vulnerabilities discovered in CyberAuditWeb and videx-legacy-ssl"
---
DIVD researchers discovered multiple vulnerabilities in CyberAuditWeb (versions < 9.8.11) and in videx-legacy-ssl (versions 1.0.9 up to at least 1.1.3).

DIVD is a CVE Numbering Authority (CNA) and has used these rights to assign the following CVEs to the vulnerabilities described in this case:
- {% cve CVE-2205-22367 %} — SQL injection / credential overwrite in CyberAuditWeb (chained via the authentication bypass)
- {% cve CVE-2025-22366 %} — Server-Side Request Forgery in videx-legacy-ssl

The rest of this post contains the full technical write-up of the vulnerabilities.

## Vulnerability 1: Authentication bypass via missing return statement — CyberAuditWeb (fixed in 9.8.11)

- CVE: {% cve CVE-2025-22366 %}
- Case: {% divd DIVD-2024-00043 %}
- Products: CyberAuditWeb (versions < 9.8.11)
- CVSS: CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N/S:N/AU:Y/R:A/V:D/RE:L/U:Green
- Solution: Add the missing `return`/abort after the authorization check in `DownloadServlet`, so that failing the check actually halts request processing. Update to CyberAuditWeb 9.8.11 or later.

The vulnerable code is located in `caw_ent.jar:com/videx/cyberaudit/webtier/manage/trim/DownloadServlet.class`. The handler checks for a `manage` session attribute and sends a 404 ("Please log in") if it is absent — but does not stop execution afterward. Because there is no `return` (or equivalent halt) following the error response, control flow continues and unconditionally sets `manage` to `true` on the session regardless of whether the check passed:

```java
Boolean manage = (Boolean) req.getSession().getAttribute("manage");
if (manage == null) {
     resp.sendError(404, "Please log in");
}
req.getSession().setAttribute("manage", true);
```

This can be reproduced by following these steps in order:

1. Request `https://<host>/CyberAuditWeb/mobile/Login.do` and click "Next" to obtain a valid session, including CSRF tokens.
2. Request `https://<host>/CyberAuditWeb/manage/trim/download/3`. This hits the flawed check above and — regardless of the outcome of the check — sets `manage=true` on the session via `req.getSession().setAttribute("manage", true);`.
3. Request `https://<host>/CyberAuditWeb/manage/ManageHome.act`. The session now carries `manage=true`, so this management endpoint is reachable without ever having authenticated.

**Suggested actions**

Add a proper halt (`return;` or equivalent) immediately after the `sendError` call so that failing the authorization check actually prevents the subsequent code from running. Update to CyberAuditWeb 9.8.11 or later, which is reported to return HTTP 404 correctly for this path.

## Vulnerability 2: Server-Side Request Forgery in videx-legacy-ssl (tested up to version 1.1.3)

- CVE: {% cve CVE-2025-22367 %}
- Case: {% divd DIVD-2024-00043 %}
- Products: videx-legacy-ssl (tested on version 1.1.3; patch status to be confirmed with vendor)
- CVSS: CVSS:4.0/AV:N/AC:L/AT:P/PR:L/UI:N/VC:L/VI:H/VA:N/SC:L/SI:L/SA:N/S:N/AU:Y/R:A/V:D/RE:L/U:Green
- Solution: Validate and restrict the destination of proxied/CONNECT-style requests server-side (allowlist of permitted hosts), and reject requests to internal/loopback address ranges. Confirm and apply the vendor's fix once available.

The `videx-legacy-ssl` component accepts a CONNECT-style request whose path embeds a base64-encoded target URL, and issues a GET request to that target on behalf of the server. This allows an attacker to make the server perform requests against arbitrary destinations, including internal-only services such as `127.0.0.1`, effectively bypassing network-level access restrictions.

```http
CONNECT 1111:a@eradix.nl/CyberAuditWeb/services/../../ssrf/aHR0cHM6Ly8xMjcuMC4wLjE6ODQ0Mi9DeWJlckF1ZGl0V2ViL0hvbWUuYWN0 HTTP/1.1
Host: 192.168.132.129:54443
<headers omitted for the PoC>

userName=TopLevel&password=TopLevel
```

The base64 segment in the path decodes to a target URL (in this example, a request to `https://127.0.0.1:8442/CyberAuditWeb/Home.act`), demonstrating that the server can be made to issue requests to arbitrary destinations of the attacker's choosing, including addresses that should only be reachable internally.

**Suggested actions**

Restrict the set of destinations the proxy/CONNECT handler will forward to (allowlist known-good hosts), explicitly block loopback and private address ranges, and remove or authenticate the base64-URL-in-path pattern rather than trusting it directly. Confirm with the vendor whether this is fixed in a version beyond 1.1.3, since the source PoC only confirms presence up to that version.

## More information

* {% cve CVE-2025-22366 %}
* {% cve CVE-2025-22367 %}
