
Note: Mac support is new for us. We have it working on all hardware
platforms (P-ROC, P3-ROC, and FAST), though right now getting it
running for P-ROC/P3-ROC requires following a `58-step process`_.
We're working on getting the compiled drivers extracted from that so
we can build a nice all-in-one installer like we have for Windows and
Linux. We expect to have that done soon. (Sept 2015) Also note that
the Movies module is not available on the Mac. This is because Pygame
for Mac does not support movies. We will be moving MPF off of Pygame
in late 2015, but until then, no movies on the Mac. Here are some raw
notes if you want to try with Mac in the meantime:


+ Python 2.7 is built in.
+ Install Pygame (1.9.2pre for Apple-supplied Python 2.7)
+ Install pip
+ Run `sudo pip install pyyaml`
+ Install the `FTDI driver`_ for Mac.
+ Install the pinball controller interface libraries:

    + FAST, run `sudo pip install pyserial`
    + P-ROC/P3-ROC, follow the 58-step procedure from above

+ Download MPF from GitHub




Next Steps
----------

At this point you're all set! Check out our `tutorial`_ which will
walk you through running the *Demo Man* sample game that comes with
MPF and will show you how to build your own game!

.. _FTDI driver: http://www.ftdichip.com/Drivers/D2XX.htm
.. _58-step process: http://www.pinballcontrollers.com/forum/index.php?topic=1204.0
.. _tutorial: /tutorial


