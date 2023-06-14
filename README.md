
# Mission Pinball website source code

This repo contains all the source code for MissionPinball.org.


## Technical details

This site is built using [MkDocs](http://www.mkdocs.org/), which is a static
site generator that uses Markdown files as the source. It uses the
[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme.

The site is hosted on GitHub Pages, and the `main` branch of this repo is
what's published to the live site. GitHub Actions are used to automatically
build and publish the site whenever a commit or merge is made to the `main` branch
(assuming no bad links were added).

## To build / run locally

1. Clone the repo
2. Open a terminal window and `cd` into the root folder of this repo
3. `pip install -r requirements.txt` (to install mkdocs and what it needs)
4. `mkdocs serve` (runs a local webserver on port 8000)

You should be able to access the doc site via your web browser at `localhost:8000`.

## To contribute

Yes!!

## Configuring site navigation

It's all in `mkdocs.yml`. I tried to use the auto pages plugin to automatically
create the navigation, and/or at least keep it local to each subfolder, but
unfortunately our navigation tree is different from our folder hierarchy which
makes that impossible. So we have to manually configure the navigation in the
`mkdocs.yml` file.