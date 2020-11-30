## Adding new news items
1. Create a new file in the `_posts` folder with filename `<year>-<month>-<day>-<title>.md`
2. Start the file with the following template configuration:
```markdown
---
layout: news
title: <-- title-- >
author: <-- your name -->
excerpt: <-- one or two line summary -->
---
```

## Adding new reports
1. Create a new file in the `reports` folder with filename `<year>-<month>-<day>-<title>.md`
2. Start the file with the following template configuration:
```markdown
---
title: <-- title -->
date: <-- date (e.g. 1 January, 2020) -->
author: <-- author -->
excerpt: <-- one or two line summary -->
---
<header>
    <h2><-- title --></h2>
    <span><-- date (e.g. 1 January, 2020) -->, by <-- author --></span>
</header>
```

## Development
The site is easiest deployed locally with [Docker](https://docker.com). 

1. Install Docker
2. Clone this repository
3. Open the .env file in a text-editor
4. Add your [Github personal access token](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line) to the `JEKYLL_GITHUB_TOKEN=` setting.
5. Run the docker-compose file to start the Docker stack
6. Open your favorite Internet Explorer and go to `http://localhost:4000`
