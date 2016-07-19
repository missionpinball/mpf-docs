flashers:
=========

*Config file section*

.. include:: _machine_config_yes.rst
.. include:: _mode_config_no.rst

.. overview

The ``flashers:`` section of your config is where you configure your
machine's flashers. Note that flashers in MPF are lights that are connected
to driver outputs. Most new custom machines use LEDs (or groups of LEDs)
connected to the LED boards, so those configured as LEDs, not flashers.
But for WPC and Stern machines with driver-based flashers, you'd configure
those here.

Here's an example from a Williams *Road Show* machine:

::


    flashers:
        f_little_flipper:
            number: c37
            label: Flasher above middle left flipper
            tags: white
        f_left_ramp:
            number: c38
            label: Flasher above Bob's Bunker
            tags: yellow
        f_back_white:
            number: c39
            flash_ms: 40
            label: Two white rear wall flashers
            tags: white
        f_back_yellow:
            number: c40
            flash_ms: 40
            label: Two yellow rear wall flashers
            tags: yellow
        f_back_red:
            number: c41
            flash_ms: 40
            label: Two red rear wall flashers
            tags: red
        f_blasting_zone:
            number: c42
            label: Blasting Zone flasher
            tags: white
        f_right_ramp:
            number: c43
            label: Flasher in front of Red
            tags: white
        f_jets_at_max:
            number: c44
            label: Playfield insert in the pop bumpers
            tags: white


Required settings
-----------------

The following sections are required in the ``flashers:`` section of your config:

<FlasherName>:
~~~~~~~~~~~~~~

Each subsection of *flashers:*is the name of the flasher as you’d like
to refer to it in your game code. This can really be anything you
want, but it’s obviously best to pick something that makes sense.


number:
~~~~~~~
Single value, type: ``string``. 

This is the number for the flasher which specifies which driver output
the flasher is physically connected to. The exact format used here will
depend on the hardware controller and machine type you're using.

Since flashers are are connected to driver outputs
(just like coils), the number scheme here is identical to coils. Refer
to the ``number:`` section of your hardware platform's ``coils:`` documentation
for details.

The *Road Show* example file above is for WPC driver boards, which is why the
flasher numbers are in the *Cxx* format.)



Optional settings
-----------------

The following sections are optional in the ``flashers:`` section of your config. (If you don't include them, the default will be used).

debug:
~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

.. todo::
   Add description.

flash_events:
~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``ms``. Default: ``None``

List of events that causes this flasher to flash using its default *flash_ms:* time.

flash_ms:
~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings) </config/instructions/time_strings>` . Default: ``None``

The default time, in milliseconds, that this flasher will flash for
when it's sent a "flash" command.

hold_power:
~~~~~~~~~~~
Single value, type: ``integer``. Default: ``None``

.. todo::
   Add description.

hold_power32:
~~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``None``

.. todo::
   Add description.

hold_pwm_mask:
~~~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``None``

.. todo::
   Add description.

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

pulse_ms:
~~~~~~~~~
Single value, type: ``integer``. Default: ``None``

.. todo::
   Add description.

pulse_power:
~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``None``

.. todo::
   Add description.

pulse_power32:
~~~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``None``

.. todo::
   Add description.

pulse_pwm_mask:
~~~~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``None``

.. todo::
   Add description.

pwm_off_ms:
~~~~~~~~~~~
Single value, type: ``integer``. Default: ``None``

.. todo::
   Add description.

pwm_on_ms:
~~~~~~~~~~
Single value, type: ``integer``. Default: ``None``

.. todo::
   Add description.

recycle:
~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings) </config/instructions/time_strings>` . Default: ``None``

.. todo::
   Add description.

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

.. todo::
   Add description.


