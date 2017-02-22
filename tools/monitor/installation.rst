Installing the MPF Monitor
==========================

Here's how you install the MPF Monitor. These instructions are a bit rough
since MPF Monitor is an early prototype.

Windows
-------

1. Install PyQt5 from here: https://sourceforge.net/projects/pyqt/files/PyQt5/PyQt-5.5.1/
   Just choose all the defaults and you should be ok.
2. Open a command prompt and run: (You can run this from any folder)

::

   pip install mpf-monitor

.. note::

   If you originally ran "pip" in a different way, perhaps with ``pip3`` or
   ``python3 -m pip``, then do that again here instead of the plain "pip".

To update MPF Monitor to the latest version at any time, run:

::

   pip install mpf-monitor --upgrade

Note that since MPF Monitor is a separate app from MPF and MPF-MC, the version
numbers of the Monitor and MPF are not the same. (For example, the same version
of MPF Monitor can work across several versions of MPF.)

Mac
---

Open a terminal window and run the following command: (You can run this from
any folder)

::

   pip3 install mpf-monitor

To update MPF Monitor to the latest version at any time, run:

::

   pip3 install mpf-monitor --upgrade

Note that since MPF Monitor is a separate app from MPF and MPF-MC, the version
numbers of the Monitor and MPF are not the same. (For example, the same version
of MPF Monitor can work across several versions of MPF.)

Linux
-----

Note that these instructions assume you're running Python 3.5. If you're
running Python 3.4, you'll need to first manually download and install
`PyQt5 <https://sourceforge.net/projects/pyqt/files/PyQt5>`_. You could also
potentially run ``apt-get install python3-pyqt5``.

Install mpf-monitor via pip:

::

   pip install mpf-monitor

To update MPF Monitor to the latest version at any time, run:

::

   pip install mpf-monitor --upgrade

Note that since MPF Monitor is a separate app from MPF and MPF-MC, the version
numbers of the Monitor and MPF are not the same. (For example, the same version
of MPF Monitor can work across several versions of MPF.)
