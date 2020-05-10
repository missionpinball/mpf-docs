Arduino Pinball Controller
==========================

MPF can control System6 to System11c machines directly using the Arduino
Pinball Controller (APC).
It contains CPU and drivers so it can also be used to build full custom
machines.
Uses the :doc:`LISY protocol </hardware/lisy/protocol>`.

This is how APC generally works: https://www.youtube.com/watch?v=w4Po8OE5Zkw

See `Arduino Pinball Controller Documentation <https://github.com/AmokSolderer/APC>`_
on github for details.

This is an example config:

.. code-block:: mpf-config

   #config_version=5
   hardware:
     platform: lisy
   lisy:
     connection: serial
     port: com1      # change this for your setup
     baud: 115200
   digital_outputs:
     game_over_relay:
       number: 1
       type: light
       enable_events: ball_started
       disable_events: ball_will_end
   segment_displays:
     info_display:
       number: 0
     player1_display:
       number: 1
     player2_display:
       number: 2
     player3_display:
       number: 3
     player4_display:
       number: 4
   hardware_sound_systems:
     default:
       label: APC


See the :doc:`LISY platform </hardware/lisy/index>` for more details on
configuring hardware.


.. toctree::
   :titlesonly:

   connection
