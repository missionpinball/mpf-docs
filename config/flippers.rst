flippers:
=========

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

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
Read the :doc:`/mechs/flippers/index` tech note for details. (You
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

.. versionchanged:: 0.32

List of one or more events (with optional delay timings), in the
:doc:`device control events </config/instructions/device_control_events>` format.

Default: ``ball_will_end, service_mode_entered`` (Note that if you add an entry here, it will replace the default. So if you
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

power_setting_name:
~~~~~~~~~~~~~~~~~~~

.. versionadded:: 0.31

TODO

include_in_ball_search:
~~~~~~~~~~~~~~~~~~~~~~~
Boolean (True/False or Yes/No). Default is ``False``.

.. versionadded:: 0.33

Controls whether this flipper is included in ball search.

Usually flippers aren't included in ball search. However if you have upper flippers,
it's probably good to include them in the ball search since it's often possible for
an upper flipper to disable and hold a ball under the flipper. Usually this isn't
an issue since the player can just flip to release the ball. However if the machine has
tilted (or the flippers are otherwise disabled), then it's possible for a flipper to
come down on the ball and get it stuck. So you definitely want to include upper flippers
in ball search.

BTW, this is something that happened to us in *Wizard of Oz*, so that's how we thought
to include an option for flippers in ball search. :)

ball_search_order:
~~~~~~~~~~~~~~~~~~
Numeric value, default is ``100``

.. versionadded:: 0.33

A relative value which controls the order individual devices are pulsed when ball search is running. Lower numbers are
checked first. See the :doc:`/game_logic/ball_search/index` documentation for details.

ball_search_hold_time:
~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``time string`` (:doc:`Instructions for entering time strings) </config/instructions/time_strings>` . Default: ``1s``

.. versionadded:: 0.33

How long this flipper will be activated for when it is activated during ball search.


playfield:
~~~~~~~~~~

.. versionadded:: 0.33

The name of the playfield that this flipper is on. The default setting is "playfield", so you only have to
change this value if you have more than one playfield and you're managing them separately.
