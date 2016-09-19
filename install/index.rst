MPF Installation
================

Installing MPF is fairly straightforward. It can be used on Windows, Mac OS X, or Linux, on both Intel x86 and ARM
processors, and in 64-bit and 32-bit systems.

Full step-by-step install guides
--------------------------------

We've created step-by-step installation guides which walk you through the entire process. Select the OS you're using
from the list below:

.. toctree::
   :maxdepth: 1

   Windows <windows>
   Mac OS X <mac>
   Linux <linux>
   Raspberry Pi <raspberry>


Hardware drivers
----------------

Once you have MPF installed, you will need to install the drivers for the particular pinball controller you're using.
Select the appropriate guide from our :doc:`/install/drivers/index` list:

.. toctree::
   :maxdepth: 1

   /install/drivers/index

Keeping MPF up-to-date
----------------------

.. toctree::
   :maxdepth: 1

   Updating MPF <upgrading>

Choosing a host computer
------------------------

.. toctree::

   host_computer

Quick install guide
-------------------

If you're already Python-savvy and know what you're doing, here's the quick-and-dirty on MPF installation:

+ For Windows, MPF requires Python 3.4 (3.5 does not work). x86 or x64 is ok. Install "mpf-mc" via pip. That's it.
+ For Mac, we have an MPF.app package which includes the Python 3.5 binaries and all the other libraries MPF needs. Just
  use that. (See the Mac OS X link above.)
+ For Linux, we have a Debian installer. See the Linux link above for details.

In all cases you'll need to install the USB drivers for your controller hardware separate from MPF. See the controller
hardware section of the How To guides for details.



