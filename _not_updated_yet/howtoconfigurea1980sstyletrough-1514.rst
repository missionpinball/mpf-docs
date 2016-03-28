
This How To guide explains how you configure a classic style trough
which has a dedicated outhole (drain) coil which is separate from
where the balls are stored. This was common on classic machines of the
1980s, up through System 11 and in some early WPC machines. If you're
just landing on this page randomly, you might also want to check out
our `tutorial on how to configure a trough`_, as it provides some more
background information about many of the things we reference here.
Also if you're using MPF with a System 11 machine, we have a full `How
To guide on System 11`_.



(A) Understand how classic troughs are different from modern troughs
--------------------------------------------------------------------

The first step to configuring a classic trough is to understand how
it's different than a modern style troughs. Rather than having a
single ball device which holds all the balls and then ejects them into
the shooter lane, classic machines actually have two devices that work
together. Device #1 can be called the "Drain." (Some manuals call it
an "outhole", but we'll call it a drain here.) A ball enters this
device when it drains from the playfield. The machine doesn't
storeballs in this device, rather, it immediately fires the coil to
kick the ball up over a hump, with the ball (or balls) are permanently
stored on the right side of the hump. Device #2 can be called the
"Trough," as it's more like a modern day trough. It has switches for
each ball position and a coil to kick the ball out into the plunger
lane. Take a look at the following diagram which illustrates how the
two-coil ball systems work: (This diagram shows three balls on the
right-hand trough side, though many classic machines only held one or
two. The configuration is the same either way.) ` `_ The coil on the
left and the switch which detects a ball there will make up the ball
device we'll call the "drain", and the coil and three switches on the
right will make up the ball device we'll call the "trough".



(B) Add your coils and switches to your config file
---------------------------------------------------

In the *switches:* section of your config file, add your drain switch
plus the ball switches for your trough. (I think there were either two
or three switches on the trough side, but you should enter as many
switches as you have.) Then in the *coils:* section of your config
file, add entries for your drain and trough coils. These new entries
in your config file should look something like this: (Note that if
you're building this config for aphysical machine, your * `number:`*
entries will need to correspond to the actual hardware numbers and
formats for your machine. See the *`switches:`_*and *`coils:`_*section
of our configuration file reference for details.)


::

    
    coils:
        drain_eject:
            number: 0
        trough_eject:
            number: 1
    
    switches:
        drain:
            number: 0
        trough1:
            number: 1
        trough2:
            number: 2
        trough3:
            number: 3




(C) Configure your draindevice
------------------------------

Next, create an entry in your *ball_devices:* section for your drain.
Add *ball_switches: drain* which means this device will read the drain
switch to know whether or not this device has a ball. Add *eject_coil:
drain_eject* which is the name of the coil that will eject the ball.
Add *entrance_count_delay: 300ms* (or whatever value you want) to
allow for settling time when a ball enters before MPF will process the
new ball. Add *confirm_eject_type: target* to configure MPF so that
this device will confirm a ball eject via a new ball entering another
ball device. Add *eject_targets: trough* which tells MPF that this
ball device ejects its balls into the device called trough. Add *tags:
drain* which tells MPF that balls entering this devicemean that a ball
has drained from the playfield. Your drain configuration should look
something like this:


::

    
        drain:
            ball_switches: drain
            eject_coil: drain_eject
            entrance_count_delay: 300ms
            confirm_eject_type: target
            eject_targets: trough
            tags: drain




(D) Configure your trough device
--------------------------------

The actual trough configuration in a System 11 style machine is
similar to the configuration of a modern trough, and you'll configure
your entrance count delays, switches, and eject coils as you would any
trough. The only difference is your tags. A modern-style trough would
have three tags: *drain*, *trough*, and *home*. But with System 11
style troughs, the drain device is the drain, not the trough, so your
trough will only have *trough* and *home* tags. (The *trough* tag
tells MPF that this device wants to hold as many balls as it can, and
the *home* tag tells MPF that it's okay for balls to be contained in
this device when the machine is first booted and when games start.)
Your trough configuration should look something like this:


::

    
        trough:
            ball_switches: trough1, trough2, trough3
            eject_coil: trough_eject
            entrance_count_delay: 300ms
            confirm_eject_type: target
            eject_targets: plunger_lane
            tags: home, trough




(E) Configure your plunger lane device
--------------------------------------

You can configure your plunger lane (or "shooter lane" or whatever
you're calling it) in a classic machine just like any other machine,
as outlined `here`_.



(E) Understanding how this works
--------------------------------

When a ball drains from the playfield, it will enter your drain ball
device. Since that device is tagged with *drain*, that will trigger
MPF's ball drain handler which will remove a ball from play, trigger
ball save, etc. Since the drain doesn't desire to hold any balls, it
will immediately eject the ball. It will watch for a ball entering the
trough device to confirm its eject. Then at this point the balls are
stored in the trough and it works just like a machine with a modern
style trough.

.. _How To guide on System 11: https://missionpinball.com/docs/howto/system-11/
.. _coils:: https://missionpinball.com/docs/configuration-file-reference/coils/
.. _here: https://missionpinball.com/docs/tutorial/create-your-plunger-lane/
.. _switches:: https://missionpinball.com/docs/configuration-file-reference/switches/
.. _tutorial on how to configure a trough: https://missionpinball.com/docs/tutorial/create-your-trough/


