#!/bin/bash

echo "Updating cases"
(
	cd _cases
	rm -f *.md
	cp ../../csirt.divd.nl/_cases/*.md .
)
echo "Updating csirt posts"
(
	cd _csirt_posts
	rm -f *.md
	cp ../../csirt.divd.nl/_posts/*.md .
)
echo "Updating cves"
(
	cd _cves
	rm -f *.md
	cp ../../csirt.divd.nl/_cves/*.md .
)
echo "Updating data"
(
	cd _data
	rm -f scanners.yml
	cp ../../csirt.divd.nl/_data/scanners.yml .
)
