#!/bin/bash
set -e # Need to fail on error
TIDY_OUT=/tmp/tidy_out.$$
apt update -y
apt install python3-pip default-jdk -y
pip3 install html5validator 

TEAMCOUNT_HERE=$( ls _team|wc -l )
TEAMCOUNT_THERE=$( ls ../www.divd.nl/_team|wc -l )
if [[ $TEAMCOUNT_HERE -le 0 || $TEAMCOUNT_HERE -ne $TEAMCOUNT_THERE ]]; then
	echo "_team directory is not updated, run ./update.sh"
	exit 1
fi
gem install html-proofer
echo "*** Internal link check ***"
htmlproofer \
	--check-html \
	--disable_external \
	--allow-hash-href  \
	--url-ignore="/#english/" _site
echo "*** External link check ***"
(set +e ; htmlproofer \
	--allow-hash-href \
	--url-ignore="/www.linkedin.com/","/twitter.com/","/www.infoo.nl/","/#english/","/x1sec.com/" _site || exit 0)
(
	html5validator _site/*.html _site/*/*.html _site/*/*/*.html _site/*/*/*/*.html _site/*/*/*/*.html 
) | tee $TIDY_OUT
WARNS=$( grep 'warn:' $TIDY_OUT | wc -l )
if [[ $WARNS -gt 0 ]] ; then
	echo "------------------------------------------------------------------------------------"
	echo "There are $WARNS warnings in html files" #, not good enough!"
fi
ERRORS=$( grep 'error:' $TIDY_OUT | wc -l )
if [[ $ERRORS -gt 0 ]] ; then
	echo "------------------------------------------------------------------------------------"
	echo "There are $ERRORS errors in html files, not good enough!"
	grep 'Error:' $TIDY_OUT
	exit 1
fi
#if [[ $WARNS -gt 0 ]] ; then
#	exit 1
#fi
