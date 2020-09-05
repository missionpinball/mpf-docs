Debugging MPF installation problems
===================================

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
