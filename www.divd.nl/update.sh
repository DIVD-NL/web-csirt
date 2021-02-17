#!/bin/bash

echo "Updating cases"
(
	cd _cases
	rm -f *.md
	cp ../../csirt.divd.nl/cases/*.md .
)
echo "Updating csirt posts"
(
	cd _csirt_posts
	rm -f *.md
	cp ../../csirt.divd.nl/_posts/*.md .
)