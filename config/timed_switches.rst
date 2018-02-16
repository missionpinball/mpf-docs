timed_switches:
===============

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. versionadded:: 0.33

Specifies :doc:`timed switches </game_logic/timed_switches/index>` which are used to
post events when a switch is active for a continuous amount of time.

Here's an example. This example is actually built-in to MPF via the MPF default config
file, so if you want to use these flipper cradle events, you don't have to enter them
yourself as they're already there.

.. code-block:: yaml

   timed_switches:
     flipper_cradle:
       switch_tags: left_flipper, right_flipper
       time: 3s
       events_when_active: flipper_cradle
       events_when_released: flipper_cradle_release

Like other devices in MPF, the format is:

.. code-block:: yaml

   timed_switches:
      name_of_your_timed_switch:
         <settings>
      some_other_timed_switch:
         <settings>

Settings
--------

The following settings can be used in each named timed switch section:

switches:
~~~~~~~~~

A list of switches (or a single switch) that will be used for these timed switch
settings. Note that you can use ``switch_tags:`` instead of ``switches:``.

switch_tags:
~~~~~~~~~~~~

A list of switch tags (or a single tag) that will be used to set which switches are
used with these timed switch settings. Each switch with these tags will be added.

time: (required)
~~~~~~~~~~~~~~~~
Single value, type: ``time string`` (:doc:`Instructions for entering time strings) </config/instructions/time_strings>`.

How long a switch must be continuously active before the ``events_when_active`` are posted.

state:
~~~~~~
Single value, either ``active`` or ``inactive``. Default is ``active``.

Controls whether the ``events_when_active:`` are posted when the switch is active for
the ``time:`` amount, or whether it's flipped and the events are posted when the switch
is ``inactive`` for the time amount.

events_when_active:
~~~~~~~~~~~~~~~~~~~
A single event, or list of events, that's posted once a switch is continuously active for
the ``time:`` setting. If you have multiple switches. this event will only be posted once,
even if a second switch becomes active for that time while the first is still active.

If you don't enter any events here, an event will automatically be posted in the format
*<name_of_this_timed_switch>_active*. In other words, in the example at the top of this
page, the timed switch entry is called "flipper_cradle", so the automatically-created
event would be called *flipper_cradle_active*, but since that config has an
``events_when_active: flipper_cradle`` entry, then the event will just be
*flipper_cradle*.

events_when_released:
~~~~~~~~~~~~~~~~~~~~~
A single event, or list of events, that will be posted when a timed switch is released.
Unlike the active events which are only posted when the switch is continuously active
for that period of time, the released events are posted immediately.

If you've defined multiple switches and two switches go active, the release event will
not be posted until all the switches are released.
