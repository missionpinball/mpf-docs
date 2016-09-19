Tutorial step 1: Prerequisites
==============================

The first step to using MPF is to understand some basics about how it works and to actually
get MPF installed on your computer. So that's what these next few steps will do.

1. You don't need a physical pinball machine yet
------------------------------------------------

First, you do *not* need to have physical hardware to go through this
tutorial. You can complete the entire thing via MPF's "virtual" hardware
platform which lets you run MPF on your computer with no actual hardware attached.

We should point out that MPF's virtual platform is *not* pinball emulation software. There is no
3D-rendered playfield, and it's not like Future Pinball or Visual Pinball or anything.

MPF is a bit different because it's designed to control a real, physical pinball
machine, so when you run MPF's virtual platform interface, really all you're
going to see is a lot of text and log messages as well as whatever's on your
machine's DMD or LCD.

Still, it's enough to get started. We'll show you how to map keyboard keys on your computer so
you can "play" your machine to test it out.

2. Read the overview of MPF
---------------------------

You certainly don't have to read through all the documentation to
start this tutorial. However, the documentation is arranged in the order you should
read it, so if you haven't read the documentation leading up to this point, please
do that now. (If you're reading this online, start with the ":doc:`/start/index`" entry
on the left. If you're reading a PDF, please turn to Page 1. :)


3. Check your MPF version
-------------------------

This tutorial is written for MPF version |version|, so let's make sure the version
of MPF you have installed matches that.

To do this, open a command prompt and run the following command:

::

   mpf --version

That command should print something like ``MPF v0.31.0``. Note that the version is three numbers, ``x.y.z``.
The last number (the "z") is the patch number and doesn't matter for the documentation. In other words,
the documentation for 0.31 is valid for 0.31.0 or 0.31.1 or 0.31.212.

If this command gives you an error, then go back to the :doc:`/install/index` section to make sure
MPF is installed. If it prints a version number lower than |version|, then install the latest version of
MPF. And if it shows that you have a newer version of MPF (based on the first two numbers), then go to
`docs.missionpinball.org <http://docs.missionpinball.org>`_ to get the version of this documentation that matches the version of MPF
you have.


4. Let's go!
------------

If you're reading this tutorial online, note that there are "Previous" and
"Next" navigation buttons at the bottom of each page. You should be able to just
click those to follow along. (And if you'd like to download a copy of this
documentation to read offline, click the "Read the Docs" link at the bottom
of the menu bar on the left for links to PDF, HTML, and Epub versions of this
documentation.
