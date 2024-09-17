#!/bin/bash
echo -n "Update cve records..."
CVEPATH=$(which cve)
if [[ "$CVEPATH" != "" ]]; then
	(
		echo
		cd _data/cves
		for RECORD in $(curl -s https://divd-nl.github.io/cna-admin/published.json|jq --compact-output '.[]'); do
			DIR=$(echo $RECORD|jq --raw-output .year)
			CVE=$(echo $RECORD |jq --raw-output .cve)
			echo $DIR/$CVE
			(cd $DIR;curl -s https://divd-nl.github.io/cna-admin/records/$CVE.json > $CVE.json)
		done
	)
	echo "done"
else
	echo "skipped, bercause cvelib is in in path" 
fi