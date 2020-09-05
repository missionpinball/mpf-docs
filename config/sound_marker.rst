sound_marker:
=============

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **NO**  |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``markers:`` setting in your ``sounds:`` section of your config is where
you configure markers which trigger events at certain points in playback.

.. config


Required settings
-----------------

The following sections are required in the ``sound_marker:`` section of your config:

events:
~~~~~~~
List of one (or more) events.

A list of one or more names of events that MPF will post when this marker is reached during sound
playback. Enter the list in the MPF config list format. These events are posted exactly as they’re
entered.

time:
~~~~~
Single value, type: ``time string (secs)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`).

The marker time (in seconds) relative to the beginning of the sound file.


Related How To guides
---------------------

* :doc:`/sound/index`
