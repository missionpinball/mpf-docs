---
title: Contributing to MPF
---

# Contributing to MPF


Want to add a feature? A missing event somewhere? Wrote a new device
which might be useful for other users? Fixed a bug? Added some small
missing piece?

We'd love to take your contribution upstream!

Found a bug which you can reproduce? Fill an issue:

* [MPF Issues on
    github](https://github.com/missionpinball/mpf/issues). Use this for
    game and platform related bugs
* [MPF-MC Issues on
    github](https://github.com/missionpinball/mpf-mc/issues). Use this
    for media controller bugs such as problems with slides, widgets or
    audio.

If you want to discuss a feature or bug (or if you are unsure). Visit
our forum: <https://github.com/orgs/missionpinball/discussions>

## Install MPF in development mode

To make changes to MPF you need to install it in developer/editable
mode:

1.  Fork the [mpf repo](https://github.com/missionpinball/mpf/) on
    GitHub. Do this by clicking on the Fork button in the top right
    corner.
2.  Clone your fork of the mpf repo to your local machine. Determine the
    folder where you want this to reside. Consider using a different
    folder than where your personal MPF code resides. Then run the
    following command:
    (`git clone https://github.com/YOUR_GITHUB_HANDLE/mpf/`)
3.  Install the MPF dependencies if you haven't installed mpf before.
    On linux you can run our [mpf dependency
    installer](https://raw.githubusercontent.com/missionpinball/mpf-debian-installer/dev/install-mpf-dependencies).
    On other platforms check the
    [installation instructions](../install/index.md) instructions.
4.  Navigate to your cloned repository and run:
    `pip3 install mpf-mc --pre` to install MPF in editable mode.

## Install MPF-MC in development mode

If you want to make changes to MPF-MC (Media Controller) you will need
to install it in developer/editable mode:

1.  Fork the [mpf-mc repo](https://github.com/missionpinball/mpf-mc/) on
    GitHub. Do this by clicking on the Fork button in the top right
    corner.
2.  Clone your fork of the mpf-mc repo to your local machine
    (`git clone https://github.com/YOUR_GITHUB_HANDLE/mpf-mc/`).
3.  Install the MPF-MC dependencies if you haven't installed mpf-mc
    before. On linux you can run our [mpf mc dependency
    installer](https://raw.githubusercontent.com/missionpinball/mpf-debian-installer/dev/install-mc-dependencies).
    On other platforms check the
    [installation instructions](../install/index.md) instructions.
4.  Navigate to your cloned repository and run:`pip3 install -e .` to
    install MPF-MC in editable mode

To work on both the MPF and the MPF-MC complete both sets of
instructions. Make sure you don't install the

After cloning and installing the dependencies for the desired project
follow these steps.

1.  Switch your repository to the branch corresponding to the version
    you want to work with. This should be `dev` in most cases or the
    current release for smaller bug fixed. Do what works best for you.
    We can help to forward or backport your changes.

2.  From your MPF folder that is connected with git, create a local
    branch to work on (`git checkout -b your_feature_name`).

3.  Make your changes.

4.  Add your name to the `AUTHORS` file.

5.  If possible add an unit test. We can help with that and a first Pull
    Request without a test is definitely fine.

6.  Run `python3 -m unittest discover -s mpf.tests` and check that all
    tests still pass.

    To check that all tests will still pass for mpf-mc run
    `python3 -m unittest discover -s mpfmc.tests`.

    If you get an error message that Python was not found, try running
    the following command: `python -m unittest discover -s mpfmc.tests`.
    This is the same basic command, but runs on python instead of
    python3.

7.  Commit your changes (`git commit -a`)

8.  In the git commit screen type your title on line 1. Leave a blank
    line, and then type out a description of what is included in this
    commit. Once you are done typing your commit notes, press escape.
    This will bring your cursor to the bottom of this panel. From there
    type ('':wq'') and press Enter. This will complete your commit
    notes.

9.  Push your changes to your github
    (`git push origin your_feature_name`).

10. Open up your Fork on github and create and submit your pull request
    to merge from your local back to MPF.

We recommend you to use a decent IDE because it makes life easier. Most
of the MPF developers use PyCharm but other IDEs will work as well.

## Getting started with an open issue

We maintain a list of issues which are self-contained and good to solve
on their own without too much interaction with core code. We label those
as [help
wanted](https://github.com/missionpinball/mpf/labels/help%20wanted)
(although they do not have to be easy, just self-containted). If you
want to work on one of them (or any other issue) comment on the issue or
write in the forum and we will assist you along the way.
