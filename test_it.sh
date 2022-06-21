#!/bin/bash

docker pull mrseccubus/github-pages:latest
docker run --volume="$PWD:/root/project:delegated" --entrypoint /bin/bash -ti mrseccubus/github-pages \
-c "
	set -e
	cd /root/project/;
	bundle install
	git config --global --add safe.directory /root/project/csirt.divd.nl
	./update.sh;
	rm -rf _site/*;
	bundle exec jekyll build  --future 2>&1 |grep -Ev 'rb:[0-9]+: warning';
	./proof_html.sh
"
