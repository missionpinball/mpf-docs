How to configure switches (P3-ROC)
==================================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/switches`                                                      |
+------------------------------------------------------------------------------+

To configure switches on a P3-ROC, you can follow the guides and instructions
in the :doc:`/mechs/switches/index` docs.

However there are a few things to know about using switches with a P3-ROC.

number:
-------

Unlike the P-ROC, the P3-ROC does not have switch inputs on the P3-ROC itself.
Instead, you add SW-16 boards which each have 16 direct switch inputs. (e.g.
there is no switch matrix.) You can connect up to 16 SW-16s to support as many
as 256 switches.

To configure the ``number:`` of a switch connected to an SW-16 board and a
P3-ROC, you have two options.

The first (and easier) option is to enter the number as a combination of the
SW-16 board address (0-15, as configured by the DIP switches), then the bank
number (A=0, B=1), then the switch number (0-7).

For example:

.. code-block:: mpf-config

   switches:
      my_switch:
         number: 0/0/0  # SW-16 board at address 0, Bank A, Switch 0
      my_other_switch:
         number: 2/1/5  # SW-16 board at address 2, Bank B, Switch 5

Debounce options
----------------

The P-ROC has the ability to configure :doc:`debounce settings </mechs/switches/debounce>`
for switches. A non-debounced switch which report its state change immediately,
while a debounced switch will report its state change after it's been in the
new state for two consecutive reads.

By default, MPF will enable debouncing in both directions (open and close) for
all switches. However you can override this on a per-switch basis with a
switch's ``debounce:`` setting.

Valid options are ``normal``, ``quick``, and ``auto``.

To disable debouncing for a switch, add ``debounce: quick`` to the switch
config, like this:

.. code-block:: mpf-config

   switches:
      my_switch:
         number: 0/0/0
         debounce: quick

To force debouncing to always be used (which is also the default on the P-ROC,
so not really needed), configure it like this:

.. code-block:: mpf-config

   switches:
      my_switch:
         number: 0/0/0
         debounce: normal

