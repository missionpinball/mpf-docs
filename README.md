
# Mission Pinball website & documentation

This repo contains all the source code for [MissionPinball.org](https://missionpinball.org), which also includes all user documentation.

## Technical details

The MPF website is built using [MkDocs](http://www.mkdocs.org/), a static
site generator using Markdown files as the source. It uses the
[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme.

The site is hosted on GitHub Pages, and the `main` branch of this repo controls
what's published to the live site. A [GitHub workflow](https://github.com/missionpinball/mpf-docs/blob/main/.github/workflows/deploy.yml) is used to automatically
build and deploy the site whenever a commit or merge is made to the `main` branch.
You can see the commits and page builds in the [Actions tab](https://github.com/missionpinball/mpf-docs/actions).

## To build / run locally

1. Clone the repo
2. Open a terminal window and `cd` into the root folder of this repo
3. `pip install -r requirements.txt` (to install mkdocs and what it needs)
4. `mkdocs serve` (runs a local web server on port 8000)

You should be able to access the doc site via your web browser at `localhost:8000`.

## To contribute

We would love contributions to the docs! We have a Contributing Guide ([view on GitHub](https://github.com/missionpinball/mpf-docs/blob/main/docs/about/help_docs.md) | [view on the website](https://missionpinball.org/about/help_docs/))
which explains how to contribute.

## Configuring site navigation

All the navigation for the site is configured in the `mkdocs.yml` file. This
is somewhat annoying since it means that if you add a new page, you have to
go to a completely separate place to set up the nav.

I tried to use the auto pages plugin to automatically
create the navigation, and/or at least keep it local to each subfolder, but
unfortunately our navigation tree is different from our folder hierarchy which
made that not possible. We may be able to combine both methods, and this is
something someone could look into.

## Script to build the showcase pages

The MPF project showcase is published at [missionpinball.org/showcase](https://missionpinball.org/showcase/).
The source content for each showcase entry are YAML files [`/showcase`](https://github.com/missionpinball/mpf-docs/tree/main/showcase) folder of this repo. The script [`generate_showcase_pages.py`](https://github.com/missionpinball/mpf-docs/blob/main/build_tools/generate_showcase_pages.py) generates the .md files for each project, and also generates the showcase index
page.

This script is run automatically as part of the GitHub Actions workflow.
