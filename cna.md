---
---
# CVE Numbering Authority

The Dutch Institute for Vulnerability Disclosure is an official [CVE Numbering Authority (CNA)](https://www.cve.org/ProgramOrganization/CNAs). Within the CVE system, CNAs are organizations "responsible for the regular assignment of CVE IDs to vulnerabilities and for creating and publishing information about the vulnerability in the associated CVE Record." Within DIVD the CNA is operated by our CNA Admins.

Each CNA has a specific scope for which it operates, our scope (as visible on our [CVE partner page](https://www.cve.org/PartnerInformation/ListofPartners/partner/DIVD)) is:

Vulnerabilities in software discovered by DIVD, and vulnerabilities reported to DIVD for coordinated disclosure, which are not in another CNA’s scope

This means that we can issue CVE ID and publish CVE records for:
* Vulnerabilities discovered by our own researchers, including researchers of our sister organization csirt.global
* Vulnerabilities that are reported to us for coordinated disclosure by DIVD, if the systems these vulnerabilities apply to are not in the scope of another CNA

We are not a [CNA of last resort](https://www.cve.org/ResourcesSupport/Glossary?activeTerm=glossaryCNALR), nor is it our role to assign a CVE ID in case of a dispute between a CNA and a researcher. Disputes are handled by the appropriate "Root" CNA or ultimately by a CNA of Last resort (search for "root" or "CNA-LR" on the [CVE partner page](https://www.cve.org/PartnerInformation/ListofPartners)).

## Can you assign a CVE ID for me?

It depends. 

Are you a DIVD researcher or a researcher of csirt.global?
Yes, we can handle the creation of a CVE ID and publication of the CVE record for you.

Are you not a DIVD or csirt.global researcher?

In that case:
* Do you want to report a vulnerability to DIVD, and
* Do you want us to handle the coordinated disclosure for you, and
* Is the software not in the scope of another CNA?

Yes, we can help you.

Are you reaching out to us because you disagree with another CNAs decision?

In that case, we cannot help you. Please reach out to the appropriate Root CNA or a CNA of last resort.

## How do I submit a vulnerability to you?

The best way is to [send us an email](mailto:csirt@divd.nl). Once we have received your email we will get in touch with you.

## What happens when I submit a vulnerability to you?

First, we will try to validate your submission, to determine if:
* The submission is in line with our [code of conduct](https://www.divd.nl/code/)
* The submission is in line with our [CNA scope](https://www.cve.org/PartnerInformation/ListofPartners/partner/DIVD)
* The submission is not in the scope of another CNA
* The submission is (likely) valid.

If this checks out, and we are allowed to issue a CVE ID we will issue it to you and start our disclosure process.

## What is your disclosure process?

Our process consists of the following steps:
* Vendor notification
* Publication of a case file
* (Potential) product warning
* Limited disclosure and publication of CVE record
* (Optional) regular csirt case (scan & notify)
* (Optional) full disclosure

Please note that the timelines given below are an indication and not set in stone. We reserve the right to deviate from these timelines if this better suits our mission.

### Vendor notification

The first step in the disclosure process is to report the vulnerability to the vendor and for the vendor to acknowledge receipt of the notification.

We allow a vendor a reasonable time for acknowledgment of the notification. If we have put sufficient effort into notifying a vendor and the vendor has not acknowledged receipt, we will consider the notification as received after 30 days of sending the first notification.

### Publication of the case file

The DIVD CNA Admins will maintain one or more case files that cover a CVE ID requests and subsequent disclosures. This case file typically contains:
* The software and vendor related to the disclosure
* A detailed timeline, including time to acknowledge and time to fix.
* The associated CVE IDs
* (if desired) credits to the researchers that found the CVE and those that helped in the disclosure process

This case file will be published either:
* 30 days after the initial disclosure to the vendor, if the vendor fails to acknowledge receipt of the notification, or
* When we issue a product warning or publish a (limited) disclosure of the vulnerability

### (Potential) product warning

We know and understand that vendors need a reasonable time to fix vulnerabilities in their software. We generally adhere to the following timelines:
* 60 days after acknowledgment of receipt of the notification in case of a vulnerability in software
* 90 days after acknowledgment of receipt of the notification in case of a vulnerability in hardware/firmware

If a vendor fails to acknowledge the receipt of a notification we consider the notification to be received 30 days after we sent the first notification (see above).


If we feel a vulnerability is significantly critical and the vendor fails to fix the vulnerability within these timelines we will consider the publication of a "product warning". An advisory about the vendor's product to make users aware that the product contains a serious issue including guidance on how to mitigate the issue (usually by taking it offline).

We will only issue a product warning if it is in line with our mission: "We aim to make the digital world safer by reporting vulnerabilities we find in digital systems to the people who can fix them. We have a global reach, but do it Dutch style: open, honest, collaborative, and for free."  

### Limited disclosure and publication of the CVE record

We will publish limited details of the vulnerability in the CVE records and on the [CVEs section](/cves/) of our website in the following cases:
* When the vendor issues a fix for the vulnerability, 
* When the vendor fails to issue a fix for more than 60 / 90 days after (assumed) confirmation of the notification or assumed confirmation.
* When we deem limited disclosure necessary for the mission of DIVD (e.g. in case of a product warning)

### Regular CSIRT case

In case a vulnerability can be remotely detected within our [code of conduct](https://www.divd.nl/code), especially given the criteria of proportionality and subsidiarity we turn the disclosure into a regular CSIRT case. Meaning that DIVD will scan for vulnerability and notify owners of the affected systems.

We will typically do this either shortly before or right after the vendor releases a fix.

### Full disclosure

We typically postpose full disclosure of the details of a vulnerability to at least 6-12 months after the vendor has released a patch for the vulnerability. A full disclosure of the technical details of a vulnerability is a double-edged sword that aids both those that try to prevent exploitation as well as those that try to exploit systems.

We will only publish the details of a vulnerability if it helps us in our mission.

## Summary of timelines

| Action | When |
|----------|-------|
| Triage | Within 2 weeks after submission |
| Vendor notification | Within 1 week after successful triage |
| Vendor acknowledgment | Either 30 days after the vendor is first notified, or when the vendor acknowledges receipt of the notification. Whichever happens first, given that we put enough effort into the notification process. | 
| Publication of case file | On limited disclosure, publication of a product warning, or when a vendor fails to acknowledge receipt of notification within 30 days. |
| Product warning | If we feel a vulnerability is significantly critical and the vendor fails to fix the vulnerability within 60 days (software) or 90 days (hardware/firmware) after (assumed) acknowledgment of notification. (When this is in line with our mission.) |
| Limited disclosure | When the vendor issues a fix, or when the vendor fails to issue a fix within 60 / 90 days after (assumed) notification, or when we deem it necessary for the mission of DIVD. (But only if it does not harm the mission of DIVD.) |
| Full disclosure | 6-12 months after the vendor has released a fix or when we deem it necessary for the mission of DIVD. (But only if it does not harm the mission of DIVD.) |


Please note that the timelines given below are an indication and not set in stone. We reserve the right to deviate from these timelines if this better suits our mission.
