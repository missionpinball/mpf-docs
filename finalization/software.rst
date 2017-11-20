Tuning Software for Production
==============================

Some random hints (there is probably more; please let us know if you notice anything):

- Make sure you are running the latest supported Python version.
  In our experience the performance of MPF increases with newer Python version.

- Install uvloop using pip (requires Python 3.5+).
  This should reduce latency and improve throughput for I/O operations.
  Please let us know if this improves performance for you.

- Optimise assets for your hardware.
  Audio should have the same sampling rate as your hardware is using.
  Images and videos should be at native resolution to prevent scaling up or down.

- Reencode your videos in a codec which can be efficiently decoded on your target hardware.
