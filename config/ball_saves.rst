ball_saves:
===========

*Config file section*

.. include:: _machine_config_yes.rst
.. include:: _mode_config_yes.rst

.. overview

The ``ball_saves:`` section of your config is where you create `ball save devices`.
Here's an example:

::

    ball_saves:
      default:
        active_time: 10s
        hurry_up_time: 2s
        grace_period: 2s
        enable_events: mode_base_started
        timer_start_events: balldevice_plunger_lane_ball_eject_success
        auto_launch: yes
        balls_to_save: 1
        debug: yes

<name>:
~~~~~~~

The name of this ball save device. (This is "default" in the config
snippet above.) The name is used in the events that are posted from
this ball save. (The complete list of events posted by ball saves is
included in the events reference.)

Optional settings
-----------------

The following sections are optional in the ``ball_saves:`` section of your config. (If you don't include them, the default will be used).

active_time:
~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings) </config/instructions/time_strings>` . Default: ``0``

How long the ball save is active (in `MPF time string format`_) once
it starts counting down. This includes the *hurry_up_time,* but does
not include the *grace_period* time. Leave this setting out (or set it
to 0) for unlimited time. Default is *0*.

auto_launch:
~~~~~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``True``

True/False which controls whether the ball save should auto launch the
saved ball or wait for the player to launch it.

balls_to_save:
~~~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``1``

How many balls this ball saver should save before disabling itself.
Set it to -1 for unlimited.

debug:
~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

.. todo::
   Add description.

disable_events:
~~~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``ms``. Default: ``ball_ending``

.. todo::
   Add description.

enable_events:
~~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``ms``. Default: ``None``

.. todo::
   Add description.

grace_period:
~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings) </config/instructions/time_strings>` . Default: ``0``

The “secret” time (in `MPF time string format`_) the ball save is
still active. This is added onto the *active_time*. Default is *0*.

hurry_up_time:
~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings) </config/instructions/time_strings>` . Default: ``0``

The time before the ball save ends (in `MPF time string format`_) that
will cause the *ball_save_<name>_hurry_up* event to be posted. Use
this to change the script for the light or trigger other effect.
Default is *0*.

label:
~~~~~~
Single value, type: ``string``. Default: ``%``

.. todo::
   Add description.

source_playfield:
~~~~~~~~~~~~~~~~~
Single value, type: string name of a ``ball_devices:`` device. Default: ``playfield``

.. todo::
   Add description.

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

.. todo::
   Add description.

timer_start_events:
~~~~~~~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``ms``. Default: ``None``

An optional event (or list of events) in `MPF control event format`_
which starts this ball saver's countdown timer. Default is *None*.


