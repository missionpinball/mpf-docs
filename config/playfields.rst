playfields:
===========

.. include:: /not_updated_yet.rst

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``playfields:`` section of your config is where you configure your playfields in your machine.
You can have multiple playfields and MPF will track balls per playfield.
One playfield should contain the tag `default` so that the game knows which playfield to use.

Optional settings
-----------------

The following sections are optional in the ``playfields:`` section of your config. (If you don't include them, the default will be used).

ball_search_failed_action:
~~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``new_ball``

When ball search failed this action is taken. Either ``new_ball`` which will
eject a new ball from the default default source device or ``end_game`` which
will end the game.

ball_search_interval:
~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings) </config/instructions/time_strings>` . Default: ``150ms``

The delay after each fired coil/searched device.

ball_search_phase_1_searches:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``3``

Ball search will run in multiple phases with increasing intensity.
For instance, in phase 1, only ball devices without a ball will be pulsed.
This defines how many time phase 1 is repeated until ball_search proceeds to phase 2.

ball_search_phase_2_searches:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``3``

Ball search will run in multiple phases with increasing intensity.
For instance, in phase 2, all ball devices except the trough will try to dejam.
This defines how many time phase 2 is repeated until ball_search proceeds to phase 3.

ball_search_phase_3_searches:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``4``

Ball search will run in multiple phases with increasing intensity.
For instance, in phase 3, all ball devices except the trough pulse their coil.
This defines how many time phase 3 is repeated until ball search gives up.

ball_search_timeout:
~~~~~~~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings) </config/instructions/time_strings>` . Default: ``15s``

`ball_search_timeout` configures the time of inactivity which has to pass until ball search starts.

ball_search_wait_after_iteration:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings) </config/instructions/time_strings>` . Default: ``5s``

Extra delay after each iteration.

ball_search_block_events:
~~~~~~~~~~~~~~~~~~~~~~~~~
Default: ``flipper_cradle``

Event to block ball search. Used by flipper cradle.

ball_search_unblock_events:
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Default: ``flipper_cradle_release``

Event to unblock ball search. Used by flipper cradle.

ball_search_enable_events:
~~~~~~~~~~~~~~~~~~~~~~~~~~
Default: None

Event to enable ball search.

ball_search_disable_events:
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Default: None

Event to disable ball search.

debug:
~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

Turn on/off debugging.

default_source_device:
~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``BallDevice``. Default: ``None``

The source ball device to use to feed balls to this playfield.
This source device must be able to eject directly to the playfield.
Usually this is your launcher ball device.
If you do not have a launcher use the trough device.

enable_ball_search:
~~~~~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``None``

Enable ball_search by default. Use with care during development
since coils may hurt you. Should be enabled in any production
machine.

label:
~~~~~~
Single value, type: ``string``. Default: ``%``

Label for service menu.

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

Set tag `default` to your default playfield. The game will use
the default playfield to eject balls.

