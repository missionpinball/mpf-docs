autofire_coils:
===============

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The *autofire_coils:* section of your config file contains all the
settings for the coils which you would like to fire automatically
based on a switch activation in a pinball machine.

Here’s an example:

.. code-block:: mpf-config

   switches:
     s_left_sling:
       number: 1
     s_right_sling:
       number: 2
   coils:
     c_left_sling:
       number: 1
       default_pulse_ms: 10ms
     c_right_sling:
       number: 2
       default_pulse_ms: 10ms
   autofire_coils:
     left_sling:
       coil: c_left_sling
       switch: s_left_sling
     right_sling:
       coil: c_right_sling
       switch: s_right_sling

Note that autofire coils in MPF are 1-to-1 in terms of coils-to-
switches, so a single entry is for one switch to control one coil. On
some platforms, you can have two switches control a single coil (or
two coils controlled by a single switch), but to do that you would
create two separate *autofire_coils:* entries with one coil and one
switch each. (And again, that's platform-specific. Check your hardware
platform documentation for details.)

If you're wiring your slingshots and you want two switches to control a single coil, on
nearly 100% of pinball machines in the world, those two switches are
wired together and use a single input, so the hardware sees them as a
single switch. (Just be sure to wire them in parallel, not series, so
that either switch closing causes the hardware to see the switch
activation.) The top-level setting is the name you can refer to this
autofire coil as, such as ``left_sling:`` or ``right_sling:`` in the example
above.

Then each entry has the following required and optional settings:

Required settings
-----------------

The following sections are required in the ``autofire_coils:`` section of your config:

<name>:
~~~~~~~

The name of the ball device. (``left_sling`` and ``right_sling``
in the example config above.)

The rest of the settings here apply to individual ball devices (and
are indented under them).

coil:
~~~~~
Single value, type: string name of a ``coils:`` device.

The name of the coil you want to fire. (Actually, perhaps we should
phrase it as the name of the coil you want to change the state on,
because you can also use these autofire coil rules to cause coils to
stop firing based on a switch change.)

switch:
~~~~~~~
Single value, type: string name of a ``switches:`` device.

Optional settings
-----------------

The following sections are optional in the ``autofire_coils:`` section of your config. (If you don't include them, the default will be used).

coil_overwrite:
~~~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``str``. Default: ``None``

You can overwrite ``recycle``, ``pulse_ms``, ``pulse_power`` or ``hold_power``
of the coil for this device.

This is an example:

.. code-block:: mpf-config

   switches:
     s_left_sling:
       number: 1
   coils:
     c_left_sling:
       number: 1
       default_pulse_ms: 10ms
   autofire_coils:
     stronger_left_sling:
       coil: c_left_sling
       switch: s_left_sling
       coil_overwrite:
         pulse_ms: 20ms

In this example we increase ``pulse_ms`` of the slingshot.
If you define multiple versions of a autofire_coil (here slingshot) make
sure that you only enable one of them at a time.

debug:
~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

See the :doc:`documentation on the debug setting </config/instructions/debug>`
for details.

disable_events:
~~~~~~~~~~~~~~~

List of one or more events (with optional delay timings), in the
:doc:`device control events </config/instructions/device_control_events>` format.

Default: ``ball_ending, service_mode_entered`` (Note that if you add an entry here, it will replace the default. So if you
also want the default value(s) to apply, add them too.)

Disables this autofire coil by clearing the hardware rule from the
pinball controller hardware.

enable_events:
~~~~~~~~~~~~~~
List of one or more events (with optional delay timings), in the
:doc:`device control events </config/instructions/device_control_events>` format.

Default: ``ball_started`` (Note that if you add an entry here, it will replace the default. So if you
also want the default value(s) to apply, add them too.)

Enables this autofire coil by writing the hardware rule to the pinball
controller hardware.

label:
~~~~~~
Single value, type: ``string``. Default: ``%``

The plain-English name for this device that will show up in operator
menus and trouble reports.

reverse_switch:
~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

Boolean which controls whether this autofire device fires when the
switch is active or inactive. The default behavior is that the coil is
fired when the switch goes to an active state. If you want to reverse
that, so the coil fires when the switch goes to inactive, then set
this to False. (This is what you would use if you have an opto.)
Default is *False*.

switch_overwrite:
~~~~~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``str``. Default: ``None``

You can overwrite the ``debounce`` setting of your switch in this device.

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

Special / reserved tags for autofire coils: *None*

See the :doc:`documentation on tags </config/instructions/tags>` for details.

ball_search_order:
~~~~~~~~~~~~~~~~~~
Numeric value, default is ``100``

A relative value which controls the order individual devices are pulsed when ball search is running. Lower numbers are
checked first. Set to ``0`` if you do not want this device to be included in the ball search.
See the :doc:`/game_logic/ball_search/index` documentation for details.

playfield:
~~~~~~~~~~

The name of the playfield that this autofire device is on. The default setting is "playfield", so you only have to
change this value if you have more than one playfield and you're managing them separately.
