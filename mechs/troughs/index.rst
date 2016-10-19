Ball Trough
===========

This is a type of ball device

2. Understand the  "trough" ball devices
----------------------------------------

In modern pinball machines, the trough is the ball device that holds
balls after they've drained off the playfield. The act of a ball
entering a trough device usually triggers a *ball drain* event, and
when the game wants to launch a ball into play, it usually ejects a ball from
the trough (typically into another ball device like the plunger lane
or some sort of launch catapult). So when we're building the MPF
config for a new machine, the first ball device we create is the
trough.

That said, we should probably talk about what exactly a trough is.
A modern Stern- or Williams-style trough usually holds between 4 and 6
balls. The trough sits underneath the playfield so that a ball
entering it is gravity-fed and rolls down to the end of the line.
There's a switch (either a physical leaf switch or an opto switch) for
each ball position which lets the machine know how many balls are in
the it, and there's a solenoid (coil) at the end that pulses to kick a
ball out of the trough and into the shooter lane.

Most modern troughs
also have a switch in the upper position near the exit that's used to
detect if a ball falls back into the trough from the "exit"
side—something that tends to happen if your eject coil pulse is too
strong or too weak. (Too weak means the ball falls back in because it
didn't have enough oomph to make it out, and too strong means the ball
flies out too fast, bounces off the right edge rail of the plunger
lane, and lands back in the trough after the other balls have rolled
down into their new positions.) In MPF we refer to this as a "jam"
switch though it's also called a "ball stacked" or "up ball" switch
depending on whose manual you're reading.

Here's a side-view diagram of a modern style trough:

.. image:: /mechs/images/modern_trough.jpg

The diagram above does not show the ball switches, but you get the idea.

If this trough diagram does not look like your trough...
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Of course not all troughs are the same. In older machines (most 1980s
machines, Williams System 11, and early WPC machines), the trough was
entirely above the playfield, and there were two solenoids instead of one.
(The first coil kicked the ball out of the drain hole, and a second coil
kicked the ball into the plunger lane.) This style of trough is actually
configured as two separate ball devices in MPF, and they look something like
this:

.. image:: /mechs/images/system_11_style_trough.jpg


If you have a older style outhole + trough combination that looks something like the
diagram above, you can see how to configure it via this "How To" guide
for 1980s-style troughs.

.. todo::

    Need to migrate this guide to the new documentation


Older single-ball machines (almost all EMs and most early solid state
machines) typically just have one switch and one coil and eject the ball from
the drain hole directly to the plunger lane, like this:

.. image:: /mechs/images/em_style_trough.jpg

You can actually configure older single ball, single coil troughs just like
modern troughs--it's just that there's only one switch and one
coil, but everything in Steps 3 and 4 below still apply.

Finally, if you don't have a
trough jam switch that's fine, just enter your other switches.