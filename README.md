Web/www
=======

This repository contain the files for www.divd.nl


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
Layout: news
author: <-- author -->
excerpt: <-- one or two line summary -->
---
Lorum ipsum...
```

## Development
The site is easiest deployed locally with [Docker](https://docker.com). 

1. Install Docker
2. Clone this repository
3. Run the `./serve` script