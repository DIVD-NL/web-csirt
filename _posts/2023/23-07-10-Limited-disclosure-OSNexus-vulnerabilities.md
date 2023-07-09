---
layout: post
title: Limited disclosure of 6 vulnerabilities in OSNexus Quantastor
author: DIVD
excerpt: "DIVD researched Wiets Boonstra has foudn 6 vulnerabilities in OSNexus Quantastor. We are disclosing these vulnerabilities and issueing a product warning as a last resort, due to a severly limited cooperation form the vendor."
---
The story of DIVD case [DIVD-2021-00020](/DIVD-2021-00020) is a story that started more then 1.5 years ago, when DIVD researcher [Wietse Boondsta](https://www.divd.nl/people/Wietse%20Boonstra/) discovered six vulnerabilities ( {% cve 2021-42079 %}, {% cve 2021-42080 %}, {% cve 2021-42080 %}, {% cve 2021-42080 %}, {% cve 2021-42080 %}, and {% cve 2021-4066 %} ) in [OSNexus Quantastor](https://www.osnexus.com/products/software-defined-storage).

As per our [CNA policy](/cna) we tried to contact the vendor and this was not a smooth ride. We started the process in November 2021 and it took us a lot of effort, and help from [NCSC-NL](https://www.ncsn.nl) and its US partners to finally, on the 12th of November 2022, get confiormation that our report was received and that these vulnerabilities would be addressed.

When OSNexus released version 6.0.0.533 of their product on 22 Nov 2022 of which they stated that these vulnerabilities would be fixed, we had good hopes to close this case, but it turned out that only two of the six vulnerabilities were fixed {% cve 2021-42080 %} and {% cve 2021-42083 %}.

We again tried to address the remaining vulnerabilities with OSNexus and again we were unable to get a reply from, or any kind of dialog with the vendor.

In line with our CNA policy we are now at a point where we feel that a limited disclosure of these vulnerabilities and a product warning is in order.

If you are using any version of OSNexus QuantaStor we strongly recommend that you make sure i it can only be accessed from trusted networks or by trusted individuals, as it may or may not contain Server Side Request Forgery (SSRF), Remote Command Execution and Local Privilege Escalation vulnerabilities that can be combined to fully own the device.

We strongly hope that OSNexus will reach out to us (via csirt@divd.nl) so we can work together to fix these vulnerabilities, but until that time we see disclosing these vulnerabilities and this product warning as our only option to make sure adminisrators can take the required measures.

For more information see:
* [Case file DIVD-2021-00020](/DIVD-2021-00020)
* {% cve CVE-2021-41079 %}
* {% cve CVE-2021-41080 %}
* {% cve CVE-2021-41081 %}
* {% cve CVE-2021-41082 %}
* {% cve CVE-2021-41083 %}
* {% cve CVE-2021-4406 %}
* [Wietse writeup](https://wbsec.nl/writeups/osnexus/)
