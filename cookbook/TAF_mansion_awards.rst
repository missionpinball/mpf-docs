Recipe: The Addams Family Mansion Awards & Tour the Mansion
===========================================================

This guide shows you how to build an MPF config for *The Addams Family's*
Mansion Awards and Tour the Mansion feature. The idea is you can use this as
a guide to implement a similar feature in your machine.

This guide uses the following concepts in MPF that you should be familiar
with:

* :doc:`/game_logic/modes/index`
* :doc:`/game_logic/achievements/index`
* :doc:`/game_logic/achievements/achievement_groups`
* :doc:`/shows/index`

This guide will also show you how to do a few tricky things, including:

* From a group of 12 achievements, ensure that the randomly selected one when
  the game starts is 1 of 2, not random from all 12.
* Have two shots that light the achievements, but one of the shots lights the
  achievements indefinitely and the other only lights them for 3 seconds.

What are the Mansion Awards & Tour the Mansion?
-----------------------------------------------

In The Addams Family, the Mansion Awards are the name for the 12 "goals" which
each have a light in the mansion on the playfield just above the flippers.

Tour the Mansion is a wizard mode (associated with the question mark insert
at the top of the mansion) that can be started after all 12 mansion awards have
been collected.

.. image:: images/taf_mansion.jpg

Here are the specific rules we need to implement:

**Mansion Awards**

* Lights for incomplete awards are off.
* Complete awards are on solid.
* The currently selected award's light is flashing.
* Hitting any pop bumper will change the currently selected award to another
  random from the awards that are not yet complete.
* When the game starts, either "Hit Cousin It" or "Mamushka" are selected.
* The selected award is awarded / collected when the electric chair is lit
  (yellow and red lights on the chair toy) and either the electric chair or
  swamp shot is hit. (The swamp is technically an operator setting, but we'll
  use it since that's what the default it.)
* Some of the awards start modes, and others are instant awards with a short
  show. Collecting an award immediately turns its light on solid and selects
  another random uncollected award.
* If 3 Mil is awarded, 6 Mil is spotted (automatically set to complete) as
  well, and vice-versa.  (This differs in the Gold Edition of the game, and is
  also an operator setting, but we're just going to hard code this behavior
  for this recipe.)
* The electric chair is lit for 3 seconds after the right inlane is hit.
* The electric chair is lit indefinitely after either ramp is hit.
* The electric chair is lit at the beginning of each ball
* For awards that start modes, the chair can be relit and another award
  awarded even while the prior award's mode is running.
* Accumulating 15, 25, 35, 45, 55, 65, 75, 85, 95 bear kicks (center ramp)
  collects the currently selected award (except Tour the Mansion), even if the
  chair is not lit.
* Each award collected adds 500k to the bonus.

**Tour the Mansion**

* Once all 12 Mansion Awards have been collected, the Tour the Mansion light
  (the question mark at the top of the mansion) is selected.
* The electric chair must be lit in the same way as before, and then the shot
  must be made to the electric chair or the swamp as before.
* This starts the Tour the Mansion mode
* When Tour the Mansion completes, all the mansion awards are reset and a new
  random one is selected.
* If Tour the Mansion ends before the ball ends, no mansion award can be
  awarded until the next ball.

Step 1. The machine-wide prerequisites
--------------------------------------

Before we dig into how to handle the mansion itself, we need to create a
machine-wide config that has all the devices we'll need, including the lights
for the mansion, switches for the shots we need, the ramps, the right inlane,
and the switches, coils, and ball devices we need to glue it all together.

Here's what our machine config looks like. (Note that this is complete in terms
of what we need to make this recipe work, but if you have a real Addams Family
then you'll probably have a lot more than this in your machine config file.)

.. code-block:: yaml

   #config_version=4

   modes:
     - mansion_awards

   switches:
     start:
       number: S13
       tags: start
     drain:
       number:
     trough1:
       number: S15
     trough2:
       number: S16
     trough3:
       number: S17
     plunger_lane:
       number: S27
     swamp_kickout:
       number: S74
     electric_chair:
       number: S43
     left_ramp:
       number: S66
     center_ramp:
       number: S65
     right_inlane:
       number: S25
     upper_left_jet:
       number: S31
       tags: jet
     upper_right_jet:
       number: S32
       tags: jet
     center_left_jet:
       number: S33
       tags: jet
     center_right_jet:
       number: S34
       tags: jet
     lower_jet:
       number: S35
       tags: jet

   coils:
     drain:
       number: 05
     trough:
       number: 04
     swamp_kickout:
       number: 08
     electric_chair:
       number: 01

   matrix_lights:
     9_mil:
       number: L66
     6_mil:
       number: L54
     3_mil:
       number: L68
     thing:
       number: L51
     quick_multiball:
       number: L55
     grave_yard_at_max:
       number: L67
     raise_the_dead:
       number: L52
     festers_tunnel_hunt:
       number: L56
     lite_extra_ball:
       number: L53
     seance:
       number: L57
     hit_cousin_it:
       number: L58
     mamushka:
       number: L45
     mansion_question:
       number: L65
     electric_chair_yellow:
       number: L64
     electric_chair_red:
       number: L47

   ball_devices:

     drain:
       ball_switches: drain
       eject_coil: drain
       eject_targets: trough
       tags: drain

     trough:
       ball_switches: trough1, trough2, trough3
       eject_coil: trough
       eject_targets: plunger_lane
       tags: trough, home

     plunger_lane:
       ball_switches: plunger_lane
       mechanical_eject: true
       tags: home, ball_add_live

     electric_chair:
       ball_switches: electric_chair
       eject_coil: electric_chair

     swamp_kickout:
       ball_switches: swamp_kickout
       eject_coil: swamp_kickout

Step 2. Add the achievements
----------------------------

Each mansion award will be an achievement. We decided to create a separate mode
called "mansion_awards" just so we can keep everything separate. (This isn't
required, it's just to help us keep it clear in our minds, and it's ok to have
lots and lots of modes in MPF.)

We'll configure this mode to start on the *ball_starting* event so it's
always running when a ball is in play. We won't configure a stop event which
means this mode will automatically stop when the ball ends.

Next we add an ``achievements:`` section and then subsections for our 12
mansion achievements.

You'll notice that most of them are almost identical. For
example, here's the entry for Thing Multiball:

.. code-block:: yaml

  thing_multiball:
    show_tokens:
      lights: thing
    show_when_selected: flash
    show_when_completed: on
    events_when_started: award_thing_multiball  # starts thing_multiball mode
    enable_events: initialize_mansion, reset_mansion
    events_when_completed: enable_light_chair
    complete_events: award_thing_multiball
    reset_events: reset_mansion

Stepping through how we're using each setting:

``show_tokens:``
   link this achievement to it's light on the playfield.

``show_when_selected: flash``
   Plays the show called "flash" when this achievement is selected

``show_when_completed: on``
   Plays the show called "on" when this achievement is complete

``events_when_started: award_thing_multiball``
   Posts an event called *award_thing_multiball* when this achievement is
   started. We'll use this as the start event for the Thing Multiball mode.

``enable_events: initialize_mansion, reset_mansion``
   Enables this achievement when either of the events *initialize_mansion* or
   *reset_mansion* is posted. Prior to that, this achievement will be disabled.

``events_when_completed: enable_light_chair``
   Posts the event *enable_light_chair* when this achievement is complete.
   We'll use this event to start a mode which will watch for shots to the
   center ramp and right inline which light the chair. (Remember the player
   has to light the chair before they can be awarded the currently selected
   mansion award.)

``complete_events: award_thing_multiball``
   Watches for the event *award_thing_multiball*, and when it sees it, it marks
   this achievement as complete. Notice this is the same event that this
   achievement posts when it starts. In other words, we've configured it so
   the achievement is complete as soon as it starts! This is by design, because
   the rules state that once an achievement is awarded, the chair can be
   relit immediately, and it's possible to receive the next award even while
   the mode from the prior award is still running.

``reset_events: reset_mansion``
   Watches for an event called *reset_mansion* that will reset this achievement
   back to its initial (disabled) state.

This achievements configuration takes care of the following rules:

* Lights for incomplete awards are off.
* Complete awards are on solid.
* The currently selected award's light is flashing.

Step 3. Create an achievement group
-----------------------------------

Next we need to create an achievement group called "mansion_awards" which will
group the 12 mansion achievements together. That will look like this:

.. code-block:: yaml

   achievement_groups:
     mansion_awards:
       achievements:
           9_mil
           6_mil
           3_mil
           thing_multiball
           quick_multiball
           graveyard_at_max
           raise_the_dead
           festers_tunnel_hunt
           lite_extra_ball
           seance
           hit_cousin_it
           mamushka
       show_tokens:
         lights: electric_chair_yellow, electric_chair_red
       auto_select: yes
       events_when_all_completed: select_tour_mansion
       disable_while_achievement_started: no
       enable_while_no_achievement_started: no
       show_when_enabled: on
       select_random_achievement_events: sw_jet
       allow_selection_change_while_disabled: yes
       start_selected_events: balldevice_electric_chair_ball_enter, balldevice_swamp_kickout_ball_enter

Let's look at each of these settings:

``achievements:``
   This is just the list of the 12 achievements that make up this group.

``show_tokens:``
   These are the show tokens for the group itself. In this case they're the
   two lights on the electric chair, since those lights turn on and off
   to indicate whether the chair or swamp can be shot to award the currently
   selected item.

``auto_select: yes``
   This is used to make sure that one achievement is selected at all times.
   If the currently selected achievement is completed, the achievement group
   will notice that there is no currently selected achievement and it will pick
   one from random from the remaining achievements (those that are "enabled").

``events_when_all_completed: select_tour_mansion``
   Posts an event called *select_tour_mansion* once all 12 achievements in this
   group in complete.

``enable_while_no_achievement_started: no``
   In our case, we do not want to automatically enable the achievement group
   when no achievement is started, because the rules for Addams Family say that
   the player has to shoot the center ramp or right inlane to light the
   chair (which is enabling this achievement group).

``show_when_enabled: on``
   This plays the show called "on" when the achievement group is in the
   enabled state. This will have the effect of turning on the red and yellow
   chair lights (from the ``show_tokens:`` section) when the achievement
   group is enabled and the selected item can be awarded.

``select_random_achievement_events: sw_jet``
   In Addams Family, each pop bumper hit changes the currently selected
   mansion award. To make this happen, we added a tag called "jet" to the five
   pop bumper switches. (That will post an event called *sw_jet* any time one
   of these switches is hit. Then we add that event name here which will cause
   this achievement group to change the currently selected award.

``allow_selection_change_while_disabled: yes``
   The pop bumper hits to change the current selection happens regardless of
   whether the group is enabled (e.g. the chair is lit) or not, so we use this
   setting to allow that selection change to happen at any time.

``start_selected_events: balldevice_electric_chair_ball_enter, balldevice_swamp_kickout_ball_enter``
   A shot to either the electric chair or the swamp kickout will award the
   selected achievement.

This step takes care of:

* Hitting any pop bumper will change the currently selected award to another
  random from the awards that are not yet complete.

Step 4. Select the proper award at game start
---------------------------------------------

One of the twists of the Addams Family mansion awards is that when the game
first starts, it always starts with either "Hit Cousin It" or "Mamuska"
selected. So we have to figure out a way to randomly pick from one of those
two (instead of all 12), and we also have to figure out a way for it to happen
only when the game starts, and not at the beginning of every ball.

We'll tackle this in two parts.

First, take a look at the Hit Cousin It and Mamuska achievements:

.. code-block:: yaml

   hit_cousin_it:
     show_tokens:
       lights: hit_cousin_it
     show_when_selected: flash
     show_when_completed: on
     events_when_started: award_hit_cousin_it  # starts hit_cousin_it mode
     events_when_completed: enable_light_chair
     complete_events: award_hit_cousin_it
     reset_events: reset_mansion
   mamushka:
     show_tokens:
       lights: mamushka
     show_when_selected: flash
     show_when_completed: on
     events_when_started: award_mamushka  # starts mamushka mode
     events_when_completed: enable_light_chair
     complete_events: award_mamushka
     reset_events: reset_mansion

Notice that they're slightly different than the other 10 mansion awards in that
they do NOT have enable events.

The reason for this is that devices in MPF that have enable_events in their
configurations are NOT automatically enabled when they're created. (This is
because MPF thinks, "Hey, you have enable events, so you have some way to
enable them, so you can enable them whenever you want." But if there are no
enable events, like these two, then MPF will enable them immediately.

This means that when this mode first starts and these 12 mansion achievements
are created, the ``hit_cousin_it`` and ``mamuska`` achievements are enabled
immediately (since they don't have enable events), and the other 10 mansion
awards are disabled (since they do have enable events). Since the achievement
group is configured for ``auto_select: yes``, it will automatically (and
immediately) pick one of the enabled achievements which will change into the
selected state (and start it's select show, etc.). This means that the initial
selection will always be one of those two.

However, once the initial selection is made, we need a way to enable the
remaining 10 mansion awards. For this we'll use a counter logic block:

.. code-block:: yaml

   logic_blocks:
     counters:
       initialize_mansion:
         count_events: mode_mansion_awards_started
         events_when_complete: initialize_mansion
         count_complete_value: 1
         persist_state: true

This is a simple counter that "counts" the *mode_mansion_awards_started"
event (which is posted by this mode once it's fully started and done
initializing). The count complete value is one, meaning that once it sees this
event once, it's done. We tell it to persist its state so that it remembers
where it was from ball-to-ball (meaning it will only run once ever in the game)
and when it's done (which is after it sees that event once) it will post the
event *initialize_mansion*.

(Remember that logic block states are stored on a per-player basis, so
everything we say happens "once" here is really "once per player".

Note also that in the 10 "other" mansion achievements, we have
*initialize_mansion* listed as one of their enable events. This means that
when this counter completes its count (of 1) that it will post that event
which will enable the other 10 achievements.

At this point you'll have 1 achievement selected (which will be either Hit
Cousin It or Mamushka), and you'll have the other 11 in the "enabled" state.

Hitting a pop bumper will pick a new random selected achievement.

Step 5. Light the electric chair
--------------------------------

* The electric chair is lit for 3 seconds after the right inlane is hit.
* The electric chair is lit indefinitely after either ramp is hit.
* The electric chair is lit at the beginning of each ball
* For awards that start modes, the chair can be relit and another award
  awarded even while the prior award's mode is running.

Step 6. Collect the selected award via a shot
---------------------------------------------

* The selected award is awarded / collected when the electric chair is lit
  (yellow and red lights on the chair toy) and either the electric chair or
  swamp shot is hit.
* Some of the awards start modes, and others are instant awards with a short
  show. Collecting an award immediately turns its light on solid and selects
  another random uncollected award.

Step 7. Collect the selected award via the bear kick
----------------------------------------------------

* Accumulating 15, 25, 35, 45, 55, 65, 75, 85, 95 bear kicks (center ramp)
  collects the currently selected award (except Tour the Mansion), even if the
  chair is not lit.

Step 8. Setup the 3 Mil / 6 Mil linking
---------------------------------------

* If 3 Mil is awarded, 6 Mil is spotted (automatically set to complete) as
  well, and vice-versa.

Step 8. Add 500k to the bonus for each award collected
------------------------------------------------------

* Each award collected adds 500k to the bonus.

Step 9. Move on to Tour the Mansion after all 12 awards have been completed
---------------------------------------------------------------------------

* Once all 12 Mansion Awards have been collected, the Tour the Mansion light
  (the question mark at the top of the mansion) is selected.
* The electric chair must be lit in the same way as before, and then the shot
  must be made to the electric chair or the swamp as before.
* This starts the Tour the Mansion mode

Step 10. Reset everything when Tour the Mansion is complete
-----------------------------------------------------------

* When Tour the Mansion completes, all the mansion awards are reset and a new
  random one is selected.
* If Tour the Mansion ends before the ball ends, no mansion award can be
  awarded until the next ball.
