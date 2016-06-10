Tutorial step 1: Prerequisites
==============================

Before we dig into building your own machine's configuration, let's make sure
you have everything you need to get started.


1. You don't need a physical pinball machine yet
------------------------------------------------

First, you do *not* need to have physical hardware to go through this
tutorial. You can complete the entire thing via MPF's "virtual" hardware
platform which lets you run MPF on your computer with no hardware attached.

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

You certainly don't have to read through hundreds of pages of documentation to
start this tutorial. However, we want to point out a few specific docs that you
should read first which will help you understand some core concepts of MPF that
we'll be using as we go through the tutorial.

Here are the docs that we suggest you read before we proceed.

#. :doc:`/start/overview`
#. :doc:`/start/hardware_interface`


3. Install MPF |version|
------------------------

We have separate documentation that walks you through downloading and installing
MPF, as well as running our *Demo Man* example game. So if you haven't done so
already, get MPF installed and make sure you can run *Demo Man*, and then come
back here to start creating your own machine!

#. :doc:`/install/index`
#. :doc:`/howto/installation/demo_man`

If you do have MPF installed, let's make sure it's the right version. Open a
command prompt and run the following command. If this gives you an error, it
means MPF is not installed, or you have an older version.

::

   mpf --version

This tutorial is written for MPF |version|, so make sure that's what you have,
and follow the installation links above if not.


4. Let's go!
------------

If you're reading this tutorial online, note that there are "Previous" and
"Next" navigation buttons at the bottom of each page. You should be able to just
click those to follow along. (And if you'd like to download a copy of this
documentation to read offline, check the :doc:`/download`
page links to this entire documentation set in multiple downloadable formats.)
