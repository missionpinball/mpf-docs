Tuning Software for Production
==============================

Run MPF in production mode
--------------------------

Add the ``-P`` flag to the commandline to run MPF in production mode.
This will give you some performance gains and reduce the amount of debug
output.
MPF will also try to keep running in some cases instead of exiting the game.
This will not be helpful to find bug but a when you ship machines you won't
see the log anyway.

Run MPF without text UI
-----------------------

Text UI costs some performance so disable it in production or on less powerful
hardware in general.
You can do this by adding the ``-t`` flag to the MPF commandline.

Run MPF with pypy
-----------------

This will currently only work for MPF and not for MPF-MC because kivy is not
yet compatible to pypy.
Performance and latency improvements are around 10x in our benchmarks so
this might be essential on low-end hardware.
Download pypy and install it.
Since pypy is a separate python environment you need to install pip and
reinstall all pip packages for pypy.

.. code-block:: console

   curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
   pypy get-pip.py
   pypy -m pip install mpf

Afterward, you can start MPF within your game folder using:

.. code-block:: console

  pypy -m mpf game

Instead of the ``mpf`` command just use ``pypy -m mpf``.
For ``pip`` use ``pypy -m pip``.

You still need to run MPF-MC using normal python.
This might change in the future.

Install the latest Python version
---------------------------------

For instance, MPF runs significantly faster on Python 3.6 than on 3.5.
Similarly, 3.5 is faster than 3.4.
We expect the same for the next releases.
You might not need this if you are using pypy.

Install uvloop
--------------

When running MPF on linux install ``uvloop`` to reduce latency and increase
throughput for I/O operations.
That will keep your game responsive:

.. code-block:: console

   pip3 install uvloop

MPF will use uvloop once it is available.
Requires at least Python 3.5.


Some random hints
-----------------

- Optimise assets for your hardware.
  Audio should have the same sampling rate as your hardware is using.
  Images and videos should be at native resolution to prevent scaling up or down.

- Reencode your videos in a codec which can be efficiently decoded on your target hardware.

- Let us know if we missed something here.

