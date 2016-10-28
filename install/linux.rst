Installing MPF on Linux
=======================
While this procedure is being refined, here are the basic steps for installing MPF .30 and up on Debian flavors of Linux.

Download the MPF Debian Installer from https://github.com/missionpinball/mpf-debian-installer/archive/master.zip

Unzip, and from a terminal run ./install from the folder you unzipped the files to. You'll be asked to choose what
platform you're running (FAST or P-ROC), and it will install the prerequisites you need based on your selection. If
you're unsure which platform you'll use, select P-ROC and you'll get everything you need to run either.

When it's complete, you'll be ready to install MPF. The easiest way to do that is to run the following command from
a Terminal window:

::

   sudo pip3 install mpf-mc

Running MPF
-----------

Starting with MPF 0.30, you run MPF by running the "mpf" command directly. (e
.g. you do not have to run "python" from the command prompt). For example, to
launch both the MPF game engine and the media controller, you simply run:

::

   mpf both

This is the same command on all platforms. See the :doc:`running/index` for
details and command-line options.

Keeping MPF up-to-date
----------------------
Since MPF is a work-in-progress, you can use the pip command to update your MPF installation.

To to this, run the following:

::

   sudo pip3 install mpf-mc --upgrade

See :doc:`upgrading`.
