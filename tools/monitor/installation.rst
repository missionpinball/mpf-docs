Installing the MPF Monitor
==========================

Here's how you install the MPF Monitor. These instructions are a bit rough
since MPF Monitor is an early prototype.

Windows and Mac
---------------

MPF Monitor has dependencies on MPF and should be run in the same environment.
If you use a virtual environment for MPF, activate it before proceeding.

1. Install PyQt5.  Open a command prompt and run:

.. code-block:: console

   pip install PyQt5
   
.. note::  

   If this does not work, you can also try to download and install from here: https://sourceforge.net/projects/pyqt/files/PyQt5/PyQt-5.5.1/
   Just choose all the defaults and you should be ok.
   
2. Open a command prompt and run: (You can run this from any folder)

.. code-block:: console

   pip install mpf-monitor

.. note::

   If you originally ran "pip" in a different way, perhaps with ``pip3`` or
   ``python3 -m pip``, then do that again here instead of the plain "pip".

To update MPF Monitor to the latest version at any time, run:

.. code-block:: console

   pip install mpf-monitor --upgrade

Note that since MPF Monitor is a separate app from MPF and MPF-MC, the version
numbers of the Monitor and MPF are not the same. (For example, the same version
of MPF Monitor can work across several versions of MPF.)


Linux
-----

Note that these instructions assume you're running Python 3.5+.
You need to download and install
`PyQt5 <https://sourceforge.net/projects/pyqt/files/PyQt5>`_.
It is best to use the package manager of your distribution to achieve that.
For example, in debian/ubuntu, you should run ``apt-get install python3-pyqt5``.

Install mpf-monitor via pip:

.. code-block:: console

   pip install mpf-monitor

To update MPF Monitor to the latest version at any time, run:

.. code-block:: console

   pip install mpf-monitor --upgrade

Note that since MPF Monitor is a separate app from MPF and MPF-MC, the version
numbers of the Monitor and MPF are not the same. (For example, the same version
of MPF Monitor can work across several versions of MPF.)
