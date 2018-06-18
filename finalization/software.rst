Tuning Software for Production
==============================

Run MPF in production mode
--------------------------

Add the ``-p`` flag to the commandline to run MPF in production mode.
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

Some random hints (there is probably more; please let us know if you notice anything)
-------------------------------------------------------------------------------------

- Make sure you are running the latest supported Python version.
  In our experience the performance of MPF increases with newer Python version.

- Install uvloop using pip (requires Python 3.5+).
  This should reduce latency and improve throughput for I/O operations.
  Please let us know if this improves performance for you.

- Optimise assets for your hardware.
  Audio should have the same sampling rate as your hardware is using.
  Images and videos should be at native resolution to prevent scaling up or down.

- Reencode your videos in a codec which can be efficiently decoded on your target hardware.

