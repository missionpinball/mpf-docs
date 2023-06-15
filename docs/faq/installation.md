---
title: FAQ: Installation
---

# FAQ: Installation


## How do I get started?

Start with the [Start Here](../start/index.md)
link in the menu on the left. That will explain an overview of how MPF
works and then lead you through the features, the tutorial, and so on.

## What are the prerequisites?

If you just want to start playing with MPF, you do not need a physical
pinball machine. In fact we have a graphical tool (the [MPF
Monitor](https://github.com/missionpinball/mpf-monitor)) which simulates
a real pinball machine, so you can probably build an entire game without
having an actual pinball machine.

If you want to use a real pinball machine (or build a real machine), you
need to pick a pinball control system. (We have a list of supported
control systems [here](../hardware/index.md).)
If you want to get started as cheaply as possible, the Open Pinball
Project hardware is open source which you can build yourself. You can
probably build all the hardware you need for under \$100.

## What computer hardware do I need?

MPF supports Windows, Mac, and Linux, so pretty much any computer is
fine. Most people do their development of MPF on whatever computer they
use in their daily lives, then when they're getting close to done with
their machine, they install a dedicated computer (or even a Raspberry
Pi) in their machine to run MPF.

## What Python version can I use with MPF?

Your need Python 3.5 or 3.6. Python 3.4 is end of life and will no
longer be supported. Python 3.7 and newer are not yet supported. We walk
you through getting Python installed in our
[installation documentation](../install/index.md).

## Should I use the stable version or development version?

We recommend that people use the latest "stable" (or "release")
version of MPF unless you need specific features from the "dev" (next)
version.

## Where do I find information on older versions of MPF?

If you want information about an older version (0.30 and newer), click
the "Read the Docs" link in the lower-left corner of any page on
docs.missionpinball.org and select the version you want to read about.

You can install older versions of MPF with pip, like this:

    pip install mpf-mc==0.31

Documentation for versions of MPF prior to 0.30 is available in [this
post](https://groups.google.com/forum/#!msg/mpf-users/7I-phnq9rOs/)
