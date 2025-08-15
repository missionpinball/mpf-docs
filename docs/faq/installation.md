---
title: "FAQ: Installation"
---

# FAQ: Installation


## How do I get started?

Start with the [Start Here](../start/index.md)
link in the menu. That will explain an overview of how MPF works and then lead you through the features, the tutorial, and so on.

## What are the prerequisites?

If you just want to start playing with MPF, you do not need a physical
pinball machine. In fact we have a graphical tool (the [MPF Monitor](../tools/monitor/index.md)) which simulates
a real pinball machine, so you can probably build an entire game without
having an actual pinball machine.

If you want to use a real pinball machine (or build a real machine), you
need to pick a pinball control system. (We have a list of supported
control systems [here](../hardware/index.md).)
If you want to get started as cheaply as possible, the Open Pinball
Project hardware is open source which you can build yourself. You can
probably build all the hardware you need for under $100.

## What computer hardware do I need?

MPF supports Windows, Mac, and Linux, so pretty much any computer is
fine. Most people do their development of MPF on whatever computer they
use in their daily lives, then when they're getting close to done with
their machine, they install a dedicated computer (or even a Raspberry
Pi) in their machine to run MPF.

## What Python version can I use with MPF?

The stable version (0.57, currently on 0.57.3) of MPF can be used with
Python versions 3.8-3.11 (with 3.12+ being tested with minor issues).
We walk you through getting Python installed in our
[installation documentation](../install/index.md).

The previous version of MPF, 0.56. is only compatible with Python from
version 3.7 through 3.9.

The next revision (0.80.x) of MPF supports Python 3.8 - 3.11, but does
not support the legacy Media Controller. The media controller for 0.80
is called GMC, and is in active development.

## Should I use the stable version or development version?

We recommend that people use the latest "stable" (or "release")
version of MPF unless you need specific features from the "dev" (next)
version.

## Where do I find information on older versions of MPF?

If you want information about an older version of MPF, we have
[prior version documentation bundles](../versions/docs.md).

You can install older versions of MPF with pip, like this:

    pip install mpf==0.56.0.dev33
