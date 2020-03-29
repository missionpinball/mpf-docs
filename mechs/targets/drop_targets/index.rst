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

Mission Pinball Framework's (MPF) *drop target* device represents a switch in a pinball machine.
This device is used for drop target banks with a coil for resetting.
If the reset coil resets more than just this one drop target configure all
targets as a :doc:`drop target bank <drop_target_bank>` and put the coil there.
Additionally, there may be a knockdown coil which allows the software to knock the
target down.

.. image:: /mechs/images/drop_target_front.jpg
.. image:: /mechs/images/drop_target_side.jpg
.. image:: /mechs/images/drop_target_back.jpg

This is an example:

.. code-block:: mpf-config

   switches:
     s_drop_target:
       number:
   coils:
     c_reset_drop_target:
       number:
     c_knock_down_coil:
       number:
   drop_targets:
     d_drop_target:
       switch: s_drop_target
       reset_coil: c_reset_drop_target
       knockdown_coil: c_knock_down_coil

Monitorable Properties
----------------------

For :doc:`dynamic values </config/instructions/dynamic_values>` and
:doc:`conditional events </events/overview/conditional>`,
the prefix for drop targets is ``device.drop_targets.<name>``.

*complete*
   Boolean (true/false) which shows whether this drop target is complete (down).

Related How To guides
---------------------

* :doc:`drop_target_bank`
* :doc:`fixing_drop_target_reset_issues`

Related Events
--------------

.. include:: /events/include_drop_targets.rst

.. toctree::

   drop_target_bank
   fixing_drop_target_reset_issues
