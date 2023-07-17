#!/bin/bash

docker pull mrseccubus/github-pages:latest
docker run --volume="$PWD:/root/project:delegated" --entrypoint /bin/bash -ti mrseccubus/github-pages \
-c "
	cd /root/project/;
	pip install requests
	if [[ -e Gemfile ]]; then
		echo \"*** Installing Gems in Gemfile ***\"
		bundle install 
		EXEC=\"bundle exec\"
	fi
	git config --global --add safe.directory /root/project/www.divd.nl
	./update.sh;
	rm -rf _site/* jekyll-build.log;
	\$EXEC jekyll build  --future 2>&1 |grep -Ev 'rb:[0-9]+: warning' 2>&1 | tee jekyll-build.log
	apt-get update -y
	apt-get install python3-pip libcurl4 -y
	pip3 install html5validator 
	gem install --no-document html-proofer
	./proof_html.sh
"