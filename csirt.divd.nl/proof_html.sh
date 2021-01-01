#!/bin/bash
gem install html-proofer
htmlproofer \
	--allow-hash-href  \
	--url-ignore="/www.linkedin.com/","/twitter.com/","/www.infoo.nl/","/#english/","/x1sec.com/" _site