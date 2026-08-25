---
layout: post
title: Sungrow web portal full disclosure
author: Victor Pasman
researchers:
    - Harm van den Brink
excerpt: "Full disclosure of a vulnerability discovered in the Sungrow web portal"
---
DIVD received a vulnerability report from [ENCS](https://encs.eu/) about the Sungrow web portal. The vulnerability was discovered by researcher Harm van den Brink.

DIVD is a CVE Numbering Authority (CNA) and has used these rights to assign the following CVE to the vulnerability included in the write-up below:
- {% cve CVE-2025-29756 %}

The rest of this post contains the full technical write-up of the vulnerability.

## MQTT endpoint and credentials used by the web portal can be used to obtain data of other Sungrow inverters (and potentially manipulate them) - CVE-2025-29756

- CVE: {% cve CVE-2025-29756 %}
- Case: {% divd DIVD-2025-00009 %}
- Discovered by: Harm van den Brink
- Credits: Reported to DIVD by [ENCS](https://encs.eu/). Discovered by researcher Harm van den Brink.
- Products: Sungrow web portal
- CVSS: 8.3 (HIGH) in case the connection is read only — `CVSS:4.0/AV:N/AC:L/AT:N/PR:L/UI:N/VC:H/VI:N/VA:N/SC:H/SI:N/SA:N/AU:Y/V:C`. 9.0 (CRITICAL) in case commands can also be sent — `CVSS:4.0/AV:N/AC:L/AT:P/PR:L/UI:N/VC:H/VI:H/VA:H/SC:H/SI:H/SA:H/S:P/AU:Y/V:C`
- Reference: Case {% divd DIVD-2025-00009 %}, {% cve CVE-2025-29756 %}
- Solution: Restrict access to the MQTT topics to only those that belong to the account, either by using a unique key pair for the devices in an account or by restricting rights on the MQTT broker.

The Sungrow web portal uses an underlying MQTT broker service to receive live updates of the status of the inverter. The web portal makes an API call to retrieve obfuscated/encrypted information about the MQTT broker's endpoint from the Sungrow API and decrypts those credentials in JavaScript.

Via the JavaScript debugger it is possible to obtain the MQTT endpoint and credentials and subscribe to the topic(s) for the inverter(s) in the account.

The messages sent over MQTT are encrypted using asymmetrical encryption, but, again via JavaScript debugging, it is possible to obtain the RSA key that can be used for decryption (and potentially encryption) of MQTT messages.

This is all more or less expected, as it is impossible to implement an MQTT client in JavaScript in which this is not possible. However, the steps below should not be possible.

Using the MQTT credentials it is possible to subscribe to all topics, at which point the MQTT client starts receiving metadata about all other Sungrow inverters connected to the same MQTT broker. When we summed up the power production of 20 seconds of MQTT messages, we observed a total of over 400 MW of power.

We suspect that, by encrypting control messages with the same key and publishing them to these MQTT topics, it might also be possible to change settings on other inverters, but we have not verified this for fear of causing damage to or adverse effects on other inverters.

**Suggested actions**

Restrict access to the MQTT topics to only those that belong to the account, either by using a unique key pair for the devices in an account or by restricting rights on the MQTT broker.

Screenshot 1: MQTT credentials (secrets redacted)

![MQTT credentials obtained via the JavaScript debugger (redacted)](/img/DIVD-2025-00009/CVE-2025-29756-01.png)

Screenshot 2: obtaining keys (secrets redacted)

![Obtaining the decryption material via JavaScript debugging (redacted)](/img/DIVD-2025-00009/CVE-2025-29756-02.png)

Screenshot 3: obtaining keys (secrets redacted)

![Obtaining the RSA public key via JavaScript debugging (redacted)](/img/DIVD-2025-00009/CVE-2025-29756-03.png)
