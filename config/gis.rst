gis:
====

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The *gis:* section of the config file is for :doc:`/mechs/gis/index` settings
for hardware that uses them. (This is typically with only used when you're writing
new code for an existing pinball machine.

Here's an example from *Judge Dredd*:


::


    gis:
        gi01:  # lower backglass
            number: G01
        gi02:  # mid backglass and rear playfield
            number: G02
        gi03:  # upper left backglass and slings, variable
            number: G03
        gi04:  # upper right backglass and Deadworld globe, variable
            number: G04
        gi05:  # coin slot lights & side cabinet fire buttons
            number: G05

Required settings
-----------------

The following sections are required in the ``gis:`` section of your config:

number:
~~~~~~~
Single value, type: ``string``.

This is the number of the GI string which specifies which output the
GI is physically connected to. The exact format used here will
depend on which control system you're using.

See the :doc:`hardware documentation for your platform </hardware/index>` for details.

Optional settings
-----------------

The following sections are optional in the ``gis:`` section of your config. (If you don't include them, the default will be used).

debug:
~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

Set this to *true* to add lots of logging information about this GI string
to the debug log. This is helpful when you’re trying to troubleshoot
problems with this shot.

dimmable:
~~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

Specifies whether this GI string is dimmable. See your hardware documentation
for details.

disable_events:
~~~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``ms``. Default: ``None``

Events that disable (turn off) this GI string.
See the :doc:`/config/instructions/device_control_events` documentation for details.

enable_events:
~~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``ms``. Default: ``machine_reset_phase_3``

Events that enable (turn on) this GI string.
See the :doc:`/config/instructions/device_control_events` documentation for details.

label:
~~~~~~
Single value, type: ``string``. Default: ``%``

The plain-English name for this device that will show up in operator
menus and trouble reports.

platform:
~~~~~~~~~
Single value, type: ``string``. Default: ``None``

Name of the platform this GI string is connected to. The default value of ``None`` means the
default hardware platform will be used. You only need to change this if you have
multiple different hardware platforms in use and this coil is not connected
to the default platform.

See the :doc:`/hardware/platform` guide for details.

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

A list of one or more tags that apply to this device. Tags allow you
to access groups of devices by tag name.
