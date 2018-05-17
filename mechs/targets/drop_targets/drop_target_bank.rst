Drop Target Bank
================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/drop_target_banks`                                             |
+------------------------------------------------------------------------------+

.. contents::
   :local:

In MPF, you can combine multiple drop targets into drop target
banks. The main reasons for doing this are to combine reset
coils (since one coil typically resets an entire bank) and to
get additional events posted when the entire bank is up, down
or in a mixed state.

Monitorable Properties
----------------------

For :doc:`dynamic values </config/instructions/dynamic_values>` and
:doc:`conditional events </events/overview/conditional>`,
the prefix for drop target banks is ``device.drop_target_banks.<name>``.

*complete*
   Boolean (true/false) which shows whether every target in this bank is complete (down).

*down*
   Number of drop targets in the bank that are in the down state.

*up*
   Number of drop targets in the bank that are in the up state.

Related How To guides
---------------------

* :doc:`index`

Related Events
--------------

* :doc:`/events/drop_target_bank_name_down`
* :doc:`/events/drop_target_bank_name_up`
* :doc:`/events/drop_target_bank_name_mixed`
