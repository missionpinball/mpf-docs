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
   #! drop_targets:
   #!   j:
   #!     switch: drop_target_j
   #!     reset_coil: reset_drop_targets
   #!   u:
   #!     switch: drop_target_u
   #!     reset_coil: reset_drop_targets
   #!   d:
   #!     switch: drop_target_d
   #!     reset_coil: reset_drop_targets
   #!     knockdown_coil: trip_drop_target_d
   #!   g:
   #!     switch: drop_target_g
   #!     reset_coil: reset_drop_targets
   #!   e:
   #!     switch: drop_target_e
   #!     reset_coil: reset_drop_targets
   drop_target_banks:
     judge:
       drop_targets: j, u, d, g, e
       reset_coils: reset_drop_targets
       reset_on_complete: 1s

Notice there are no settings to control lights associated with drop
targets, but many machines (like *Judge Dredd* used in the example)
have lights for each drop target. To control those lights, you'd
create shots based on the lights and switches for each drop target,
and then you control them just like any other shot with the shot
settings, shot_group settings, and shot profiles. In this
case you'd end up specifying your switch for this drop target as well
as for a shot for it. It's ok to have the same switch in both places.

Create a subsection under *drop_target_banks:* for each bank of drop
targets you have. The name of each section is the name you'll refer to
the drop target as in your game code. ("judge", in this example.)

.. config


Required settings
-----------------

The following sections are required in the ``drop_target_banks:`` section of your config:

drop_targets:
~~~~~~~~~~~~~
List of one (or more) values, each is a type: string name of a :doc:`drop_targets <drop_targets>` device. Defaults to empty.

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

ignore_switch_ms:
~~~~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`). Default: ``500ms``

How long this device should ignore switch changes while ball search is running. (Otherwise the ball search pulsing
coils will set switches that could add to the score, start modes, etc.

reset_coil:
~~~~~~~~~~~
Single value, type: string name of a :doc:`coils <coils>` device. Defaults to empty.

The name of the coil that is fired to reset this bank of drop targets.

reset_coil_max_wait_ms:
~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`). Default: ``100ms``

Max time allowed to delay the pulse of the reset coil.
This is used to prevent excess power usage.
See :doc:`psus` for details.

reset_coils:
~~~~~~~~~~~~
List of one (or more) values, each is a type: string name of a :doc:`coils <coils>` device. Defaults to empty.

If your drop target bank has two reset coils (as was common in older
machines which huge banks of drop targets), you can add a
*reset_coils* section (plural) and then specific a list of multiple
coils. In this case, MPF will pulse all the coils at the same time to
reset the bank of drop targets.

reset_events:
~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Default: ``machine_reset_phase_3, ball_starting``

Resets this drop target bank by pulsing this bank's ``reset_coil`` or ``reset_coils``.

reset_on_complete:
~~~~~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`). Defaults to empty.

By default, when a drop target bank completes, it does not automatically reset.
If you want it to reset, then use this setting along with a time delay for when you
want it to reset after it completes.

For example:

.. code-block:: yaml

   reset_on_complete: 500ms

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

Special / reserved tags for drop target banks: *None*

See the :doc:`documentation on tags </config/instructions/tags>` for details.


Related How To guides
---------------------

* :doc:`/mechs/targets/drop_targets/drop_target_bank`
