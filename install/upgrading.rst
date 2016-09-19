How to upgrade MPF to the latest version
========================================

Since MPF is a work-in-progress that's changing often, there are times when
you'll need to upgrade your installation to the latest version.

To check your MPF version:
--------------------------

For Windows or Linux, run the following command:

::

  mpf --version

For Mac (using our MPF app):

::

  kivy -m mpf --version

Finding the last versions of MPF
--------------------------------

You can see what the latest versions of MPF and MPF-MC are by visiting the PyPI
website:

* https://pypi.python.org/pypi/mpf
* https://pypi.python.org/pypi/mpf-mc

Updating your installation of MPF
---------------------------------

If you already have MPF installed, you can upgrade it to the latest version
via the following commands: (If you don't have MPF installed, see our
:doc:`installation documentation <index>`.

For Windows and Linux:

::

  pip install mpf --upgrade
  pip install mpf-mc --upgrade

(If you have Python 2 and Python 3 installed, you need to use "pip3" instead of "pip".)

For Mac (using our MPF app):

::

  kivy -m pip install mpf --upgrade
  kivy -m pip install mpf-mc --upgrade

These command tell pip to contact PyPI to see if there's a newer version of the
"mpf" and "mpf-mc" packages, anf if newer versions are found, it downloads and installs them.

This commands are safe to run any time, and if a newer version of MPF is not available,
it will tell you that you have the latest version and exit.
