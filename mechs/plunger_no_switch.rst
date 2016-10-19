Plunger lanes with no ball switch
=================================

Modern pinball machines have a switch in the plunger lane that tells
the software that a ball is sitting in the plunger lane waiting to
be plunged.


This document describes how you configure MPF to work with plunger
lanes when the plunger lane has no switch which is active when a ball
is sitting at the plunger. (This is common is older single-ball
machines, including many EM and early solid state machines.)If you're
just landing on this page randomly, you might also want to check out
our `tutorial on how to configure a trough`_, as it provides some more
background information about many of the things we reference here.
Here's an example of what we're talking about: ` `_ In modern
machines, we configure the plunger lane as a `ball device`_. This is
possible since there's a switch in the plunger lane, so when that
switch is active then the machine knows there's a ball "in" the
plunger ball device, and when that switch is inactive then the machine
knows the plunger ball device does not contain a ball. Simple. But
what happens if your plunger lane doesn't have a switch which is
activated when the ball is sitting at the plunger? How does it know
there's a ball there? The solution is simple: In machines like this,
the plunger lane is *not* a ball device. Instead the plunger lane area
is considered part playfield, so a ball in the plunger lane that's not
sitting on a switch is just like any other area of the playfield where
the ball might be rolling around while it's not on a switch. So if you
have this type of plunger lane, then you would *not* have a "plunger"
ball device configured in your *ball_devices:* section. There's one
other change you have to make to get this all to work. In modern
machine where your plunger is set up as a ball device, that's the
device that has the *ball_add_live* tag. (This is the tag that tells
MPF that it should add a live ball into play from this device.) So in
this situation since your plunger lane isn't actually a ball device,
you need to add the *ball_add_live* tag to your trough, like this:


::


    ball_devices:
        trough:
            tags: drain, home, trough, ball_add_live
            ball_switches: drain
            eject_coil: trough_eject
            entrance_delay_count: 0.3s
            exit_delay_count: 0.3s


Then when MPF needs to add a live ball into play, it will eject a ball
from the trough and you're all set! If you have a `classic 1980s-style
trough`_ with separate drain and trough devices, you'd simply add the
*ball_add_live* tag to the second device in the chain, like this:


::


    ball_devices:
        drain:
            ball_switches: drain
            eject_switch: drain
            eject_coil: drain_eject
            entrance_count_delay: 300ms
            confirm_eject_type: target
            eject_targets: trough
            tags: drain
        trough:
            ball_switches: trough1, trough2, trough3
            eject_switch: trough1
            eject_coil: trough_eject
            entrance_count_delay: 300ms
            confirm_eject_type: target
            eject_targets: plunger_lane
            tags: home, trough, ball_add_live


.. _tutorial on how to configure a trough: https://missionpinball.com/docs/tutorial/create-your-trough/
.. _classic 1980s-style trough: https://missionpinball.com/docs/howto/configure-1980s-style-trough/
.. _ball device: https://missionpinball.com/docs/mpf-core-architecture/mechs/logical-mechs/ball-device/


