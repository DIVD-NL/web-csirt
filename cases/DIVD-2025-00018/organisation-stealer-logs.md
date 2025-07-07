---
layout: page
case: DIVD-2025-00018
title: Recommendations for organisation of which account credentials were  found in operation Endgame 2.0 stealer logs
excerpt: This page contains recommendation for organisations that have received a notification from us about credentials for undetermined origin were found as part of Operation Endgame
redirect_from:  /DIVD-2025-00018/organisation-stealer-logs/
---
This page is a sub page of the case file for case [DIVD-2025-00018 - Victim Notification Operation Endgame](/DIVD-2025-00018/), which contains the general information about this case.

## Operation Endgame 2.0 stealer logs, 62M accounts

[Operation Endgame 2.0](https://www.politie.nl/nieuws/2025/mei/22/11-internationale-politiediensten-pakken-met-operation-endgame-door-in-bestrijding-ransomware.html) marks new takedowns and new information obtained by the organizations behind this operation.

Part of the information obtained by law enforcement is information from [stealer logs](https://socradar.io/stealer-logs-everything-you-need-to-know/). Log files that contain account credentials obtained from devices by specialised infomation stealer malware (infostelaers). These stealers logs contain a username, a (obfuscated) password, the url the password relates to as well as a date (and sometime time) the credentials where stolen.

DIVD is performing victim notification on this dataset, in line with our [stolen credentials](/credentials) policy. 

## What does this mean?

If you, or your users are in the stealer logs it means two things:
* At some point in time they used a device which was infected with (infostealer) malware
* The credentials in the log have been compromised and should not be used anywhere anymore


## What is DIVD doing with the data?

As per the stolen credentials policy we have compiled a [two lists of apex domains](/downloads/DIVD-2025-00018/stealer-apexes.tgz) one with the apex domains of the usernames and one with the apex domains of the services the credentials belong two. So if e.g. the stealer log says that `somebody@gmail.com` is user password `hj*******H5` to access `facebook.com`, `gmail.com` would be on the `email_apex` list and `facebook.com` will be on the `url_apexes` list.

We will provide certs, csirts and security teams with the records for those domains they can prove falls under their jursidiction. Please review the apex lists for you domains. Beware the certain lists are long then excel can handle.

## My domains are on the list, what should I do?

* Contact us at [DIVD-2025-00018@csirt.divd.nl](mailto:DIVD-2025-00018@csirt.divd.nl?SUBJECT:Question+about+DIVD-2025-00018+steaqler+logs) to get all recors related to these domains
* Determine the severity of this situation based on the number of records you receive
* Investigate the accounts of these users for suspicious activities like large volumes of sent messages or unusual log in times or unusual mail rules
* Consider scanning the devices of these users with malware detection tools and advice these users to do the same thing with personal devices
* Dual factor authentication can stop an attacker that has a valid username and password combination from abusing the account [implement two-step verification](https://ssd.eff.org/module/how-enable-two-factor-authentication) in as many places as possible.
* Consider reporting this event to the appropriate authorities, e.g. law enforcement, privacy and other regulators.

## More questions?

The [main case file](/DIVD-2025-00018/) contains a Frequently Asked Questions (FAQ) section. If that does not answer your questions, please reply to the email you received or email us at [DIVD-2025-00018@csirt.divd.nl](mailto:DIVD-2025-00018@csirt.divd.nl?SUBJECT:Question+about+DIVD-2025-00018+steaqler+logs).

For more information, see the [main case file](/DIVD-2025-00018/).



