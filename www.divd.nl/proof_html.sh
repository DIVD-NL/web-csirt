#!/bin/bash
gem install html-proofer
echo "*** Internal link check ***"
htmlproofer \
	--disable_external \
	--allow-hash-href  \
	--url-ignore="/#menu/" _site
echo "*** External link check ***"
htmlproofer \
	--allow-hash-href \
	--url-ignore="/www.linkedin.com/","/twitter.com/","/#menu/" _site || exit 0