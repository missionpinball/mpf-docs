Troubleshooting
===============

1. Run diagnosis
----------------

If your game won't run, let's make sure MPF is ok.
Run ``mpf diagnosis`` from within your machine folder to see if your installation is fine:

.. code-block:: console

  $ mpf diagnosis
  MPF version: MPF v0.50.0-dev.11
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
  
2. Ask in our forum
-------------------

If you cannot solve the problem ask in our `support forum <https://groups.google.com/forum/#!forum/mpf-users>`_.
Please include the following information:

1. The output of `mpf diagnosis`
2. In case you suspect an installation problem include the output of unittests and if you can run demo_man.
3. Add a log of your game. Therefore, run your game with `mpf both -v -V` and grab the latest MPF and MC log from the log folder in your machine.
4. Describe how to reproduce your problem.
5. Provide relevant config snippets or, if possible, a link to download/checkout your machine config so we can reproduce the issue.
