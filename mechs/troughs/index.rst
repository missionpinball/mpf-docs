Ball Troughs / Drain Devices
============================

Every pinball machine will have some kind of ball trough / drain device. This
is the place where the balls go when they drain from the playfield before
they're ejected into the plunger lane.

In many cases, this device (or series of devices) holds multiple balls and is
the location where unused balls are stored.

There are several different designs for troughs and drains that have been used
over the past 70 years, and (as far as we know), MPF supports all of them.
So regardless of what's in your machine, we're talking about whatever is under
here:

.. image:: /mechs/images/trough_drain.jpg

Here are the options:

.. toctree::
   :maxdepth: 1

   Modern trough with opto sensors <modern_opto>
   Modern trough with mechanical switches <modern_mechanical>
   Older style with two coils and switches for each ball <two_coil_multiple_switches>
   Older style with two coils and only one ball switch <two_coil_one_switch>
   Classic single ball, single coil <classic_single_ball>

Since there are so many different options, you need to first identify which
type of trough or ball drain system your machine has. So look at the following
pictures to match up what you have, and then follow the specific links to see
how to configure MPF to use it in your machine.

Option 1: Modern trough with opto sensors
-----------------------------------------

Modern-style troughs (which have been used since about 1993 or so) are mostly
located underneath the playfield and hold the balls at an incline so they roll
down to the end. There is a single coil which fires to eject a ball up and out
where it's directed to the plunger lane.

The advantage of modern troughs are (1) the balls entering are gravity-fed,
meaning they only need one coil, and (2) they can hold a lot of balls. (Most
hold 4-6 balls but you can buy ones that hold up to 8.)

If you have a modern-style trough with a circuit board on each side, that means
your trough uses opto sensors to detect the presence of a ball. One of those
circuit boards contains infrared LEDs which are always on which shoot invisible
beams across the ball paths, and the board has sensors that detect if a light
beam is broken, meaning a ball is sitting there blocking the path.

If you have a modern trough with opto sensors, read the :doc:`modern_opto`
guide to continue.

Option 2: Modern trough with mechanical switches
------------------------------------------------

If you have a modern-style trough with mechanical switches instead of opto
boards, then read the :doc:`modern_mechanical` guide to continue.

Option 3: Older style with two coils and switches for each ball
---------------------------------------------------------------

Many machines from the 1980s and early 1990s have a ball trough system that
consists of two separate coils and which sits entirely on top of the playfield
underneath the apron.

In this case, when a ball drains, a coil in the drain area fires to shoot the
ball up over a hump where it's stored. Then a second coil near the plunger lane
is used to eject a single ball at a time into the plunger lane.

Some of these types of devices have multiple switches on the side that stores
the ball, with one switch for each ball. That allows the machine to know
exactly how many balls are there because each ball is sitting on a switch.

If you have this kind of trough system, read the
:doc:`two_coil_multiple_switches` guide to continue.

Option 4: Older style with two coils and only one ball switch
-------------------------------------------------------------

If you have a system that is similar to Option 3 above, but instead of one
switch for each ball, you only have one switch total on the right side, then
read the :doc:`two_coil_one_switch` guide to continue.

Option 5: Classic single ball, single coil
------------------------------------------

Older single-ball machines have a trough system that is on top of the playfield
under the apron, but they only have a single coil near the ball drain position.
The ball is stored in teh drain area, and when it needs to be ejected, a coil
fires it from the drain all the way into the plunger lane in a single action.

If you have a system like this, read the :doc:`classic_single_ball` guide to
continue.

Option 6: Something we haven't seen yet
---------------------------------------

If you're using MPF with a machine that has some kind of trough or drain system
that we haven't covered here, we would like to know about it so we can write a
how to guide and/or add support for it in MPF.

If that's your case, please `post a message to the MPF Users Google Group
<https://groups.google.com/forum/#!forum/mpf-users>`_ and we'll go from there.
