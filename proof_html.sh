#!/bin/bash
set -e # Need to fail on error
#
# Prerequisites
# apt-get update -y
# apt-get install python3-pip libcurl4 -y
# pip3 install html5validator 
# gem install --no-document html-proofer

TIDY_OUT=/tmp/tidy_out.$$

TEAMCOUNT_HERE=$( ls _team|wc -l )
TEAMCOUNT_THERE=$( ls www.divd.nl/_team|wc -l )
if [[ $TEAMCOUNT_HERE -le 0 || $TEAMCOUNT_HERE -ne $TEAMCOUNT_THERE ]]; then
	echo "_team directory is not updated, run ./update.sh"
	exit 1
fi
echo "*** Internal link check ***"
export LANG=en_US.UTF-8
htmlproofer \
	--disable_external \
	--allow-hash-href  \
	--ignore-urls="/#english/,/www.bacnet.org/,/fish2.com/" \
	_site
(
	html5validator _site/*.html _site/*/*.html _site/*/*/*.html _site/*/*/*/*.html _site/*/*/*/*.html 
) | tee $TIDY_OUT
ERRORS=$( grep 'error:' $TIDY_OUT | wc -l )
if [[ $ERRORS -gt 0 ]] ; then
	echo "------------------------------------------------------------------------------------"
	echo "There are $ERRORS errors in html files, not good enough!"
	grep 'Error:' $TIDY_OUT
	exit 1
else
	echo "------------------------------------------------------------------------------------"
	echo " HTML checked and found flawles, \0/ \0/ \0/ \0/ \0/ \0/ "
	echo "------------------------------------------------------------------------------------"
fi
if [[ -e jekyll-build.log ]]; then
	ERRORS=$( grep -i ERROR jekyll-build.log | grep -v DIVD-3000-0000 | wc -l )
	WARNS=$( grep WARN jekyll-build.log | wc -l )
	if [[ $WARNS -gt 0 ]] ; then
		echo "There are $WARNS warnings in the Jekyll build log"
		grep -i 'WARN' jekyll-build.log
	fi
	if [[ $ERRORS -gt 0 ]] ; then
		echo "------------------------------------------------------------------------------------"
		echo "There are $ERRORS errors in the Jekyll build log, not good enough!"
		grep -i 'ERROR' jekyll-build.log
		exit 1
	fi
fi
