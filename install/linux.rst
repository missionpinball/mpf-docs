Installing MPF on Linux
=======================

As part of our automated build process, we build and test MPF and MPF-MC against Ubuntu 14.04 & 16.04 and Debian jessie.

Download the MPF Debian Installer (which is used for all of these) from
https://github.com/missionpinball/mpf-debian-installer/archive/dev.zip

Unzip it, and from a terminal run ``chmod +x install && sudo ./install`` from the folder you unzipped the files to. If you are using a P-Roc
or P3-Roc also run ``chmod +x install-proc && ./install-proc`` (skip for other platforms). Consult the README for more information.

Download & run the "Demo Man" example game
------------------------------------------

Now that you have MPF installed, you probably want to see it in action. The easiest way to do that is
to download a bundle of MPF examples and run our "Demo Man" example game. To do that, follow
the instructions in the :doc:`/example_machines/demo_man` guide.

There's another example project you can also check out if you want called the "MC Demo" (for media controller demo)
that lets you step through a bunch of example display things (slides, widgets, sounds, videos, etc).
Instructions for running the MC Demo are :doc:`here </example_machines/mc_demo>`.

Running MPF
-----------

See the :doc:`/running/index` for details and command-line options.

Keeping MPF up-to-date
----------------------

To upgrade MPF just re-run the installer which will make sure that you will also get updated dependencies:

::

  sudo ./install


Alternatively, since MPF is a work-in-progress, you can use the *pip* command to update your
MPF installation.

To to this, run the following:

::

  pip3 install mpf mpf-mc --upgrade

This will cause *pip* to contact PyPI to see if there's a newer version of the
MPF MC (and any of its requirements, like MPF). If newer versions are found, it
will download and install them.

To install the latest dev release (not generally recommended) which allows you to try bleeding-edge features run:

::

  pip3 install mpf mpf-mc --pre --upgrade
  
To downgrade (or install a specific release x.yy.z) run:

::

  pip3 install mpf=x.yy.z
  pip3 install mpf-mc=x.yy.z
