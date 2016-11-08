Sound player
============

The *sound player* is a :doc:`config player </config_players/index>` that's used to control
sounds. (This player is part of the MPF media controller and only available if you're using MPF-MC
for your media controller.)

Usage in config files
---------------------

In config files, the sound player is used via the ``sound_player:`` section.  Event names that
will trigger sound actions are nested sub-headings and sound names are either listed as nested
sub-headings below that.

Example:

::

    sound_player:
        play_sound_slingshot: slingshot_01
        play_sound_weird_sfx:
            weird_sfx_pool:
                loops: 3
                priority: 100
                volume: 0.75
        play_sound_extra_ball: extra_ball
        stop_sound_extra_ball:
            extra_ball:
                action: stop

Usage in shows
--------------

In shows, the sound player is used via the ``sounds:`` section of a step.

Example:

::

    shows:
        my_show_with_sound:
            - time: 0
                sounds:
                    weird_sfx_pool:
                        loops: 2
                        volume: 0.5
                    tick_tock:
                        volume: 0.6
            - time: 3.5
                sounds:
                    explosion:
                        volume: 0.8

Optional settings
-----------------

action:
~~~~~~~
Single value, type: one of the following options: play, stop. Default: ``play``

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

Other available optional settings:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Several other settings may be used in the sound player to override settings specified in the
``sounds:`` section of config files.  Please refer to the :doc:`sounds: </config/sounds>`
documentation for details about each setting.

+ ``priority:``
+ ``loops:``
+ ``volume:``
+ ``max_queue_time:``

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

