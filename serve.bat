@echo off
echo.
echo Use http://localhost:4000 to access the site
echo.
:loop
rd /s /q _site
mkdir _site
docker run --volume="%CD%:/root/project:delegated" --entrypoint /bin/bash --publish 4000:4000 -ti mrseccubus/github-pages -c "cd /root/project;rm -rf _site/*;jekyll serve --incremental --host=0.0.0.0 --future 2>&1 |grep -Ev 'rb:[0-9]+: warning'"
echo Press CTRL+C twice to exit this script
goto loop