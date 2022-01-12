#!/bin/bash

docker pull mrseccubus/github-pages:latest
docker run --volume="$PWD/..:/root/project:delegated" --entrypoint /bin/bash -ti mrseccubus/github-pages \
-c "
	cd /root/project/www.divd.nl;
	rm -rf _site/*;
	jekyll build  --future 2>&1 |grep -Ev 'rb:[0-9]+: warning';
	./update.sh
	./proof_html.sh
"
