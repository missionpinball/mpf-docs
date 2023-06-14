---
title: Contributing to MPF's Documentation
---

# Contributing to MPF's Documentation

!!! note "The MPF Docs website was majorly updated in June 2023"

    All of the various MPF websites have been consolidated into
    this one, and a major technology refresh was done on the backend.
    If you've contributed to the docs in the past, everything is
    different (and _much_ easier) now. Details of the upgrade are
    in [this GitHub discussion](https://github.com/orgs/missionpinball/discussions/100)


Want to help make these docs better! Great! We'd love any help, whether
it's as small as correcting a typo, adding to a section that isn't
clear, adding your own How To guide, or whatever else you want to
change.

## How this website works

There's a GitHub repository called [mpf-docs`](https://github.com/missionpinball/mpf-docs)
which contains the source code for this website. It's a [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
site. Every time a change is made to that repository, a GitHub action runs that
builds the site and deploys it to GitHub pages.

Making a change (whether it's a simple typo or a major overhaul)

## To make a quick change to an existing page

Quick changes to existing pages can be done right on the web!

To do that:

1.  Browse to the page you want to update, and click sparkly magic
    wand icon to the right of the page headline. That will link you
    to that page in the GitHub repo on GitHub.com.
2.  Login to GitHub. (And create an account if you don't have one!)
2.  Click the pencil icon in the upper-right corner of the page's text.
    This will create a fork of mpf-docs in your
    GitHub account.
3.  Make your change, and click the "Propose file change". This will
    create a pull request. Type a name describing your change, and click
    "Create pull request".
4.  Details and screen shots of this entire process are
    [here](https://help.github.com/articles/editing-files-in-another-user-s-repository/).

## To make a suggestion for a new doc (or to point out an error)

Even if you don't feel comfortable actually changing or editing docs,
you can still tell us about an error in the documentation or suggest new
documentation that we should add. To do this:

1.  Go to the ["Issues" page of the `mpf-docs` repository on
    GitHub](https://github.com/missionpinball/mpf-docs/issues).
2.  Create a GitHub account if you don't have one, and/or login.
3.  Click the "New Issue" button and describe what you'd like us to
    fix or add!

## How do these docs work?

* This website is built using [MkDocs](https://www.mkdocs.org/), which
  is a static site generator for building project documentation.
* It uses the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
  theme, which is a Material Design theme for MkDocs. 99% of your reading about
  how this site works will be here.
* The navigation structure is completely defined in the
  `mkdocs.yml`. So if you add a page, or want to change the order of
  anything, you'll need to edit that file too.

## To clone the mpf-docs repo locally to make bigger changes

If you want to make bigger changes to the docs, or if you want to
download the mpf-docs repo so you can work on it offline, do the
following:

1.  Clone the [`mpf-docs` repo](https://github.com/missionpinball/mpf-docs) from GitHub.
2.  Install the requirements for the site, by running the following in the root of the repo: `pip3 install -r requirements.txt`
3.  Use `mkdocs serve` to build the site and serve it locally. (You can then browse to `http://localhost:8000` to view the site.)
4.  Makes your changes.
5.  Add your name to the `/about/authors.md` doc.
6.  [Submit your pull
    request](https://help.github.com/articles/creating-a-pull-request-from-a-fork/)
