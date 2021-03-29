#!/bin/bash
set -e
apt-get update && apt-get install npm -y
npm install html-minifier uglify-js uglifycss -g
find _site -regex ".*\.\(html\|xml\)" -type f \
 	-printf "echo \"%p\";cat \"%p\" | html-minifier -c html-minifier.conf > /tmp/minifier ; mv /tmp/minifier \"%p\"\n" |
 	sort |
 	sh -e
 for file in $( find _site -name "*.js" | grep -v min.js | sort ); do
 	echo $file
 	uglifyjs $file > /tmp/minifier
 	mv /tmp/minifier $file
 done
 for file in $( find _site -name "*.css" | grep -v min.css | sort ); do
 	echo $file
 	uglifycss $file > /tmp/minifier
 	mv /tmp/minifier $file
 done
