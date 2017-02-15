Drop Targets
============

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/drop_targets`                                                  |
+------------------------------------------------------------------------------+
| :doc:`/config/drop_target_banks`                                             |
+------------------------------------------------------------------------------+

.. contents::
   :local:

Mission Pinball Framework's (MPF) *drop target* device represents a switch in a pinball machine. This device is
used for drop target banks with a coil for resetting.

Monitorable Properties
----------------------

For :doc:`config placeholders </config/instructions/placeholders>` and
:doc:`conditional events </events/overview/conditional>`,
the prefix for drop targets is ``device.drop_targets.<name>``.

*complete*
   Boolean (true/false) which shows whether this drop target is complete (down).

Related How To guides
---------------------

.. todo:: TODO

Related Events
--------------

* :doc:`/events/drop_target_name_down`
* :doc:`/events/drop_target_name_up`

.. toctree::

   drop_target_bank
