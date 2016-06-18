Tutorial step 8: Add your plunger lane
======================================

The previous step was really long since we had to go through all the
basics of what ball devices are and how they're configured. In this
step we're going to create a second ball device—-your *plunger lane*
(or *shooter lane* or *ball launcher* or *catapult* or whatever you
want to call it). We'll just call it the *plunger lane* in this
tutorial, but again, feel free to call it whatever makes you happy.

At this point you might be thinking, "Wha?? Why is this a thing?" Remember that
MPF attempts to keep track of where balls are at all times. So even if you have
a mechanically-operating spring-loaded plunger, MPF wants to know that a ball
it ejected from the trough has successfully made it out and landed in the
plunger lane, and it wants to know when a ball has left the plunger lane and
is heading for the playfield.

Remember that in MPF, a ball device is anything in a pinball machine that can
hold a ball, so the plunger lane is no exception. The exact settings
you use for the plunger lane will vary depending on the type of plunger
you have. Options include:


+ A mechanical plunger (where the player pulls on the spring knob to launch
  the ball).
+ A coil-powered ball launcher where the player hits a "launch" button
  which fires a coil to launch the ball.
+ A combination of both (where the player has the option to use a
  manual spring loaded plunger but where the machine can also use a coil
  to launch the ball).

Regardless of the type of plunger, all modern machines have one thing
in common: there's a switch in the plunger lane/catapult/whatever
which is active when a ball is sitting in the plunger waiting to be
fired. So in this step of the tutorial, we'll first get the plunger ball device
set up, and then if
you have a coil-powered plunger we'll walk through the additional
steps you need to configure that.

That said, what if your plunger lane
doesn't have a switch in it which is activated when a ball is sitting
at the plunger? (This is common is single ball machines, like EMs and
older solid state machines.) In this case you can't follow this step
in the tutorial since you don't have the switch. Instead check our
guide "How to configure plunger lanes that don't have plunger
switches". Then come back and continue with the next step of the tutorial.

1. Add your plunger lane switch
-------------------------------

The first thing to do is to add the switch in your plunger lane to
your list of switches in the ``switches:`` section of your config file.
By now this should be pretty easy for you:

::

    switches:
        s_left_flipper:
            number: 00
        s_right_flipper:
            number: 01
        s_trough1:
            number: 02
            type: NC
        s_trough2:
            number: 03
            type: NC
        s_trough3:
            number: 04
            type: NC
        s_trough4:
            number: 05
            type: NC
        s_trough5:
            number: 06
            type: NC
        s_trough6:
            number: 07
            type: NC
        s_trough_jam:
            number: 08
            type: NC
        s_plunger_lane:
            number: 09

Again, we're just using the number value of ``09`` as an example. If
you're following this tutorial with a physical machine then you'll
need to enter the number that corresponds to your physical switch.

2. Create your plunger ball device
----------------------------------

Next, go to the ``ball_devices:`` section of your config file and create
a new entry called ``bd_plunger:`` under your ``bd_trough:`` section. This
plunger entry should be at the same indent level as the trough (i.e. 4
spaces).

2a. Add your ball switch
~~~~~~~~~~~~~~~~~~~~~~~~

Under the line that defines your plunger, create an entry called
*ball_switches:* and add the name of the switch that you created in
Step 1. Even though this setting mentions "switches" (plural), your
plunger lane probably only has one switch since it only holds one
ball. (Though some have two switches for two balls. If that's your
scenario then add them both here.)

2b. Configure the eject timeout
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

One of the things we touched on but haven't really talked about is the
concept of eject confirmations. In MPF, a ball device needs to know
(to the best of its ability) that a ball that was supposed to eject
actually ejected properly.

MPF also knows which ball devices eject into other devices (as you'll see
shortly). So, for example, MPF knows that the trough ejects to the plunger lane,
and the plunger lane ejects to the playfield, and that a new ball entering the
trough either came from the playfield (drain) or the plunger lane (ball fell
back in). Knowing what's connected to what helps MPF keep things moving and not
get confused as balls do weird things.

Because of all this, MPF needs to "know" when a ball has successfully ejected
from one device and safely made it into another device. In scenarios where one
device ejects directly into another (e.g. trough to plunger), that eject
confirmation is pretty easy—-it just looks to see
when the ball made it into the target device and it knows that
everything went ok.

But with devices that eject to the playfield (such
as the plunger), it can get a bit tricky. If there are no balls on the
playfield, it's pretty easy to know when a ball made it out because as
soon as a playfield switch is hit, MPF knows there's a ball on the
playfield. But if there's already a ball on a playfield and then an
additional ball is ejected to the playfield, then when a playfield
switch is hit, MPF has no way of knowing whether that switch was hit
by the new ball or the existing ball.

Therefore when you configure a
ball device that ejects to the playfield, you need to configure an
*eject timeout* setting which basically says, "if you eject a ball and
the ball leaves (because the ball switch deactivated), and then the
ball doesn't come back after this amount of time, then MPF assumes the
ball made it out of the device."

The exact amount of time you should
use for your eject timeout depends on your machine. For a plunger
lane, you want to try to figure out what the longest possible time is
that a failed plunge could still end up with the ball coming back to
the plunger lane. If you have a manual spring plunger and an plunger
lane that wraps all the way up the side, the eject timeout could be 3
or 4 seconds. Even if you have a coil-fired eject plunger, you have to
set your timeout in case your coil gets weak and can't eject the ball
all the way.

So get out your stopwatch and put a ball in your plunger
lane and time how long it takes for the ball to go from the plunger to
the very end of the plunger lane, stop, and then roll back down to the
plunger. You'll have to play with this setting to get it right.

If it's set too short, then you could wind up with a scenario where you
have two balls in the plunger lane. (This could happen if you had an
eject timeout set for 2 seconds and your machine was adding a bunch of
balls into play for multiball. In this case 2 seconds after launch,
MPF would think the ball made it out and kick the next ball into the
plunger lane to eject it, but if the first ball didn't make it out and
was rolling back, then you'll have two balls stuck.)

It's probably
best to err on the longer side, since if your eject timeout is too
long that will just mean that you can't add lots of balls into play as
fast, but really if you're adding them at a 2 second pace or a 3
second pace, that shouldn't matter.

Anyway, once you decide what you
want your timeout to be, then create a setting in your plunger lane
for it, like ``eject_timeouts: 3s``. (Note that you can enter time
values in config files in seconds or milliseconds. By the way,
if you're wondering why that setting is
called ``eject_timeouts:`` (plural) instead of *eject_timeout:*
(singular), that's because MPF's ball devices are integrated with
diverter devices that are used to automatically route balls to
different locations, and each location can have its own timeout. But
for now you just need to enter the one and if you have diverters and
stuff you can configure those once you're done with the tutorial.

2d. Add the tags
~~~~~~~~~~~~~~~~

Like the trough, there's a magic tag we need to add to our plunger
lane: ``ball_add_live``. The ``ball_add_live`` tag is used to tell MPF
that this ball device should be used to add a live ball into play. The
way it works is when MPF's game controller wants to add a ball into
play (typically at the start of a ball), it looks for a device tagged
with ``ball_add_live`` and makes sure that device has a ball that can be
ejected. (And if that device doesn't have a ball, it will request one. Since
MPF knows which ball devices feed other devices, MPF knows to request a ball
eject from the trough if the plunger needs a ball.)

You add this tag by adding a line ``tags: ball_add_live``. At
this point your plunger lane ball device configuration should look something
like this:

::

        bd_plunger:
            ball_switches: s_plunger_lane
            eject_timeouts: 3s
            tags: ball_add_live


3. Configure your human-power spring plunger
--------------------------------------------

If your plunger has a traditional mechanical spring-driven human-powered
plunger, then you need to add another configuration option which is
``mechanical_eject: true``.

Add this option any time the player can manually eject a ball, even if your
pluger also has a coil-powered eject.


The reason you need to add this is that MPF likes to
know what's going on with all the balls at all times. If you have a
mechanical plunger, when the player plunges the ball, from MPF's
perspective it's like the ball just vanished! So setting the
``mechanical_eject: true`` lets MPF know that if the ball just
disappears then that means the player ejected it and MPF needs to look
for the ball to end up in the target device. So if this applies to
your plunger, then your plunger device config should look like this:

::

        bd_plunger:
            ball_switches: s_plunger_lane
            eject_timeouts: 3s
            tags: ball_add_live
            mechanical_eject: true

Again, if your plunger has both a mechanical eject and a coil-fired eject,
then go ahead and add *mechanical_eject: true* here.

4. Add your coil for coil-fired plungers
----------------------------------------

If you have a coil-fired ball launcher or plunger, you can configure
that now too. To do this:


4a. Add the coil to your coils: configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First, add an entry for your plunger lane eject coil to the ``coils:``
section of your config file. Your complete section will probably now
look something like this:

::

    coils:
        c_flipper_left_main:
            number: 00
            pulse_ms: 25
        c_flipper_left_hold:
            number: 01
        c_flipper_right_main:
            number: 02
            pulse_ms: 25
        c_flipper_right_hold:
            number: 03
        c_trough_eject:
            number: 04
            pulse_ms: 25
        c_plunger_eject:
            number: 05
            pulse_ms: 25

Again, if you have physical hardware then make sure your new coil's
``number:`` is accurate, and remember you can adjust the ``pulse_ms:``
setting here if your plunger eject ends up being too strong or too
weak.

4b. Add your eject coil to your plunger
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Next add your newly-entered coil name to your plunger ball device
configuration so MPF knows that's the coil that should be used to
eject a ball from that device. Based on the entry from Step 4a above,
that would be ``eject_coil: c_plunger_eject``.

4c. Add your plunger eject switch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If your plunger device is coil-fired, and if you want the player to
hit a button to launch a ball into play, then you can set up that
switch now. To do this, add that switch to the ``switches:`` section of
your config. You also need to add a tag to that switch entry which is
how MPF will know that switch is the one that will be used to launch
the ball from the plunger. We typically call that tag "launch". So you
would add the following to the switches: section of your config:

::

        s_launch_button:
            number: 09
            tags: launch


Note that if you have a plunger lane with both a spring-powered
plunger and a coil-fired eject, it's possible that you don't actually
have a launch button. (Many Stern games are like this.) In those cases
the coil is only used for ball save and to auto-launch balls for
multiball, so it's possible that you will still add the ``eject_coil:``
to your plunger but you won't actually wire up a switch to it in this
step and the next one.

4d. Configure your plunger to eject based on the launch button
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you configured a switch to launch the ball in the previous step,
now go back to your plunger ball device and add a setting so that the
plunger knows it should eject a ball based on the switch you just
setup. To do that, create an entry called
``player_controlled_eject_event:`` and then set the value to ``sw_``
followed by the name of the tag you just added to your launch button.
(For example, ``sw_launch``.)

The reason this works is because by
default, when you add tags to switches, whenever that switch is
activated then MPF posts an event with the name ``sw_<tag_name>``. So
every time you hit a switch tagged with ``launch``, MPF will post an
event called ``sw_launch``. (Don't worry-—this event won't actually
launch a ball from the plunger every time that switch is hit. It's
just used when a player-controlled eject is setup from that device
which is what MPF does with the ball device tagged with
``ball_add_live`` whenever a new ball starts.) So now your plunger ball
device config will look something like this:

::

        bd_plunger:
            ball_switches: s_plunger_lane
            eject_timeouts: 3s
            tags: ball_add_live
            eject_coil: c_plunger_eject
            player_controlled_eject_event: sw_launch


If you have a dual spring/coil fired plunger, you'll also have the
``mechanical_eject: true`` setting in there.

5. Go back to your trough device and reconfigure its eject settings
-------------------------------------------------------------------

We talked a little bit about how MPF is able to confirm ball ejects
because it "knows" which ball devices eject into other devices. In
other words when the trough attempts to eject a ball, it will watch
the plunger device, and when the plunger device receives a ball, the
trough will mark its eject as successful.

Now that you have a plunger
device setup, you can go back to the trough settings and configure its
eject target. To do this, in the ``bd_trough:`` ball device settings,
create a new entry called ``eject_targets:`` with a value of
``bd_plunger``. This tells the trough that the ``bd_plunger`` ball device
is the target of its ejects. (The ``eject_targets:`` setting can
actually be a list of more than one device, but in this case the
trough only ejects to one place—-the plunger-—so we only need one entry
here.)

This ``eject_targets:`` entry is used for a few things.

First, as we already mentioned, configuring a target device is how the trough
knows which ball device to watch to know that an eject was successful. A
ball device configured with ``eject_targets:`` setting will also monitor
the target devices to see if any of them ever wants a ball. For
example, remember before we added the tag ``ball_add_live`` to the
plunger device. This means that when MPF wants to launch a ball into
play, it will go to the device tagged with ``ball_add_live`` and ask
that device make sure it has a ball. What happens if that device
doesn't have any balls to eject? In that case the plunger device would
post an event that says, "I want a ball!" And the trough device, since
its target device is the plunger device, would say, "Hey! I have a
ball and I can give it to you." So by linking your devices together
via the ``eject_targets:`` settings you can set up a ball path which
ensures that any device that needs a ball can get it. (By the way,
every ball device needs to have at least one eject target since the
balls have to go somewhere. If you don't explicitly add
``eject_targets:`` to a ball device config, then MPF assumes that device
ejects to the playfield. This is why we don't have to add an
``eject_targets:`` setting to the plunger.) Now your trough device
should look like this:

::

    ball_devices:
        bd_trough:
            ball_switches: s_trough1, s_trough2, s_trough3, s_trough4, s_trough5, s_trough6, s_trough_jam
            entrance_count_delay: 300ms
            eject_coil: c_trough_eject
            tags: trough, home, drain
            debug: yes
            eject_targets: bd_plunger

6. Verify your trough and plunger ball device settings
-------------------------------------------------------

At this point you can go back and look at both your trough and plunger
ball device settings to make sure everything looks good. Something
like this:

::

    ball_devices:
      bd_trough:
        tags: trough, home, drain
        ball_switches: s_trough1, s_trough2, s_trough3, s_trough4, s_trough5, s_trough_jam
        eject_coil: c_trough_eject
        jam_switch: s_trough_jam
        eject_targets: bd_plunger
        debug: yes
      bd_plunger:
        ball_switches: s_plunger_lane
        eject_timeouts: 3s
        tags: ball_add_live
        eject_coil: c_plunger_eject
        player_controlled_eject_event: sw_launch

At this point we like to run the game in software only mode just to
make sure everything starts properly and that we don't have any typos.
You don't event need to launch the media controller for this, so you
can just launch the MPF core engine like this:

::

    C:\Pinball\your_machine>mpf -x -v

(Remember the ``-x`` forces MPF to run in "virtual" mode and not connect to
physical hardware.)

You can quit (``CTRL+C``) once everything is settled. If you
scroll through the log files you should see information about both
your trough and plunger, as well as a bunch of other things going on
that we don't have to worry about yet.

7. Add a keyboard entries
--------------------------

If you're keeping your keyboard shortcuts up to date, you might also
want to create a keyboard entry for your plunger lane switch. Like the
entry for your trough switches, you'll want to include ``toggle: true``
so you don't have to hold down the key constantly to simulate a ball
being in the plunger. At this point the keyboard layout is getting
confusing, so who knows what key is best for the plunger lane. Maybe
``P``? So you could make an entry like this to the `keyboard:` section of
your config file:

::

        p:
            switch: s_plunger_lane
            toggle: true

If you have a launch button for a coil-fired plunger, add that too:

::

        L:
            switch: s_launch_button

Note that the launch button switch is not a toggle switch, and also
notice that we add an uppercase letter "L". The case of letters for
keys doesn't matter, but since a lowercase L and the number 1 look
similar, we decided to add "L" in uppercase.


At this point we're
really close to being able to play a game! Next is to create a start
button (and a launch button if you have a coil-fired plunger), add a
few more ball options, and we're off and running a real game!

Check out the complete config.yaml file so far
----------------------------------------------

If you want to see a complete ``config.yaml`` file up to this point, it's in the ``mpf-examples/tutorial``
folder with the name ``step8.yaml``.

You can run this file directly by switching to that folder and then running the following command:

::

   C:\mpf-examples\tutorial>mpf both -c step8
