#!/bin/bash

docker pull mrseccubus/github-pages:latest
while [ 1 ] ; do
	docker run --volume="$PWD:/root/project:delegated" --entrypoint /bin/bash -ti mrseccubus/github-pages \
	-c "
		cd /root/project;
		rm -rf _site/*;
		jekyll build  --future 2>&1 |grep -Ev 'rb:[0-9]+: warning';
		./proof_html.sh
	"
	set -e
	echo 'Press CTRL+C now to quit'
	sleep 1
	set +e
	echo 'Restarting...'
done

