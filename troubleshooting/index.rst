Troubleshooting
===============

1. Run MPF without text ui
--------------------------

The text ui which is shown by default may hide some errors and make
troubleshooting more difficult.
To disable text ui run mpf using:

.. code-block:: console

  $ mpf game -t

You can also add some more logging output:

.. code-block:: console

  $ mpf game -t -v -V

Scroll up in the console (or check the log file in the ``logs`` folder) to find
the error which was emitted.


2. Run diagnosis
----------------

If your game won't run and you don't get an error, let's make sure MPF is ok.
Run ``mpf diagnosis`` from within your machine folder to see if your installation is fine:

.. code-block:: console

  $ mpf diagnosis


  MPF version: MPF v0.50.0-dev.11
  MPF install location: /data/home/jan/cloud/flipper/src/mpf/mpf
  Machine folder detected: /data/home/jan/cloud/flipper/src/good_vs_evil
  MPF-MC version: MPF-MC v0.50.0-dev.5 (config_version=5, BCP v1.1, Requires MPF v0.50.0-dev.10)

  Serial ports found:
  /dev/ttyUSB3
      desc: Quad RS232-HS
      hwid: USB VID:PID=0403:6011 LOCATION=1-12
  /dev/ttyUSB2
      desc: Quad RS232-HS
      hwid: USB VID:PID=0403:6011 LOCATION=1-12
  /dev/ttyUSB1
      desc: Quad RS232-HS
      hwid: USB VID:PID=0403:6011 LOCATION=1-12
  /dev/ttyUSB0
      desc: Quad RS232-HS
      hwid: USB VID:PID=0403:6011 LOCATION=1-12

If you suspect a problem with MPF itself you can try to run the demo_man game.
Make sure that you select the same version as your MPF version (i.e. demo_man 0.33.x for MPF 0.33.10).

Additionally, you can run the MPF and MPF-MC unit tests (the number of tests may be different).

.. code-block:: console

  $ python3 -m unittest discover -s mpf.tests
  [...]
  ----------------------------------------------------------------------
  Ran 622 tests in 20.818s

  OK

Similarly, you can run MPF-MC unit tests (they will take a bit longer and might show some deprecation warnings from kivy):

.. code-block:: console

  $ python3 -m unittest discover -s mpfmc.tests
  [...]
  Ran 182 tests in 193.610s

  OK

3. Debug crashes/segfaults/hangs
--------------------------------

If you experience a crash/segfault or hang (especially in MC) you can run
`gdb on python <https://wiki.python.org/moin/DebuggingWithGdb>`_ to find the
crash or hang.
You can attach a debugger to the running mc process like this:

.. code-block:: console

  $ ps aux | grep mpf
  jan       9678 12.4  0.3 1082068 127304 pts/2  SNl+ 23:17   0:06 /usr/bin/python3 /usr/local/bin/mpf mc
  jan       9760 37.0  0.1 571368 56660 pts/3    Sl+  23:17   0:01 /usr/bin/python3 /usr/local/bin/mpf game -X

In this example ``9678`` is the pid of MC and ``9760`` is the pid of MPF.
You can then attach gdb:

.. code-block:: console

  $ sudo gdb python3 9678
  [...]
  (gdb) thread apply all bt
  [...]
  (gdb) thread apply all py-bt
  [...]

Please send us the complete output of gdb.
That will help us to figure out the problem.


4. Ask in our forum
-------------------

If you cannot solve the problem ask in our `support forum <https://groups.google.com/forum/#!forum/mpf-users>`_.
Please include the following information:

#. The output of ``mpf diagnosis``
#. In case you suspect an installation problem include the output of unittests and if you can run demo_man.
#. If you got a problem with a device (e.g. a ball_lock) or a platform (e.g. P-Roc or FAST) add `debug: True` to the relevant config section to enable extra debug output.
#. Add a log of your game. Therefore, run your game with ``mpf both -v -V`` and grab the latest MPF and MC log from the log folder in your machine.
#. Describe how to reproduce your problem.
#. Provide relevant config snippets or, if possible, a link to download/checkout your machine config so we can reproduce the issue.

.. toctree::
   :hidden:

   debugging_memory_leaks
