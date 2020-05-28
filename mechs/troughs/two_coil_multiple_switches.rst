How to configure an older style trough with two coils and switches for each ball
================================================================================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/ball_devices`                                                  |
+------------------------------------------------------------------------------+
| :doc:`/config/playfields`                                                    |
+------------------------------------------------------------------------------+

This guide will show you how to configure MPF to use an older-style drain
and trough combination that uses two coils (one to eject the ball from the
drain hole and a second to release a ball into the plunger lane).

This guide is written for the types of systems where the trough side (after
the "hump") has multiple switches—one for each ball that's sitting there.

Here's an example of a Williams System 11 trough that uses this system, from
a Pin*Bot machine:

.. image:: /mechs/images/two_coil_multiple_switches_trough_photo.jpg

If your machine's trough system is like this but you only have one switch
on the trough side (like Gottlieb System 3 machines), then use
:doc:`this guide <two_coil_one_switch>` instead.

The following diagram shows how the layout that this guide is written for
works: (This is a side view)

.. image:: /mechs/images/two_coils_multiple_switches.png

This style of trough and drain was used in Williams System 11 machines and
early WPC machines (Addams Family, T2, Hurricane, and a few others).

1. Add the switches
-------------------

The first step is to add all the switches to the ``switches:``
section of your config file. Create an entry in your ``switches:`` section for
the drain switch as well as each switch in your trough, like this: (This
example has three switches in the trough. Yours may have more or less.)

.. code-block:: mpf-config

    switches:
      s_drain:
        number: 1
      s_trough1:
        number: 2
      s_trough2:
        number: 3
      s_trough3:
        number: 4

Note that we configured this switches with numbers ``01`` through ``04``, but
you should use the actual switch numbers for your control system that the trough
switches are connected to. (See :doc:`/hardware/numbers` for instructions for
each type of control system.)

It makes no difference which switch is which (in terms of whether
Switch 1 is on the left side or the right side). Also the actual switch
names don't really matter. We use *s_trough1* through *s_trough3* though you can
call them *s_ball_trough_1* or *trough_ball_1* or *s_mr_potatohead*.

2. Add the coils
----------------

Next, create the entries in your ``coils:`` section for the drain eject
coil and the trough release coil. Again, the names don't matter. We'll call
them *c_drain_eject* and *c_trough_release* and enter them like this:

.. code-block:: mpf-config

    coils:
      c_drain_eject:
        number: 3
        default_pulse_ms: 20
      c_trough_release:
        number: 4
        default_pulse_ms: 20

Again, the ``number:`` entries in your config will vary depending on your actual
hardware, and again, you can pick whatever name you want for your coil.

You'll also note that we went ahead and entered ``default_pulse_ms:`` values of 20
which will override the default pulse times of 10ms. It's hard to say
at this point what values you'll actually need. You can always adjust
this at any time. You can play with the exact values in a bit once we
finish getting everything set up.

Note that some trough coils use a shorter pulse to pop the ball into the plunger
lane. However, some machines have gates or rotational devices that need to be
active for much longer. So having a long pulse time, like ``default_pulse_ms: 1000``
(for one second) is totally fine. However, if the pulse time is over 255ms, then
technically that coil is enabled and disabled versus pulsed, so in that case,
you also need to add ``allow_enable: true`` which tells MPF it's ok to enable
this coil for more than 255ms (since 255ms is the maximum pulse time for most
platforms).

In other words, a trough release time of 1s would look like this:

.. code-block:: mpf-config

   coils:
     c_trough_release:
       number: 4
       default_pulse_ms: 1000
       allow_enable: true

3. Add your "drain" ball device
-------------------------------

In MPF, anything that holds and releases a ball is a
:doc:`ball device </mechs/ball_devices/index>`. With this drain/trough setup,
there are actually two ball devices—one for the drain and a second for the
trough.

Let's add the drain device first, which we'll add to the ``ball_devices:``
section of your machine config. (If you don't have that section add it now.)

Then in your ``ball_devices:`` section, create an entry called ``bd_drain:``,
like this:

::

    ball_devices:
        bd_drain:

This means that you're creating a ball device called *bd_drain*.
We use the preface *bd_* to indicate that this is a ball device
which makes it easier when we're referencing them later. Then under
your ``bd_drain:`` entry, you'll start entering the
configuration settings for your drain ball device.

* Add ``ball_switches: s_drain`` which means this device will use the *s_drain*
  switch to know whether or not this device has a ball.
* Add ``eject_coil: c_drain_eject`` which is the name of the coil that will
  eject the ball from the drain.
* Add ``eject_targets: bd_trough`` which tells MPF that this ball device
  ejects its balls into the device called *bd_trough*. (We'll create that
  device in the next step.)
* Add ``tags: drain`` which tells MPF that balls entering this device mean that
  a ball has drained from the playfield.

Your drain device configuration should look now look like this:

.. code-block:: mpf-config

    #! switches:
    #!   s_drain:
    #!     number: 1
    #!   s_trough1:
    #!     number: 2
    #!   s_trough2:
    #!     number: 3
    #!   s_trough3:
    #!     number: 4
    #!   s_plunger:
    #!     number: 10
    #! coils:
    #!   c_drain_eject:
    #!     number: 3
    #!     default_pulse_ms: 20
    #!   c_trough_release:
    #!     number: 4
    #!     default_pulse_ms: 20
    ball_devices:
      bd_drain:
        ball_switches: s_drain
        eject_coil: c_drain_eject
        eject_targets: bd_trough
        tags: drain
    #!   bd_trough:
    #!     ball_switches: s_trough1, s_trough2, s_trough3
    #!     eject_coil: c_trough_release
    #!     tags: home, trough

4. Add your "trough" ball device
--------------------------------

Next create a second entry in the ``ball_devices:`` section called ``bd_trough``
that will be for the trough device that holds the balls that are ejected from
the drain before they're released into the plunger lane.

The configuration is pretty straightforward:

* Add ``ball_switches: s_trough1, s_trough2, s_trough3`` tells this device that
  those switches are used to count balls in the trough. (You may have more or
  less than 3. Also the order of these doesn't matter.
* Add ``eject_coil: c_trough_release`` which is the name of the coil that will
  be pulsed to eject the ball from the drain.
* Add ``eject_targets: bd_plunger_lane`` which tells MPF that this ball device
  ejects its balls into the device called *bd_plunger_lane*. (We won't actually
  create the plunger device in this How To guide, but you need to have it, so
  see the :doc:`/mechs/plungers/index` documentation for full details since
  there are lots of different types of plungers.
* Add ``tags: home, trough`` which tells MPF that it's ok to store unused balls
  here and that it's ok for balls to be here when games start.
* Set ``eject_timeouts`` to the maximum time the ball can take to return if the
  eject fails.

Your trough device configuration should look now look like this:

.. code-block:: mpf-config

    #! switches:
    #!   s_drain:
    #!     number: 1
    #!   s_trough1:
    #!     number: 2
    #!   s_trough2:
    #!     number: 3
    #!   s_trough3:
    #!     number: 4
    #!   s_plunger:
    #!     number: 10
    #! coils:
    #!   c_drain_eject:
    #!     number: 3
    #!     default_pulse_ms: 20
    #!   c_trough_release:
    #!     number: 4
    #!     default_pulse_ms: 20
    ball_devices:
      bd_trough:
        ball_switches: s_trough1, s_trough2, s_trough3
        eject_coil: c_trough_release
        eject_targets: bd_plunger_lane
        tags: home, trough
        eject_timeouts: 3s
    #!   bd_plunger_lane:
    #!     ball_switches: s_plunger
    #!     mechanical_eject: true

5. Configure your virtual hardware to start with balls in the trough
--------------------------------------------------------------------

While we're talking about the trough, it's probably a good idea to configure
MPF so that when you start it in virtual mode (with no physical hardware) that
it starts with the trough full of balls. To do this, add a new section to your
config file called ``virtual_platform_start_active_switches:``. (Sorry this
entry name is hilariously long.) As its name implies,
*virtual_platform_start_active_switches:* lets you list the names of
switches that you want to start in the "active" state when you're
running MPF with the virtual platform interfaces.

The reason these only work with the virtual platforms is because if you're
running MPF while connected to a physical pinball machine, it doesn't
really make sense to tell MPF which switches are active since MPF can
read the actual switches from the physical machine. So you can add
this section to your config file, but MPF only reads this section when
you're running with one of the virtual hardware interfaces. To use it,
simply add the section along with a list of the switches you want to
start active. For example:

.. code-block:: mpf-config

    #! switches:
    #!   s_trough1:
    #!     number: 2
    #!   s_trough2:
    #!     number: 3
    #!   s_trough3:
    #!     number: 4
    virtual_platform_start_active_switches: s_trough1, s_trough2, s_trough3

Here's the complete config
--------------------------

.. begin_mpfdoctest:config/config.yaml

.. code-block:: mpf-config

    #config_version=5
    switches:
      s_drain:
        number: 1
      s_trough1:
        number: 2
      s_trough2:
        number: 3
      s_trough3:
        number: 4
      s_plunger:
        number: 10
    coils:
      c_drain_eject:
        number: 3
        default_pulse_ms: 20
      c_trough_release:
        number: 4
        default_pulse_ms: 20
    ball_devices:
      bd_drain:
        ball_switches: s_drain
        eject_coil: c_drain_eject
        eject_targets: bd_trough
        tags: drain
      bd_trough:
        ball_switches: s_trough1, s_trough2, s_trough3
        eject_coil: c_trough_release
        eject_targets: bd_plunger_lane
        tags: home, trough
        eject_timeouts: 3s
      bd_plunger_lane:
        ball_switches: s_plunger
        mechanical_eject: true
        eject_timeouts: 5s
    playfields:
      playfield:
        default_source_device: bd_plunger_lane
        tags: default
    virtual_platform_start_active_switches: s_trough1, s_trough2, s_trough3

.. end_mpfdoctest
