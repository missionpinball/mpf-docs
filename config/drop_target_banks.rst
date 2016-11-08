drop_target_banks:
==================

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+

.. overview

Once you've configured your individual drop targets, you group them
together into banks via the ``drop_target_banks:`` section of your
config file. Here's an example from *Judge Dredd*:

::

    drop_target_banks:
        judge:
            drop_targets: j, u, d, g, e
            reset_coils: c_reset_drop_targets
            reset_events:
                drop_targets_judge_complete: 1s

What about drop target banks with lights?
-----------------------------------------

Notice there are no settings to control lights associated with drop
targets, but many machines (like *Judge Dredd* used in the example)
have lights for each drop target. To control those lights, you'd
create shots based on the lights and switches for each drop target,
and then you control them just like any other shot with the shot
settings, shot_group settings, and shot profiles. In this
case you'd end up specifying your switch for this drop target as well
as for a shot for it. It's ok to have the same switch in both places.

Required settings
-----------------

The following sections are required in the ``drop_target_banks:`` section of your config:

<name>:
~~~~~~~

Create a subsection under *drop_target_banks:* for each bank of drop
targets you have. The name of each section is the name you'll refer to
the drop target as in your game code. ("judge", in this example.)

drop_targets:
~~~~~~~~~~~~~
List of one (or more) values, each is a type: string name of a ``drop_targets:`` device.

A list of the names of the individual drop targets (from the names you
chose in the *drop_targets:* section of your config file) that are
included in this bank. Note that single drop target devices can be
members of multiple banks at the same time. For example, you might
have two banks of three drop targets, from which you could actually
actually three drop target banks. One for the first three, one for the
second three, and one for all six. Then you could track separate up
and down events for a subset of three or for all six getting knocked
down.

Optional settings
-----------------

The following sections are optional in the ``drop_target_banks:`` section of your config. (If you don't include them, the default will be used).

debug:
~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

See the :doc:`documentation on the debug setting </config/instructions/debug>`
for details.

label:
~~~~~~
Single value, type: ``string``. Default: ``%``

A descriptive name for this device which will show up in the service menu
and reports.

reset_coil:
~~~~~~~~~~~
Single value, type: string name of a ``coils:`` device. Default: ``None``

The name of the coil that is fired to reset this bank of drop targets.

reset_coils:
~~~~~~~~~~~~
List of one (or more) values, each is a type: string name of a ``coils:`` device. Default: ``None``

If your drop target bank has two reset coils (as was common in older
machines which huge banks of drop targets), you can add a
*reset_coils* section (plural) and then specific a list of multiple
coils. In this case, MPF will pulse all the coils at the same time to
reset the bank of drop targets.

reset_events:
~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``ms``. Default: ``machine_reset_phase_3, ball_starting``

Resets this drop target bank by pulsing this bank's *reset_coil* or
*reset_coils*. Default is *machine_reset_phase_3, ball_starting*.

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

Special / reserved tags for drop target banks: *None*

See the :doc:`documentation on tags </config/instructions/tags>` for details.

