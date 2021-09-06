---

layout: post

title: Warehouse Botnet

author: Gerard Janssen

excerpt: "

    DIVD-researcher Tom Wolters vond een grote database met gebruikersnamen, wachtwoorden en authenticatie-cookies /

    DIVD researcher Tom Wolters has found a large database with usernames, passwords and authentication cookies

"

---

 <p>
    <small><a href='{{ page.url }}#english'>English below</a></small>
</p>


### Nederlands

 

Wat doe je als je een database vindt met miljoenen gestolen wachtwoorden?

 
Het overkwam de ethische hacker Tom Wolters. Zoals vaker zocht hij met behulp van de zoekmachine Shodan naar onveilige databases. Regelmatig vindt hij zo’n database. Van een webwinkel, of laatst nog, een uitgever van schoolboeken. De procedure is altijd hetzelfde. Hij neemt contact op met de eigenaar van de database, en geeft aanwijzingen over hoe de database wél beveiligd kan worden.  


Maar deze keer was het anders. In de late avond van 20 mei stuitte Wolters op een enorme database met in de titel de woorden ‘latest_stolen_passwords’ en ‘warehouse_stolen_cookies_manual’. Met een muisklik bevond hij zich in een database met een enorm aantal emailadressen en wachtwoorden. Wolters hield er rekening mee dat het een oude database was, en een bekend lek. Hij probeerde een aantal e-mailadressen in haveibeenpwnd.com. Tot zijn grote schrik zag hij dat ieder mailadres dat hij probeerde onbekend was in de HIBP-database. Dat deze wachtwoorden gelekt waren, was nog bij niemand bekend.

 
Normaal gesproken meldt Wolters bij de eigenaar van de database dat hij niet goed beveiligd is. Maar wat doe je als de eigenaar een crimineel is? Wolters werd zenuwachtig van de database. De slachtoffers moesten zo snel mogelijk gewaarschuwd worden. Wolters nam diezelfde avond contact op met Rickey Gevers van Scattered Secrets, een website waar je kunt controleren of je wachtwoorden gelekt zijn. Voor Gevers waren de gelekte data ook nieuw.

 
Hij nam de volgende ochtend contact op met Team High Tech Crime van de politie, maar kreeg geen gehoor. Hij probeerde daarna via Twitter. Opnieuw geen reactie. Ook Troy Hunt liet niets van zich horen. Hierop besloot Wolters de database zelf te downloaden. 24 uur duurde het om de bestanden op zijn computer te krijgen. Uit een snelle analyse bleek dat er ruim 178.000 unieke emailadressen in de database stonden. Aan elke emailadres waren meerdere wachtwoorden authenticatie-cookies gekoppeld. Wachtwoorden van e-mailaccounts, sociale media profielen en cryptohandelsplatformen en overheidsportalen.

 
24 mei stuurt hij een bericht naar Leaseweb, de service provider op wiens netwerk de database zich bevond. 26 mei ging de site offline, daarna deelde hij de data met Rickey Gevers van Scattered Secrets. Uiteindelijk lukte het via via om 27 mei contact te krijgen met Team High Tech Crime. 27 mei is een kopie van de database gedeeld met THTC. Een medewerker beloofde er ‘naar te gaan kijken.’

 
Maar nog steeds was er niemand gewaarschuwd. Wolters besloot dit via de DIVD te doen. Op 2 en 3 juni gingen er duizenden mailtjes naar de getroffen mailadressen. Als ik dit schrijf staat de teller op 77.000. De meeste komen uit de Verenigde Staten, Brazilië, India, Duitsland, Engeland en Turkije.


Opmerkelijk is dat onderzoeker Bob Diachenko van het bedrijf Cyber Threat Intelligence een maand eerder op het zelfde ip-adres ook een grote database met gestolen wachtwoorden vond. Wekenlang probeerde Diachenko de site offline te krijgen. 5 mei verdween de website ‘mysteriously’, zoals Catalin Cimpanu schrijft op The Record.

 
https://therecord.media/malware-group-leaks-millions-of-stolen-authentication-cookies/


In dat artikel schrijft Cimpanu verder dat de database sporen bevat van Raccoon, malware die vanaf 2019 opduikt en wachtwoorden, autofill-informatie en cookies uit alle populaire browsers haalt. Authenticatiecookies zorgen voor toegang tot een account zonder gebruikersnamen en wachtwoorden. Deze cookies zijn daarom veel waard in het criminele circuit.


Na in april verdwenen te zijn dook de database dus in mei dus weer op. En de inhoud lijkt anders te zijn. De database bevatte nu niet 9 maar 2 miljoen wachtwoorden. Het leek erop dat er opnieuw gevoelige gegevens naar de database werden gupload naar deze database.
 

Zie ook: [case DIVD-2021-00012](/DIVD-2021-00012/)

 

### English

 
What do you do when you find a database with millions of stolen passwords?

 
It happened to the ethical hacker Tom Wolters. As is often the case, he searched for unsafe databases using the Shodan search engine. He regularly finds such a database. From an online store, or most recently, a publisher of textbooks. The procedure is always the same. He contacts the owner of the database and gives instructions on how the database can be secured.


But this time it was different. In the late evening of May 20, Wolters stumbled upon a huge database titled "latest_stolen_passwords" and "warehouse_stolen_cookies_manual." With a mouse click, he found himself in a database with a huge number of email addresses and passwords. Wolters kept in mind that it was an old database and a known vulnerability. He tried out several email addresses in haveibeenpwnd.com. He was shocked to see that every email address he tried was unknown in the HIBP database. It was not yet known to anyone that these passwords had been leaked.


Normally, Wolters reports to the owner of the database that it is not properly secured. But what do you do if the owner is a criminal? Wolters got nervous about the database. The victims had to be warned as soon as possible. That same evening, Wolters contacted Rickey Gevers of Scattered Secrets, a website where you can check if your passwords have been leaked. The leaked data were also new for Gevers.


He contacted the Police High Tech Crime Team the next morning but received no response. He then tried via Twitter. Again no response. Troy Hunt was also silent. Wolters decided to download the database himself. It took 24 hours to get the files on his computer. A quick analysis revealed that there were more than 178,000 unique email addresses in the database. Multiple password authentication cookies were associated with each email address. Passwords of email accounts, social media profiles, and crypto trading platforms, and government portals.


May 24, he sends a message to Leaseweb, the service provider on whose network the database was located. The site went offline on May 26, after which he shared the data with Rickey Gevers of Scattered Secrets. Finally, on May 27, it was possible to contact Team High Tech Crime. On May 27, a copy of the database was shared with THTC. An employee promised to "go and look at it."

 
But still, no one had been warned. Wolters decided to do this through the DIVD. On June 2 and 3, thousands of emails were sent to the affected email addresses. As I write this, the counter is at 77,000. Most come from the United States, Brazil, India, Germany, England, and Turkey.

 
Remarkably, a month earlier researcher Bob Diachenko of the company Cyber ​​Threat Intelligence also found a large database of stolen passwords at the same IP address. For weeks, Diachenko tried to take the site offline. On May 5, the website "mysteriously" disappeared, as Catalin Cimpanu writes on The Record.

 
https://therecord.media/malware-group-leaks-millions-of-stolen-authentication-cookies/


In that article, Cimpanu further writes that the database contains traces of Raccoon, malware that appears from 2019 and takes passwords, autofill information, and cookies from all popular browsers. Authentication cookies allow access to an account without usernames and passwords. These cookies are therefore of great value in the criminal circuit.


After disappearing in April, the database reappeared in May. And the content seems to be different. The database contained not 9 but 2 million passwords. It appeared that sensitive data was uploaded to this database again. 


For more information: [case DIVD-2021-00011](/DIVD-2021-00012/)

 

 