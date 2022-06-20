---
title: Report DIVD-2020-00009 - Pulse Secure VPN enterprise Leak
date: 11 May 2021
author: Jeroen van de Weerd
excerpt: A list of usernames and IP addresses of more than 900 Pulse Secure VPN enterprise servers was leaked online. Security researchers forwarded this list to DIVD who notified the victims.   
---
<header>
    <h2>Report DIVD-2020-00009 - Pulse Secure VPN enterprise Leak</h2>
    <span>11 May by Jeroen van de Weerd</span>
</header>
Case lead Frank Breedijk

On August 4, 2020, a list of usernames and IP addresses of more than 900 Pulse Secure VPN enterprise servers was leaked online. Security researchers forwarded this list to DIVD to notify the victims.

The following data was present in the dataset:
- IP addresses of Pulse Secure VPN servers
- Pulse Secure VPN server firmware version
- SSH keys for each server
- A list of all local users and their password hashes
- Admin account details
- Last VPN logins, including usernames and unencrypted passwords
- VPN session cookies

Pulse Secure VPN servers are often used as a gateway to a corporate network. Staff can remotely connect to internal apps via such a server. Pulse VPN and similar services are therefore a target of ransomware gangs and APTs.

A vulnerability of the Pulse systems was first disclosed in August 2019. In June, a hacker scanned the vulnerable systems. At the time, there were still more than 600 vulnerable systems.

Researchers from DIVD CSIRT have obtained the dataset of usernames and IP addresses. On August 5, 2020, the DIVD started to warn Dutch companies. Notifications were sent to the abuse email addresses of the administrators of the Dutch IP addresses on the list.

December 3, 2020, the case was closed.
