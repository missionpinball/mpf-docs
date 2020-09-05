How to configure dual-wound flippers
====================================

.. include:: /hardware/voltages_and_power/common_ground_warning.rst

This guide shows you how to configure dual-wound flippers in MPF. If you don't
know what "dual-wound" flippers are, or whether you have them, take a look at
the coil that your flipper uses. If it has three wires (or three tabs to
connect three wires), then it's a dual-wound coil and this guide is for you.

If it has two wires (or two tabs), then read the :doc:`single_wound` guide.

Read more about "dual wound" versus "single wound" coils in the
:doc:`/mechs/coils/dual_vs_single_wound` guide.

See :doc:`coil hardware </mechs/coils/index>` for more details about the
current, resistance, number of windings and the strength of coils.
See :doc:`dual-wound hardware </mechs/coils/dual_wound_coils>` for details
about how to find out which terminals on your coils are hold, which are the
main coil and how to connect them.

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
config. These will be added to a section called ``coils:``. Since we're using
dual-wound coils, there will actually be two coil entries for each coil—one for
the power (main) winding, and one for the hold winding.

.. code-block:: mpf-config

    coils:
      c_flipper_left_main:
        number: 0
      c_flipper_left_hold:
        number: 1
        allow_enable: true
      c_flipper_right_main:
        number: 2
      c_flipper_right_hold:
        number: 3
        allow_enable: true

Again, the ``number:`` entries in your config will vary depending on your actual
hardware, and again, you can pick whatever names you want for your coils.

Also note that the two hold coils have ``allow_enable: true`` entries added.
(In MPF config files, values of "yes" and "true" are the same.) The purpose of
the ``allow_enable: true`` setting is that as a safety precaution, MPF does not
allow you to enable (that is, to hold a coil in its "on" position) unless you
specifically add ``allow_enable: true`` to that coil's config.

So in the case if your flippers, the hold coil of a flipper needs to have
``allow_enable: true`` since in order for it to act as a flipper, that coil
needs to be allowed to be enabled (held on).

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
    #!   c_flipper_left_main:
    #!     number: 0
    #!   c_flipper_left_hold:
    #!     number: 1
    #!     allow_enable: true
    #!   c_flipper_right_main:
    #!     number: 2
    #!   c_flipper_right_hold:
    #!     number: 3
    #!     allow_enable: true
    flippers:
      left_flipper:
        main_coil: c_flipper_left_main
        hold_coil: c_flipper_left_hold
        activation_switch: s_left_flipper
      right_flipper:
        main_coil: c_flipper_right_main
        hold_coil: c_flipper_right_hold
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
    #!   c_flipper_left_main:
    #!     number: 0
    #!   c_flipper_left_hold:
    #!     number: 1
    #!     allow_enable: true
    #!   c_flipper_right_main:
    #!     number: 2
    #!   c_flipper_right_hold:
    #!     number: 3
    #!     allow_enable: true
    flippers:
      left_flipper:
        main_coil: c_flipper_left_main
        hold_coil: c_flipper_left_hold
        activation_switch: s_left_flipper
        enable_events: machine_reset_phase_3
      right_flipper:
        main_coil: c_flipper_right_main
        hold_coil: c_flipper_right_hold
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

.. literalinclude:: /mpf_examples/flippers/config/hold_no_eos.yaml
   :caption: `/config/config.yaml </mpf_examples/flippers/config/hold_no_eos.yaml>`_
   :language: yaml
   :emphasize-lines: 4-5,9,11,15,18,21,24

Related How To guides
---------------------

* :doc:`/mechs/coils/dual_wound_coils`
* :doc:`/mechs/coils/dual_vs_single_wound`
