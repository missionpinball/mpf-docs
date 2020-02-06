hardware_sound_player:
======================

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+

.. note:: This section can also be used in a show file in the ``hardwares:`` section of a step.

.. overview

The ``hardware_sound_player:`` section of your config is where you can control external sound modules (e.g. in LISY).

This is an example:

.. code-block:: mpf-config

   hardware_sound_systems:
     default:
       label: Default external sound system
   hardware_sound_player:
     event_posted_elsewhere1:
       2:
         action: play
     ball_started:
       3: play
     test_stop: stop

Optional settings
-----------------

The following sections are optional in the ``hardware_sound_player:`` section of your config. (If you don't include them, the default will be used).

action:
~~~~~~~
Single value, type: one of the following options: play, stop. Default: ``play``

``play`` will play a sound. Depending on the hardware this might stop previous sounds.
Also loop behaviour depends on the hardware and might be different per sound.

``stop`` will stop all sounds.

sound:
~~~~~~
Single value, type: ``integer``. Default: ``None``

The number of your sound.

sound_system:
~~~~~~~~~~~~~
Single value, type: string name of a ``hardware_sound_systems:`` device. Default: ``default``

In case you got multiple hardware_sound platforms you can expliticly select one here.


