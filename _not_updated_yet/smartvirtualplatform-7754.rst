
The *Smart Virtual Platform* is based on the `Virtual Platform`_
interface with one key difference: The Smart Virtual platform watches
for coil pulse events and simulates balls moving from device to device
by activating and deactivating switches as necessary. The Smart
Virtual platform is the default platform that's used if you don't
specify a platform in the *hardware: platform:* section of your
machine config file. To understand why the smart virtual platform
exists, consider this simple machine configuration for a trough, a
plunger lane, and keyboard key mappings to simulate their switches:


::

    
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
            pulse_ms: 25
        c_plunger_eject:
            number: c03
            pulse_ms: 25
    
    ball_devices:
        bd_trough:
            tags: trough, home, drain
            ball_switches: s_trough1, s_trough2, s_trough3, s_trough4
            eject_coil: c_trough_eject
            eject_targets: bd_plunger
        bd_plunger:
            ball_switches: s_plunger_lane
            eject_coil: c_plunger_eject
            tags: ball_add_live
    
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


MPF's virtual platform interface is "dumb" in the sense that all
switch actions need to be controlled externally (either via keyboard
keys, the OSC interface, etc.) So if you have the above configuration
and then MPF wants to eject a ball from the trough, it will fire the
trough coil but the switches won't actually change. Of course you can
manually simulate the ball leaving the trough by hitting the "1" key
to deactivate a trough switch and then hitting the "P" key to activate
the plunger lane switch, but doing this manually is difficult. Why?
Because ball devices in MPF are "smart". So when the trough coil
fires, if MPF doesn't see the ball leave the trough (by the switches
changing), then it will mark the eject as failed, retry the eject, see
if the switches changes, retry again, etc. Ultimately it will decide
the trough coil is broken and mark the coil as broken. The same is
true for the timing between the ball leaving the trough and the ball
entering the plunger lane. If you don't hit the plunger lane key fast
enough, MPF will think the ball got stuck somewhere in between the
trough and plunger and try to find it. One workaround is to set your
eject timeouts to be really long to give you enough time to deal with
things, but that means you'd have to manage two different sets of
configurations for real and virtual hardware.



A better solution? The "smart" virtual interface.
-------------------------------------------------

In order to address these challenges, MPF includes a smart virtual
platform interface. The smart virtual interface works by watching for
coil pulse commands. If it sees a coil pulse from a coil that's used
for a ball device's eject coil, then it looks to see if there are any
balls in that device. If so, it knows that in a "real" machine, that
coil pulse would move the ball out of that device, so it automatically
deactivates one of the ball switches from that device. The smart
virtual platform also knows (thanks to the *eject_targets:* ball
device setting) where the ball is ejected to, so when a ball is
ejected from a device, the smart virtual platform will also simulate
the ball going into the target ball device. Going back to the example
machine config above, if the smart virtual platform interface is being
used, when a game is started, you'll see the *s_trough1* switch
automatically deactivate in response to the trough coil pulsing, and
then 100ms later you'll see the *s_plunger* switch activate. So simply
starting a game puts the ball in the plunger lane without you having
to mess with the "1" and "P" keys. The smart virtual platform
interface is used automatically by MPF if you do not specific a
platform. You can also manually specify the smart virtual interface
for scenarios where you're chaining together multiple config files
like this:


::

    
    hardware:
        platform: smart_virtual


You can also specify the smart virtual platform interface via the *-X*
(uppercase *X*) from the command line, like this:


::

    
    mpf your_machine -X


.. _Virtual Platform: https://missionpinball.com/docs/mpf-core-architecture/platform-interfaces/virtual/


