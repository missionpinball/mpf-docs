---
title: Diverters
---

# Diverters


Related Config File Sections:

* [diverters:](../../config/diverters.md)

In MPF, a diverter (sometimes spelled "divertor") is anything that
alters the path of the ball based on the state it's in, including:

![image](../images/diverter1.jpg)

![image](../images/diverter2.jpg)

* A traditional diverter which is a metal flap at the end of a rod,
    typically used on ramps to "divert" the ball one way or the other.
* A coil-controlled post that pops up (or down) to let the ball either
    pass over it or bounce back in some other direction. (This is
    sometimes called an "up/down" post.)
* A coil-controlled gate, typically which only allows the ball to flow
    through it in a single direction, but lifted out of the way via a
    coil when active which allows the ball to travel through it in both
    directions.
* A "trap door" pop-up which captures the ball when it's up but
    lets the ball roll over it to another shot when it's down. (Like
    the trap door / basement in Theatre of Magic.)
* A single drop target that blocks the entrance to a shot when it's
    up, such as in the back of the saucer in Attack from Mars or the
    ones that block the ramps in Ghostbusters.
* Something else completely custom, such as the Ringmaster in Cirqus
    Voltaire. (When it's up the ball can hit it and drop down under the
    playfield, and when it's down the ball rolls over it and hits
    standup targets behind it.)

At this point you might be thinking, "Wait, you consider a trap door or
the Ringmaster to be a diverter?? What???" But if you think about it
from the perspective of pinball software, yeah, trap doors and the
Ringmaster *are* diverters because when then are not active, a ball shot
to them goes towards one place, and when they're active, a ball is
"diverted" to go somewhere else.

In MPF, a diverter (sometimes spelled "divertor") is anything that
alters the path of the ball based on the state it's in, including:

![image](../images/diverter1.jpg)

![image](../images/diverter2.jpg)

* A traditional diverter which is a metal flap at the end of a rod,
    typically used on ramps to "divert" the ball one way or the other.
* A coil-controlled post that pops up (or down) to let the ball either
    pass over it or bounce back in some other direction. (This is
    sometimes called an "up/down" post.)
* A coil-controlled gate, typically which only allows the ball to flow
    through it in a single direction, but lifted out of the way via a
    coil when active which allows the ball to travel through it in both
    directions.
* A "trap door" pop-up which captures the ball when it's up but
    lets the ball roll over it to another shot when it's down. (Like
    the trap door / basement in Theatre of Magic.)
* A single drop target that blocks the entrance to a shot when it's
    up, such as in the back of the saucer in Attack from Mars or the
    ones that block the ramps in Ghostbusters.
* Something else completely custom, such as the Ringmaster in Cirqus
    Voltaire. (When it's up the ball can hit it and drop down under the
    playfield, and when it's down the ball rolls over it and hits
    standup targets behind it.)

At this point you might be thinking, "Wait, you consider a trap door or
the Ringmaster to be a diverter?? What???" But if you think about it
from the perspective of pinball software, yeah, trap doors and the
Ringmaster *are* diverters because when then are not active, a ball shot
to them goes towards one place, and when they're active, a ball is
"diverted" to go somewhere else.) note

!!! note

    MPF's diverters are integrated with
    [Ball Devices](../ball_devices/index.md) and MPF's
    ball management and routing system so they can be used to ensure that
    MPF is able to move balls to where they need to be.

Most diverters are held in their "on" position as long as their driver
coil enabled, and then when they're disabled they return back to their
off position. That said, some are different. The Ringmaster has a motor
which raises and lowers it, and drop targets have coils that are just
pulsed to raise/lower them, so this is not a hard and fast rule.

So based on all that, let's look at how the MPF actually handles
diverters. At the most basic level, most diverters are just a coil, so
fundamentally we don't really need to do anything special to control a
diverter. As a game programmer you just need to enable a coil. But if
you want to program your game code to control a diverter, there's a lot
of glue you need to fully integrate it into your machine, and that's
the glue that we've pre-written into our diverter device code.

For example, many diverters attached to ramps do not hold their coils in
the "on" position for the entire time that they're on. Instead they
use the ramp entry switch to see when a ball is coming their way, and
when one is they quickly activate so they can catch the ball in time to
divert it. They also typically have a timeout where they deactivate
themselves if they don't actually see a ball get diverted, (like with a
weak ramp shot that trips the ramp entry switch but that isn't powerful
enough to make it all the way up the ramp to the diverter.)

MPF's diverter devices also include support for automatic enabling and
disabling (based on events), and they include intelligence to know which
target devices a diverter will send a ball to when it's enabled or
disabled.

## Understanding the difference between "enabling" and "activating" diverters

When talking about diverters in MPF, we use the terms *activate* and
*enable* (as well as *deactivate* and *disable*). Even though these
words sound like they're the same thing, they're actually different,
so it's important to understand them.

When a diverter is *active*, that means it's physically activated in
its active position. A diverter that is *enabled* means that it's ready
to be activated, but it's not necessarily active at this time. To
understand this, let's step through an example.

Imagine a typical ramp in a pinball machine which has one entrance and
two exits. These kinds of ramps usually have a diverter at the top of
them that can send the ball down one of the two paths. When the diverter
is *inactive* (its default state), the ball goes down one path, and when
the diverter is *active*, the ball is sent down the other path (perhaps
towards a ball lock).

There is typically an entrance switch on the ramp which lets the game
know that a ball is potentially headed towards that diverter, so when
the game wants to route the ball to the "other" ramp exit, rather than
turning on that diverter and holding it on forever, the game just
watches for that ramp entry switch and then quickly fires the diverter
to route the ball to the other exit. Then once the ball passes by the
diverter, it hits a second switch which turns off the diverter.
(Typically the diverter activation also has a timeout which is used when
a weak shot is made where the ball trips the ramp entrance switch but
doesn't actually make it all the way up the ramp to the diverter.)

So in MPF parlance, we say that the diverter is *enabled* whenever it's
ready to be fired, but it's not actually *active* until the coil is
physically on.

Again using our example, let's say we have a ramp with a diverter, and
when that diverter is *active* it sends a ball into a lock. When the
game starts, the diverter is *disabled* and *inactive*. Ramp shots just
go up the ramp and come out the default path, and the diverter ignores
the ramp entrance switch.

Then when the player does whatever they need to do to light the lock,
the diverter is *enabled*. At this point the diverter is *not* active
since it's not actually firing, but it's *enabled* (which means it's
ready to fire) and the diverter is watching that ramp entrance switch.
(So the diverter is *enabled* but *inactive*.) Then when the player
shoots the ball up that ramp, the diverter sees the ramp entrance switch
hit and the diverter activates. (So now the diverter is *enabled* and
*active*.)

Then once the ball passes by the diverter, the diverter deactivates. At
this point whether the diverter is disabled or enabled depends on the
game logic. If the lock should stay lit, then the diverter remains
enabled even though it's not *active*, and if the player has to do
something else to re-light the lock, then the diverter is *disabled* and
*inactive*.

Hopefully that makes sense? :)

## Monitorable Properties

For
[dynamic values](../../config/instructions/dynamic_values.md) and
[conditional events](../../events/overview/conditional.md), the prefix for diverters is `device.diverters.(name)`.

*active*

:   Boolean (true/false) as to whether this diverter is actively on and
    in the powered state.

*enabled*

:   Boolean (true/false) as to whether this diverter is enabled (meaning
    it will be activated when a ball approaches it).

*eject_state*

:   Boolean (true/false) which shows whether this diverter will be
    activating to route a ball eject from an upstream ball device.

## Related How To guides

* [/events/diverter_diverter_deactivating](dual_coil_diverter.md)
* [/events/diverter_diverter_deactivating](up_down_ramps.md)

## Related Events

* [diverter_(name)_enabling](../../events/diverter_diverter_enabling.md)
* [diverter_(name)_disabling](../../events/diverter_diverter_disabling.md)
* [diverter_(name)_activating](../../events/diverter_diverter_activating.md)
* [diverter_(name)_deactivating](../../events/diverter_diverter_deactivating.md)
