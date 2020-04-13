sound_player:
=============

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+

.. note:: This section can also be used in a show file in the ``sounds:`` section of a step.

.. overview

The ``sound_player:`` section of your config is where you specify actions to perform on sounds
when MPF events are received.

This is an example:

.. code-block:: mpf-config

    sound_player:
      mode_attract_started:
        song_01:
          action: play
          loops: -1
      mode_attract_stopped:
        song_01:
          action: stop

Additional information may be found in the
:doc:`sound_player </config_players/sound_player>` documentation.


Express configuration
---------------------

When referencing sounds in the sound player, there is an alternative syntax to specify a sound when
you don't wish to provide any additional settings.  This shortcut notation is known as the "express
configuration" and for the sound player it is simply the name of the sound asset.  It can be used in
both configuration files and show steps.  In the config file example above,
``play_sound_slingshot: slingshot_01`` is an example using the express configuration (sound name
only).

Sound behavior upon mode (or show) stop
---------------------------------------

When the mode or show stops that contains a ``sound_player``, all sounds started in that mode or
show will continue to play and stop automatically when they reach their end. Sounds that are
looping will have their looping stopped so the sound will no longer continue to loop and will stop
when they reach their end. Sounds that are pending playback and are queued will be canceled
(removed from the queue) and will not be played. If you need a sound to be stopped immediately
when a mode or show ends, you will need to add an entry in the ``sound_player`` to trigger a stop
action based on the mode or show stop event.

.. config


Optional settings
-----------------

The following sections are optional in the ``sound_player:`` section of your config. (If you don't include them, the default will be used).

about_to_finish_time:
~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``time string (secs)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`). Default: ``-1``

.. todo:: :doc:`/about/help_us_to_write_it`

action:
~~~~~~~
Single value, type: one of the following options: play, stop, stop_looping, load, unload. Default: ``play``

The ``action:`` setting controls what action will be performed on the specified sound. Options for
``action:`` are:

+ ``play`` - The specified sound will be played.  Any optional parameter values will override the
  sound's settings.
+ ``stop`` - All currently playing and queued instances of the specified sound will stopped/canceled.
  Any optional parameter values will be ignored as the stop action takes no parameters.  There is
  currently no way to stop specific instances of a particular sound while leaving others playing,
  but that is on the list to be implemented in a future version.
+ ``stop_looping`` - Looping will be canceled for all currently playing instances of the specified
  sound (the sound will continue to play to the end of the current loop). In addition, any queued
  instances of the sound awaiting playback will be removed/canceled.
+ ``load`` - Loads the specified sound or sound pool from its source file into memory to prepare it
  to be played.  The request is ignored if the sound is already loaded.
+ ``unload`` - Unloads the specified sound or sound pool from memory.  All instances of the sound
  or sound pool will be immediately stopped. The request is ignored if the sound is not currently
  loaded.

events_when_about_to_finish:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
List of one (or more) events. Those will be posted by the device. Default: ``use_sound_setting``

Please refer to the :doc:`sounds: </config/sounds>` documentation for details
about this setting as it just overwrites the setting in your sound.

events_when_looping:
~~~~~~~~~~~~~~~~~~~~
List of one (or more) events. Those will be posted by the device. Default: ``use_sound_setting``

Please refer to the :doc:`sounds: </config/sounds>` documentation for details
about this setting as it just overwrites the setting in your sound.

events_when_played:
~~~~~~~~~~~~~~~~~~~
List of one (or more) events. Those will be posted by the device. Default: ``use_sound_setting``

Please refer to the :doc:`sounds: </config/sounds>` documentation for details
about this setting as it just overwrites the setting in your sound.

events_when_stopped:
~~~~~~~~~~~~~~~~~~~~
List of one (or more) events. Those will be posted by the device. Default: ``use_sound_setting``

Please refer to the :doc:`sounds: </config/sounds>` documentation for details
about this setting as it just overwrites the setting in your sound.

fade_in:
~~~~~~~~
Single value, type: ``time string (secs)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`). Defaults to empty.

Please refer to the :doc:`sounds: </config/sounds>` documentation for details
about this setting as it just overwrites the setting in your sound.

fade_out:
~~~~~~~~~
Single value, type: ``time string (secs)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`). Defaults to empty.

Please refer to the :doc:`sounds: </config/sounds>` documentation for details
about this setting as it just overwrites the setting in your sound.

key:
~~~~
Single value, type: ``string``. Default: ``use_sound_setting``

Used to reference this sound entry when stopping/pausing/resuming it.

loops:
~~~~~~
Single value, type: int_or_token. Defaults to empty.

Please refer to the :doc:`sounds: </config/sounds>` documentation for details
about this setting as it just overwrites the setting in your sound.

max_queue_time:
~~~~~~~~~~~~~~~
Single value, type: ``time string (secs)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`). Default: ``-1``

Please refer to the :doc:`sounds: </config/sounds>` documentation for details
about this setting as it just overwrites the setting in your sound.

mode_end_action:
~~~~~~~~~~~~~~~~
Single value, type: one of the following options: stop, stop_looping, use_sound_setting. Default: ``use_sound_setting``

Please refer to the :doc:`sounds: </config/sounds>` documentation for details
about this setting as it just overwrites the setting in your sound.

pan:
~~~~
Single value, type: float_or_token. Defaults to empty.

Please refer to the :doc:`sounds: </config/sounds>` documentation for details
about this setting as it just overwrites the setting in your sound.

priority:
~~~~~~~~~
Single value, type: int_or_token. Defaults to empty.

Please refer to the :doc:`sounds: </config/sounds>` documentation for details
about this setting as it just overwrites the setting in your sound.

start_at:
~~~~~~~~~
Single value, type: ``time string (secs)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`). Defaults to empty.

Please refer to the :doc:`sounds: </config/sounds>` documentation for details
about this setting as it just overwrites the setting in your sound.

track:
~~~~~~
Single value, type: ``string``. Defaults to empty.

Please refer to the :doc:`sounds: </config/sounds>` documentation for details
about this setting as it just overwrites the setting in your sound.

volume:
~~~~~~~
Single value, type: ``gain setting`` (-inf, db, or float between 0.0 and 1.0). Defaults to empty.

Please refer to the :doc:`sounds: </config/sounds>` documentation for details
about this setting as it just overwrites the setting in your sound.


Related How To guides
---------------------

* :doc:`/sound/index`
