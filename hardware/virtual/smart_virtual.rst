The "Smart Virtual" Platform
============================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/hardware`                                                      |
+------------------------------------------------------------------------------+
| :doc:`/config/smart_virtual`                                                 |
+------------------------------------------------------------------------------+

MPF's *Smart Virtual Platform* is based on the :doc:`virtual platform <virtual>`
with one key difference: The Smart Virtual platform watches
for coil pulse events and adjusts switches in response to simulate
how those switches would have changed if that coil fired on real
hardware.

To understand why the smart virtual platform exists, consider this simple
machine config for a trough, a plunger lane, and keyboard key mappings to
simulate their switches:

.. code-block:: mpf-config

    switches:
      s_trough1:
        number: s31
      s_trough2:
        number: s32
      s_trough3:
        number: s33
      s_trough4:
        number: s34
      s_plunger_lane:
        number: s27
    coils:
      c_trough_eject:
        number: c01
        default_pulse_ms: 25
      c_plunger_eject:
        number: c03
        default_pulse_ms: 25
    ball_devices:
      bd_trough:
        tags: trough, home, drain
        ball_switches: s_trough1, s_trough2, s_trough3, s_trough4
        eject_coil: c_trough_eject
        eject_targets: bd_plunger
      bd_plunger:
        ball_switches: s_plunger_lane
        eject_coil: c_plunger_eject
    playfields:
      playfield:
        default_source_device: bd_plunger
        tags: default
    keyboard:
      1:
        switch: s_trough1
        toggle: true
      2:
        switch: s_trough2
        toggle: true
      3:
        switch: s_trough3
        toggle: true
      4:
        switch: s_trough4
        toggle: true
      p:
        switch: s_plunger_lane
        toggle: true

MPF's regular virtual platform interface is "dumb" in the sense that
all switch actions need to be controlled externally (either via keyboard
keys, the OSC interface, etc.)

So if you have the above configuration and then MPF wants to eject a ball
from the trough, it will fire the trough coil but the switches won't actually
change. (In fact this will cause MPF to think that the eject failed, because
it will fire the eject coil and not see the ball leave.)

If you wanted to "play" an MPF game with the example config above,
you'd have to manually manually simulate the ball leaving the trough by
hitting the "1" key to deactivate a trough switch, and then hitting the "P"
key to activate the plunger lane switch. (And you'd have to do this
fast enough for the eject failure detection not to kick in.)

A better solution? The "smart" virtual interface.
-------------------------------------------------

In order to address these challenges, MPF includes a smart virtual
platform interface. The smart virtual interface works by watching for
coil pulse commands. If it sees a coil pulse from a coil that's configured
in a mechanism that would ordinarily cause a switch to change state,
then it will automatically change that switches state.

For example, if you have the trough config from above and the trough's
eject coil fires, the smart virtual platform will look to see if there are
any balls in that device, and, if so, simulate the ball leaving (which
could be by deactivating one of the device's ball switches).

The smart virtual platform also knows (thanks to the *eject_targets:* ball
device setting) where the ball is ejected to, so when a ball is
ejected from a device, the smart virtual platform will also simulate
the ball going into the target ball device.

Going back to the example machine config above, if the smart virtual platform
interface is being used, when a game is started, you'll see the *s_trough1* switch
automatically deactivate in response to the trough coil pulsing, and
then 100ms later you'll see the *s_plunger* switch activate to simulate a
ball going into the plunger lane. So simply starting a game with the smart
virtual platform puts the ball in the plunger lane without you having
to mess with the "1" and "P" keys.

Using the smart virtual platform
--------------------------------

There are three ways you can use the smart virtual platform:

1. No platform setting
^^^^^^^^^^^^^^^^^^^^^^

If you do not have a ``platform:`` setting in your machine config's
``hardware:`` section (or if you don't have a ``hardware:``
section, then MPF will use the smart virtual platform anyone you
run it.

2. Manually setting the platform
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can also manually specify the smart virtual interface
in the machine config, like this:

.. code-block:: mpf-config

    hardware:
      platform: smart_virtual

3. Via the command line
^^^^^^^^^^^^^^^^^^^^^^^

You can also specify the smart virtual platform interface via the ``-X``
(uppercase *X*) from the command line, like this:

::

    mpf -X

Or

::

   mpf both -X

etc.

What does the smart virtual platform do?
----------------------------------------

The smart virtual platform currently simulates the following pinball mechanisms.
You can configure some of them in the
:doc:`smart_virtual section </config/smart_virtual>`.

Ball Devices
^^^^^^^^^^^^

If a ball device's eject coil is pulses, it will simulate a ball leaving that device
(as long as that device has at least one ball). It is smart enough to know how many
balls are in a device, and works with special scenarios (such as timed entrance
switches that are only active when the device is full and eject confirmation
switches).

It will also simulate a ball entering the target device when a ball is ejected, and
again it knows how to work with various ball switch and entrance switch combinations.

Drop Targets
^^^^^^^^^^^^

The smart virtual platform will reset drop target switches if their associated
reset coil is pulsed.


