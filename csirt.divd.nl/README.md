## Adding new news items
1. Create a new file in the `_posts` folder with filename `<year>-<month>-<day>-<title>.md`
2. Start the file with the following template configuration:
```markdown
---
layout: news
title: <-- title-- >
author: <-- your name -->
excerpt: <-- one line summary in Dutch / And English will show on blog page -->
---
```

## Development
The site is easiest deployed locally with [Docker](https://docker.com). 

1. Install Docker
2. Clone this repository
3. Run `./serve`
4. Open your favorite Internet Explorer and go to `http://localhost:4000`

## Markdown

See: https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
