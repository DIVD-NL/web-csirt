#!/bin/bash
set -e # Need to fail on error
TEAMCOUNT_HERE=$( ls _team|wc -l )
TEAMCOUNT_THERE=$( ls ../www.divd.nl/_team|wc -l )
if [[ TEAMCOUNT_HERE -le 0 || TEAMCOUNT_HERE -ne TEAMCOUNT_THERE ]]; then
	echo "_team directory is not updated, run ./update.sh"
fi
gem install html-proofer
echo "*** Internal link check ***"
htmlproofer \
	--disable_external \
	--allow-hash-href  \
	--url-ignore="/#english/" _site
echo "*** External link check ***"
htmlproofer \
	--allow-hash-href \
	--url-ignore="/www.linkedin.com/","/twitter.com/","/www.infoo.nl/","/#english/","/x1sec.com/" _site || exit 0