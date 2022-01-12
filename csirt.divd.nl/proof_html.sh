#!/bin/bash
set -e # Need to fail on error
TIDY_OUT=/tmp/tidy_out.$$
apk update update 
apk add py3-pip 
pip3 install html5validator 
gem install html-proofer
export PATH=$PATH:/usr/gem/bin

echo "*** Internal link check ***"
htmlproofer \
	--check-html \
	--disable_external \
	--allow-hash-href  \
	--url-ignore="/#english/","/#menu" .
echo "*** External link check ***"
(set +e ; htmlproofer \
	--allow-hash-href \
	--url-ignore="/#english/","/#menu" . || exit 0)
(
	html5validator *.html */*.html */*/*.html */*/*/*.html */*/*/*.html 
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
