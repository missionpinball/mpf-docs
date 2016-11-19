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

::

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

What about drop targets with lights?
------------------------------------

Notice there are no settings to control lights associated with drop
targets, but many machines (like *Judge Dredd* used in the example)
have lights for each drop target. To control those lights, you'd
create shots based on the lights and switches for each drop target,
and then you control them just like any other shot with the *shot*
settings, *shot_group* settings, and *shot profiles*. In this
case you'd end up specifying your switch for this drop target as well
as for a shot for it. It's okay to have the same switch in both
places.

Required settings
-----------------

The following sections are required in the ``drop_targets:`` section of your config:

<name>:
~~~~~~~

Create one entry in your *drop_targets:* section for each drop target
in your machine. Don’t worry about grouping drop targets into banks
here. (That’s done in the *drop_target_banks:* section.) The drop
target name can be whatever you want, and it will be the name for this
drop target which is used throughout your machine.

switch:
~~~~~~~
Single value, type: string name of a ``switches:`` device.

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

.. todo::
   Add description.

debug:
~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

See the :doc:`documentation on the debug setting </config/instructions/debug>`
for details.

knockdown_coil:
~~~~~~~~~~~~~~~
Single value, type: string name of a ``coils:`` device. Default: ``None``

This is an optional coil that's used to knock down a drop target. Most
drop targets do not have these. (In the *Judge Dredd* example above,
you'll notice that only the *D* target has a knockdown coil.

knockdown_events:
~~~~~~~~~~~~~~~~~
One or more sub-entries, either as a list of events, or key/value pairs of
event names and delay times. (See the
:doc:`/config/instructions/device_control_events` documentation for details
on how to enter settings here.

Default: ``None``

Events in this list, when posted, pulse this drop target's knockdown coil. (If this drop target doesn't
have a knockdown coil, then these events will have no effect.)

label:
~~~~~~
Single value, type: ``string``. Default: ``%``

A descriptive name for this device which will show up in the service menu
and reports.

reset_coil:
~~~~~~~~~~~
Single value, type: string name of a ``coils:`` device. Default: ``None``

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

reset_events:
~~~~~~~~~~~~~
One or more sub-entries, either as a list of events, or key/value pairs of
event names and delay times. (See the
:doc:`/config/instructions/device_control_events` documentation for details
on how to enter settings here.

Default: ``ball_starting, machine_reset_phase_3``

Resets this drop target. If this drop target is not part of a drop
target bank, then resetting this target will pulse its reset coil. If
this drop target is part of a drop target bank, then resetting this
drop target will have no effect. (Instead you would reset the bank.)
Default is *ball_starting, machine_reset_phase_3*.

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

Special / reserved tags for drop targets: *None*

See the :doc:`documentation on tags </config/instructions/tags>` for details.

playfield:
~~~~~~~~~~

.. versionadded:: 0.32

TODO
