Lane Mode
=========

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/mode`                                                          |
+------------------------------------------------------------------------------+
| :doc:`/config/shots`                                                         |
+------------------------------------------------------------------------------+
| :doc:`/config/shot_groups`                                                   |
+------------------------------------------------------------------------------+
| :doc:`/config/variable_player`                                               |
+------------------------------------------------------------------------------+
| :doc:`/config/show_player`                                                   |
+------------------------------------------------------------------------------+

In this How To guide, we're going to look at how you can set up a
series of lanes with lights (or standup targets) which you can rotate
with the flipper buttons. We'll also look at how you can play a light
show when they're complete and assign scoring. "Lane change" is a
fairly popular thing in pinball machines, typically with a set of
lanes at the top of the machine. They start all off, and then as you
roll over them they light up. You can use the flippers to cycle
through which lanes are lit, and when they're all lit, you get a score
(or increase the bonus multiplier, etc.) For this how to guide we'll
use a Williams Indiana Jones machine. Here's a video that shows the
final result of building everything we outline in this guide.

`See it in action <https://www.youtube.com/watch?v=4Ip60PVe-oQ>`_.

Let's begin!


(A) Configure your devices
--------------------------

We'll assume that you already have your switches and lights defined in
the ``switches:`` and ``lights:`` section of your machine-wide config. (If
you have RGB LEDs, you can follow this tutorial also—just substitute
``leds:`` for ``lights:``.)

Next you need to define your ``shots``, which
is where you pair your switches and lights so you know that Switch A
is associated with Light B, and so on.

Do this in your base mode configuration (in ``/modes/base/config/base.yaml``),
following the documentation for the ``shots:`` section in the configuration
file reference.
In Indiana Jones, we've given the lights and switches the same names
(which is ok since they're different types of devices), so our ``shots:``
section looks like this:

.. code-block:: mpf-config

   #! switches:
   #!   indy_i:
   #!     number: 1
   #!   indy_n:
   #!     number: 2
   #!   indy_d:
   #!     number: 3
   #!   indy_y:
   #!     number: 4
   #! lights:
   #!   indy_i:
   #!     number: 1
   #!   indy_n:
   #!     number: 2
   #!   indy_d:
   #!     number: 3
   #!   indy_y:
   #!     number: 4
   ##! mode: base
   shots:
     indy_i:
       switch: indy_i
       show_tokens:
         light: indy_i
     indy_n:
       switch: indy_n
       show_tokens:
         light: indy_n
     indy_d:
       switch: indy_d
       show_tokens:
         light: indy_d
     indy_y:
       switch: indy_y
       show_tokens:
         light: indy_y


Next, configure a ``shot group``, which is where you can group
individual shots together so you can interact with as a single group,
like this:


.. code-block:: mpf-config

   #! switches:
   #!   indy_i:
   #!     number: 1
   #!   indy_n:
   #!     number: 2
   #!   indy_d:
   #!     number: 3
   #!   indy_y:
   #!     number: 4
   #! lights:
   #!   indy_i:
   #!     number: 1
   #!   indy_n:
   #!     number: 2
   #!   indy_d:
   #!     number: 3
   #!   indy_y:
   #!     number: 4
   ##! mode: base
   #! shots:
   #!   indy_i:
   #!     switch: indy_i
   #!     show_tokens:
   #!       light: indy_i
   #!   indy_n:
   #!     switch: indy_n
   #!     show_tokens:
   #!       light: indy_n
   #!   indy_d:
   #!     switch: indy_d
   #!     show_tokens:
   #!       light: indy_d
   #!   indy_y:
   #!     switch: indy_y
   #!     show_tokens:
   #!       light: indy_y
   shot_groups:
     indy_lanes:
       shots: indy_i, indy_n, indy_d, indy_y


Note that the order of your shots is important since that's how MPF
knows the order of them in order to do shot rotation (more on that
later.) At this point if you run MPF and start a game, if you hit one
of your shots then you should see the light turn on. (How does MPF
know this? Because you haven't specified a shot profile for these
shots, so MPF uses the default ``shot profile`` which has them in an
unlit state at first and then lights them once they're hit.) Notice
that if you hit the flippers they don't rotate, and once you light all
the shots they just stay on. We'll change both those behaviors next!
Also notice that the states of the shots are stored per-player. If you
play and drain a ball, when you start the next ball, the shots will be
in the same state before they drained. Also note that if you start a
multi-player game, the shots will reset when the second player starts
since that player hasn't hit any yet, and when the first player goes
to Ball 2, MPF will reset the shots back to what the first player had.



(B) Configure shot rotation
---------------------------

Next, let's configure the shots so that their lit/unlit states rotate
(or shift) to the left or right when the player hits the flipper. This
step is optional of course. In some situations you might not want your
shots to rotate (like the ADVENTURE standups in Indiana Jones where
the player has to hit all the shots to light the Path of Adventure).
To do this, we have to configure the shot group for rotation events.
We configure two different events—one to rotate left and one to rotate
right. You can actually configure rotation events in either your
machine-wide config or in a mode-specific config. If you do it
machine-wide, then the rotation events will always be active. If you
configure it in a mode config, then they're only active as long as
that mode's active. In this tutorial we're going to configure them in
the base mode as well but you could put that group in any other mode
and load/unload it as you need it.

.. code-block:: mpf-config

   #! switches:
   #!   indy_i:
   #!     number: 1
   #!   indy_n:
   #!     number: 2
   #!   indy_d:
   #!     number: 3
   #!   indy_y:
   #!     number: 4
   #! lights:
   #!   indy_i:
   #!     number: 1
   #!   indy_n:
   #!     number: 2
   #!   indy_d:
   #!     number: 3
   #!   indy_y:
   #!     number: 4
   ##! mode: base
   #! shots:
   #!   indy_i:
   #!     switch: indy_i
   #!     show_tokens:
   #!       light: indy_i
   #!   indy_n:
   #!     switch: indy_n
   #!     show_tokens:
   #!       light: indy_n
   #!   indy_d:
   #!     switch: indy_d
   #!     show_tokens:
   #!       light: indy_d
   #!   indy_y:
   #!     switch: indy_y
   #!     show_tokens:
   #!       light: indy_y
   shot_groups:
     indy_lanes:
       shots: indy_i, indy_n, indy_d, indy_y
       rotate_left_events: left_flipper_active
       rotate_right_events: right_flipper_active


You can specify whatever event name(s) you want for your rotation events.
By default, MPF will post
:doc:`(switch_name)_active </events/switch_active>` when every switch in the
game activates.
So in our case, our flipper buttons from the machine-wide switches: section
are named ``left_flipper`` and ``right_flipper``. If you named your switch
``s_lower_left_flipper_button``, then your event name would be
``s_lower_left_flipper_button_active``. Some older pinball machines only
rotate lane shots to the right, regardless of which flipper button is
pressed. In that case you'd only have an entry for
rotate_right_events, but you'd add both the left and right flipper
events, like this:


.. code-block:: mpf-config

   #! switches:
   #!   indy_i:
   #!     number: 1
   #!   indy_n:
   #!     number: 2
   #!   indy_d:
   #!     number: 3
   #!   indy_y:
   #!     number: 4
   #! lights:
   #!   indy_i:
   #!     number: 1
   #!   indy_n:
   #!     number: 2
   #!   indy_d:
   #!     number: 3
   #!   indy_y:
   #!     number: 4
   ##! mode: base
   #! shots:
   #!   indy_i:
   #!     switch: indy_i
   #!     show_tokens:
   #!       light: indy_i
   #!   indy_n:
   #!     switch: indy_n
   #!     show_tokens:
   #!       light: indy_n
   #!   indy_d:
   #!     switch: indy_d
   #!     show_tokens:
   #!       light: indy_d
   #!   indy_y:
   #!     switch: indy_y
   #!     show_tokens:
   #!       light: indy_y
   shot_groups:
     indy_lanes:
       shots: indy_i, indy_n, indy_d, indy_y
       rotate_right_events: left_flipper_active, right_flipper_active

Of course you can use whatever event(s) you want to rotate the shots.
Many System 11 machines had lit shots in the inlanes and outlanes that
rotate based on slingshot hits, so in that case you'd set them up and
then use ``left_slingshot_active`` and ``right_slingshot_active`` as your
events (changed based on your actual switch names, of course). Now if
you run MPF and start a game, you should be able to light a shot by
hitting it and then see it rotate when you hit the flippers. (Note
that you have to actually start a game. shots are not active when a
game is not in progress.)



(C) Configure your shots to reset when they're complete
-------------------------------------------------------

If you played with this, you most likely noticed that the shots didn't
actually reset once they were all complete. So that's what we'll do in
this step. The way we'll do that is to add an entry for
`reset_events:` which specifies what events will cause the shots to
reset. To do that, go back into your `base.yaml` file and add another
setting to your *indy_lanes* shot group for `reset_events:`, like
this:


.. code-block:: mpf-config

   #! switches:
   #!   indy_i:
   #!     number: 1
   #!   indy_n:
   #!     number: 2
   #!   indy_d:
   #!     number: 3
   #!   indy_y:
   #!     number: 4
   #! lights:
   #!   indy_i:
   #!     number: 1
   #!   indy_n:
   #!     number: 2
   #!   indy_d:
   #!     number: 3
   #!   indy_y:
   #!     number: 4
   ##! mode: base
   #! mode:
   #!   start_events: ball_started
   #! shots:
   #!   indy_i:
   #!     switch: indy_i
   #!     show_tokens:
   #!       light: indy_i
   #!   indy_n:
   #!     switch: indy_n
   #!     show_tokens:
   #!       light: indy_n
   #!   indy_d:
   #!     switch: indy_d
   #!     show_tokens:
   #!       light: indy_d
   #!   indy_y:
   #!     switch: indy_y
   #!     show_tokens:
   #!       light: indy_y
   shot_groups:
     indy_lanes:
       shots: indy_i, indy_n, indy_d, indy_y
       rotate_left_events: left_flipper_active
       rotate_right_events: right_flipper_active
       reset_events:
         indy_lanes_lit_complete: 1s
   ##! test
   #! start_game
   #! assert_str_condition unlit device.shot_groups.indy_lanes.common_state
   #! hit_and_release_switch indy_i
   #! hit_and_release_switch indy_n
   #! hit_and_release_switch indy_d
   #! hit_and_release_switch indy_y
   #! advance_time_and_run .1
   #! assert_str_condition lit device.shot_groups.indy_lanes.common_state
   #! advance_time_and_run 1
   #! assert_str_condition unlit device.shot_groups.indy_lanes.common_state

There are a few things going on here. First, notice that the name of
our event is ``indy_lanes_default_lit_complete``. That seems like a
mouthful, but it's logical if you break it down! MPF automatically
posts events from shot groups based on what's happening in that group.
What happens is that every time a shot changes state, the shot group
it belongs to checks the state of all the shots in the group. If they
are all the same, then it posts a "complete" event which we can use to
assign scores, trigger effects, and reset the group. The format of
that event is
:doc:`/events/shot_group_state_complete`. In our
case, our shot group name is ``indy_lanes``, and the state of the shots that
we're interested in is called *lit*. Also notice that instead of adding
``indy_lanes_lit_complete`` to the same line as ``reset_events``,
we put it on its own line along with a time entry of ``1s``. This format
is available for every device configuration setting where we specify
events, and it means that when that event is posted, it will wait for
the specified time to pass before actually performing its action. The
reason we did this is because without it, the shots will reset
themselves instantly when they complete, which might be confusing to
the player since it will look like they have 3 of the 4 shots
complete, they hit the 4th one, and then they all go out. The player
will think, "Wait, what just happened? Did I get it?" So by adding
this delay, we wait 1 second after completing all the shots before
they're reset. At this point you should be able to launch MPF, start a
game, hit a shot, rotate it with the flippers, and when you complete
all the shots, they should wait a second and then reset. Cool!



(D) Add some scoring
--------------------

Next lets add some scoring to your shots. We're going to make it so
the player gets 5,000 points if they hit and unlit shot (which will
then light), 100 points if they hit a shot that's already lit (since
they failed to rotate or nudge the ball into an unlit lane), and
10,000 points when they complete all the shots in the group. To do
that, add a scoring section to your base.yaml mode configuration. (Or
you can add it to your machine-wide config if you want to keep all
your scoring entries in one place.) It should look like this:

.. code-block:: mpf-config

   #! switches:
   #!   indy_i:
   #!     number: 1
   #!   indy_n:
   #!     number: 2
   #!   indy_d:
   #!     number: 3
   #!   indy_y:
   #!     number: 4
   #! lights:
   #!   indy_i:
   #!     number: 1
   #!   indy_n:
   #!     number: 2
   #!   indy_d:
   #!     number: 3
   #!   indy_y:
   #!     number: 4
   ##! mode: base
   #! mode:
   #!   start_events: ball_started
   #! shots:
   #!   indy_i:
   #!     switch: indy_i
   #!     show_tokens:
   #!       light: indy_i
   #!   indy_n:
   #!     switch: indy_n
   #!     show_tokens:
   #!       light: indy_n
   #!   indy_d:
   #!     switch: indy_d
   #!     show_tokens:
   #!       light: indy_d
   #!   indy_y:
   #!     switch: indy_y
   #!     show_tokens:
   #!       light: indy_y
   #! shot_groups:
   #!   indy_lanes:
   #!     shots: indy_i, indy_n, indy_d, indy_y
   #!     rotate_left_events: left_flipper_active
   #!     rotate_right_events: right_flipper_active
   #!     reset_events:
   #!       indy_lanes_lit_complete: 1s
   variable_player:
     indy_lanes_unlit_hit:
       score: 5000
     indy_lanes_lit_hit:
       score: 100
     indy_lanes_lit_complete:
       score: 10000
   ##! test
   #! start_game
   #! assert_str_condition unlit device.shot_groups.indy_lanes.common_state
   #! hit_and_release_switch indy_i
   #! hit_and_release_switch indy_n
   #! hit_and_release_switch indy_d
   #! hit_and_release_switch indy_y
   #! advance_time_and_run .1
   #! assert_str_condition lit device.shot_groups.indy_lanes.common_state
   #! advance_time_and_run 1
   #! assert_str_condition unlit device.shot_groups.indy_lanes.common_state
   #! assert_player_variable 30000 score


Again, these event names might seem crazy, but they're all very
logical if you break them down. The shot group will post events any
time one of its member shots is hit. This is similar to the *complete*
event from the previous step, except the
:doc:`hit event </events/shot_group_state_hit>` ends in ``_hit``
and is posted with every hit to any shot versus the *_complete* event
which is only posted when all the shots in the group have made it to
the same state. Remember that since we haven't assigned any shot
profiles (nor will we), we're using the default shot profile which has
two steps: ``unlit`` and ``lit``, with the ``unlit`` step running a light
script that turns off the associated light or LED and the *lit* step
running a light script that turns on the light. One anomaly with the
scoring is that when you hit the last shot to complete the group,
you'll actually get 15,000 points instead of 10,000. (Brian was
confused by this in the video!) That's because when you hit that final
unlit shot, you get 5,000 points for hitting an unlit shot plus the
10,000 points for completing the group. If you really only want 10,000
points total on the last hit, then you could just change the
``complete`` event to 5,000 points, or setup a logic block to track the
count and trigger the scoring.


(E) Add a light show to play a cool effect on completion
--------------------------------------------------------

As it is now, when you complete the lanes, you get the points which is
cool, but after 1 second the lights just sort of unceremoniously
reset. Boring! So let's create a light show that flashes the lane
lights when you complete the lanes. To do this, let's first create a
light show (details in Steps A and B `here`) called
`indy_lanes_complete.yaml`:


.. code-block:: mpf-config

   ##! show: indy_lanes_complete
   - duration: 1
     lights:
       indy_i: ff
       indy_n: 00
       indy_d: ff
       indy_y: 00
   - duration: 1
     lights:
       indy_i: 00
       indy_n: ff
       indy_d: 00
       indy_y: ff


Obviously you can make this show do whatever you want; I opted for a
simple one that sort of alternates the lights. Then to run the light
show, go back to your `base.yaml` mode config and add a
`light_player:` entry which plays this show when the lanes are
complete, like this:

.. code-block:: mpf-config

   #! switches:
   #!   indy_i:
   #!     number: 1
   #!   indy_n:
   #!     number: 2
   #!   indy_d:
   #!     number: 3
   #!   indy_y:
   #!     number: 4
   #! lights:
   #!   indy_i:
   #!     number: 1
   #!   indy_n:
   #!     number: 2
   #!   indy_d:
   #!     number: 3
   #!   indy_y:
   #!     number: 4
   ##! show: indy_lanes_complete
   #! - duration: 1
   #!   lights:
   #!     indy_i: ff
   #!     indy_n: 00
   #!     indy_d: ff
   #!     indy_y: 00
   #! - duration: 1
   #!   lights:
   #!     indy_i: 00
   #!     indy_n: ff
   #!     indy_d: 00
   #!     indy_y: ff
   ##! mode: base
   #! mode:
   #!   start_events: ball_started
   #! shots:
   #!   indy_i:
   #!     switch: indy_i
   #!     show_tokens:
   #!       light: indy_i
   #!   indy_n:
   #!     switch: indy_n
   #!     show_tokens:
   #!       light: indy_n
   #!   indy_d:
   #!     switch: indy_d
   #!     show_tokens:
   #!       light: indy_d
   #!   indy_y:
   #!     switch: indy_y
   #!     show_tokens:
   #!       light: indy_y
   #! shot_groups:
   #!   indy_lanes:
   #!     shots: indy_i, indy_n, indy_d, indy_y
   #!     rotate_left_events: left_flipper_active
   #!     rotate_right_events: right_flipper_active
   #!     reset_events:
   #!       indy_lanes_lit_complete: 1s
   #! variable_player:
   #!   indy_lanes_unlit_hit:
   #!     score: 5000
   #!   indy_lanes_lit_hit:
   #!     score: 100
   #!   indy_lanes_lit_complete:
   #!     score: 10000
   show_player:
     indy_lanes_default_lit_complete:
       indy_lanes_complete:
         speed: 20
         loops: 10
         priority: 1
   ##! test
   #! start_game
   #! assert_str_condition unlit device.shot_groups.indy_lanes.common_state
   #! hit_and_release_switch indy_i
   #! hit_and_release_switch indy_n
   #! hit_and_release_switch indy_d
   #! hit_and_release_switch indy_y
   #! advance_time_and_run .1
   #! assert_str_condition lit device.shot_groups.indy_lanes.common_state
   #! advance_time_and_run 1
   #! assert_str_condition unlit device.shot_groups.indy_lanes.common_state
   #! assert_player_variable 30000 score


If you've worked with shows before, these settings should be pretty
straightforward. Running this show at 20x the speed means that
it runs really fast. We set ``loops: 10`` so it loops 10 times
and then stops.
The only
slightly confusing thing might be the ``priority: 1`` setting. Any time
priority settings are added to mode config files, the setting is added
to the priority of the mode. For example, if you configure your base
mode to run at priority 100, that means that everything it does has a
priority of 100—slide shows, lights, sounds, etc. Adding ``priority: 1``
to this light_player entry just means that this light show will run
with a priority of 101 instead of 100, ensuring that it shows up "on
top" of anything else this mode is doing with those lights.

(F) Revisit your reset delay
----------------------------

At this point you should be all set and your machine's shots should
work like the shots in the video at the beginning of this guide. The
only loose end to tie up is ``reset_events`` entry of
``indy_lanes_lit_complete: 1s``. As it is now, when the lanes
complete (and while the light show is playing), your lanes will still
be in their "lit complete" state, meaning if the ball hits a lane
within that first second, the player won't get credit for it towards
the second round of lighting the lanes. You might want to remove the
1s and just change that entry to ``reset_events:
indy_lanes_lit_complete``. If you do that and the player's ball
hits a lane while the show is playing, then they will get the score
and credit towards the next round of lighting the lanes (even though
they won't see the lane light until after the show stops since the
show is running at a higher priority). Whether you do this is a matter
of personal taste. You could also set a stop event for the light show
and cancel it right away if the lane is hit again, or you could not
have a ``priority`` entry in the light_player entry so lighting the lane
shows up while the show plays around it. Really there are lots of
options you can play with.


This is a full example:

.. code-block:: mpf-config

   # switches and lights in your machine config
   switches:
     indy_i:
       number: 1
     indy_n:
       number: 2
     indy_d:
       number: 3
     indy_y:
       number: 4
   lights:
     indy_i:
       number: 1
     indy_n:
       number: 2
     indy_d:
       number: 3
     indy_y:
       number: 4
   ##! show: indy_lanes_complete
   # the show on complete
   - duration: 1
     lights:
       indy_i: ff
       indy_n: 00
       indy_d: ff
       indy_y: 00
   - duration: 1
     lights:
       indy_i: 00
       indy_n: ff
       indy_d: 00
       indy_y: ff
   ##! mode: base
   # your base mode
   mode:
     start_events: ball_started
   shots:
     indy_i:
       switch: indy_i
       show_tokens:
         light: indy_i
     indy_n:
       switch: indy_n
       show_tokens:
         light: indy_n
     indy_d:
       switch: indy_d
       show_tokens:
         light: indy_d
     indy_y:
       switch: indy_y
       show_tokens:
         light: indy_y
   shot_groups:
     indy_lanes:
       shots: indy_i, indy_n, indy_d, indy_y
       rotate_left_events: left_flipper_active
       rotate_right_events: right_flipper_active
       reset_events: indy_lanes_lit_complete
   variable_player:
     indy_lanes_unlit_hit:
       score: 5000
     indy_lanes_lit_hit:
       score: 100
     indy_lanes_lit_complete:
       score: 10000
   show_player:
     indy_lanes_default_lit_complete:
       indy_lanes_complete:
         speed: 20
         loops: 10
         priority: 1
   ##! test
   #! start_game
   #! assert_str_condition unlit device.shot_groups.indy_lanes.common_state
   #! hit_and_release_switch indy_i
   #! hit_and_release_switch indy_n
   #! hit_and_release_switch indy_d
   #! hit_and_release_switch indy_y
   #! advance_time_and_run .1
   #! assert_str_condition unlit device.shot_groups.indy_lanes.common_state
   #! assert_player_variable 30000 score
