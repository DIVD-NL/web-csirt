---
title: Report DIVD-2021-00012-Warehouse botnet
date: 2 November, 2021
author: Chris van 't Hof
excerpt: researcher Tom Wolters found a database with leaked credentials and together with DIVD he informed victims 
---
<header>
    <h2>Report DIVD 2021 00012 Warehouse botnet</h2>
    <span>2 november by Chris van 't Hof</span>
</header>
Case Lead: Frank Breedijk

Researchers: Tom Wolters and Lennaert Oudshoorn


On 20 May 2021 security researcher Tom Wolters was scanning the internet for open databases and found one which contained 2,5 million username/password combinations. Normally he would warn the owner, but this database appeared to be fed by a botnet, which got the credentials from malware infected browsers. He therefore contacted the hosting provider on 24 May, who got the database offline on the 26th. And he notified the Dutch police as well on the 25th. Neither the police nor the hoster was willing to inform the victims, so he decided to do it himself.

Analyzing the data further, Tom saw columns which mentioned the counties of the owner of the credentials, type of browser they were ‘harvested’ from and the url the credentials were associated with. The word  ‘warehouse_’ was mentioned in most column names, so Tom dubbed the dataset ‘Warehouse Botnet’.

Tom’s next problem was: how can you reach so many people? Most logical parties to involve were HaveIbeenpwnd and Scattered Secrets. They host databases with leaked credentials where each victim can check if their  own credentials have been compromised. First, Tom tested some of the credentials whether they were already in one of the databases, but they appeared not to be in either of them, so the data was still unknown. This was also confirmed by the very recent entry dates of the credentials, Rickey Gevers of Scattered Secrets replied. So, Tom submitted his data to Scattered Secrets. Haveibeenpwnd didn’t reply. Still, victims would only be informed that they were hacked if they had subscribed and for a lot of victims this is unlikely.  

Tom therefore turned to DIVD researcher Lennaert Oudshoorn for help. We, the DIVD, decided we were willing to help out, but also asked Tom to join the club and he was on boarded as new DIVD researcher. DIVD-CSIRT manager Frank Breedijk saw this dataset as an opportunity for a new branch of research. DIVD warned victims of leaked credentials in the past, for example those infected by the Mirai Botnet, but not on this scale and with fresh data, also the Mirai credentials were not personal accounts.

Before we sent out any notification, we also got in contact with the Dutch police to check whether we were not obstructing any crime investigation by notifying victims, this wasn’t the case.

On 2 June it took DIVD a full night to send all 2,5 million addresses an email with breach notification, including masked password and other details, together with the advice to change their passwords, check if their credentials have been abused, check their computer and consider reinstalling it and make sure antivirus is up to date. We also advised them to stop storing their passwords in the browser and start using a password manager. And of course: don’t use the same password on multiple sites.

The responses we received were quite diverse and interesting. Some people would send their thanks and promised to follow the advice, while some of them were distressed as they did not know what to do. We also received some responses from people who were irritated, or even cursed, thinking we were scamming them. We used these responses to adjust the notification to a more acceptable text. Finally, we also got some responses from accounts that were apparently compromised, as we got no thanks, but just a link with malware.

Next to the victims, there is another party that we wanted to make aware of this large scale credential theft, the site owners. For this we approached our network of Trusted Information Sharing Partners, like we normally do in our research. Still, unconditionally  sharing such a large set of sensitive data like usernames and passwords triggered privacy concerns. We therefore came up with the following method: first we scanned the database for unique site urls (which turned out to be 400.000), then asked our partners which site owners they could reach legitimately.  We matched these and gave the email addresses together with the first and last sign of the password and the date ‘harvested’ so site owners could test whether the passwords were reset since then.

Ironically, Tom, who works at a security company, also got a dataset on his customers through one of our TISPs.
