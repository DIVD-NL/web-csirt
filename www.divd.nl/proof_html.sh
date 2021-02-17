#!/bin/bash
CASECOUNT_HERE=$( ls _cases|wc -l )
CASECOUNT_THERE=$( ls ../csirt.divd.nl/cases|wc -l )
if [[ CASECOUNT_HERE -le 0 || CASECOUNT_HERE -ne CASECOUNT_THERE ]]; then
	echo "_cases directory is not updated, run ./update.sh"
fi
POSTCOUNT_HERE=$( ls _csirt_posts|wc -l )
POSTCOUNT_THERE=$( ls ../csirt.divd.nl/_posts|wc -l )
if [[ POSTCOUNT_HERE -le 0 || POSTCOUNT_HERE -ne POSTCOUNT_THERE ]]; then
	echo "_csirt_posts directory is not updated, run ./update.sh"
fi
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