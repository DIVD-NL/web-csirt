#!/bin/bash

./update.sh
docker pull mrseccubus/github-pages:latest
docker run --volume="$PWD:/srv/jekyll:delegated" --entrypoint /bin/bash -ti mrseccubus/github-pages \
-c "
	echo \"Running bundle install (be patient)\"
	bundle install
	rm -rf _site/*;
	bundle exec jekyll build  --future 2>&1;
	cd _site
	../proof_html.sh
"
