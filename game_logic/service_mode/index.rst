Service Mode
============

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/settings`                                                      |
+------------------------------------------------------------------------------+

MPF has a build in service mode which can be extended using settings (or in
code). Usually you map your
:doc:`service switches and door switches </mechs/switches/service_and_door_switches>`
to control service mode. Additionally, you might want to add keys of your
:doc:`keyboard </config/keyboard>` during development.

This is an example:

.. code-block:: mpf-config

   # include service mode in your modes list
   modes:
       - service

   # add tags to your switches
   switches:
       s_door_open:
           number: 1
           tags: service_door_open, power_off
       s_service_enter:
           number: 17
           tags: service_enter
       s_service_esc:
           number: 18
           tags: service_esc
       s_service_up:
           number: 19
           tags: service_up
       s_service_down:
           number: 20
           tags: service_down

   # add a setting (not used here)
   settings:
      replay_score:
         label: Replay Score
         values:
            500000: "500000 (default)"
            1000000: "1000000"
            1500000: "1500000"
         default: 500000
         key_type: int
         sort: 100

   # add keyboard switches
   keyboard:
       right:
         switch: s_service_enter
       left:
         switch: s_service_esc
       up:
         switch: s_service_up
       down:
         switch: s_service_down
