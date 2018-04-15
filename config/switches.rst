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

Required settings
-----------------

The following sections are required in the ``switches:`` section of your config:

number:
~~~~~~~
Single value, type: ``string``.

This is the number of the switch which specifies which switch input the
switch is physically connected to. The exact format used here will
depend on which control system you're using and how the switch is connected.

See the :doc:`/hardware/numbers` guide for details.

Optional settings
-----------------

The following sections are optional in the ``switches:`` section of your config. (If you don't include them, the default will be used).

debounce:
~~~~~~~~~
Single value, type: one of the following options: auto, quick, normal. Default: ``auto``

.. todo::
   :doc:`/about/help_us_to_write_it`

debug:
~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

.. todo::
   :doc:`/about/help_us_to_write_it`

events_when_activated:
~~~~~~~~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

A list of one or more names of events that MPF will post when this
switch goes active. These events are posted exactly as they're entered, in addition to any
events that are posted based on the switch's tags.

events_when_deactivated:
~~~~~~~~~~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

A list of one or more names of events that MPF will post when this
switch goes inactive.

ignore_window_ms:
~~~~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings) </config/instructions/time_strings>` . Default: ``0``

Specifies a duration of time during which additional switch activations will
be ignored.

For example, if you set ``ignore_window_ms: 100``, then a switch is activated once,
then again 50ms later, the second activation will be ignored. The timer is set based on
the last switch hit that *activated* the switch, so if another switch hit came in 105ms
after the first (which would be 55ms after the second), it will also count.

label:
~~~~~~
Single value, type: ``string``. Default: ``%``

.. todo::
   :doc:`/about/help_us_to_write_it`

platform:
~~~~~~~~~
Single value, type: ``string``. Default: ``None``

Name of the platform this switch is connected to. The default value of ``None`` means the
default hardware platform will be used. You only need to change this if you have
multiple different hardware platforms in use and this coil is not connected
to the default platform.

See the :doc:`/hardware/platform` guide for details.

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

You can add tags to switches to logically group them in your game code
to make it easier to do things. (Like "if all the switches tagged with
``droptarget_bank1`` are active, then do something.") Tags are also used
to create MPF events which are automatically posted with an ``sw_``
prefix, by tag, when a switch is activated. For example, if you have a
switch tagged with "hello", then every time that switch is activated,
it will post the event ``sw_hello``. If you have a switch tagged with
"hello" and "yo", then every time that switch is activated it will
post the events ``sw_hello`` and ``sw_yo``. MPF also makes use of several
tags on its own, including:

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
