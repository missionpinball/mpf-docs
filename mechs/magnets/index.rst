Magnets
=======

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/magnets`                                                       |
+------------------------------------------------------------------------------+


.. contents::
   :local:

MPF supports the ability to control precise timing for magnets which you can
use to grab and release balls. It also includes the ability to set timings to
"fling" a ball by grabbing, releasing, then pulsing the magnet again.

Monitorable Properties
----------------------

For :doc:`dynamic values </config/instructions/dynamic_values>` and
:doc:`conditional events </events/overview/conditional>`,
the prefix for magnets is ``device.magnets.<name>``.

*active*
   Boolean (true/false) as to whether this magnet is actively on and
   in the powered state.

*enabled*
   Boolean (true/false) which shows whether this ball hold is enabled.

Related How To guides
---------------------

.. todo:: TODO

Related Events
--------------

* :doc:`/events/magnet_name_flinged_ball`
* :doc:`/events/magnet_name_flinging_ball`
* :doc:`/events/magnet_name_grabbed_ball`
* :doc:`/events/magnet_name_grabbing_ball`
* :doc:`/events/magnet_name_released_ball`
* :doc:`/events/magnet_name_releasing_ball`
