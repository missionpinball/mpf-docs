hardware_sound_player:
======================

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+

.. note:: This section can also be used in a show file in the ``hardware_sounds:`` section of a step.

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

.. config


Optional settings
-----------------

The following sections are optional in the ``hardware_sound_player:`` section of your config. (If you don't include them, the default will be used).

action:
~~~~~~~
Single value, type: one of the following options: play, play_file, text_to_speech, set_volume, increase_volume, decrease_volume, stop. Default: ``play``

``play`` will play a sound. Depending on the hardware this might stop previous sounds.
Also loop behaviour depends on the hardware and might be different per sound.

``stop`` will stop all sounds.

platform_options:
~~~~~~~~~~~~~~~~~
Single value, type: dict. Defaults to empty.

.. todo:: :doc:`/about/help_us_to_write_it`

sound_system:
~~~~~~~~~~~~~
Single value, type: string name of a :doc:`hardware_sound_systems <hardware_sound_systems>` device. Default: ``default``

In case you got multiple hardware_sound platforms you can expliticly select one here.

track:
~~~~~~
Single value, type: ``integer``. Default: ``1``

The track number to play this sound on.
What this means depends on your hardware.
Usually, there are one or two tracks.

value:
~~~~~~
Single value, type: ``string``. Defaults to empty.

The number of your sound.


Related How To guides
---------------------

* :doc:`/hardware/apc/index`
* :doc:`/hardware/lisy/index`
