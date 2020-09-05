Tutorial step 11: Add the rest of your coils and switches
=========================================================

Okay, so at this point you have a working game. The biggest problem
you might run into is that if you shoot your ball into a playfield
device like a VUK or popper, the ball will get stuck. Why? Because you
haven't yet added the switches to your config file while let MPF know
that a ball is there, and you haven't added the coils which MPF needs
to fire to eject a ball. So MPF literally has no idea that those
switches and coils even exist, which means it has no ability to detect
a ball entering a device and to eject it. So when we're building a
config for a new game, at this point we go through our config and add
all the remaining switches and coils to and ``switches:`` and ``coils:``
sections of the config file.

1. Add the rest of your switches
--------------------------------

This step is pretty simple. If you building a config for an existing
machine, we usually use the operators manual as our
starting point and just move down the list and add all the switches as
they're listed in there. We don't worry about tags at this point
*except for* ``playfield_active`` tag. We add this tag to any switch the
ball can hit when it's active and rolling around on the playfield. (So
this is going to be your lanes, slingshots, pop bumpers, ramp entry &
exit switches, rollovers, stand up targets, and anything
else the ball can hit when it's in motion. The tricky thing is that
you do not add a ``playfield_active`` tag to switches in other ball
devices (drop_targets, kickbacks, troughs or the shooter lane).
For example, if you have a hole in the playfield that the
ball rolls into which requires a coil pulse to kick it out of -- that is
not a playfield switch (since when the ball is in that hole, it's not
actively rolling around the playfield). We'll actually set that switch
up as a part of a ball device in a later step.

2. Add the rest of your coils
-----------------------------

Next add entries for the rest of your coils, again using the operators
manual as a guide if you're building a config for an existing machine.
You don't have to worry about pulse times at this point—just get the
coils added.

Check out the complete config.yaml file so far
----------------------------------------------

If you want to see a complete ``config.yaml`` file up to this point, it's in the ``mpf-examples/tutorial/step_11``
folder.

You can run this file directly by switching to that folder and then running the following command:

.. code-block:: doscon

   C:\mpf-examples\tutorial>mpf both -X

Note that starting with this step, the actual coil, switch, and ball_device names don't 100% match
with what we have in the tutorial. This shows you that there are lots of different options when it
comes to naming things.

