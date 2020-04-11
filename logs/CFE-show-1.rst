CFE-show-1: Show does not appear to be a valid show config
==========================================================

This error occurs when MPF loads a show which is not a list of steps.
There are two ways to add shows to your machine: either as file or inside your
config.
Both can happen inside a mode or machine-wide inside your global config folder.

Examples
--------

File Shows
^^^^^^^^^^

This is how a file show should look:

.. code-block:: mpf-config

   ##! show: flash_red
   #show_version=5
   - duration: 1
     lights:
       led1: red
   - duration: 1
     lights:
       led1: off

Please note that there can be only one show per dedicated show file as MPF
uses the filename as show name.
See :doc:`/shows/file_shows` for details.

Config Shows
^^^^^^^^^^^^

This is how a show inside your config should look:

.. code-block:: mpf-config

   shows:
     flash_red:
       - duration: 1
         lights:
           led1: red
       - duration: 1
         lights:
           led1: off

See :doc:`/shows/config_shows` for details.

Common Pitfalls
---------------

Multiple shows inside one file show
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is NOT valid as file show:

.. code-block:: yaml

   # INVALID FILE SHOW
   flash_red:
     - duration: 1
       # [...]
   flash_blue:
     - duration: 1
       # [...]

Instead you have to create two files ``flash_red.yaml`` and
``flash_blue.yaml``.

Missing hyphen for your step
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You might have missed the hyphon in front of your first step (or in front of all steps):

.. code-block:: yaml

   # INVALID FILE SHOW
   #show_version=5
   duration: 1    # note the missing dash here
   lights:
     led1: red

The same can happen in config shows:

.. code-block:: yaml

   # INVALID CONFIG SHOW
   shows:
     flash_red:
       duration: 1   # hyphen missing here
       lights:
         led1: red

This often happens with one step shows.
See above for working examples.

.. include:: config_error_footer.rst

Related How To guides
---------------------

* :doc:`/shows/index`
