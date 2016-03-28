
Warning: This How To guide has not yet been updated for MPF 0.21 (the
current version). If you're reading this now and you'd like to add
this to your game, send me an email (brian@missionpinball.com) and
I'll get it updated. Many games have a kickback, so let’s go through
the process of setting one up as a mode. Typically, a kickback has a
series of things that have to be done to enable it (in our case,
completing a set of standup targets), an indicator light to let you
know kickback is enabled, a coil to be fired very quickly, and a grace
period in case the ball falls back down the outlane too quickly. The
good news is that we can do it all in via config files, so here we go!



(A) Set up your kickback coil as an AutoFire Coil
-------------------------------------------------

The first thing we need to do is define our kickback coil as an
autofire coil. Remember that autofire coils have rules written
directly on to the hardware that fire a coil the instant a switch is
hit rather than sending the switch event to MPF and letting MPF handle
the coil firing. This is done for things like slingshots and flippers
that you need to react instantaneously to a switch closure. The actual
value of autofire coils when you’re running on a super-fast host PC is
debatable, but for the kickback we don’t want any room for doubt. If
that ball goes down the left outlane crazy fast, we want it saved! To
set up a new autofire coil, we need to edit our machine-wide
configuration ( `your_machine/config/config.yaml`) with this:


::

    
    autofire_coils:
        kickback:
            coil: c_kickback
            switch: s_leftOutlane
            enable_events: mode_kickback_started
            disable_events: mode_kickback_stopped


Note that in addition to connecting the *s_leftOutlane* switch to the
*c_kickback coil*, we also added enable and disable events. That’s
because we don’t want the kickback to always be functional. You have
to earn it! The event we’re using to enable the kickback is the
*mode_kickback_started* event that is posted when our kickback mode
begins. Likewise, we’re using the *mode_kickback_stopped* event that’s
posted when the mode ends to disable the autofire coil. That means we
need a mode called “kickback”, so let’s do that next.



(B) Create the kickback game mode
---------------------------------

First, create a folder tree just like you did for the skill_shot and
base modes, except this time substitute “kickback” for the folder and
yaml file names:


#. Create a `kickback` folder in your machine’s modes folder.
#. Create a `config` folder in the `kickback` folder.
#. Create an empty file called `kickback.yaml` in the
   `your_machine/modes/kickback/config` folder.


You should wind up with something that looks like this: ` `_ Then, in
your machine-wide configuration ( `your_machine/config/config.yaml`),
add kickback to the list of modes, like this:


::

    
    modes:
        - base
        - skill_shot
        - super_jets_phase_0
        - super_jets_phase_1
        - kickback


Now, let’s edit the mode configuration file (
`your_machine/modes/kickback/config/kickback.yaml`):


::

    
    mode:
        start_events: targets_left_bank_lit_complete
        stop_events: timer_kickback_grace_period_complete
        priority: 400


We gave it a priority of 400 because we already have a base mode
running at priority 100, a skill_shot running at a priority of 200,
and super_jets running at 300. Since we recommend giving priorities to
your early modes in multiples of 100, the kickback became 400. You’ll
appreciate this approach later on in game development when you want to
insert a mode at a priority somewhere in between two other modes
you’ve created. *(In reality, these modes that we’ve created so far
could have with the same priority since they are unrelated to one
another. We’re showing it here to illustrate that it’s best to
consider your mode priorities as you create them so you don’t run into
a major problem later when you have dozens of modes)* As you can see,
we’ve already referenced two things that haven’t been created yet:
*targets_left_bank_lit_complete* and
*timer_kickback_grace_period_complete*. Let’s set up our targets
first.



(C) Create a Target Group
-------------------------

This tutorial is going to make the player complete a bank of standup
targets in order to light kickback. To do this, we need to define our
targets in our global hardware configuration, which should already be
done. If you haven’t set them up as a `Target Group`_ yet, now is the
time to do it. So, in your machine-wide config, create a Target Group
like this:


::

    
    target_groups:
        left_bank:
            targets: t_leftBankBottom, t_leftBankTop, t_leftBankMiddle
            reset_events: targets_left_bank_lit_complete
            enable_events: ball_started
            disable_events: ball_ending


Note that Target Groups are referencing individual targets, not
switches. In MPF, “targets” is the term we use to represent a switch
that is paired with a light, like a rollover lane or standup target
with an arrow light pointing at it. If you haven’t set up your targets
yet, you can read more about that in the `Targets section`_. Inside
our Target Group, we defined a group of three targets. When these
three targets are all hit, MPF will post an event called
*targets_left_bank_lit_complete*. We’ve specified that event as the
reset event for this Target Group, so when you complete all three
targets, the lights will go out and you’ll have to start again. If you
go back and look at our mode config, though, you’ll also notice that
we’re using the same event to start the kickback mode. The
*enable_events* and *disable_events* are simply when we want to turn
on/off that Target Group. In this case, *ball_started* and
*ball_ending* are appropriate.



(D) Create a Timer for a kickback grace period
----------------------------------------------

Now that we have the TargetGroups set up, let’s go back to our mode
config. The start_events: section is taken care of, but now we need to
set up a timer. We’ll use this timer to kick off a light show, give a
bit of a grace period after kickback fires, and to end the mode when
it expires.


::

    
    timers:
        kickback_grace_period:
            start_value: 5
            direction: down
            control_events:
                - event: sw_kickback
                  action: start


The timer that we’ve set up is called *kickback_grace_period*, and
like the timer we set up in the skill_shot mode, it’s counting down
from 5 seconds. When the kickback mode is running (after the target
bank has been completed), rolling over the left outlane switch will
fire the kickback. The easiest way to trigger the timer, then, is to
use an event tied to that left outlane switch. In your machine-wide
config file, add a tag to your left outlane switch called “kickback”.


::

    
    switches:
        s_leftOutlane:
            number: S15
            label: Left outlane
            tags: playfield_active, kickback


Remember, any time a switch is hit, it posts an event that starts with
“ `sw_`” followed by any tags it might have (one event per tag). So in
our case, any time a ball rolls over *s_leftOutlane*, we get two
events: *sw_playfield_active* and *sw_kickback*. It’s that
*sw_kickback* event that we’re using to kick off our timer.



(E) Give it a shot!
-------------------

We’re ready to try out the kickback. Here’s what your config file
should look like now:


::

    
    mode:
        start_events: targets_left_bank_lit_complete
        stop_events: timer_kickback_grace_period_complete
        priority: 400



::

    
    timers:
        kickback_grace_period:
            start_value: 5
            direction: down
            control_events:
                - event: sw_kickback
                  action: start


Remember, we don’t have to tell the mode to fire a coil because the
act of starting this mode enables the kickback coil as an autofire
coil. To test this mode, start a game and hit each of the targets in
your Target Group, then drop a ball down the left outlane. It should
pop out. If you put it back in within 5 seconds, it should pop out
again, but if you wait too long you’ll have to re-enable the kickback
by hitting your targets again.



(F) Add some effects
--------------------

That was fun, but we need some sort of indication that the kickback
was lit, so let’s add some display and light elements.



1) Show something on the display
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First, let’s add some text to our DMD to let us know that your ball
has been saved (as if the fact that it’s out on the playfield isn’t
enough proof). To do that create a SlidePlayer entry in your mode
config file:


::

    
    slide_player:
        sw_kickback:
            - type: Text
            text: "Kickback!!!"
            v_pos: center
            transition:
            type: move_in
            direction: top


Here, we say that when the event *sw_kickback* happens (which is when
the left outlane switch is hit), the game will display a text element
on the DMD that says “Kickback!!!” Simple enough.



2) Turn on a light
~~~~~~~~~~~~~~~~~~

Next, we need to turn on the kickback light. Most games have this, and
most games have a few different states for that light. The first state
is to have the kickback light be on to notify the player that kickback
is enabled. To do this, we need to create a show file in the “shows”
subdirectory under our kickback folder. Name the file “
`light_kickback.yaml`” and configure it like this:


::

    
    - tocks: 1
        lights:
        l_kickback: ff


That was easy. We just told it to turn on the light named “
*l_kickback*”. While you’re in that folder, create another show file
called “ `flash_kickback.yaml`” and fill it with this:


::

    
    - tocks: 1
        lights:
        l_kickback: ff
    - tocks: 1
        lights:
        l_kickback: 00


In one tock, we’re turning on the light, and in the next we’re turning
it off. Again, nothing too crazy here. You folder tree should now look
like this: ` `_ Back in our mode config, we need to load those show
files we created into the ShowPlayer, which we do like this:


::

    
    show_player:
        mode_kickback_enabled:
            - show: light_kickback
              repeat: no
        mode_kickback_stopped:
            - show: light_kickback
              action: stop
            - show: flash_kickback
              action: stop
        sw_kickback:
            - show: flash_kickback
              repeat: yes
              tocks_per_sec: 16


Remember that the Show Player is set up to respond to events, so when
the event *mode_kickback_enabled* is posted (this is the event that
posts when the mode starts), the Show Player knows to play the “
`light_kickback`” show, which simply turns on the light. When the
*mode_kickback_stopped* event is posted after the timer runs out
(since the time running out is the stop event for the mode) or the
ball ends, it stops running the shows, which turns off the light. The
final entry in our Show Player is for the event *sw_kickback* (man
that switch is important!). When the ball rolls over the left outlane
switch and that event is posted, in addition to starting the timer and
firing the kickback coil, it also tells the Show Player to play the “
`flash_kickback`” show file that we created. In this case, we want the
flashing to be very rapid, so we set the `tock_per_sec` to 16, which
means that it will flash on and off eight times per second.



(G) Sit back and watch your kickback!
-------------------------------------

So that’s it! We’ve set up a kickback that is enabled when a certain
goal is completed, notifies you that it’s enabled by turning on a
light, shows some text on the DMD, and gives you a grace period after
the kickback has fired. You should have a kickback mode configuration
file that looks something like this:


::

    
    # kickback.yaml mode config file
    
    mode:
        start_events: targets_left_bank_lit_complete
        stop_events: timer_kickback_grace_period_complete
        priority: 400
    
    slide_player:
        sw_kickback:
            - type: Text
            text: "Kickback!!!"
            v_pos: center
            transition:
                type: move_in
                direction: top
    
    timers:
        kickback_grace_period:
            start_value: 5
            direction: down
            control_events:
                - event: sw_kickback
                  action: start
    
    show_player:
            mode_kickback_enabled:
                - show: light_kickback
                  repeat: no
            mode_kickback_stopped:
                - show: light_kickback
                  action: stop
                - show: flash_kickback
                  action: stop
            sw_kickback:
                - show: flash_kickback
                  repeat: yes
                  tocks_per_sec: 16


.. _Target Group: https://missionpinball.com/docs/configuration-file-reference/targetgroups/
.. _Targets section: https://missionpinball.com/docs/configuration-file-reference/targets/


