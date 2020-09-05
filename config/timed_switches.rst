timed_switches:
===============

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+

.. overview

Specifies :doc:`timed switches </game_logic/timed_switches/index>` which are used to
post events when a switch is active for a continuous amount of time.

Here's an example. This example is actually built-in to MPF via the MPF default config
file, so if you want to use these flipper cradle events, you don't have to enter them
yourself as they're already there.

.. code-block:: mpf-config

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

.. config


Required settings
-----------------

The following sections are required in the ``timed_switches:`` section of your config:

time:
~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`). Defaults to empty.

How long a switch must be continuously active before the ``events_when_active`` are posted.


Optional settings
-----------------

The following sections are optional in the ``timed_switches:`` section of your config. (If you don't include them, the default will be used).

events_when_active:
~~~~~~~~~~~~~~~~~~~
List of one (or more) events. Those will be posted by the device. Defaults to empty.

If you don't enter any events here, an event will automatically be posted in the format
*<name_of_this_timed_switch>_active*. In other words, in the example at the top of this
page, the timed switch entry is called "flipper_cradle", so the automatically-created
event would be called *flipper_cradle_active*, but since that config has an
``events_when_active: flipper_cradle`` entry, then the event will just be
*flipper_cradle*.

events_when_released:
~~~~~~~~~~~~~~~~~~~~~
List of one (or more) events. Those will be posted by the device. Defaults to empty.

If you've defined multiple switches and two switches go active, the release event will
not be posted until all the switches are released.

state:
~~~~~~
Single value, type: one of the following options: active, inactive. Default: ``active``

Controls whether the ``events_when_active:`` are posted when the switch is active for
the ``time:`` amount, or whether it's flipped and the events are posted when the switch
is ``inactive`` for the time amount.

switch_tags:
~~~~~~~~~~~~
List of one (or more) values, each is a type: ``string``. Defaults to empty.

A list of switch tags (or a single tag) that will be used to set which switches are
used with these timed switch settings. Each switch with these tags will be added.

switches:
~~~~~~~~~
List of one (or more) values, each is a type: string name of a :doc:`switches <switches>` device. Defaults to empty.

A list of switches (or a single switch) that will be used for these timed switch
settings. Note that you can use ``switch_tags:`` instead of ``switches:``.

console_log:
~~~~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``basic``

Log level for the console log for this device.

debug:
~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

Set this to true to see additional debug output. This might impact the performance of MPF.

file_log:
~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``basic``

Log level for the file log for this device.

label:
~~~~~~
Single value, type: ``string``. Default: ``%``

Name of this device in service mode.

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Defaults to empty.

Not used.


Related How To guides
---------------------

* :doc:`/game_logic/timed_switches/index`
