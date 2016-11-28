Plunger lanes with no ball switch
=================================

Modern pinball machines have a switch in the plunger lane that tells
the software that a ball is sitting in the plunger lane waiting to
be plunged.

This document describes how you configure MPF to work with plunger
lanes when the plunger lane has no switch which is active when a ball
is sitting at the plunger. (This is common is older single-ball
machines, including many EM and early solid state machines.)

Here's an example from a Gottlieb Big Shot

.. image:: /mechs/images/plunger_no_switch.jpg

.. literalinclude:: /example_configs/ball_device/config/test_ball_device_no_plunger_switch.yaml
   :language: yaml

1. Configure your trough / ball drain
-------------------------------------

MPF's plunger lanes work hand-in-hand with the trough / ball drain
devices. So if you haven't configured that yet, go back and
:doc:`do that now </mechs/troughs/index>`, then come back here and
configure your plunger.

2. Understand that your plunger is *not* a ball device
------------------------------------------------------

Most pinball machines have a switch in the plunger lane which is used
to tell MPF that there's a ball in the plunger waiting to be plunged.

However, this How To guide is for plunger lanes with no ball switch. (If
your plunger lane has a ball switch, then follow the
:doc:`mechanical_with_switch` guide instead.)

In machines where the plunger lane does not have a ball switch, that means
that MPF has no idea whether a ball is in the plunger lane. That's totally
fine, and MPF can support that no problem. However, in this case,
*you do not configure your plunger lane as a ball device*!

Instead the plunger lane area is considered part playfield, so a ball in the
plunger lane that's not sitting on a switch is just like any other area of the
playfield where the ball might be rolling around while it's not on a switch.

3. Add a ball_add_live tag to your trough
-----------------------------------------

In machines where the plunger lane is a ball device, we add a tag called
``ball_add_live`` to the plunger ball device. The "ball_add_live" tag
is used to tell MPF that this is the device which is used (by default) to
add a live ball into play.

But since your plunger lane with no switch is not a ball device, that means
we have to go back to the trough ball device and add the ``ball_add_live``
tag to it. (Your trough device will already have the ``trough`` tag applied
to it, and depending on how your machine is laid it, it might also have the
``ball_drain`` tag applied.)

So add ``ball_add_live`` to your trough now.

Then when MPF needs to add a live ball into play, it will eject a ball
from the trough and you're all set!

4. What happens if MPF starts with a ball in the plunger?
---------------------------------------------------------

One of the downsides to not having a switch in the plunger lane is that MPF
has no way of knowing if there's a ball in there. Throughout the ordinary
course of operation, this is fine, because MPF "knows" that the trough ejected
a ball, and it "knows" when the ball is on the playfield, so if the trough has
ejected a ball and that ball hasn't yet entered the playfield, MPF can
"assume" that ball is in the plunger lane.

However, what happens if MPF boots up from scratch and there's a ball in the
plunger lane? In that case, the ball is not activating any switches, so MPF
really has no idea if the ball is in the plunger line (which is fine) or if
the ball is stuck somewhere on the playfield (which is not fine).

TODO: This does not work yet and will be fixed soon.

5. Configuring the ball save timer
----------------------------------

Be sure to set your ball save start event based on a tag from your switches
tagged with ``playfield_active`` rather than *ball_starting* or your trough eject
confirmation, since you don't want the timer to start running when the ball is
sitting in the plunger lane.

See the :doc:`/game_logic/ball_saves/index` documentation for details.
