track_player:
=============

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+

.. versionadded:: 0.32

TODO (the following is a dump of notes that have to be incorporated)

New 'track_player' config player to control individual audio tracks with events.  Using '__all__' applies the action to
all tracks. Supported actions:

* 'play' - Play the track after is has been stopped or paused (with optional timed fade in).
* 'stop' - Stop the track (with optional timed fade out).  All sound processing on the track is stopped and the track is cleared.  All playing and queued sounds are canceled. All sound requests will be discarded while the track is stopped.
* 'pause' - Pause the track (with optional timed fade out).  All sound processing on the track is paused.  The track will pick-up where it left off when resumed.  All sound requests will be discarded while the track is stopped.
* 'set_volume' - Set a new volume level for the track (with optional timed fade from current volume)
* 'stop_all_sounds' - Stops all sounds on the track (with optional time fade out).  Track continues to process new requests.

action: (required)
------------------
single|enum(play,stop,pause,set_volume,stop_all_sounds)|

TODO

volume:
-------
single|gain|None

TODO

fade:
-----
single|secs|0.1sec

TODO
