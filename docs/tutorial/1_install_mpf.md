---
title: "Tutorial 1: Installing MPF on your computer"
---

# Tutorial 1: Installing MPF on your computer

--8<-- "tutorial.md"

The first step to using MPF is to understand some basics about how it
works and to actually get MPF installed on your computer. So that's
what these next few steps will do.

## 1. You don't need a physical pinball machine yet

First, you do *not* need to have physical hardware to go through this
tutorial. You can complete the entire thing via MPF's "virtual"
hardware platform which lets you run MPF on your computer with no actual
hardware attached.

We should point out that MPF's virtual platform is *not* pinball
emulation software. There is no 3D-rendered playfield like Pinball
Arcade, and you can't really "play" your game. (This is because MPF
is not pinball emulation software, rather, it's software to control a
real pinball machine!)

That said, MPF has tools which let you control switches and see lights
flash on your computer screen, and you can arrange them onto an image of
your playfield, so you can actually build a complete game in MPF before
you ever start on a physical machine!

## 2. Read the overview of MPF

You certainly don't have to read through all the documentation to start
this tutorial. However, the documentation is arranged in the order you
should read it, so if you haven't read the stuff leading up to this
point, please do that now. (If you're reading this online, start with
the "[MPF overview: How MPF works](../start/index.md)" entry on the left.
If you're reading a PDF, please turn to Page 1. :)

## 3. Install MPF

Obviously before you can start using MPF, you need to install it. At
this point it's best to install MPF on whatever computer you use daily.
There is certainly no need to try to put it on some small Linux single
board computer or Raspberry Pi or whatever you ultimately plan to put in
your pinball machine. For now just install it on your laptop.

MPF runs on Windows, Mac, and Linux. You can find the installation
instructions [here](../install/index.md).

Go do that now, and make sure that you get both MPF and the MPF-MC
installed.

## 3a. What if you already installed MPF?

If you already installed MPF, let's quickly make sure you're using the
same version this tutorial is written for.

This tutorial is written for MPF versions .

To see what version you have, open a command prompt (like you did when
you installed MPF) and run the following command:

``` console
mpf --version
```

That command should print something like `MPF v0.51.3`. Note that the
version is three numbers, `x.y.z`. The last number (the "z") is the
patch number and doesn't have any functional changes. (In other words,
MPF 0.51.0 and 0.51.2 and 0.51.56 have the same functions and features.)

!!! tip "Use the latest version of MPF"

    We highly recommend that you use the latest version of MPF, especially
    if you're starting out and don't have config files to migrate. To find
    out which version of MPF is the latest, visit the [MPF Users Google
    Group](https://groups.google.com/forum/#!forum/mpf-users) and look at
    the banner welcome message at the top of the page.

If this command gives you an error, then go back to the
[Downloading & Installing MPF (2023 Version)](../install/index.md) section to make sure MPF
is installed. If it prints a version number lower than , then install
the latest version of MPF. And if it shows that you have a newer version
of MPF (based on the first two numbers), then go to
[docs.missionpinball.org](http://docs.missionpinball.org) to get the
version of this documentation that matches the version of MPF you have.

## 4. Let's go!

If you're reading this tutorial online, note that there are
"Previous" and "Next" navigation buttons at the bottom of each page.
You should be able to just click those to follow along. (And if you'd
like to download a copy of this documentation to read offline, click the
"Read the Docs" link at the bottom of the menu bar on the left for
links to PDF, HTML, and Epub versions of this documentation.)
