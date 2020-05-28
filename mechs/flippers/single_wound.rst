How to configure single-wound flippers
======================================

.. include:: /hardware/voltages_and_power/common_ground_warning.rst

This guide shows you how to configure single-wound flippers in MPF. If you don't
know what "single-wound" flippers are, or whether you have them, take a look at
the coil that your flipper uses. If it has two wires (or two tabs to
connect two wires), then it's a single-wound coil and this guide is for you.

If it has three wires (or three tabs), then read the :doc:`dual_wound` guide.

Read more about "dual wound" versus "single wound" coils in the
:doc:`/mechs/coils/dual_vs_single_wound` guide.

See :doc:`coil hardware </mechs/coils/index>` for more details about the
current, resistance, number of windings and the strength of coils.

1. Add your flipper buttons
---------------------------

First, make sure you have entries in your machine config for your flipper
buttons.

Here's an example ``config.yaml`` with two switches added:

.. code-block:: mpf-config

    switches:
      s_left_flipper:
        number: 1
        tags: left_flipper
      s_right_flipper:
        number: 2
        tags: right_flipper

You can pick whatever names you want for your switches. We chose
``s_left_flipper`` and ``s_right_flipper``.

Note that we configured this switches with numbers ``1`` and ``2``, but you
should use the actual switch numbers for your control system that the flipper
buttons are connected to. (See :doc:`/hardware/numbers` for instructions for
each type of control system.)

We also added tags called ``left_flipper`` and ``right_flipper``.
These are optional, but recommended. The reason is that MPF includes
a :doc:`combo switch </game_logic/combo_switches/index>` feature which
posts events when player switches are held in combination. If you add
these tags to your flipper switches, an event called *flipper_cancel*
will be posted when the player hits both flipper buttons at the same time
which you can use to cancel shows and other things you want the player to
be able to skip.

2. Add your flipper coils
-------------------------

Next you need to add entries for your flipper coils to your machine-wide
config. These will be added to a section called ``coils:``.

.. code-block:: mpf-config

    coils:
      c_flipper_left:
        number: 0
        allow_enable: true
        default_hold_power: 0.125
      c_flipper_right:
        number: 1
        allow_enable: true
        default_hold_power: 0.125

Again, the ``number:`` entries in your config will vary depending on your actual
hardware, and again, you can pick whatever names you want for your coils.

Also note that the coils have ``allow_enable: true`` entries added.
(In MPF config files, values of "yes" and "true" are the same.) The purpose of
the ``allow_enable: true`` setting is that as a safety precaution, MPF does not
allow you to enable (that is, to hold a coil in its "on" position) unless you
specifically add ``allow_enable: true`` to that coil's config.

Since flippers need to be held on (as long as the flipper button is active),
you need ``allow_enable: true`` in the coil config for them.

Finally, notice that there's a ``default_hold_power: 0.125`` setting for each coil. That
is the power value (from 0-1) which controls how much power is applied to the
flipper when it's held on. A value of 0.125 is 12.5% power, a value of 2
is 25% which, a value of 0.375 is 37.5%, 0.5 is 50%, etc.

We just start with the lowest setting for now and you can increase it later if
it's not enough.

3. Add your flipper entries
---------------------------

At this point you have your coils and switches defined, but you can't
flip yet because you don't have any flippers defined. Now you might be
thinking, "Wait, but didn't I just configure the coils and switches?"
Yes, you did, but now you have to tell MPF that you want to create a
flipper mechanism which links together the switch and the coils
to become a "flipper".

You create your flipper mechanisms by adding a ``flippers:`` section to
your machine config, and then specifying the switch and coils for each
flipper that you defined in Steps 1 and 2.

Here's what you would create based on the switches and coils we've defined so far:

.. code-block:: mpf-config

    #! switches:
    #!   s_left_flipper:
    #!     number: 1
    #!     tags: left_flipper
    #!   s_right_flipper:
    #!     number: 2
    #!     tags: right_flipper
    #! coils:
    #!   c_flipper_left:
    #!     number: 0
    #!     allow_enable: true
    #!     default_hold_power: 0.125
    #!   c_flipper_right:
    #!     number: 1
    #!     allow_enable: true
    #!     default_hold_power: 0.125
    flippers:
      left_flipper:
        main_coil: c_flipper_left
        activation_switch: s_left_flipper
      right_flipper:
        main_coil: c_flipper_right
        activation_switch: s_right_flipper

4. Enabling your flippers
-------------------------

By default, MPF only enables flippers when a game is in progress. So if this
is a first-time config and you haven't configured your ball devices and start
button and everything, you can't actually start a game yet, which means you
can't test your flippers.

Fortunately we can get around that by configuring your flippers to just
automatically enable themselves when MPF starts. To do
this, add the following entry to each of your flippers in your config
file:

::

    enable_events: machine_reset_phase_3

So now the ``flippers:`` section of your config file should look like this:

.. code-block:: mpf-config

    #! switches:
    #!   s_left_flipper:
    #!     number: 1
    #!     tags: left_flipper
    #!   s_right_flipper:
    #!     number: 2
    #!     tags: right_flipper
    #! coils:
    #!   c_flipper_left:
    #!     number: 0
    #!     allow_enable: true
    #!     default_hold_power: 0.125
    #!   c_flipper_right:
    #!     number: 1
    #!     allow_enable: true
    #!     default_hold_power: 0.125
    flippers:
      left_flipper:
        main_coil: c_flipper_left
        activation_switch: s_left_flipper
        enable_events: machine_reset_phase_3
      right_flipper:
        main_coil: c_flipper_right
        activation_switch: s_right_flipper
        enable_events: machine_reset_phase_3

5. Configure your control system hardware
-----------------------------------------

At this point your flipper configuration is technically complete, though there
are two other important things you may have to do first:

If you're using physical hardware, you may need an additional section in your
machine config for your control system. (For example, FAST Pinball and Open
Pinball Project controllers require a one-time port configuration, etc.) See the
:doc:`control system documentation </hardware/index>` for details.

6. Adjust your flipper power
----------------------------

As a safety precaution, MPF uses very low (10ms) default pulse times for coils.
In most cases, 10ms will not be enough power to physically move the flippers
when you hit the button. (You might hear them click or buzz without actually
seeing them move.)

So check out the documentation in the coils section for instructions on how to
adjust the :doc:`pulse power </mechs/coils/pulse_power>` and the
:doc:`hold power </mechs/coils/hold_power>` for the coils you're using for
your flippers.

Here's the complete config
--------------------------

Here's the complete machine config file (or sections of the machine config file)
we created in this How To guide:

.. code-block:: mpf-config

    #config_version=5
    switches:
      s_left_flipper:
        number: 1
        tags: left_flipper
      s_right_flipper:
        number: 2
        tags: right_flipper
    coils:
      c_flipper_left:
        number: 0
        allow_enable: true
        default_hold_power: 0.125
      c_flipper_right:
        number: 1
        allow_enable: true
        default_hold_power: 0.125
    flippers:
      left_flipper:
        main_coil: c_flipper_left
        activation_switch: s_left_flipper
        enable_events: machine_reset_phase_3
      right_flipper:
        main_coil: c_flipper_right
        activation_switch: s_right_flipper
        enable_events: machine_reset_phase_3

