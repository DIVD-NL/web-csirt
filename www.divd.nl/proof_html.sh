#!/bin/bash
set -e
#set -x
TIDY_OUT=/tmp/tidy_out.$$
CASECOUNT_HERE=$( ls _cases|wc -l )
CASECOUNT_THERE=$( ls ../csirt.divd.nl/cases|wc -l )
if [[ $CASECOUNT_HERE -le 0 || $CASECOUNT_HERE -ne $CASECOUNT_THERE ]]; then
	echo "_cases directory is not updated, run ./update.sh"
	exit 1
fi
POSTCOUNT_HERE=$( ls _csirt_posts|wc -l )
POSTCOUNT_THERE=$( ls ../csirt.divd.nl/_posts|wc -l )
if [[ $POSTCOUNT_HERE -le 0 || $POSTCOUNT_HERE -ne $POSTCOUNT_THERE ]]; then
	echo "_csirt_posts directory is not updated, run ./update.sh"
	exit 1
fi
CVECOUNT_HERE=$( ls _cves|wc -l )
CVECOUNT_THERE=$( ls ../csirt.divd.nl/_cves|wc -l )
if [[ $CVECOUNT_HERE -le 0 || $CVECOUNT_HERE -ne $CVECOUNT_THERE ]]; then
	echo "_cves directory is not updated, run ./update.sh"
	exit 1
fi
gem install html-proofer
echo "*** Internal link check ***"
htmlproofer \
	--disable_external \
	--allow-hash-href  \
	--url-ignore="/#menu/" _site
echo "*** External link check ***"
(set +e ; htmlproofer \
	--allow-hash-href \
	--url-ignore="/www.linkedin.com/","/twitter.com/","/#menu/" _site || exit 0 )
apt update -y
apt install tidy -y 
(
	find _site -name "*.html" -exec echo {} \; -exec tidy -e -q {} \; 2>&1 |
	  grep -v 'Warning: trimming empty' |
	  grep -v 'Warning: inserting implicit <body>'
) | tee $TIDY_OUT
WARNS=$( grep 'Warning:' $TIDY_OUT | wc -l )
if [[ $WARNS -gt 0 ]] ; then
	echo "------------------------------------------------------------------------------------"
	echo "There are $WARNS warnings in html files" #, not good enough!"
fi
ERRORS=$( grep 'Error:' $TIDY_OUT | wc -l )
if [[ $ERRORS -gt 0 ]] ; then
	echo "------------------------------------------------------------------------------------"
	echo "There are $ERRORS errors in html files, not good enough!"
	grep 'Error:' $TIDY_OUT
	exit 1
fi
#if [[ $WARNS -gt 0 ]] ; then
#	exit 1
#fi
