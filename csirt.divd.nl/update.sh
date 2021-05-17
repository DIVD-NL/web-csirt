#!/bin/bash

echo "Updating team"
(
	cd _team
	rm -f *.html
	cp ../../www.divd.nl/_team/*.html .
)