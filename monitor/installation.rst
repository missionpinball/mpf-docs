Installing the MPF Monitor
==========================

Here's how you install the MPF Monitor. These instructions are a bit rough
since MPF Monitor is an early prototype. We'll eventually clean these up and
make a proper installer.

For non-Git users
-----------------

If you don't know what "git" is, or you're not using git, follow these
instructions:


1. If you have Windows, first install this:
   https://sourceforge.net/projects/pyqt/files/PyQt5/PyQt-5.5.1/ (Mac and Linux
   will install it automatically when mpf-monitor is installed.)
2. Download the MPF monitor from here: https://github.com/missionpinball/mpf-monitor
   (Click the green "Clone or download" button, then "Download ZIP.)
3. Unzip the file to whatever location you want.
4. Open a command prompt / terminal window, change to the new folder where you
   unzipped the file, and run one of the following commands (the trailing dot
   is part of the command):
    * If you run MPF by running ``mpf``, then run ``pip install .``
    * If you run MPF by running ``python3 -m mpf`` then run
      ``python3 -m pip install .``
    * If you run MPF by running ``kivy -m mpf`` then run
      ``kivy -m pip install .``

For git users
-------------

1. If you have Windows, first install this:
   https://sourceforge.net/projects/pyqt/files/PyQt5/PyQt-5.5.1/ (Mac and Linux
   will install it automatically when mpf-monitor is installed.
2. Clone the MPF monitor repo from here: https://github.com/missionpinball/mpf-monitor
3. Run one of the following commands from the repo folder on your computer.
   (The trailing dot is part of the command):
    * If you run MPF by running ``mpf``, then run ``pip install -e .``
    * If you run MPF by running ``python3 -m mpf`` then run
      ``python3 -m pip install -e .``
    * If you run MPF by running ``kivy -m mpf`` then run
      ``kivy -m pip install -e .``
4. The ``-e`` option means that this package is installed in "editable" mode,
   meaning that you can pull/sync the mpf-monitor repo to update your
   mpf-monitor installation. This is useful in MPF monitor's early stages as it
   will change often.
