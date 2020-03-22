switch_player:
==============

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``switch_player:`` section of your config is where you can replay a series
of switches for testing purposes.

This is an example:

.. code-block:: mpf-config

   #config_version=5
   switches:
     s_test1:
       number:
       x: 0.4
       y: 0.5
       z: 0
     s_test2:
       number:
       x: 0.6
       y: 0.7
     s_test3:
       number:
   plugins: switch_player
   switch_player:
     start_event: test_start
     steps:
       - time: 100ms
         switch: s_test1
         action: activate
       - time: 600ms
         switch: s_test3
         action: hit
       - time: 100ms
         switch: s_test1
         action: deactivate
       - time: 1s
         switch: s_test2
         action: activate
       - time: 1s
         switch: s_test3
         action: hit
       - time: 100ms
         switch: s_test2
         action: deactivate
       - time: 1s
         switch: s_test3
         action: hit

.. config


Optional settings
-----------------

The following sections are optional in the ``switch_player:`` section of your config. (If you don't include them, the default will be used).

start_event:
~~~~~~~~~~~~
Single value, type: ``string``. Default: ``machine_reset_phase_3``

Event to trigger the start of the switch player.

