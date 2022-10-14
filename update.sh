#!/bin/bash

if [[ ! -e serve ]]; then
	echo "It looks like you are not in the root directory because I don;t see the serve script"
	echo "I'm cowardly quitting"
	exit 1
fi
if [[ ! -d www.divd.nl ]]; then
	git clone https://github.com/DIVD-NL/web-www.git www.divd.nl
else
	( cd www.divd.nl ; git pull )
fi


echo "Updating team"
(
	cd _team
	rm -f *.html
	cp ../www.divd.nl/_team/*.html .
)

echo "Updating reports"
(
	cd _reports
	rm -f *.md
	cp ../www.divd.nl/_reports/*.md .
)
