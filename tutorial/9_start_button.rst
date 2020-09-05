Tutorial step 9. Add the start button
=====================================

Obviously in order to play an actual game, you have to be able to
start a game, and that requires a start button. So let's add that now.

1. Add a switch for your Start button
-------------------------------------

First, add the switch for your start button to the ``switches:`` section
of your config file. Again this should be easy by now. In this
tutorial we'll just call this button ``s_start`` and add it like this:

.. code-block:: mpf-config

   switches:
     s_start:
       number: 11

2. Add a "start" tag to your Start button
-----------------------------------------

Just like the special-purpose tags we used when configuring the ball
devices, MPF uses some :doc:`special purpose tags for switches </config/switches>`, too. One of
them is ``start``, as MPF watches for switches tagged with "start" to
start games and add players to running games.

Sometimes people ask
"Why do you use a tag for this? Why not just look for a switch named
"start?" Again, we want MPF to be as flexible as possible, and we
feel that game builders should be able to name their switches whatever
they want. (Some want to preface with ``s_``, others might not, etc.) So
we use a "start" tag behind the scenes to make whatever switch you
want act as the start button. So now your start switch in your
``switches:`` section should look like this:

.. code-block:: mpf-config

   switches:
     s_start:
       number: 11
       tags: start

3. Add keyboard entries for your start switch
---------------------------------------------

If you're keeping your keyboard shortcuts up to date, you can create a
keyboard entry for your start switch. This is especially helpful if
you're building a custom machine from scratch and you don't have a
physical start button wired up yet. In that case just enter some dummy
value for the ``number:`` of your start switch. Then when you run a
physical machine (without the -x command line option), you can start
the game with your computer keyboard but actually play it on physical
hardware. For your start button keyboard key, how about using the ``S``
key? To do so, add an entry like this to the ``keyboard:`` section of
your config file:

.. code-block:: mpf-config

   keyboard:
     s:
       switch: s_start

4. Add at least one playfield switch
------------------------------------

Another thing you need to do is to configure at least one playfield
switch. Why? Because when a ball is launched from your plunger onto
the playfield, MPF "confirms" that the ball actually made it onto the
playfield when a playfield switch is activated. How do you configure a
switch as a playfield switch? You use tags, by adding a
``playfield_active`` tag to a switch.

At this point you might be
wondering, "Wait, I thought the eject_timeouts for the plunger was
used to let MPF know when a ball really made it out of the plunger?"
That's true, and technically at this point you don't need a playfield
switch. However, this will speed up your ejects in a real machine and
you'll eventually tag all your playfield switches with
``playfield_active``, so we're just getting starting on this now. To do
this, create a new entry in your ``switches:`` section for one of your
playfield switches, for example:

.. code-block:: mpf-config

   switches:
     s_right_inlane:
       number: 12
       tags: playfield_active

Note: The tags playfield_active and above the start tag are :doc:`special 
purpose tags for switches </config/switches>`.

While you're at it, create a keyboard key mapping for this switch in
the ``keyboard:`` section of your config, like this:

.. code-block:: mpf-config

   keyboard:
     q:
       switch: s_right_inlane

If you want you can go ahead and add entries for all your playfield
switches, though that will take awhile. For now just make sure you
have at least one, and make sure the ball hits that switch after it
launches from the plunger before it drains. (There are lots of options
for what you can do if a ball drains before it hits a switch, but
we're not going to go into those now.)

If you do decide to add all
your playfield switches now, you'll want to add the *playfield_active*
tag to all the switches that might be hit by a ball being loose on the
playfield. (So lane switches, ramp switches, rollovers, standups etc.)
You do *not* want to tag ball device switches with
``playfield_active`` since if a ball is in a ball device, then it's not
loose on the playfield.

At this point we're really, really close!
There are a few more quick things we want to do, then run some checks.
But then we're ready to play a real game!

Check out the complete config.yaml file so far
----------------------------------------------

If you want to see a complete ``config.yaml`` file up to this point, it's in the ``mpf-examples/tutorial/step_9``
folder.

You can run this file directly by switching to that folder and then running the following command:

.. code-block:: doscon

   C:\mpf-examples\tutorial>mpf both
