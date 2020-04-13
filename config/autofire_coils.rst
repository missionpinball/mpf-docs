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

.. config


Required settings
-----------------

The following sections are required in the ``autofire_coils:`` section of your config:

coil:
~~~~~
Single value, type: string name of a :doc:`coils <coils>` device. Defaults to empty.

The name of the coil you want to fire. (Actually, perhaps we should
phrase it as the name of the coil you want to change the state on,
because you can also use these autofire coil rules to cause coils to
stop firing based on a switch change.)

switch:
~~~~~~~
Single value, type: string name of a :doc:`switches <switches>` device. Defaults to empty.

The name of the switch which will trigger the autofire coil.
More precisely, this switch is used together with the ``coil`` in the hardware
rules which will instruct your pinball hardware to pulse the coil.


Optional settings
-----------------

The following sections are optional in the ``autofire_coils:`` section of your config. (If you don't include them, the default will be used).

ball_search_order:
~~~~~~~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``100``

A relative value which controls the order individual devices are pulsed when ball search is running. Lower numbers are
checked first. Set to ``0`` if you do not want this device to be included in the ball search.
See the :doc:`/game_logic/ball_search/index` documentation for details.

coil_overwrite:
~~~~~~~~~~~~~~~
Single value, type: :doc:`coil_overwrites <coil_overwrites>`. Defaults to empty.

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

coil_pulse_delay:
~~~~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`). Default: ``0``

This setting will delay the pulse of your ``coil`` by a certain milliseconds
after your ``switch`` has activated.
Please note that this has to be supported in your hardware platform and not
all platforms do that.

disable_events:
~~~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Default: ``ball_will_end, service_mode_entered``

Disables this autofire coil by clearing the hardware rule from the
pinball controller hardware.

enable_events:
~~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Default: ``ball_started``

Enables this autofire coil by writing the hardware rule to the pinball
controller hardware.

playfield:
~~~~~~~~~~
Single value, type: string name of a :doc:`playfields <playfields>` device. Default: ``playfield``

The name of the playfield that this autofire device is on. The default setting is "playfield", so you only have to
change this value if you have more than one playfield and you're managing them separately.

reverse_switch:
~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

Boolean which controls whether this autofire device fires when the
switch is active or inactive. The default behavior is that the coil is
fired when the switch goes to an active state. If you want to reverse
that, so the coil fires when the switch goes to inactive, then set
this to False. (This is what you would use if you have an opto.)
Default is *False*.

switch_overwrite:
~~~~~~~~~~~~~~~~~
One or more sub-entries. Each in the format of ``string`` : ``string``

You can overwrite the ``debounce`` setting of your switch in this device.

timeout_disable_time:
~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`). Default: ``0``

To prevent machine gunning of your autofire coils (i.e. pops or slings) you can
define a windows ``timeout_watch_time``.
If more than ``timeout_max_hits`` hits to your switch (and thus responses
by your coil) are seen by MPF it will disable the hardware rule for
``timeout_disable_time`` and reinstall it afterwards.

timeout_max_hits:
~~~~~~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``0``

To prevent machine gunning of your autofire coils (i.e. pops or slings) you can
define a windows ``timeout_watch_time``.
If more than ``timeout_max_hits`` hits to your switch (and thus responses
by your coil) are seen by MPF it will disable the hardware rule for
``timeout_disable_time`` and reinstall it afterwards.

timeout_watch_time:
~~~~~~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`). Default: ``0``

To prevent machine gunning of your autofire coils (i.e. pops or slings) you can
define a windows ``timeout_watch_time``.
If more than ``timeout_max_hits`` hits to your switch (and thus responses
by your coil) are seen by MPF it will disable the hardware rule for
``timeout_disable_time`` and reinstall it afterwards.

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

The plain-English name for this device that will show up in operator
menus and trouble reports.

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Defaults to empty.

Special / reserved tags for autofire coils: *None*

See the :doc:`documentation on tags </config/instructions/tags>` for details.


Related How To guides
---------------------

* :doc:`/mechs/autofire_coils/index`
* :doc:`/mechs/pop_bumpers/index`
* :doc:`/config/kickbacks`
