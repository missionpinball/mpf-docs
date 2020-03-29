event_player:
=============

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+

.. note:: This section can also be used in a show file in the ``events:`` section of a step.

.. overview

You can use the ``event_player:`` section of your config files to cause
additional events to be automatically posted when a specific event is
posted. The event_player can be thought of as a really simple way to
implement game logic. (e.g. "When this happens, do this.")

If you add
this section to your machine-wide config file, the entries here will
always be active. If you enter it into a mode-specific config file,
entries will only be active while that mode is active.

This is an example:

.. code-block:: mpf-config

    event_player:
      ball_starting:
        - show_ball_start_animation
        - play_start_sound
        - start_first_mode
      ball_ending:
        - show_ball_ending_animation
        - play_drain_sound

See :doc:`/config_players/event_player` for details.

.. config


Related How To guides
---------------------

* :doc:`/config_players/event_player`
