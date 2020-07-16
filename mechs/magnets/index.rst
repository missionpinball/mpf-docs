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

.. image:: /mechs/images/magnet1.jpg
.. image:: /mechs/images/magnet2.jpg
.. image:: /mechs/images/magnet3.jpg


Config
------

This is an example:

.. code-block:: mpf-config

   coils:
     magnet_coil:
       number:
       default_pulse_ms: 100
       default_hold_power: 0.375

   switches:
     grab_switch:
       number:

   magnets:
     magnet:
       magnet_coil: magnet_coil
       grab_switch: grab_switch
       release_ball_events: magnet_release
       fling_ball_events: magnet_fling

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

:doc:`stern_magnet_pcb`

Related Events
--------------

.. include:: /events/include_magnets.rst

.. toctree::
   :titlesonly:

   stern_magnet_pcb
