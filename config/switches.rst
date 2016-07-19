switches:
=========

*Config file section*

.. include:: _machine_config_yes.rst
.. include:: _mode_config_no.rst

.. overview

The *switches:* section of the config files is used to map switch names
to controller board inputs. You can map both direct and matrix
switches. Here’s an example section:

::


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
            debounce: slow
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

The number is the physical switch input number. The exact format if
this will vary depending on what type of pinball controller you're
using and how the switch is connected. You can refer the the how to
guides for each hardware platform for details. There is no standard format--it
really depends on your hardware platform.


Optional settings
-----------------

The following sections are optional in the ``switches:`` section of your config. (If you don't include them, the default will be used).

debounce:
~~~~~~~~~
Single value, type: one of the following options: auto, quick, normal. Default: ``auto``

.. todo::
   Add description.

debug:
~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

.. todo::
   Add description.

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
   Add description.

platform:
~~~~~~~~~
Single value, type: ``string``. Default: ``None``

.. todo::
   Add description.

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
  playfield that indicate a ball is loose on the playfield. This tag is
  used to validate the playfield as well as to reset the ball search
  timer. (i.e. as long as switches with the playfield_active tag are
  being activated, the ball search timer won't start.)
+ ``start`` - Used to tell the game that the player has hit the start
  button.

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
