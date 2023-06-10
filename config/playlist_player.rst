playlist_player:
================

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+

.. note:: This section can also be used in a show file in the ``playlists:`` section of a step.

.. overview

The ``playlist_player:`` section of your config is where you specify actions to perform on playlists
when MPF events are received.  Additional information may be found in the
:doc:`playlist_player </config_players/playlist_player>` documentation.

Examples:

.. code-block:: mpf-config

   playlist_player:
     play_attract_music:
       playlist:
         playlist: attract_music
         action: play
     advance_playlist:
       playlist:
         action: advance
     stop_playlist:
       playlist:
         action: stop

Basic usage:

.. code-block:: yaml

   playlist_player:
     <triggering_event_name>:
       <playlist track name>:
         action: <action name>
         <optional settings>
     <triggering_event_name>:
       <playlist track name>:
         action: <action name>
         <optional settings>

.. config


Optional settings
-----------------

The following sections are optional in the ``playlist_player:`` section of your config. (If you don't include them, the default will be used).

action:
~~~~~~~
Single value, type: one of the following options: play, stop, advance, set_repeat. Default: ``play``

.. todo:: :doc:`/about/help_us_to_write_it`


Related How To guides
---------------------

.. todo:: :doc:`/about/help_us_to_write_it`
