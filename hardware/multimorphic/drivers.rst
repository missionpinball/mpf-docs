How to configure coils/drivers/magnets (P-ROC/P3-ROC)
=====================================================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/coils`                                                         |
+------------------------------------------------------------------------------+

To configure coils, drivers, motors, and/or magnets (basically anything
connected to PD-16 board's driver outputs) with P-ROC/P3-ROC hardware, you can
follow the guides and instructions in the :doc:`/mechs/coils/index` docs.

(If you're using a P-ROC with an existing machine's driver board, like a WPC
machine, then see the existing machine documentation. Link TODO)

The only specific thing you have to know for this platform is the number format:

number:
-------

For PD-16-based devices, the numbering format is:

::

   number: Ax-By-z

The “A” and “B” capital letters are required. (A means Address, B means Bank).
The lowercase x, y, and z letters should be replaced with numbers to represent
the following on a PD-16 driver board:

* x : Board address (0-31)
* y : Bank address (0 for A, 1 for B)
* z : Output number (0-7)

.. note::

   The output number is the logical number, *not* the pin number. For example, Output 0 is on Pin 1, and there is a key
   pin at 2 or 3. Check the manual for the exact mapping.

For example:

.. code-block:: mpf-config

   coils:
      some_coil:
         number: A0-B1-6
         default_pulse_ms: 30
