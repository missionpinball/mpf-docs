Diverter
========

In MPF, a diverter (sometimes spelled "divertor") is anything that alters
the path of the ball based on the state it's in, including:

+ A traditional diverter which is a metal flap at the end of a rod,
  typically used on ramps to "divert" the ball one way or the other.
+ A coil-controlled post that pops up (or down) to let the ball either
  pass over it or bounce back in some other direction. (This is
  sometimes called an "up/down" post.)
+ A coil-controlled gate, typically which only allows the ball to flow
  through it in a single direction, but lifted out of the way via a coil
  when active which allows the ball to travel through it in both
  directions.
+ A "trap door" pop-up which captures the ball when it's up but lets
  the ball roll over it to another shot when it's down. (Like the trap
  door / basement in Theatre of Magic.)
+ A single drop target that blocks the entrance to a shot when it's up,
  such as in the back of the saucer in Attack from Mars or the ones that
  block the ramps in Ghostbusters.
+ Something else completely custom, such as the Ringmaster in Cirqus
  Voltaire. (When it's up the ball can hit it and drop down under the
  playfield, and when it's down the ball rolls over it and hits standup
  targets behind it.)

At this point you might be thinking, "Wait, you consider a trap door
or the Ringmaster to be a diverter?? What???" But if you think about it
from the perspective of pinball software, yeah, trap doors and the
Ringmaster *are* diverters because when then are not active, a ball
shot to them goes towards one place, and when they're active, a ball is
"diverted" to go somewhere else.

Most diverters are held in their "on"
position as long as their driver coil enabled, and then when they're
disabled they return back to their off position. That said, some are
different. The Ringmaster has a motor which raises and lowers it, and drop
targets have coils that are just pulsed to raise/lower them, so this is not
a hard and fast rule.

So based on all that, let's look
at how the MPF actually handles diverters. At the most basic level,
most diverters are just a coil, so fundamentally we don't really need
to do anything special to control a diverter. As a game programmer you
just need to enable a coil. But if you want to program your game code
to control a diverter, there's a lot of glue you need to fully
integrate it into your machine, and that's the glue that we've pre-
written into our diverter device code.

For example, many diverters
attached to ramps do not hold their coils in the "on" position for the
entire time that they're on. Instead they use the ramp entry switch to
see when a ball is coming their way, and when one is they quickly
activate so they can catch the ball in time to divert it. They also
typically have a timeout where they deactivate themselves if they
don't actually see a ball get diverted, (like with a weak ramp shot
that trips the ramp entry switch but that isn't powerful enough to
make it all the way up the ramp to the diverter.)

MPF's diverter devices
also include support for automatic enabling and disabling (based on
events), and they include intelligence to know which target devices a
diverter will send a ball to when it's enabled or disabled.


Diverters are configured in the :doc:`diverters: </config/diverters>`
section of your config files. You can see the full details of options (and how
you configure them) there.
