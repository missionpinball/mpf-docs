combo_switches:
===============

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+

.. overview

The ``combo_switches:`` section of your config is where you configure
:doc:`combo switches </game_logic/combo_switches/index>` which are used for
things like "flipper cancel" or super skill shots where the player holds in
one flipper button while hitting the launch button.

Here's an example machine config file using them:

.. literalinclude:: /mpf_examples/combo_switches/config/combo_switches.yaml
   :language: yaml

To use combo switches, add a ``combo_switches:`` section to either a mode or
machine config. Then create subsections for each combo you want to use. (A
switch can be part of more than one combo.)

The name of each combo doesn't really matter, though it's used to construct
the events that are posted by this combo unless you override them.

Note about switch and tag "groups"
----------------------------------

MPF's combo switches are meant to be used in pairs of two. (We figure that
players only have two hands, so it doesn't really make sense to do combos that
require three buttons to be pushed at once. Though if you want that then you
can write some custom code for it.)

Usually combos would just be two switches. ``left_flipper + right_flipper`` or
``left_flipper + launch_button``. However to give the most flexibility, you can
enter your switches using either tags or switch names. It doesn't matter which
you use (and you can mix-and-match if you want), the main thing is for the
combo to work, you need to have at least one switch in the "1" side and one
switch on the "2" side.

Note that if you have more than one switch in either group (either by specifying
multiple switches for the switch config, or by using a tag that's applied to
multiple switches, or both), then the combo will become active when *any*
switch from either group is active. (This can be useful if you have two-stage
flipper buttons where a half-push of the button controls the bottom flipper and
a full push controls the top flipper. In that case you technically have two
switches per flipper button and you can add both to each group in your combo.)

.. config


Optional settings
-----------------

The following sections are optional in the ``combo_switches:`` section of your config. (If you don't include them, the default will be used).

events_when_both:
~~~~~~~~~~~~~~~~~
List of one (or more) events. Those will be posted by the device. Defaults to empty.

This is an event (or a list of events) that will be posted when both switches
are held in. If you have a ``max_offset_time:`` configured, then both switches
will need to have been pressed within that time. If you have a ``hold_time:``
configured, then both switches will need to be active for at least that long
before this event (or these events) are posted.

If the player pushes both switches, then releases one, then pushes in the
switch that was released again, this event will be re-posted.

If you don't set this value, then a default event with the name of your
combo plus ``_both`` will be used.

events_when_inactive:
~~~~~~~~~~~~~~~~~~~~~
List of one (or more) events. Those will be posted by the device. Defaults to empty.

This is an event (or list of events) that will be posted when the player
releases both of the buttons, essentially "releasing" the combo.

If you don't set this value, then a default event with the name of your
combo plus ``_inactive`` will be used.

events_when_one:
~~~~~~~~~~~~~~~~
List of one (or more) events. Those will be posted by the device. Defaults to empty.

This is an event (or list of events) that will be posted when the player
releases one switch after both switches have been pressed together. (In other
words, this event will only be posted after the ``events_when_both`` event
is posted.)

If you don't set this value, then a default event with the name of your
combo plus ``_one`` will be used.

events_when_switches_1:
~~~~~~~~~~~~~~~~~~~~~~~
List of one (or more) events. Those will be posted by the device. Defaults to empty.

This is event (or list of events) will be posted when only switches from
``switches_1`` were active for ``max_offset_time``.

events_when_switches_2:
~~~~~~~~~~~~~~~~~~~~~~~
List of one (or more) events. Those will be posted by the device. Defaults to empty.

This is event (or list of events) will be posted when only switches from
``switches_2`` were active for ``max_offset_time``.

hold_time:
~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`). Default: ``0``

How long each button has to be pressed in order for it to count as a combo.
The default is ``0`` which means that as soon as both switches are active, the
combo is active.

If you set ``hold_time: 1s``, that means that the player will have to press and
hold both buttons for 1 second before the combo's "both" event is posted.

max_offset_time:
~~~~~~~~~~~~~~~~
Single value, type: ``time string (secs)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`). Default: ``-1``

Specifies a time window that a switch from group 1 and group 2 have to be hit
within in order to register as a combo.

The default value of ``-1`` means there is no time limit, meaning that the
player can hit and hold one button, and then five minutes later hit the next
button, and the combo will count.

If you set ``max_offset_time: 1s``, that means that the player will have to
hit (and hold) both switches within 1 second of each other.

release_time:
~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`). Default: ``0``

How long a button has to be released before the combo will switch from "both"
state to the "one" state. The default is ``0`` which means this is instant.

Note that once both buttons are released, the combo is cleared. This setting
only affects the scenario when one button is held in while the other is
released.

switches_1:
~~~~~~~~~~~
List of one (or more) values, each is a type: string name of a :doc:`switches <switches>` device. Defaults to empty.

A switch name (or a list of switches) that will be used for the group 1 of the
combo. You can use this setting or the ``tag_1:`` setting above.

switches_2:
~~~~~~~~~~~
List of one (or more) values, each is a type: string name of a :doc:`switches <switches>` device. Defaults to empty.

A switch name (or a list of switches) that will be used for the group 1 of the
combo. You can use this setting or the ``tag_2:`` setting above.

tag_1:
~~~~~~
List of one (or more) values, each is a type: ``string``. Defaults to empty.

A tag (or list of tags) of switches (in the ``switches:`` section of your
machine config that will be used for switches for group 1 of the combo. You
can either use a tag, or use the ``switches_1:`` setting (or both, really).

tag_2:
~~~~~~
List of one (or more) values, each is a type: ``string``. Defaults to empty.

A tag (or list of tags) of switches (in the ``switches:`` section of your
machine config that will be used for switches for group 2 of the combo. You
can either use a tag, or use the ``switches_2:`` setting (or both).

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

* :doc:`/game_logic/combo_switches/index`
