CFE-coils-1: Driver must have a number
======================================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/coils`                                                         |
+------------------------------------------------------------------------------+

This error occurs when MPF loads a coil which is has an empty number or misses
a number entry.
Unfortunately, hardware needs a switch number to address your coil and it
cannot continue without a number.

Examples
--------

Physical Coils
^^^^^^^^^^^^^^

This is how a coil should look:

.. code-block:: mpf-config

    coils:
      your_coil:
        number: 1

The actual number depends on your hardware platform.
See the :doc:`/hardware/numbers` guide for details.


Virtual Coils
^^^^^^^^^^^^^

Sometimes you did not wire up a coil but you know that you will need it later.
This is a problem for your physical hardware controller but you can tell MPF
to use the ``virtual`` hardware platform for one particular coil:

.. code-block:: mpf-config

    coils:
      your_virtual_coil:
        number:
        platform: virtual

In this case the number can be empty.

.. include:: config_error_footer.rst

Related How To guides
---------------------

* :doc:`/mechs/coils/index`
