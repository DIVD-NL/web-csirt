---
layout: page
case: DIVD-2026-00007
title: Recommendations for victims whos WordPress website was found to be compromised with SocGholish in Operation Endgame S03E03 
excerpt: This page contains recommendation for administrators that have received a notification from DIVD that their website was compromisedas part of Operation Endgame S03E03
redirect_from:  
- /DIVD-2026-00007/instructions-for-wordpress-admins/
---
This page is a sub page of the case file for case [DIVD-2026-00007 - Victim Notification Operation Endgame S03E03](/DIVD-2026-00007/), which contains the general information about this case.

## It was determined that your website was spreading malware via the SocGholish malware downloader during Operation Endgame edition S03E03

If you are reading this it probably means that your website was spreading malware via the SocGholish malware downloader, and maybe still is. You website was likely compromised through stolen administrator credentials.

## What does this mean?

Your WordPress adminisator credentials have been stolen at some point. Criminals have used these credentials to compromise your WordPress site and impant the SocGholish stealer there. The malware downloader has been using your site to serve fake browsers update dialog screens to convince innocent visitors of you website to download infostealer malware.

## What should I do?

Your website has been compromised. We have sent you the URL and the email address of the account on it that was used to compromise it.

The following articles describe the malware and how to remove it:
- [SocGholish (FakeUpdate) Malware: How to Protect WordPress Websites?](https://secure.wphackedhelp.com/blog/fakeupdates-socgholish-malware/) — WPHacked Help, January 2024
- [How to Clean-Up a WordPress Website Infected with SocGholish Malware](https://zealth.net/how-to-clean-up-a-wordpress-website-infected-with-socgholish-malware/) — Zealth Digital Marketing, July 2024
- [Steps to Protect Your Site from SocGholish Malware](https://thewhitelabelagency.com/socgholish-malware/) — The White Label Agency, March 2026
- [SocGholish Malware Attack – UPDATED 08/03/24](https://helpme.haleymarketing.com/hc/en-us/articles/28413323899796-SocGholish-Malware-Attack-UPDATED-08-03-24) — Haley Marketing, August 2024
- [SocGholish Malware: What It Is & How to Prevent It](https://blog.sucuri.net/2024/06/socgholish-malware.html) — Sucuri Blog, June 2024
- [New Wave of SocGholish Infections Impersonates WordPress Plugins](https://blog.sucuri.net/2024/03/new-wave-of-socgholish-infections-impersonates-wordpress-plugins.html) — Sucuri Blog, March 2024
- [What is SocGholish Malware? Detection & Removal](https://www.sitelock.com/blog/socgholish-malware/) — SiteLock, March 2026

### Summary of steps
We have created the AI summary below to help you


#### What is SocGholish?

SocGholish (also known as FakeUpdates) is a JavaScript-based malware campaign that compromises legitimate websites by injecting malicious scripts. Visitors to infected sites are presented with fake browser or software update prompts, tricking them into downloading malware. Once executed, secondary payloads can lead to ransomware infections, credential theft, or unauthorized network access.

The malware is associated with threat actor **TA569** and is notable for its multi-layered infection approach, which can make detection and cleanup more difficult.

**Common signs of infection:**
- Fake browser update pop-ups presented to visitors
- Unusual redirects to unfamiliar pages
- Email disruptions (outbound mail flagged or quarantined by services like Proofpoint)
- Site warnings in Google Safe Browsing or browser security tools
- Unknown/suspicious JavaScript injected into page source or database records

#### Cleanup Steps

##### Step 1 – Identify the Infection

Use one or more scanning tools to confirm infection and locate malicious code:

- [Sucuri SiteCheck](https://sitecheck.sucuri.net/) (free, external scanner)
- [Wordfence](https://wordpress.org/plugins/wordfence/) (WordPress plugin, server-side scan)
- [MalCare](https://wordpress.org/plugins/malcare-security/) (WordPress plugin)

Also check for unauthorized DNS subdomains — SocGholish sometimes uses **domain shadowing**, adding subdomains (e.g. `update.yourdomain.com`) that point to malicious servers.

##### Step 2 – Take a Full Backup

Before touching anything, create a complete backup of:
- All website files
- The WordPress database

This ensures you have a fallback in case cleanup goes wrong.

##### Step 3 – Take the Site Offline (Optional but Recommended)

To prevent further visitors from being exposed to the malicious payload, consider placing the site in maintenance mode or blocking public access temporarily.

##### Step 4 – Revoke and Reset All Credentials

Change all credentials that could have been compromised or used for unauthorized access:
- WordPress admin account passwords
- FTP/SFTP credentials
- Database passwords
- Hosting control panel passwords

Use strong, unique passwords for each.

##### Step 5 – Locate and Remove Malicious Code

Manually inspect the WordPress installation for injected scripts and unauthorized files.

**Key locations to check:**
- Root directory (`/public_html/`, `index.php`, `wp-config.php`)
- `wp-content/uploads/` (should contain no PHP files)
- `wp-content/themes/` (active theme files)
- `wp-content/plugins/`
- `wp-includes/`

**WordPress plugins that help locate injections:**
- **String Locator** – search file contents for suspicious strings (e.g. known SocGholish domain fragments or obfuscated JavaScript patterns)
- **Better Search Replace** – useful for finding and removing injected URLs or scripts across the database

**In the database:**
Check `wp_posts`, `wp_options`, and `wp_usermeta` for injected `<script>` tags or base64-encoded content. The `siteurl`, `home`, and widget option fields are common targets.

> ⚠️ Note: Some SocGholish variants use malicious PHP files that load additional obfuscated code layers, fetching the final payload from an external server. The total number of infected files can run into the thousands. If manual cleanup is impractical, use an automated solution or restore from a known-clean backup.

##### Step 6 – Run a Full Malware Scan

After manual cleanup, run a full server-side scan with a security plugin (Wordfence, Sucuri, or MalCare) to catch anything missed.

##### Step 7 – Update Everything

Outdated components are the most common entry point for this malware:
- WordPress core
- All installed themes (active and inactive)
- All installed plugins

Remove any plugins or themes that are unused or abandoned.

##### Step 8 – Fix File Permissions

Incorrect file permissions can leave the site vulnerable to re-infection:
- Directories: `755`
- Files: `644`
- `wp-config.php`: `600` (recommended)

##### Step 9 – Harden the Installation

After cleanup, implement additional hardening measures:
- Enable two-factor authentication (2FA) on all admin accounts
- Install a Web Application Firewall (WAF) — e.g. Wordfence, Cloudflare, or Sucuri Firewall
- Limit login attempts
- Disable XML-RPC if not needed
- Restrict access to `wp-admin` by IP if feasible

##### Step 10 – Verify the Site is Clean

Re-run external and internal scans to confirm no malicious code remains. Check the page source of the live site for any lingering `<script>` injections.

##### Step 11 – Request Review from Search Engines and Email Services

If the site was flagged or blacklisted:
- Submit for review via [Google Search Console](https://search.google.com/search-console) (Security Issues → Request Review)
- Submit via [Bing Webmaster Tools](https://www.bing.com/webmasters/)
- If outbound email is being quarantined by services like Proofpoint, request a URL reputation review with those vendors after confirming the site is clean

##### Step 12 – Monitor and Maintain

- Set up ongoing file integrity monitoring
- Schedule regular automated backups
- Monitor DNS records for unauthorized subdomains
- Regularly review WordPress user accounts for unauthorized admins

## More questions?

The [main case file](/DIVD-2026-00007/) contains a Frequently Asked Questions (FAQ) section. If that does not answer your questions, please reply to the email you received or email us at [DIVD-2026-00007@csirt.divd.nl](mailto:DIVD-2026-00007@csirt.divd.nl?SUBJECT:Question+about+DIVD-2026-00007-victim).

For more information, see the [main case file](/DIVD-2026-00007/).
