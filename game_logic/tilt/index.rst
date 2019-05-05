Tilt
====

Tilt is a built-in mode.
To enable it, just add the ``tilt`` mode to your machine config list of modes.
Additionally, add the ``tilt_warning`` tag to your
:doc:`tilt bob switch </mechs/tilt_bob/index>` and the ``slam_tilt`` to your
slam tilt switch.
Tilt runs at all times, since the machine has to look for slam tilts while
games are not running.

The tilt mode contains three logic paths:

* Slam tilt (slam_tilt)
* Instant tilt (tilt)
* Tilt warnings (tilt_warning)

You can provide a switch tag or list events for each of them.
Let us go over all of them quickly:

The slam tilt is usually triggered by the slam tilt switch at the coin
door.
It clears all credits and ends the current game.

The *normal* tilt is usually triggered by a
:doc:`tilt bob switch </mechs/tilt_bob/index>`.
It will give ``warnings_to_tilt`` warnings until it ends the current ball.
The remaining warnings are reset by the ``reset_warnings_events`` events.
By default they are reset on ball end but you can also change it to game end.
The warnings count is stored in the player variable configured in
``tilt_warnings_player_var`` (which defaults to ``tilt_warnings``) and you can
mess with them using :doc:`/config_players/variable_player` if you like.

Instant tilt is rarely used in normal machines but it might be useful for
custom tilt logic or special modes.

Minimal config
--------------

The minimal example is to just load the default ``tilt`` mode:

.. code-block:: mpf-config

   modes:
      - tilt

Change defaults
---------------

If you want to customize the mode you can also create a tilt mode inside your
mode folder (config would be in ``modes/tilt/config/tilt.yaml``):

.. code-block:: mpf-config

   # in your machine config
   modes:
      - tilt

   ##! mode: tilt
   # in your tilt mode
   tilt:    # the following are the defaults only copy those if you want to change them
     multiple_hit_window: 300ms
     settle_time: 5s
     warnings_to_tilt: 3

Add operator settings to service mode
-------------------------------------

.. code-block:: mpf-config

   # in your machine config
   modes:
      - tilt

   settings:
     warnings_to_tilt:
        label: Number of tilt warnings
        values:
           0: "no warnings"
           1: "1"
           2: "2"
           3: "3"
           5: "5"
           10: "10"
        default: 3
        key_type: int
        sort: 600
     settle_time:
        label: Time to wait on tilt to settle bob
        values:
           3000: "3s"
           5000: "5s"
           10000: "10s"
        default: 5000
        key_type: int
        sort: 610
     multiple_hit_window:
        label: Tilt sensitivity
        values:
           150: "sensitive"
           300: "normal"
           500: "insensitive"
           1000: "very insensitive"
        default: 300
        key_type: int
        sort: 620

   ##! mode: tilt
   # in your tilt mode
   tilt:
     multiple_hit_window: settings.multiple_hit_window
     settle_time: settings.settle_time
     warnings_to_tilt: settings.warnings_to_tilt

The tilt modes contains default slides but you can
:doc:`change them <overwrite_tilt_slides>`.

+------------------------------------------------------------------------------+
| Related How To guides                                                        |
+==============================================================================+
| :doc:`/game_design/index`                                                    |
+------------------------------------------------------------------------------+
| :doc:`overwrite_tilt_slides`                                                 |
+------------------------------------------------------------------------------+

.. toctree::
   :hidden:

   overwrite_tilt_slides
