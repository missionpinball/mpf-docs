switches:
=========

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The *switches:* section of the config files is used to map switch names
to controller board inputs. You can map both direct and matrix
switches. Here’s an example section:

.. code-block:: mpf-config

   switches:
     flipper_lwr_eos:
       number: SF1
     flipper_lwr:
       number: SF6
     fire_r:
       number: S12
       tags: plunger
     start:
       number: S13
       tags: start
     plumbbob:
       number: S14
       tags: tilt
     outlane_l:
       number: S16
       tags: playfield_active
       debounce: normal
     inlane_l:
       number: S17
       tags: playfield_active
       debounce: quick
     trough1:
       number: S81
       type: 'NC'
     shooter_lane:
       number: S82
       events_when_activated: ball_in
       events_when_deactivated: ball_out

Each subsection of ``switches:`` is a switch name, which is how you
refer to the switch in your game code. Then there are several
parameters for each switch:

.. config


Required settings
-----------------

The following sections are required in the ``switches:`` section of your config:

number:
~~~~~~~
Single value, type: ``string``. Defaults to empty.

This is the number of the switch which specifies which switch input the
switch is physically connected to. The exact format used here will
depend on which control system you're using and how the switch is connected.

Note: In a virtual environment with :doc:`/config/keyboard` section you don't
have to fill in a switch number. With a keyboard section the switch is activated
by a defined keyboards key.

See the :doc:`/hardware/numbers` guide for details.


Optional settings
-----------------

The following sections are optional in the ``switches:`` section of your config. (If you don't include them, the default will be used).

debounce:
~~~~~~~~~
Single value, type: one of the following options: auto, quick, normal. Default: ``auto``

The debounce setting to use in hardware.
``quick`` means very low to no debounce (could also be named "off").
``normal`` implies debounce "on" and should be used in most cases.
The exact timings of those settings depend on your hardware platform.
(``quick`` usually is 0-1ms, ``normal`` is 1-4ms).

The main purpose of this is to reduce the number of events/amount of
communication from the hardware.
For targets and swiches in debounce ``normal`` should be good in almost all
cases.

However, in some cases, you want to disable debounce (e.g. use ``quick``)
when using :doc:`hardware rules </config/autofire_coils>` such as pop bumpers
or sling shots.
``auto`` will use ``normal`` if no hardware rules are configured or ``quick``
when rules are configured. Therefore, you usually can leave this at ``auto``.

Switch debouncing is somewhat different from debouncing in other domains since
the switch has to be active for the whole period of debouncing (at least
during sampling).
It could also be referred as "minimum activation time" (as one discipline of
debouncing).
If you want to make sure that the switch does not activate again within
a certain period have a look at ``ignore_window_ms`` (another discipline of
debouncing).
If you want to control the fire rate of your :doc:`coil </config/coils>` have
a look at the ``recycle`` setting (configurable in some platforms).

See :doc:`/mechs/switches/debounce` for details.

events_when_activated:
~~~~~~~~~~~~~~~~~~~~~~
List of one (or more) events. Those will be posted by the device. Defaults to empty.

A list of one or more names of events that MPF will post when this
switch goes active. These events are posted exactly as they're entered, in addition to any
events that are posted based on the switch's tags.

events_when_deactivated:
~~~~~~~~~~~~~~~~~~~~~~~~
List of one (or more) events. Those will be posted by the device. Defaults to empty.

A list of one or more names of events that MPF will post when this
switch goes inactive.

ignore_window_ms:
~~~~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`). Default: ``0``

Specifies a duration of time during which additional switch activations will
be ignored.

For example, if you set ``ignore_window_ms: 100``, then a switch is activated once,
then again 50ms later, the second activation will be ignored. The timer is set based on
the last switch hit that *activated* the switch, so if another switch hit came in 105ms
after the first (which would be 55ms after the second), it will also count.

platform:
~~~~~~~~~
Single value, type: ``string``. Defaults to empty.

Name of the platform this switch is connected to. The default value of ``None`` means the
default hardware platform will be used. You only need to change this if you have
multiple different hardware platforms in use and this switch is not connected
to the default platform.

See the :doc:`/hardware/platform` guide for details.

platform_settings:
~~~~~~~~~~~~~~~~~~
Single value, type: dict. Defaults to empty.

Dict of platform specific settings.
See your :doc:`platform documentation </hardware/index>` about this.

type:
~~~~~
Single value, type: one of the following options: NC, NO. Default: ``NO``

You can add ``NC`` as a type (like ``type: NC``) to indicate that this
switch is a normally closed switch, i.e. it's closed when it's
inactive and open when it's active. This is mostly used for optos.

Switches which are type NC are automatically inverted by the Switch
Controller. In other words an NC switch is still "active" when it's
being activated, but the Switch Controller knows that activation
actually occurs when the switch opens, rather than closes. Setting the
type to NC here means that you never have to worry about this
inversion anywhere else in your game code.

x:
~~
Single value, type: ``number`` (will be converted to floating point). Defaults to empty.

X Position of this switch on the playfield.
Currently unused.

y:
~~
Single value, type: ``number`` (will be converted to floating point). Defaults to empty.

Y Position of this switch on the playfield.
Currently unused.

z:
~~
Single value, type: ``number`` (will be converted to floating point). Defaults to empty.

Z Position of this switch on the playfield.
Currently unused.

console_log:
~~~~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``basic``

Log level for the console log for this device.

debug:
~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

Set this to true to get additional debug output.

file_log:
~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``basic``

Log level for the file log for this device.

label:
~~~~~~
Single value, type: ``string``. Default: ``%``

Name of this switch in service mode.

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Defaults to empty.

You can add tags to switches to logically group them in your game code
to make it easier to do things. (Like "if all the switches tagged with
``droptarget_bank1`` are active, then do something.") Tags are also used
to create MPF events which are automatically posted with an ``sw_``
prefix, by tag, when a switch is activated. For example, if you have a
switch tagged with "hello", then every time that switch is activated,
it will post the event ``sw_hello``. If you have a switch tagged with
"hello" and "yo", then every time that switch is activated it will
post the events ``sw_hello`` and ``sw_yo``. MPF also makes use of several
tags on its own.

Special-purpose tags for switches include:

+ ``playfield_active`` - This tag should be used for all switches on the
  playfield that indicate a ball is loose on the playfield. This tag is used
  by the playfield to know that balls are on it. Note that if you have more
  than one playfield, the tag name is (playfield_name)_active, so if you have
  a playfield called "upper playfield", you'd tag the switches on that
  playfield with "upper_playfield_active".
+ ``start`` - Let's MPF know that this switch is used to start a game. (Note
  that in MPF, the game start process is kicked off when this switch is
  released, not pressed, which allows the "time held down" to be sent to MPF
  to perform alternate game start actions.)


Related How To guides
---------------------

* :doc:`/mechs/switches/index`
* :doc:`/mechs/switches/optos`
* :doc:`/mechs/switches/mechanical_switches`
