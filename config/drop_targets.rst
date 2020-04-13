drop_targets:
=============

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

You configure individual *drop targets* in your machine in the
``drop_targets:`` section of your machine config file. (This section is
only used for individual targets. Once you configure them here, then
you group them into banks in the ``drop_target_banks:`` section.)
Here's an example from *Judge Dredd*, with five drop targets we've given names
*J*, *U*, *D*, *G*, and *E*.

.. code-block:: mpf-config

   #! switches:
   #!   drop_target_j:
   #!     number:
   #!   drop_target_u:
   #!     number:
   #!   drop_target_d:
   #!     number:
   #!   drop_target_g:
   #!     number:
   #!   drop_target_e:
   #!     number:
   #! coils:
   #!   reset_drop_targets:
   #!     number:
   #!   trip_drop_target_d:
   #!     number:
   drop_targets:
     j:
       switch: drop_target_j
       reset_coil: reset_drop_targets
     u:
       switch: drop_target_u
       reset_coil: reset_drop_targets
     d:
       switch: drop_target_d
       reset_coil: reset_drop_targets
       knockdown_coil: trip_drop_target_d
     g:
       switch: drop_target_g
       reset_coil: reset_drop_targets
     e:
       switch: drop_target_e
       reset_coil: reset_drop_targets

Important: Not all "drop targets" in your machine will be configured
as "drop targets." Some machines have drop target mechanisms that
actually act as diverters. For example, in *Attack From Mars*, the
drop target under the saucer is actually a diverter. When it's up, the
ball stays on the playfield. When it's down, the ball enters the lock.
*Star Trek: The Next Generation* has this with the drop target up
above the lanes, and *The Wizard of Oz* has this for the drop target
in front of the Winkie Guard. If a drop target in your machine is
guarding a path to somewhere the ball can go, it might be a
diverter. Of course sometime a drop target can be both, like the
"D" target in *Judge Dredd*. Feel free to post to the forum with
questions.

Notice there are no settings to control lights associated with drop
targets, but many machines (like *Judge Dredd* used in the example)
have lights for each drop target. To control those lights, you'd
create shots based on the lights and switches for each drop target,
and then you control them just like any other shot with the *shot*
settings, *shot_group* settings, and *shot profiles*. In this
case you'd end up specifying your switch for this drop target as well
as for a shot for it. It's okay to have the same switch in both
places.

Create one entry in your ``drop_targets:`` section for each drop target
in your machine. Don’t worry about grouping drop targets into banks
here. (That’s done in the ``drop_target_banks:`` section.) The drop
target name can be whatever you want, and it will be the name for this
drop target which is used throughout your machine.

.. config


Required settings
-----------------

The following sections are required in the ``drop_targets:`` section of your config:

switch:
~~~~~~~
Single value, type: string name of a :doc:`switches <switches>` device. Defaults to empty.

The name of the switch that's activated when this drop target is down.
(Note that active switch = target down, so if your drop target uses
opto switches which are reversed, then you need to configure this
switch with *type: NC* in the *switches:* section of your config file.)
MPF will automatically update the state of the drop target whenever
the switch changes state.


Optional settings
-----------------

The following sections are optional in the ``drop_targets:`` section of your config. (If you don't include them, the default will be used).

ball_search_order:
~~~~~~~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``100``

A relative value which controls the order individual devices are pulsed when ball search is running. Lower numbers are
checked first. Set to ``0`` if you do not want this device to be included in the ball search.
See the :doc:`/game_logic/ball_search/index` documentation for details.

disable_keep_up_events:
~~~~~~~~~~~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

Events in this list, when posted, will send a "disable" command to the drop target's reset coil,
disabling the "keep up".

enable_keep_up_events:
~~~~~~~~~~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

Events in this list, when posted, will send enable the drop target's reset coil which
means that balls that hit it do not cause the drop target to fall since the reset
coil is being held on. Note that this will require either ``allow_enable: true`` in the coil's
configuration or a ``default_hold_power:``/``max_hold_power`` setting. See the (:doc:`Adjust coil hold power </mechs/coils/hold_power>`) documentation for details.

Also note that many drop target coils are not designed to be held on at full power, so you'll
most likely want to use a hold power of less than 8. Start low and only use the minimum power
you need to keep the drop target up.

ignore_switch_ms:
~~~~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`). Default: ``500ms``

How long this device should ignore switch changes while ball search is running. (Otherwise the ball search pulsing
coils will set switches that could add to the score, start modes, etc. Default is ``500ms``.

knockdown_coil:
~~~~~~~~~~~~~~~
Single value, type: string name of a :doc:`coils <coils>` device. Defaults to empty.

This is an optional coil that's used to knock down a drop target. Most
drop targets do not have these. (In the *Judge Dredd* example above,
you'll notice that only the *D* target has a knockdown coil.

knockdown_coil_max_wait_ms:
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`). Default: ``100ms``

Max time allowed to delay the pulse of the knockdown coil.
This is used to prevent excess power usage.
See :doc:`psus` for details.

knockdown_events:
~~~~~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

Events in this list, when posted, pulse this drop target's knockdown coil. (If this drop target doesn't
have a knockdown coil, then these events will have no effect.)

playfield:
~~~~~~~~~~
Single value, type: string name of a :doc:`playfields <playfields>` device. Default: ``playfield``

The name of the playfield that this autofire device is on. The default setting is "playfield", so you only have to
change this value if you have more than one playfield and you're managing them separately.

reset_coil:
~~~~~~~~~~~
Single value, type: string name of a :doc:`coils <coils>` device. Defaults to empty.

The name of the coil that is pulsed to reset this drop target. The
pulse time will be whatever you configure as the default pulse time
for this coil in the *coils:* section of your machine configuration
file. Important: Only enter a *reset_coil* name here if this coil is
only resets this drop target. For banks of drop targets where a single
coil resets the entire bank of targets, enter the *reset_coil* in the
*drop_target_banks:* configuration, not here. Why? Because if you have
three drop targets in a bank, you only want to pulse the coil once to
reset all the drop targets. If you enter the coil three times (one for
each drop target), then it will pulse three times when the bank is
reset.

reset_coil_max_wait_ms:
~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`). Default: ``100ms``

Max time allowed to delay the pulse of the reset coil.
This is used to prevent excess power usage.
See :doc:`psus` for details.

reset_events:
~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Default: ``ball_starting, machine_reset_phase_3``

Default: ``ball_starting, machine_reset_phase_3``

Resets this drop target. If this drop target is not part of a drop
target bank, then resetting this target will pulse its reset coil. If
this drop target is part of a drop target bank, then resetting this
drop target will have no effect. (Instead you would reset the bank.)
Default is *ball_starting, machine_reset_phase_3*.

console_log:
~~~~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``basic``

Log level for the console log for this device.

debug:
~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

See the :doc:`documentation on the debug setting </config/instructions/debug>`
for details.

file_log:
~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``basic``

Log level for the file log for this device.

label:
~~~~~~
Single value, type: ``string``. Default: ``%``

A descriptive name for this device which will show up in the service menu
and reports.

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Defaults to empty.

Special / reserved tags for drop targets: *None*

See the :doc:`documentation on tags </config/instructions/tags>` for details.


Related How To guides
---------------------

* :doc:`/mechs/targets/drop_targets/index`
