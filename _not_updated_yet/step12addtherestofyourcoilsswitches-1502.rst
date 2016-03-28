
Okay, so at this point you have a working game. The biggest problem
you might run into is that if you shoot your ball into a playfield
device like a VUK or popper, the ball will get stuck. Why? Because you
haven't yet added the switches to your config file while let MPF know
that a ball is there, and you haven't added the coils which MPF needs
to fire to eject a ball. So MPF literally has no idea that those
switches and coils even exist, which means it has no ability to detect
a ball entering a device and to eject it. So when we're building a
config for a new game, at this point we go through our config and add
all the remaining switches and coils to and `switches:`and `coils:`
sections of the config file.



(A) Add the rest ofyour switches
--------------------------------

This step is pretty simple. We usually use the operators manual as our
starting point and just move down the list and add all the switches as
they're listed in there. We don't worry about tags at this point
*except for* `playfield_active` tag. We add this tag to any switch the
ball can hit when it's active and rolling around on the playfield. (So
this is going to be your lanes, slingshots, pop bumpers, ramp entry &
exit switches, rollovers, stand up targets, drop targets, and anything
else the ball can hit when it's in motion. The tricky thing is that
you do not add a `playfield_active` tag to switches in other ball
devices. For example, if you have a hole in the playfield that the
ball rolls into which requires a coil pulse to kick it out of—that is
not a playfield switch (since when the ball is in that hole, it's not
actively rolling around the playfield). We'll actually set that switch
up as a part of a ball device in a later step.



(B) Add the rest ofyour coils
-----------------------------

Next add entries for the rest of your coils, again using the operators
manual as a guide if you're building a config for an existing machine.
You don't have to worry about pulse times at this point—just get the
coils added.



Check out the complete config.yaml file so far
----------------------------------------------

If you want to see a complete `config.yaml` file up to this point for
a *Demolition Man* machine, it’s available in the MPF package at
`<your_mpf_root>/machine_files/tutorial/config/step12.yaml`. (You need
to rename this file to `config.yaml` to use it.) And remember if
you’re using physical hardware, your coil and switch numbers will be
different than the ones in the sample file, since you’ll need to
configure them based on your driver boards’ actual inputs and outputs.



