---
title: Report DIVD-2021-00002 - KASEYA VSA, behind the scenes
date: April 4, 2022
author: Gerard Janssen
excerpt:
---
<header>
    <h2>{{ page.title }}</h2>
    <span>{{ page.date }}</span>
</header>
Case Lead: Frank Breedijk

Researchers: Wietse Boonstra, Victor Gevers, Joost Hendricksen, and Lennaert Oudshoorn

In April 2021 Dutch hackers found a number of vulnerabilities in software used by Kaseya, a business that makes tools for system managers working remotely. An enormous number of companies could be attacked through this vulnerability, from banks to transport companies and shop chains. The problem was nearly solved when Russian hackers also received wind of it. The result was a race between Dutch hackers and Russian criminals.

This is a translation of a chapter from [the book Hackers](https://www.thomasrap.nl/boek/hackers/) by [Gerard Janssen](/team/Gerard%20Janssen). This chapter starts after the story of Dutch hacker [Victor Gevers](/team/Victor%20Gevers) discovered that two-factor authentication of Donald Trump's Twitter account was disabled and guessed his Twitter password, in November 2020.

You can read about that in the Dutch magazine [Vrij](https://www.vn.nl/hackers-twitter-trump-english/) [Nederland](https://www.vn.nl/trump-twitter-hacked-again/).


Kaseya
---

This is not the first time that journalists have discounted Gevers; he repeatedly had to deal with the PR techniques employed by 'Big Tech' and large governments. Gevers seems to like the fact that I now have now seen it all from the inside: the inaccessibility and arrogance of big companies, the inflated egos of journalists, and the strange anonymous accounts on Twitter that spread all kinds of nonsense.

He decides to introduce me to the DIVD (Dutch Institute for Vulnerability Disclosure), a group of volunteers who watch over the Dutch part of the internet. Gevers leads the DIVD with Frank Breedijk, Chris van 't Hof and Astrid Oosenbrug. Breedijk is the Chief Information Security Officer (CISO) of Schuberg Philis, an IT company that focuses on essential systems for banks and other critical infrastructure, Van 't Hof is a sociologist who has written several books about the hacker community, and at almost every fair or conference on the subject of hackers, he is the discussion leader or moderator. Oosenbrug is a former member of parliament for the Dutch Labour Party. Moreover, she has been a hacker herself.

The volunteers of the DIVD communicate through Slack, a chat program that allows users to work remotely as a team. I notice that every few days, attention is drawn to a security leak. Some of these leaks are given names, such as Proxy-logon, Printer Nightmare, or OmiGod. Patch Tuesday, the second Tuesday of the month, is notorious, because it is the day when Microsoft sends out the monthly security updates to its users. These updates can be seen as indications of where the leaks are in Microsoft applications.

When a new leak appears, volunteers from the DIVD investigate how dangerous it is. They use the search engines Shodan and Censys to see which companies are vulnerable. Sometimes they scan the internet themselves, looking for computers on which vulnerable programs are running. They use reconnaissance techniques similar to the ones used by state hackers or criminals, but instead of infecting computers with viruses, they send an e-mail to the administrator, stating that a 'backdoor' is open and containing short instructions on the best way to close it.

Every week there is an online DIVD-meeting during which the state of affairs is discussed. Chris van 't Hof usually leads the meeting, with a bookcase in the background. Victor Gevers sits in front of a green screen on which he usually projects a black background. The meeting is filled with hackers and computer professionals, wearing headphones, listening, and tapping their keyboards at the same time. The meeting starts formally. The various agenda items are discussed one by one. Then there is an informal part where people chat a little. A core group of three or four hackers enjoy working together and stay behind at the end to look for new vulnerabilities.

One of them is Wietse Boonstra. A man with an East-Dutch accent, surrounded by computers and a large quantity of Star Wars Lego. He turns out to have a remarkable talent for finding leaks. Boonstra in particular has a sixth sense for finding bugs in web applications. He inherited the hacker's mindset from his father, an electronics wizard. As a child, when Wietse whined that he wanted a toy, his father would take apart a few old devices and use the parts to build the toy from scratch.

‘My father understood everything about capacitors and resistors,' says Boonstra. 'From him, I learned early on that you can make anything yourself.'
Learning from books was not easy for Wietse. He went to a vocational technical school and became an electrician. He knew his way around computers. This is how he ended up as an IT employee for an internet provider. In the logs of the internet provider, Boonstra saw that hackers had gained access to the internal systems. He was interested and wanted to learn how they had managed to do so.

And he learned very quickly. A few years later he ended up at a company in the vital infrastructure, there he showed his employer that he could take over the place within ten minutes, just using a laptop and an internet connection. Boonstra was immediately promoted to member of the team responsible for security. There he learned about the sums of money that were paid to external research companies. He realized that he could earn much more as a self-employed security researcher than as a permanent employee. Since then Boonstra became a pentester. Commissioned by companies he searches for weak links in their digital infrastructure. He also earns a nice living by hunting down bug bounties, premiums that companies pay to hackers who report leaks.

At a large company where Wietse is carrying out a penetration test in early 2021, he comes across software that he doesn’t recognize, but which gives him highly provileged access to the computer systems. The software is called Kaseya Virtual Systems Administrator (VSA). Boonstra feels that something is not right with this software, but - within the assignment - there is no time to find out properly. He is unable to put it out of his head. At home on the couch, ‘while watching Netflix’, he searches for Kaseya on Google.
The Kaseya VSA software is intended for a Managed Service Providers (MSPs), companies that remotely manage a business’s computer network. Every company needs someone who can solve computer problems. You can hire a system administrator, but sometimes it is cheaper and more convenient to outsource this work to a Managed Service Provider that uses specialized software with which users can be added to a corporate environment, backups can be made and software can be installed or updated. Kaseya VSA is an example of this type of software.

It is convenient but not without risk because someone who can log on as a system administrator using Kaseya VSA is immediately in God mode and can do whatever he wants.

Boonstra sends an e-mail to Kaseya. He poses as an employee of an MSP and asks for a trial version of Kaseya, which he receives immediately. He quickly recognizes errors that point to vulnerabilities. And indeed, after some searching, he finds a logical flaw. He immediately understands that this could theoretically have major consequences. It seems that he has caught a zeroday, one of the highest order, in an American company worth billions of dollars. Reporting this kind of leak could get him into trouble.

Boonstra therefore decides to make the report on behalf of the DIVD. The core of the DIVD consists of hackers who know where the line is, how to warn system administrators, how to respond to angry reactions, who know what the severity of a vulnerability is and who know who to contact when ’something involving shit and fan’ happens.

March 23
--------

On March 23, 2021, Wietse Boonstra creates a closed channel on the Slack account of the DIVD. He adds Victor Gevers, Frank Breedijk, Lennaert Oudshoorn and Joost Hendricksen. ‘I’ve found a zeroday,’ Boonstra writes. 'What does the software do? It manages systems at the end-users via an agent.'

Frank Breedijk is the first to respond. 'Pretty annoying, holes in these kinds of products that are high privilege by design,' he says.

The next day, Boonstra already withdrew his claim. Maybe I cried wolf to soon. I did a fresh install and now it doesn't work anymore.

Then he typed in seven emoticons side by side. Emoticons of a head, with curse symbols. ‘So much time sank into an exploit route only to find that I simply didn't get a request validation cookie right.’

‘On their website, it just says that they are secure,’ Joost Hendricksen jokes.

‘But the exploit is working right now!’

Boonstra finds two vulnerabilities. ‘A difficult one and an easy one,’ he writes, ‘with the difficult one containing an SQL injection.’ Breedijk and Boonstra take another closer look at the vulnerabilities and see that they can be combined and then used to take over the entire system, to break into Kaseya's software.

'Why do you attach something like that to the interwebz,' sighs Breedijk, 'it shouldn't surprise me anymore, but it does.'

Boonstra reports the findings to a client where he knows Kaseya is used: a large company that criticizes human rights violations in China and is, therefore, a target for Chinese hackers. The IT boss of that company starts stammering when Boonstra tells him what is going on. Another of Boonstra's clients also panics when Boonstra informs him.

‘How are we going to approach this?’ is the question in the DIVD-Slack group. Where should they start?

'First, let's see how many people could be affected.'

Kaseya uses an unusual port to connect to the Internet. By searching the internet for all computers with that port, Boonstra finds the Kaseya users. Such a global scan takes about a day. A list of more than 2000 ip-addresses is produced.

‘Talk about a supply chain attack,' says Boonstra. And he puts a link in the Slack group of a vulnerable company that 'supplies critical components in the defense, aerospace, commercial military, medical, automotive, oil and gas, industrial, transport and energy markets.'

If you shut down this kind of company, the production of many others grinds to a halt.

‘What should they do? Patch it?’, asks Gevers.

‘Can anything be done? Is it possible for Kaseya to quickly improve the software and send an update to all users?'

‘I have no idea how,' says Boonstra.

It is not a programming error that can be easily fixed. Boonstra and Breedijk come together in an online meeting. They go over the facts. Some of the addresses belong to Managed Service Providers that use Kaseya. Each of these MSPs has multiple clients, each of which can have thousands of computers under management. Transport companies and banks are also on the list. Boonstra and Breedijk feel a combination of old hacker excitement and fear, a mixture of "Hack The Planet!" and anxiety. They have in their hands a fireman's key that gives them access to millions of computers of very interesting companies at once. On the one hand, there is the urge to look into a few places. On the other hand, there is the fear of what they might see and what could happen if someone with malicious intentions got hold of this same key. They look again at the list of companies and begin to realize that they could disrupt the whole of the Netherlands. And not just the Netherlands.

‘Let's stop this,' says Breedijk at one point, 'it's giving me a stomach ache.’

They must take action. The bomb must be defused. But how? Boonstra and Breedijk seek contact with Kaseya. They expected - as usual - to be brushed aside. But contrary to usual, their message was taken seriously and they were immediately contacted by Kaseya's Chief Technology Officer, the highest-ranking technician. Fortunately, he immediately recognizes the seriousness of the problem. He wants to know all the details and understands that the problem must be resolved as soon as possible. From that moment on, Boonstra works closely with the CTO. He tests the solutions the Kaseya technicians come up with.

Soon there is the first update, and Kaseya informs all users that they need to update immediately. Risky, because this message might attract the attention of attackers. And that's not good, because the most serious leak has not yet been closed. Precisely that leak is the most difficult one to solve. To make matters worse, Boonstra discovered new vulnerabilities during the testing of the update. It is like water running into a leaky boat, and every time a hole is plugged, a new leak appears.

The good news is that the cooperation with Kaseya is going well and solutions are being worked on, with the aim of creating a patch – a band-aid on the leak – that solves all the problems, after which a coordinated vulnerability disclosure can be made. Then the whole story can be told, so other researchers and other companies can also learn from it.

The 6th of July is the agreed upon deadline. This has to become a story of success: how the Dutch volunteers of the DIVD working together with the technicians of the American company Kaseya have made the Internet a lot safer again. That is why I am allowed to read along in the private group. The plan is to write a nice background story about it for Vrij Nederland.

I already have some idea of what the story will look like: once upon a time, there was a hacker who found a zeroday. Through good cooperation with Kaseya, the problem was solved. The time bomb ticked but was defused just in time. The big bad ransomwarewolf could blow all he wanted. A small disaster had been averted. And everyone lived happily ever after.

But then on the evening of Friday July 2nd, Boonstra receives a message from Kaseya via LinkedIn, an invitation to a meeting. When he opens his laptop, he sees a news message: 'Kaseya Ransomware Attack'.

Uh oh, he thinks.

When he clicks on the meeting link, he drops into an online meeting. He recognizes the CTO of Kaseya and a few other technical specialists. They look strange. He sees fear in their eyes. Russian criminals have also found Boonstra's leak. They are encrypting customer files. It looks like a disaster is unfolding.

All over the world, screens go black. Frank Breedijk is still standing by the campfire of his sea scout group. As he walks away from the fire, he sees that the screen of his phone is filled with messages about the ransomware attack.

There goes my weekend, he thinks.

It’s no coincidence that this is the weekend of 'the 4th of July’. There is no time to reflect now. The DIVD already has a list of 2250 IP addresses, with Kaseya users who are vulnerable to an attack. That night Gevers, Breedijk and the volunteers Lennaert Oudshoorn and Joost Hendricksen warn potential victims. Anyone using Kaseya should turn it off as soon as possible.
The researchers continue to scan at the same time and see that people are listening. The number of vulnerable systems drops to around 140.

That night, Breedijk also forwards the list to the National Cyber Security Centre (NCSC), the Dutch’s government's Incident Response Team for government agencies and critical infrastructure. The DIVD wants to share the list of vulnerable systems with them, so they can send information to foreign partners. The initial response was enthusiastic, but when he called again to ask how he could best share the list, no response came.

‘And then it becomes one o'clock, and then it becomes two o'clock, and then it becomes half-past two,' grumbles Breedijk.
‘Not on call, but on one ear,’ someone jokes.

On Sunday, the 4th of July, there is an all-day online meeting. Tired faces that appear and disappear. Grumbling family members in the background.

‘Are you really still behind that screen,’ I hear a voice say.

‘It's a rotten feeling,' says Gevers, ‘I know we did well, but it's never good enough.’

By now the criminals are demanding seventy million dollars in ransom.

On Monday July 5th, media interviews follow. It begins early in the morning with an interview on the Radio 538 morning show, the most popular morning radio show in the country. The NOS Journaal, RTL Nieuws (the two primary TV new showsd), and Nieuwsuur (a popular current affaris show) follow with items about how a small group of Dutch volunteers who almost managed to prevent the biggest ransomware attack of all time. Camera crews arrive at Breedijk and Boonstra's home. Gevers is sitting in the television studio in the Media Park, with big The Matrix-numbers dripping down and - yes - a black T-shirt. In the background, behind Gevers, to top it all off: a screen with a huge golden bitcoin logo.
If we had had a little more time, we would have succeeded," says Gevers.

Meanwhile, paranoia is growing in the Slack group. How did the attackers get the zeroday? Is it an inside job? Who all had access to the zeroday, to the proof of concept exploits that Wietse had developed?

'Thirty percent of seventy million dollars is a lot of money,' says someone.

‘You might rat on someone for that.’

A tweet from a security researcher appears on Twitter, in which he suggests the same thing that Boonstra has just shared in great confidentiality in the closed Kaseya group.

‘That is quite a coincidence,’ writes Boonstra.

Is someone passing on information? After that, I and a few others are removed from the Kaseya Slack channel.

DIVD's CISO (Chief Information Security Officer) Fleur van Leusden is investigating whether she can find evidence that the zeroday was leaked. She discovered strange things in the logs of GitHub, a platform where the zeroday was shared internally. But she found no evidence of a leak.

Just like after the Trump story, there are 'signals' again. Through the grapevine. ‘We are dealing with serious Russian crime here,’ a warning reads. The message is that the DIVD should be careful with the stories they tell the media. It is not wise to boast that the DIVD has been a thorn in the side of the REvil criminal group. It is smarter to tell the story that the DIVD was outwitted by brilliant Russian criminals.

The next day, Boonstra reports that his servers are under attack from Russia. Then a photo appears of a kicked-in screen door. The door to Boonstra's house has been forced! In a panic, Boonstra ran inside. He called out his son's name. No response. He called out again. Again no response.

The computers are still there - no Russians, he thought.

‘Where are you?’ he called again.

From the upper floor, he now heard a soft voice. ‘Here.’

His little son sat guiltily in a corner. He turned out to be the burglar too. He had accidentally walked through the screen door.

It is difficult for me to assess how serious the Russian threat is. Would I also be a target? I can imagine that for the Russians I am 'low hanging fruit', a weak link through which they can penetrate to the core of the DIVD. Should I be worried? I read an interview with one of the REvil members on an Russian site. They do not strike me as really dangerous. I get the impression that they are amoral technicians, like some - I imagine - at Facebook.

Boonstra has since been officially hired by Kaseya. Gevers talks to a whole lot of people including the FBI and I don’t know who else. He hardly tells me everything anymore. Someone notes that Gevers is mentioned in a video by DEFCON. Jen Easterly, the new director of the US Cybersecurity & Infrastructure Security Agency, mentions Gevers and thanks him for giving such clear insight into the threat, in explaining the chain of vulnerabilities in Kaseya.

The ransomware attack was the largest of all time, yet the consequences could have been much worse. Only a relatively small proportion of all vulnerable systems were attacked. The reality was less serious than the disaster scenario that Boonstra and Breedijk feared. Did the criminals not see what they had in their hands? Did they not dare to go any further? Did someone press a 'stop' button? Or was there something else going on?

One of the theories that I hear is that it is a cover-up. The thought runs as follows. Suppose the Russian (or some other) intelligence service had been spying on companies in the Kaseya VSA systems for years. Then they might have seen in the mail that the vulnerability had been discovered. Did they use the ransomware attack as a distraction while they covered their tracks under the banner of a ransomware attack? And what happened to the Russian ransomware group REvil? They suddenly disappeared on July 6th. On July 10th, Putin and Biden hold a one-hour telephone conversation.

And then, all of a sudden, Kaseya has the decryption key to help all the victims. Even the CTO of Kaseya has no idea where that key came from. And the top boss won't say anything. It has to remain a secret. It is clear that the ransomware attackers have gone too far and that invisible forces have begun to play in the background. It seems that the American (and other) intelligence services are using the big guns.

It later emerged that the FBI already had had the key to help all the victims at once for while, but had kept it secret to prevent the REvil gang from noticing that the FBI was looking into their servers. The choice was between helping the victims and tracking down the perpetrators. The FBI chose the latter.

On November 3rd, an article appeared in The Washington Post in which 'anonymous sources' did indeed report that U.S. Cyber Command, a branch of the American military, was involved.

Game changer
------------
The REvil attack is a game-changer in many areas. Earlier, there were attacks on the Colonial Pipeline and the meat processing company JBS. This was the starting point for the American judiciary to give the fight against ransomware gangs the same priority as the fight against terrorism. Ransomware attacks have already been a major problem for five years, but until now criminals were still using old leaks. This time, the attackers made use of a vulnerability that was not yet known. A zeroday. What does it mean that ransomware attackers are going to use zerodays? Are they going to also hold factories and power stations hostage? And the enormous sums of money they are currently raising will enable the criminals in turn to develop new zerodays themselves or to buy them on the black market, through which they could obtain enormous power and become nearly unstoppable.

Not only the fact that REvil used a zeroday for a ransomware attack is new.

There us also the fact that this type of software is now the target, software that allows you to hijack the most important systems in a company instantly. The Kaseya story has revealed a new variant of a major problem. Too many companies depend on too few software applications. In this case, the software that provides online access to a company network. Finding faults in this kind of software is much easier than most people realize. New features are given a higher priority than security. Marketability is considered more important than reliability. This is logical. Nobody is happy with an expensive update that is less useful but more secure.

It is a recurring source of frustration for software developers. The financial news medium Bloomberg published a story with anonymous accounts of programmers who have left Kaseya.

‘It was so outdated and full of problems that it should be completely replaced,’ says one of the developers.

A former employee tells Bloomberg that he wrote a 40-page memo about his concerns regarding the security of the software. He was fired two weeks later. Some employees left in anger, others were fired when Kaseya moved the programming work to Minsk, in Belarus, where Kaseya hired more than forty programmers. This is remarkable because Belarus has close relations with the Russian government, which some say protects these ransomware groups and even cooperates with them.

What is true of Kaseya is also true of much other software.

‘It's like with beer,' explains Breedijk. 'Do you think all those different beers you see in the supermarket come from different brewers? It's often the same beer, with a different label.'

The content of many software packages is also often the same. If there is an error in one package, the same error often occurs in another package. Standard building blocks of computer programs are often used, as a kind of large Lego blocks. If one of these bricks has a hole in it, all the programs containing that component are also leaking.

Because of this, many companies and individuals are therefore more vulnerable than they think, in Kaseya's case precisely because of the software intended to increase the level of security. The software that provides access, or that automatically makes backups, turns out to be full of holes. Not only Kaseya's products but also those of its competitors, such as Solarwinds, which is used by parties like Microsoft and was already hacked in the early 2020s - probably - by hacker teams working for the Russian government.

Boonstra is now also investigating Kaseya's competitors. All of them are broken.
Zoom-meetings he sometimes interrupts with a satanic laugh, or he starts a Britney Spears song: 'Oops!.... I did it again.
