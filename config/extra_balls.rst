extra_balls:
============

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **NO**  |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+

.. overview

The ``extra_balls:`` section of your config is where you configure
which events trigger and reset extra ball awards.

Note that this extra ball abstract device is fairly basic right now.
For example, there's no good way to tie this into extra ball "lit"
shots or anything at the moment.

Here's an example:

.. code-block:: mpf-config

   ##! config: mode1

   extra_balls:
       my_mode_eb:
           award_events: alien_smashed

In the above example, the extra ball called ``my_mode_eb`` will be
given to the player when the event ``alien_smashed`` is posted. After that,
future ``alien_smashed`` events will not lead to additional extra balls. (The
``my_mode_eb`` extra ball is "used up", in a sense).

This is all tracked per-player in a player variable dictionary called "extra_balls_awarded"

Required settings
-----------------

The following sections are required in the ``extra_balls:`` section of your config:

<name>:
~~~~~~~

Each subsection of ``extra_balls:`` is a name entry for a particular
extra ball award.

Optional settings
-----------------

The following sections are optional in the ``extra_balls:`` section of your config. (If you don't include them, the default will be used).

award_events:
~~~~~~~~~~~~~
One or more sub-entries, either as a list of events, or key/value pairs of
event names and delay times. (See the
:doc:`/config/instructions/device_control_events` documentation for details
on how to enter settings here.

Default: ``None``

Events in this list, when posted, award this extra ball to the current player.

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

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

Special / reserved tags for extra balls: *None*

See the :doc:`documentation on tags </config/instructions/tags>` for details.

