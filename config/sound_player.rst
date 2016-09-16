sound_player:
=============

*Config file section*

.. include:: _machine_config_yes.rst
.. include:: _mode_config_yes.rst

.. note:: This section can also be used in a show file in the ``sounds:`` section of a step.

.. overview

The ``sound_player:`` section of your config is where you specify actions to perform on sounds
when MPF events are received.  Additional information may be found in the
:doc:`sound_player </config_players/sound_player>` documentation.

Optional settings
-----------------

The following sections are optional in the ``sound_player:`` section of your config. (If you don't include them, the default will be used).

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

+ ``loops:``
+ ``priority:``
+ ``max_queue_time:``
+ ``volume:``
+ ``fade_in:``
+ ``fade_out:``
+ ``start_at:``
+ ``events_when_played:``
+ ``events_when_stopped:``
+ ``events_when_looping:``

Express configuration
---------------------

When referencing sounds in the sound player, there is an alternative syntax to specify a sound when
you don't wish to provide any additional settings.  This shortcut notation is known as the "express
configuration" and for the sound player it is simply the name of the sound asset.  It can be used in
both configuration files and show steps.  In the config file example above,
``play_sound_slingshot: slingshot_01`` is an example using the express configuration (sound name
only).

