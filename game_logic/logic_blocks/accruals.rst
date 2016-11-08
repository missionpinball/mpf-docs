Accrual Logic Blocks
====================

Accruals are a type of :doc:`Logic Block </game_logic/logic_blocks/index>`
where you can trigger a new event based on a series of one or more other events.

Accruals are almost identical to :doc:`/game_logic/logic_blocks/sequences`, the
only difference being that the steps in an Accrual Logic Block can be completed
in any order, and the steps in a Sequence Logic Block must be completed in the
specific order they're listed.

Here are the Logic Blocks that we use for our
Big Shot pinball machine:

::

    logic_blocks:
        accruals:
            light_special:
                events:
                    - sw_eightball,
                    - drop_targets_solids_lit_complete, drop_targets_stripes_lit_complete
                events_when_complete: lighting_special, action_target_specialright_light
                enable_events: ball_started, collect_special
                disable_events: ball_ended, lighting_special
                reset_events: ball_ended, lighting_special

            collect_special:
                events:
                    - target_specialLeft_lit_hit, target_specialRight_lit_hit
                events_when_complete:
                    collect_special
                enable_events: lighting_special
                disable_events: ball_ended, collect_special
                reset_events: ball_ended, collect_special

            lighteightball:
                events:
                    - sw_eightball
                events_when_complete:
                    action_light_ball8_on
                    action_light_eightBall500_on
                enable_events: ball_started
                disable_events: ball_ended
                reset_events: ball_ended

            unlighteightball:
                events:
                    - collect_special
                events_when_complete:
                    action_light_ball8_off
                    action_light_eightball500_off
                enable_events: ball_started
                disable_events: ball_ended
                reset_events: ball_ended

            openDiverter:
                events:
                    - balldevice_eightballhole_ball_enter
                events_when_complete:
                    open_diverter
                enable_events: ball_started
                disable_events: ball_ended
                reset_events: ball_ended

events:
~~~~~~~

This is where you configure the actual events that make up the "steps"
of your Accrual Logic Block. "Accrual" is another work for "sum" or
"total", and Accrual Logic Blocks fire their completion event after
each (and every) step has been completed. The real power of Accrual
Logic Blocks is that you can enter more than one events for each step,
and *only one* of the of the events of that step has to happen for
that step to be complete. Another way to look at it is that there's an
*AND* between all the steps. For the Accrual to complete, you need
Step 1 *AND* Step 2 *AND* Step 3. But since you can enter more than
one event for each step, you could think of those like *OR*s. So you
have Step 1 (event1 *OR* event2) *AND* Step 2 (event3) *AND* Step 3
(event4 *OR* event5). It might seem kind of confusing at first, but
you can build this up bit-by-bit and figure them out as you go along.
You can enter anything you want for your events, whether it's one of
MPF's built-in events or a made-up event that another Logic Block
posts when it completes. (This is how you chain multiple Logic Blocks
together to form complex logic.) The steps of an Accrual Logic Block
can be completed in any order. (In fact, that's the whole point. If
you want a Logic Block where the steps have to be completed in order,
that's what the Sequence Logic Blocks are for.) Read
our note about how to enter lists of lists into the config files to make sure you
get the configuration right.

player_variable:
~~~~~~~~~~~~~~~~

This lets you specify the name of the player variable that will hold
the progress for this logic block. If you don’t specify a name, the
player variable used will be called *<accrual_name>_status*.

.. include:: common.rst

Real world examples of Accrual Logic Blocks
-------------------------------------------

Let's go through the Big Shot example from the beginning of this
section to look at how Accrual Logic Blocks are implemented in the
real world.

::

   light_special:
       events:
           - sw_eightball,
           - drop_targets_Solids_lit_complete, drop_targets_Stripes_lit_complete
       events_when_complete: lighting_special, action_target_specialRight_light
       enable_events: ball_started, collect_special
       disable_events: ball_ended, lighting_special
       reset_events: ball_ended, lighting_special

As you can probably guess from the name, the light_special Logic Block
is responsible for lighting the special target in Big Shot. The
special is lit by (1) completing either bank of drop targets, and (2)
completing either the center 8 Ball rollover lane or the getting the
ball in the 8 ball kickout hole. So this means there are two steps
(one for the 8 Ball and one for the drop targets), and since those
steps can complete in any order, we use the Accrual Logic Block
instead of a Sequence or Counter type. For the 8 ball step, we use the
event *sw_eightball*. *sw_xxxx* events are automatically posted
whenever a switch with the xxxx tag is hit, or whenever a ball enters
a ball device with the *xxxx* tag. So in our case, we added
`eightball`to the list of tags for the 8 Ball rollover switch and the
8 Ball kickout hole ball device, meaning that either one of those
being hit will cause MPF to post the *sw_eightball*event and the first
step of our Accrual to be marked as complete. For the drop target
step, we need either bank (called "Solids" and "Stripes" in Big Shot)
to complete, so we added the events that are automatically posted when
a drop target bank is complete (drop_targets_<name>_complete). So when
either the *drop_targets_solids_lit_complete*or
*drop_targets_stripes_lit_complete*events is posted, then our second
step is complete. Once those two steps are complete, our Accrual will
post two events: *lighting_special*and
*action_target_specialright_light*. The *lighting_special*event is
what we use to actually enable the Accrual Logic Block that watches
for the special (more on that in a bit), and the
*action_target_specialright_light*is the action event which lights the
target called *specialright*. For events which enable this Accrual, we
have two: *ball_started*and *collect_special*. The first is pretty
self-explanitory: We want this Accrual to start looking for hits when
the ball starts. The second, *collect_special*, is the event that is
posted after the special is actually collected (again more on that in
a bit). We include this because in Big Shot, after the player collects
a special the drop targets are reset and they have the opportunity to
hit the 8 Ball and complete another full bank of drop targets to
repeat this process. For events which disable this Accrual, we also
have two: *ball_ended*and *lighting_special*. Again *ball_ended*is
pretty straightforward: we stop tracking progress when the ball ends.
*lighting_special*is the event that this Accrual Logic Block itself
posts when completed, so this causes it to disable itself once it's
complete. For reset events, we also reset this Accrual when the ball
ends (via *ball_ended*), and we reset it via *lighting_special*as
well. Again, lighting_specialis the event that this Accrual posts when
it completes, so if we didn't reset it when it was complete then it
would be weird because it would automatically be complete when it was
enabled again after the player collected the special. Now lets look at
how we configured our *collect_special*Accrual which picks up where
this *lighting_special*leaves off:

::

   collect_special:
       events:
           - target_specialLeft_lit_hit, target_specialRight_lit_hit
       events_when_complete:
           collect_special
       enable_events: lighting_special
       disable_events: ball_ended, collect_special
       reset_events: ball_ended, collect_special

First, notice that *collect_special*is enabled when the event
*lighting_special*is posted. *lighting_special*is the event (which we
made up) that our previous *light_special*Accrual posts, so in other
words when light_special is complete, collect_special becomes active.
For the events that make of the steps of *collect_special*, we
actually only have one step (but with two events, meaning either one
of those events completes that step, and since there's only one step
then either one of those two events actually completes this entire
Accrual. Our events for completion are *target_specialleft_lit_hit*and
*target_specialright_lit_hit*. Those are built-in events whichare
posted automatically when a target device is hit while lit. (The
target device being either *specialleft*or *specialright*in this
case.) You might think, "Wait, so anytime one of those targets is hit
while lit then this Accrual will complete?" The answer is yes! But
consider what it takes to make that happen. The special targets aren't
lit ordinarily. The *specialright*is lit based on the completion of
the *light_special*Accrual we talked about before, and the
*collect_special*Accrual that we're talking about here isn't activated
until the *lighting_special*event is posted from *light_special*.
You'll notice that we have two options for the event step here (
*target_specialleft_lit_hit*and *target_specialright_lit_hit*), but
the *light_special*accrual only lights one of them. So what gives? In
our Big Shot config file, we also have a target group configured that
groups together the two specials, and we have a target rotator set up
which is tied to our slingshot switches. So all our previous Accrual
has to do is just light one of the special targets, and then the
rotator will cycle between the two as slingshots are hit. The targets
themselves will keep track of their own status (lit or unlit) and post
the proper events when they're hit (for example,
*target_specialleft_lit_hit*or *target_specialieft_unlit_hit*), so
that's how this Accrual only completes when a the lit special is hit.
The rest of the settings for this *collect_special*accrual are pretty
straightforward. We disable and reset it when the ball ends, and we
also reset and disable it when *collect_special*is posted (which is
the event that it posts when complete) so it's ready when it's lit
again. If you're wondering what actually happens when the
*collect_special*event is posted, that's something we handle in a
scriptlet in Big Shot. In this case we have a scriptlet which
automatically loads whenever a game is started which registers a
handler for the *collect_special*event and then fires the knocker coil
and gives the player a credit. So hopefully that shows the power and
simplicity of the Accrual Logic Blocks. We know that at this point you
might be thinking, "What? You're calling that simple???" But think
about it: what if you had to write all the Python code to do all this
logic manually? It would take hours and hours, and you'd be debugging
it for weeks. But thanks to these two Logic Blocks, you can putall
this functionality into your game in just a few minutes. (In our case
we literally drew flow charts to map out the process which we used to
create these Logic Blocks.) At this point you should be able to look
at the other threeAccrual Logic Blocks from Big Shot (
*lighteightball*, *unlighteightball*, and *opendiverter*) and
understand what they're doing and why we used them.
