---
title: How we deal with leaked credentials
---
# How we deal with leaked credentials

The existence of leaked credentials is an ever-growing problem. Usernames and passwords are being stolen through malware, phishing or hacking. Afterwards, the leaked credentials are sold, traded and exchanged on a massive scale. We have taken it upon ourselves to inform victims of cybercrime, not only those with vulnerable systems but also those who have their credentials leaked online.

The expansion of this problem is evident in the rising numbers linked to cases involving stolen credentials:
Our first case in 2020, ([DIVD-2020-00013](/DIVD-2020-00013)) dealt with "only" 386 stolen credentials, the [second case](/DIVD-2021-00004), in 2021, also dealt with a small number of approximately 100 credentials. However, the [Warehouse bot case](/DIVD-2021-00012), cause us to quickly level up, when we needed to notify ~2.5M email addresses of a breach, and the [next case](/DIVD-2021-00015) had a similar number.
[Operation Endgame](/DIVD-2024-00019) caused us to level up again, with approximately 18M credentials involved. Shortly followed by [case DIVD-2024-00022](/DIVD-2024-00022) with a whopping 1.2 **billion** credentials from stealer logs and even more from combo lists.

## Practical problems

### Email

It is impossible for us to send these large volumes of emails. Emailing millions or billions of addresses (of which a large portion is no longer active) will clog our email system and get us quickly on the "known spammers" list of large email providers, effectively hurting the rest of our operation.

Managing a high volume of emails requires a specialized skill set. There are companies that handle this kind of distribution. We've had discussions with these providers, and sending such large volumes of email can be quite expensive, in the range of five figures. As a non-profit organization run by volunteers, we simply don't have the budget for this kind of expenditure, and even if we did, we wouldn't be willing to allocate those funds in this manner. (If you are willing to [donate](https://www.divd.nl/donate) that kind of money, we can think of better ways to utilize it). Additionally, since we, by nature, do not have up-front consent from the recipients of these emails, these service providers are hesitant to work with us.

### Does it help?

Lots of credentials are from so-called [combo lists](https://scirge.com/glossary/combo-list). These lists combine credentials from different breaches, are traded, and are often of low quality. Most of the time, these lists only contain a username and password and are devoid of any context, like when the credentials were "harvested," which platform, service, or system they initially belonged to, and where the breach occurred.

When does being notified of a breach help, and when does it hurt? Without additional context, it's unlikely that a user can take any positive action. Does knowing you are now in 15 breaches instead of 14 help?

## Our solution

If we want to address cases of leaked credentials, we must do so in a specific manner.

### Context required

We will only process credentials if we can provide context. This means that, in addition to the username and password, we require additional information to offer actionable advice with our notifications.

More context is better in this case. Think about:
* What service/URL are the credentials initially for?
* How, when, and where have the leaked credentials been obtained?

This means we will not process combo lists without context.

### How we handle passwords

We feel that the content of the password itself is often vital context in the decision on what to do about leaked credentials. However, we believe that distributing plain text passwords is even more problematic. 

We will therefore mask passwords with the following logic:
* For passwords of 10 or more we will provide the first two and last two characters and replace all other characters with an asterisk.
* For passwords less than 10 characters we will provide the first and last character and replace all other characters with an asterisk.

Or in Python code:

```python
def mask_password(passwd: str) -> str :
    pwlen = len(passwd)
    if pwlen >= 10 :
        return("{}{}{}".format(passwd[0:2],"*" * (pwlen-4),passwd[-2:]))
    else :
        return("{}{}{}".format(passwd[0],"*" * (pwlen-2),passwd[-1:]))
```

### Distribution in case of limited numbers

For smaller breaches (less than 2M email addresses involved) we will still opt to inform victims/targets directly.

### Distribution in case of larger numbers via (government and other) CERTS, CSIRTS and Security Teams

For larger breaches, we will make two extracts

#### Email apex extract

This extract will contain the apex domains of the emails involved in the breach and for each apex the number of unique email addresses and password combinations.

#### Url apex extract

If we have the URL that the password belongs to, we will also make this extract. It will contain the apex domains of the URLs and per apex the number of unique email addresses contained in the breach.

#### Distribution via (government and other) CERTS, CSIRTS and Security Teams

Based on these extracts we will invite (government and other) CERTS, CSIRTS and Security Teams to provide us with the apexes that are in the extract and in their constituency or that they otherwise have a demonstrable legitimate interest in. For those apexes, we will return the data.

In order to address ethical concerns regarding the sharing of PII with government organisations of countries with a less than ideal situation with regard to the upholding of human rights, we will only provide data to government organisations of countries that score higher than 4 in the most recent year of the [Human rights index](https://ourworldindata.org/grapher/human-rights-index-vdem).

## How to report a credential breach

If you want our help with breached credentials send us an email at csirt@divd.nl. From there on we will arrange the details.

## F.A.Q.

### Can I remain anonymous?

We like to know that we are processing details from a reliable source. We are not interested in your identity persé, as long as we can establish that you are a reputable source. This can e.g. be via a reference from somebody we know and trust.

### You are sharing old data, can't you deduplicate you data?

We are reaching out to various organisations that also process leaked credentials to see if we can work something out. But so far we have not found a practical solution yet.

### Can I still request my data as an individual?

Yes, you can!

### Why do you feel data country X scores Y on the Human Rights Index?

We base our judgement on the [Human rights index](https://ourworldindata.org/grapher/human-rights-index-vdem) as it was the most reliable public source we could find. We don't determine the score, we just follow it.

## Cases involving stolen credentials
{% assign cases = site.cases | reverse -%}
{%- for case in cases -%}
{%- if case.creds > 0 -%}
* [{{ case.title }}]({{ case.url }})
{% endif -%}
{%- endfor %}

