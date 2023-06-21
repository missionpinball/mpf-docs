---
title: Example MPF projects you can learn from
---

# Example MPF projects you can learn from

MPF has been around for almost ten years, so by now there are lots of examples
you can use.

## Test config files in MPF and MPF-MC

Did you know the MPF and MPF-MC repos have thousands of self-tests built in, and
most of these tests have their own YAML config files? Since these tests cover
everything, there are example config files for everything.

[This guide](tests.md) shows you how to find these files and learn from their
example configs.

## The mpf-examples repo

There's a repo called `mpf-examples` as part of the Mission Pinball org on GitHub.
That repo contains several examples of MPF configs you can run and learn from,
including:

* [Demo Man](demo_man.md)
* [MC (Media Controller) Demo](mc_demo.md)
* [Tutorial config files](../tutorial/index.md)

Full details about the mpf-examples project and how to download it are
[here](mpf-examples.md).

## The MPF Cookbook

We have a "cookbook" as part of the MPF documentation that shows example
recipes of how to do things in MPF. You can find that here:

* [Cookbook recipes](../cookbook/index.md)

## Brooks 'n Dunn

One of the projects Brian Madden & Gabe Knuth took on in 2015 was to rewire and build and MPF
config for Gottlieb's Brooks 'n Dunn. (BnD). BnD was the machine that
Gottlieb was working on when they shut down in 1996.

We like this repo as an example of the automated tests you can write which actually test your
MPF code. The BnD repo is at [github.com/gabeknuth/bnd](https://github.com/gabeknuth/bnd),
and the game tests are [here](https://github.com/GabeKnuth/BnD/blob/master/tests/test_bnd.py).

## Mass Effect 2

An extensive project to build a complete MPF game from scratch and play
on a re-skinned Game of Thrones cabinet (Spike platform), inspired by
the video game Mass Effect 2. With the exception of audio tracks
extracted from the Mass Effect 2 data files, all of the game code is
available to clone from the repo and run. MPF monitor is supported so
you can simulate gameplay without the Spike GoT hardware.

All of the project code is via [github.com/avanwinkle/masseffect2](https://github.com/avanwinkle/masseffect2).

## Check out the MPF Showcase

The [MPF Showcase](../showcase/index.md) has links to lots of MPF projects, and many of them have
"code" links which link to their code on GitHub or another public location. You can browse through them to see
how they handle things.

## Search GitHub Globally

There are hundreds of MPF projects on GitHub. GitHub has recently overhauled their search capabilities, and now you
can search all of GitHub for MPF projects. For example, go to GitHub.com and search for a term like "driverboards:" (be sure to include the colon), and then click the "Code" filter (so you're searching for source code, not repo names), and maybe also click the "YAML" Language filter so you're looking for just YAML files.

Here's a [quick search on GitHub.com for "driverboards:" in YAML files](https://github.com/search?q=driverboards%3A+language%3AYAML&type=code&l=YAML) which returns repos for 112 public MPF game configs!
