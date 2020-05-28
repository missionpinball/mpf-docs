Tutorial step 8: Add your plunger lane
======================================

In this step we're going to create your *plunger lane*
(or *shooter lane* or *ball launcher* or *catapult* or whatever you
want to call it).

This is the device that holds the ball after it's been ejected
from the trough or drain where it sits waiting for the player to
put it into play.

It's important to understand that a ball device is *anything that holds a ball*,
even if that's just a divot in the wood with no switch where the ball sits waiting for the
player to pull back on a spring plunger.

MPF's ball tracking only works if MPF knows where all the balls are at
all times, which is why it needs to "know" about the plunger lane, and you
let MPF know about a plunger lane by configuring it as another ball device.

1. Add your plunger/catapult/launcher/etc.
------------------------------------------

Like the trough, there are several different plunger designs. Some are
purely mechanical, some launch the ball with a button which fires
a coil, and some have both options. Also, some plunger lanes have
a switch which the ball sits on while it's waiting to be plunged,
and others don't.

Visit the :doc:`/mechs/plungers/index` documentation for pictures that
show each option and step-by-step guides which walk you through configuring
each type for MPF.

2. Revisit your trough/drain device and add it as source_device to your playfield
---------------------------------------------------------------------------------

Even though this is mentioned in the how-to guides, once you have your plunger
device set up, be sure to go back to your trough or ball drain device and add
the new plunger lane as an eject target, like this:

.. code-block:: yaml

   eject_targets: bd_plunger

Of course you'd add the name that you gave your plunger device, which could
be something like "bd_catapult" or whatever you called it.

Also, if you have a two-stage drain (like a System 11 machine), you'd add
this to the second device (the one that feeds the plunger).

Tell the playfield to use the plunger for new balls:

.. code-block:: mpf-config

   #! switches:
   #!   s_plunger:
   #!     number: 10
   #! ball_devices:
   #!   bd_plunger:
   #!     ball_switches: s_plunger
   #!     mechanical_eject: true
   playfields:
     playfield:
       tags: default
       default_source_device: bd_plunger


3. Check out the complete config.yaml file so far
-------------------------------------------------

Again, our example config will probably diverge from yours since you might have different types
of drain and plunger devices, but we do have a complete machine conform for Demolition Man
for this step which you can view in the ``mpf-examples/tutorial/step_8`` folder.

You can run this file directly by switching to that folder and then running the following command:

.. code-block:: doscon

   C:\mpf-examples\tutorial>mpf both

4. Fire up your game and test
-----------------------------

Unfortunately there are a few more things we need to configure before
you can play a full game, but if you want to test what you have so
far, you can launch MPF and drop a ball into your trough and you
should see some cool things in your log file. To do this,
launch the MPF game engine with the ``-v`` command line options so it
shows the verbose information in the log file, like this:

.. code-block:: doscon

    C:\pinball\your_machine>mpf -vbt

You don't have to launch the media controller this time since we're
just looking at the console output of the MPF game engine, which is
why we added the ``b`` command line option too. (The ``b`` option
tells the MPF game engine not to use the BCP protocol and not to
try to connect to the MC.)
You also have to add ``t`` to disable the text ui to see the verbose log.
Otherwise, you would only see the verbose output in the logfile in the ``logs``
directory of your machine.

Note: For more information about command line options take a look at 
:doc:`/running/commands/index` and :doc:`/running/commands/game`.

Once your game is running, drop a ball into your trough and you
should see a whole bunch of trough switches changing between active
(State: 1) and inactive (State: 0).

If you don't have a physical machine, you can run MPF with the ``-v`` option
and see a bunch of stuff in the log too by hitting the keyboard keys
for the trough switches which will add and remove balls.

Now quit MPF and open the MPF log file (which is in your machine's ``/logs``
folder). Grab the latest file with "mpf" in the name (if you ran ``mpf both``
then you'll have separate log files from MPF and the MC).

Search (or filter) the log for the name of your trough or drain device, and
you should see all sorts of interesting things. Here's a small snippet:

.. code-block:: console

   2016-11-18 03:54:06,103 : DEBUG : ball_device.bd_trough : Counting balls by checking switches
   2016-11-18 03:54:06,103 : DEBUG : ball_device.bd_trough : Confirmed active switch: s_trough1
   2016-11-18 03:54:06,103 : DEBUG : ball_device.bd_trough : Confirmed active switch: s_trough2
   2016-11-18 03:54:06,103 : DEBUG : ball_device.bd_trough : Confirmed active switch: s_trough3
   2016-11-18 03:54:06,103 : DEBUG : ball_device.bd_trough : Confirmed active switch: s_trough4
   2016-11-18 03:54:06,103 : DEBUG : ball_device.bd_trough : Confirmed active switch: s_trough5
   2016-11-18 03:54:06,103 : DEBUG : ball_device.bd_trough : Confirmed inactive switch: s_trough_jam
   2016-11-18 03:54:06,103 : DEBUG : ball_device.bd_trough : Counted 5 balls
   2016-11-18 03:54:06,103 : DEBUG : ball_device.bd_trough : Switching to state idle


What if it doesn't work?
------------------------

If you've gotten this far and your trough, drain, and/or plunger isn't working right, there
are a few things you can try:

If your log file shows a number of balls contained in one of your devices
doesn't match how many balls you actually have, that could be:

* You didn't add all the ball switches to the *ball_switches:*
  section of the device's config.
* Your trough uses opto switches but you didn't add *type: NC* to each switch's
  configuration.
* A a switch isn't adjusted properly so the ball is not actually activating it.
  (Seriously, we can't tell you how many times that's happened! We've also found that
  on some machines, if you only have one ball in the trough that the
  single ball isn't heavy enough to roll over the top of the eject coil
  shaft. In that case we just add a few more balls to the machine and it
  seems to take care of it.) Either way, if you have a ball in the
  trough, the switch entry in your log should show that the switch is
  active (*State:1*), like this:

::

    2014-10-27 20:05:29,891 : SwitchController : <<<<< switch: trough1, State:1 >>>>>

If you see State:1 immediately followed by another entry with State:0,
that means the ball isn't activating the switch even though it might
be in the trough.

If you get a YAML error, a "KeyError", or some other
weird MPF error, make sure that all the switch and coil names you
added to your ball device configs exactly match the switch and coil
names in the ``switches:`` and ``coils:`` sections of the machine config.

Also make sure that all your names are allowable names, meaning they are only
letters, numbers, and the underscore, and that none of your names start with a number.

Finally, make sure your YAML file is formatted properly, with spaces
(not tabs) and that you have no space to the left of your colons and
that you do have a space to the right of your colons.
See our :doc:`/troubleshooting/debugging_yaml_parse_errors` guide if you
got YAML errors.
At this point your trough is ready to go! Next we have to configure
your plunger lane.
