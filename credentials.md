---
title: How we deal with leaked credentials
---
# How we deal with leaked credentials

Leaked credentials are a problem that is getting bigger and bigger. Usernames and passwords are being stolen, via malware, phishing or hacking, and sold, traded and exchanged on a massive scale. As  DIVD we have taken it upon ourselves to inform victims, not only of vulnerable systems, but also of leaked credentials.

The growth of this is evident in the numbers associated with the cases that evolve around stolen credentials:
Our first case in 2020, ([DIVD-2020-00013](/DIVD-2020-00013)) dealt with "just" 386 stolen credentials, the [second case](/DIVD-2021-00004), in 2021, also dealt with a small number of aproximatly 100 credentials. But, the [Warehouse bot case](/DIVD-2021-00012), cause us to quickly level, when we needed to notify ~2.5M email addresses of a breach, and the [next case](/DIVD-2021-00015) had a similar number.
[Operation Endgame](/DIVD-2024-00019) caused us to level up again. With approximatly 18M credentials involved. Shortly followed by [case DIVD-2024-00022](/DIVD-2024-00022) with a whopping 1.2 **billion** credentials from stealer logs and even more from combo lists.

## Practical problems

### Email

It is impossible for us to send these large volumes of emails. Emailing millions or billions of addresses (of which a large portion is no longer active) will clog our email system and get us on the "known spammers" list of large email providers quickly, effectively hurting the rest of our operation.

There are commercial parties that do handle these volumes. Email at this scale is an art in itself. We had various coversations with these vendors. Sending these volumes of email is costly, 5 figure type costly. Being a not for profit, volunteer run organisation, we do not have the budget and if we had it, we would not be willing to spend that kind of money it. (If you are willing to [donate](https://www.divd.nl/donate) that kind of money, we have better uses for it). And, since we do not have up front consent from recipients of these emails, these parties are not eager to facilitate us.

### Does it help?

Lots of credentials are from so called [combo lists](https://scirge.com/glossary/combo-list). Credentials from different breaches, combined, traded and often of low quality. Most of the time these lists only contain a username and password and are devoid of any context like when the the credentials were "harvested", which platform, service or system they initially belonged to and where the breach occured.

When does notifying on a breach help and when does it hurt? Without any context it is unlikely that a user can take any postive action. Does it help to know you are now in 15 instead of 14 breaches?

## Our solution

If we want to tackle these kind of breaches we have to do so in a particular way.

### Context required

We will only process credentials if we can place them into a context. That means that besides username and password we need more information so we can give actionable advice with our notification. 

More context is better in this case. Think about:
* What are the credentials for?
* How and when was the data obtained?

This also means, that by definition we will not process combo lists, unless there is a way to provide context.

### How we handle passwords

We feel that the content of the password itself is often vital context in the decision on what to do about leaked credentials. But, feel that distributing plain text password themselves is even worse. 

We will therefore mask passwords with the followig logic:
* For passwords of 10 or more we will provide the first two and last two characters and replace all other characters with an asterisk.
* For passwords less then 10 characters we will provide the first and last character and replace all other characters with an asterisk.

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

For smaller breaches (less then 2M email addreses involved) we will still opt to inform victims/targets directly.

### Distribution in case of largers numbers via (government and other) CERTS, CSIRTS and Security Teams

For larger breaches we will make two extracts

#### Email apex extract

This extract will contain the apex domains of the emails involved in the breach and for each apex the number of unique email address and password combinations.

#### Url apex extract

If we have the url that the password belongs to, we will also make this extract. It will contain the apex domains of the urls and per apex the number of unique email addresses containted in the breach.

#### Distribution via (government and other) CERTS, CSIRTS and Security Teams

Based on these extracts we will invite (government and other) CERTS, CSIRTS and Security Teams to provide us with the apexes that are in the extract and in their constituancy or that they otherwise have a demonstrable legitimate interest in. For those apexs we will return the data.

In order to address ethical concers regarding the sharing of PII with government organisations of countries with a less than ideal situation with regards to the upholding of human rights, we will only provide data to government organisations of countries that score higher then 4 in the most recent year of the [Human rights index](https://ourworldindata.org/grapher/human-rights-index-vdem).

## How to report a credential breach

If you want our help with breached credentials send us an email at csirt@divd.nl. From there on we will arrange the details.

## F.A.Q.

### Can I remain anonymous?

We like to know that we are processing details from a reliable source. We are not interested in you identity persé, as long as we can establish that you are a reputable source. This can e.g. be via a reference from somebody we know and trust.

### You are sharing old data, can't you deduplicate you data?

We are reaching out to various organisation that also process leaked credentials to see if we can work something out. But so far we have not found a practical solution yet.

### Can I still request my data as an individual?

Yes you can!

### Why do you feel data country X scores Y on the Human Rights Index?

We base our judgement on the [Human rights index](https://ourworldindata.org/grapher/human-rights-index-vdem) as it was the most reliable public source we could find. We don't determine the score, we just follow it.

## Cases involving stolen credentials
{% assign cases = site.cases | reverse -%}
{%- for case in cases -%}
{%- if case.creds > 0 -%}
* [{{ case.title }}]({{ case.url }})
{% endif -%}
{%- endfor %}

