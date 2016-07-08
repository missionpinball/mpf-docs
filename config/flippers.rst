flippers:
=========

*Config file section*

.. include:: _machine_config_yes.rst
.. include:: _mode_config_no.rst

.. overview

The ``flippers:`` section of your config contains all the settings
for the flippers in a pinball machine.

Here's an example from a *Judge Dredd* machine with four
flippers. (Note *Judge Dredd* technically has four flipper buttons too,
but it's the style where you push the button part way in to flip the
lower flipper, and all the way in to flip the upper flipper too. But
as far as the game code is concerned, it sees two separate switches in
each flipper button—-one that's activated via the half-press, and the
second via the full press.)

Also note that flippers are kind of complex and there are a lot of options.
Read the :doc:`/tech_notes/flipper_theory` tech note for details. (You
should definitely read that first before digging into the configuration
options here.)

.. note::

   The ``flippers:`` section of the config is only used for controlled flippers
   in newer machines. Early solid-state (pre-WPC) machines used enable relays
   to enable the flippers, and those are configured elsewhere. (See the How To
   guides for details.)

::

        flippers:
            lower_left:
                main_coil: c_flipper_lower_left_main
                hold_coil: c_flipper_lower_left_hold
                activation_switch: s_flipper_left
                eos_switch: flipperLwL_EOS
                label: Left Main Flipper
            lower_right:
                main_coil: c_flipper_lower_right_main
                hold_coil: c_flipper_lower_right_hold
                activation_switch: s_flipper_right
                eos_switch: flipperLwR_EOS
                label: Right Main Flipper
            upper_left:
                main_coil: flipperUpLMain
                hold_coil: flipperUpLHold
                activation_switch: flipperUpL
                eos_switch: flipperUpL_EOS
                label: Upper Left Flipper
            upper_right:
                main_coil: flipperUpRMain
                hold_coil: flipperUpRHold
                activation_switch: flipperUpR
                eos_switch: flipperUpR_EOS
                label: Upper Right Flipper

Required settings
-----------------

The following sections are required in the ``flippers:`` section of your config:

<name>:
~~~~~~~
Create sub-entries for each flipper in your machine. In the config file
above, the flipper sub-entries are named *lower_left*,
*lower_right*, *upper_left*, and *upper_right*.

activation_switch:
~~~~~~~~~~~~~~~~~~
Single value, type: string name of a ``switches:`` device. 

The switch that controls this flipper. (i.e. the flipper button)

main_coil:
~~~~~~~~~~
Single value, type: string name of a ``coils:`` device. 

The name of the main flipper coil. For flippers that only have single-
wound coils, this is where you specify that coil. In that case you
would also configure the lower-power hold option for this coil in the
:doc:`/config/coils` section of your config.

Optional settings
-----------------

The following sections are optional in the ``flippers:`` section of your config. (If you don't include them, the default will be used).

debug:
~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

See the :doc:`documentation on the debug setting </config/instructions/debug>`
for details.

disable_events:
~~~~~~~~~~~~~~~
List of one or more events (with optional delay timings), in the
:doc:`device control events </config/instructions/device_control_events>` format.
Default: ``ball_ending`` (Note that if you add an entry here, it will replace the default. So if you
also want the default value(s) to apply, add them too.)


Disables this flipper (meaning pushing the flipper button doesn't active
the flipper).

enable_events:
~~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``ms``. Default: ``ball_started``

List of one or more events (with optional delay timings), in the
:doc:`device control events </config/instructions/device_control_events>` format.
Default: ``ball_started`` (Note that if you add an entry here, it will replace the default. So if you
also want the default value(s) to apply, add them too.)

Enables this flipper.

eos_switch:
~~~~~~~~~~~
Single value, type: string name of a ``switches:`` device. Default: ``None``

.. todo::
   Add description.

eos_switch_overwrite:
~~~~~~~~~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``str``. Default: ``None``

If you're using an end of stroke switch with this flipper, enter the
switch name here.

hold_coil:
~~~~~~~~~~
Single value, type: string name of a ``coils:`` device. Default: ``None``

The name of the hold coil winding for dual-wound flipper coils.

hold_coil_overwrite:
~~~~~~~~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``str``. Default: ``None``

.. todo::
   Add description.

label:
~~~~~~
Single value, type: ``string``. Default: ``%``

A descriptive name for this device which will show up in the service menu
and reports.

main_coil_overwrite:
~~~~~~~~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``str``. Default: ``None``

.. todo::
   Add description.

switch_overwrite:
~~~~~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``str``. Default: ``None``

.. todo::
   Add description.

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

Special / reserved tags for flippers: *None*

See the :doc:`documentation on tags </config/instructions/tags>` for details.

use_eos:
~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

Controls whether an EOS switch is used to disable the main winding or to switch
to lower-power pwm mode.
