Tutorial step 7: Add your trough
================================

At this point you have a flipping machine with a display, but you don't
have a "working" pinball machine since you can't start or play games.

So the next two steps in this tutorial, we're going to get your first two
*ball devices* set up—your trough and plunger lane.
(A ball device is anything in MPF that holds a ball).

1. Read about ball devices
--------------------------

In MPF, a "ball device" is any physical mechanism in your machine that
holds a ball.

You can read more about ball devices in the :doc:`/mechs/ball_devices/index`
documentation, which we recommend that you do now to familiarize yourself
with the concepts. (You don't have to understand everything about them
for now, just skim through that link so you get the basics.)

2. Add your trough and/or drain
-------------------------------

Now that you understand what a ball device is, lets add your first ball device,
which is going to be trough (or drain) device which collects balls that
drain from the playfield and stores them while they're not in play.

Since there are so many different types of ball drain and trough
configurations, we can't write a single tutorial that walks you through
all of them.

Instead, we have several tutorials. :)

So your next step is to visit the :doc:`/mechs/troughs/index` documentation
which lists all the options (with pictures), as well as links to
step-by-step guides which walk you through the setup of the particular
type of trough or ball drain you have in your machine.

3. Enable debugging so you can see cool stuff in the log
--------------------------------------------------------

Once you have your trough or drain device (or devices, in some cases)
set up, add one more setting to that device:

.. code-block:: yaml

   debug: true

This setting causes MPF to write detailed debugging information about this
ball device to the log file. You have to run MPF with the ``-v`` (verbose)
option to see this.

This will come in handy in the future as you're trying to debug
things, and it's nice because you can just turn on debugging for the
things you're troubleshooting at that moment which helps keep the
debug log from filling up with too much gunk.

For example, if you have a modern style trough with a jam switch, you'd
add the debug setting like this:

.. code-block:: mpf-config

    #! switches:
    #!   s_trough1:
    #!     number: 1
    #!   s_trough2:
    #!     number: 2
    #!   s_trough3:
    #!     number: 3
    #!   s_trough4:
    #!     number: 4
    #!   s_trough5:
    #!     number: 5
    #!   s_trough6:
    #!     number: 6
    #!   s_trough_jam:
    #!     number: 7
    #! coils:
    #!   c_trough_eject:
    #!     number: 3
    ball_devices:
      bd_trough:
        ball_switches: s_trough1, s_trough2, s_trough3, s_trough4, s_trough5, s_trough6, s_trough_jam
        eject_coil: c_trough_eject
        tags: trough, home, drain
        jam_switch: s_trough_jam
        eject_coil_jam_pulse: 15ms
        debug: true

4. Don't test yet
-----------------

Since the trough or drain device works hand-in-hand with the plunger lane,
and since we haven't set up a plunger lane yet, it's not worth testing your
config at this point. We'll get the plunger lane set up in the next step.

Check out the complete config.yaml file so far
----------------------------------------------

If you're following along with the example tutorial configurations, at this
point there could be some significant divergence between the examples and
your machine since the examples are based on a Demolition Man machine with
a modern opto-based trough.

We still have the examples which you can try, and they'll work fine because
they use the "virtual" platform which doesn't connect to real hardware. So
you can run them and follow along, but just be aware that they might not
match your own files exactly.

The complete machine config is in the ``mpf-examples/tutorial/step_7``
folder.

You can run this file directly by switching to that folder and then running the following command:

.. code-block:: doscon

   C:\mpf-examples\tutorial>mpf both
