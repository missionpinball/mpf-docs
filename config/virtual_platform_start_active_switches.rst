virtual_platform_start_active_switches:
=======================================

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``virtual_platform_start_active_switches:`` section of your config is where
you define all switches which should start as active when running your machine
with the virtual or smart_virtual platform (e.g. when running ``mpf -X``).

This is an example:

.. code-block:: mpf-config

   switches:
     s_ball_switch1:
       number:
     s_ball_switch2:
       number:
     s_ball_switch3:
       number:
   # Start with two (virtual) balls
   virtual_platform_start_active_switches:
     - s_ball_switch1
     - s_ball_switch2

.. config


Related How To guides
---------------------

* :doc:`/hardware/virtual/index`
* :doc:`/mechs/troughs/index`
