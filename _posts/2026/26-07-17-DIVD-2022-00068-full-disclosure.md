---
layout: post
title: White Rabbit Switch full disclosure
author: Victor Pasman
researchers:
    - Tom Wolters (finder from Chapter8)
    - Victor Pasman
    - Frank Breedijk
    - Max van der Horst
excerpt: "Full disclosure of multiple vulnerabilities discovered in the White Rabbit Switch from CERN"
---
DIVD received a vulnerability report about the White Rabbit Switch from CERN. The vulnerabilities were discovered by researcher Tom Wolters of Chapter8.

DIVD is a CVE Numbering Authority (CNA) and has used these rights to assign the following CVEs to the vulnerabilities included in the write-up below:
- {% cve CVE-2023-22577 %}
- {% cve CVE-2023-22581 %}

The rest of this post contains the full technical write-up of the vulnerabilities.

## Unauthenticated password disclosure via configuration file read - CVE-2023-22577

- CVE: {% cve CVE-2023-22577 %}
- Case: {% divd DIVD-2022-00068 %}
- Discovered by: Tom Wolters (Chapter8)
- Credits: Reported to DIVD by Tom Wolters (Chapter8, tom@chapter8.com). Analysis by Victor Pasman (DIVD).
- Products: White Rabbit Switch, all versions prior to 6.0.1 (most recent vulnerable release 7/7/21)
- CVSS: 9.8 (CRITICAL) — `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`
- Reference: Case {% divd DIVD-2022-00068 %}, {% cve CVE-2023-22577 %}
- Solution: Upgrade to White Rabbit Switch version 6.0.2, which contains a fix for this vulnerability.

Within White Rabbit Switch it's possible as an unauthenticated user to retrieve sensitive information such as password hashes and the SNMP community strings.

The web application exposes a `showfile.php` endpoint that is used to serve context-sensitive "help pages" for the various configuration screens. The `help_id` and `name` GET parameters supplied by the visitor are passed unfiltered into the `wrs_display_help()` function, defined in `functions.php`.

One of the branches of `wrs_display_help()` handles a `help_id` value of `dotconfig`, in which case the function reads out the full contents of the application's configuration file (`kconfigfile`) and returns it directly to the requester:

```php
else if (!strcmp($help_id, "dotconfig")){
    $message = file_get_contents($GLOBALS['kconfigfile']);
    $message = str_replace("\n", "<br>", $message);
}
```

No authentication or authorization check is performed before this file is read and returned. As a result, simply requesting the following URL discloses the full configuration file, including the root password hash and SNMP read/write community strings, to any unauthenticated visitor:

```
https://<URL>/showfile.php?help_id=c8&name=dotconfig
```

The returned configuration includes lines such as network configuration, hostname, and — most critically — the encrypted/hashed root password (`CONFIG_ROOT_PWD_CYPHER`) and SNMP community strings.

**Suggested actions**

Upgrade to White Rabbit Switch version 6.0.2 or later. 

## Unauthenticated OS command injection via showfile.php - CVE-2023-22581

- CVE: {% cve CVE-2023-22581 %}
- Case: {% divd DIVD-2022-00068 %}
- Discovered by: Tom Wolters (Chapter8)
- Credits: Reported to DIVD by Tom Wolters (Chapter8, tom@chapter8.com). Analysis by Victor Pasman (DIVD).
- Products: White Rabbit Switch, all versions prior to 6.0.1 (most recent vulnerable release 7/7/21)
- CVSS: 9.8 (CRITICAL) — `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`
- Reference: Case {% divd DIVD-2022-00068 %}, {% cve CVE-2023-22581 %}
- Solution: Upgrade to White Rabbit Switch version 6.0.2, which contains a fix for this vulnerability.

White Rabbit Switch contains a vulnerability which makes it possible for an attacker to perform system commands under the context of the web application. In the default installation, the webserver runs as the root user, so this results in unauthenticated remote code execution as root.

The same `wrs_display_help()` function in `functions.php` contains a second branch, triggered when `help_id` is set to `file`, which passes the unfiltered `name` parameter directly into a `shell_exec()` call:

```php
else if (!strcmp($help_id, "file")){
    $msg = shell_exec("cat ".$GLOBALS['etcdir'].$name);
    $msg = explode("\n", $msg);
    for($i=0; $i<count($msg); $i++){
        $message .= $i.":  ".$msg[$i]."<br>";
    }
}
```

Because `$name` is concatenated directly into the shell command without any sanitization, an attacker can inject arbitrary shell metacharacters. Any command placed between a semicolon (`;`) and an ampersand (`&`) in the `name` parameter will be executed by the underlying system:

```
https://<URL>/showfile.php?name=txt;whoami&help_id=file
```

In testing, this returned `root` as the result of the injected `whoami` command, confirming the web application (and therefore any injected command) runs with root privileges. This could be leveraged, for example, to change the root password and obtain SSH access to the device.

**Suggested actions**

Upgrade to White Rabbit Switch version 6.0.2 or later.

## Timeline

- 2022-11-16: Two vulnerabilities (RCE and information disclosure) reported by Tom Wolters; DIVD starts evaluation and reporting process.
- 2022-11-16: First contact between CERN and DIVD.
- 2022-11-16 to 2022-12-09: Time to acknowledge.
- 2022-12-09: Vendor acknowledges receipt of vulnerabilities.
- 2023-04-11: CERN releases White Rabbit Switch 6.0.2, containing fixes for both CVE-2023-22577 and CVE-2023-22581.
- 2023-04-11: Limited disclosure of the White Rabbit Switch vulnerabilities.
- 2023-05-31: Case closed.
- 2026-07-16: Full Disclosure.

## More information

- {% cve CVE-2023-22577 %}
- {% cve CVE-2023-22581 %}
- Source: [White Rabbit project](https://ohwr.org/project/white-rabbit)
- Vulnerable source: [rootfs_override](https://ohwr.org/project/wr-switch-sw/blob/wr-switch-sw-v4.0-rc1/userspace/rootfs_override)
