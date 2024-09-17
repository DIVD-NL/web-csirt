#!/bin/bash
set -e
if [[ ! -e serve ]]; then
	echo "It looks like you are not in the root directory because I don't see the serve script"
	echo "I'm cowardly quitting"
	exit 1
fi

echo "Updating team"
(
	cd _teams
	rm -f *.md
	cd ../_team
	rm -f *.md
)
./org_update.py --team-path _teams  --member-path _team
