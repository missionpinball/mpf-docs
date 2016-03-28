
This how to guide will show you how to create a timed skill shot. When
the ball is launched, the player will have a few seconds to make a
certain shot. If that shot is made before the timer runs out, the
player will get a extra points. If they don't make that shot in time,
the timer will run out and the skill shot mode will unload. So let's
dig in!



(A) Create your skill shot mode folder
--------------------------------------

The first step is to create the folder structure for your skill shot
mode. This will be identical to what you did when you created your
base mode and will include:


#. Create a *skill_shot* folder in your machine's modes folder.
#. Create a *config* folder in the *skill_shot* folder.
#. Create an empty file called *skill_shot.yaml* in the
   *modes/skill_shot/config* folder.


Your new folder structure should look something like this: ` `_



(B) Configure your skill shot mode settings
-------------------------------------------

Next open the config file for the skill shot mode (
*modes/skill_shot/config/skill_shot.yaml*) and set it up like this:


::

    
    Mode:
        start_events: ball_starting
        stop_events: timer_skill_shot_complete
        priority: 300


Just like your base mode, configure the skill shot to start when the
ball starts. What's different though is that we're also going to
configure the skill shot mode so that it ends when an event called
*timer_skill_shot_complete* is posted. (Remember that event name,
because we're going to come back to it when we setup our timer which
will endthe skill shot mode when the time runs out.) Also note that
we're configuring the skill shot so it runs at a higher priority than
the base mode. Our best practices are that modes priorities should be
multiples of 100. That gives you enough space between the modes to
adjust the priorities of specific things up or down within a mode
without interfering with other modes. (This will become more apparent
as you get deeper into the configuration of your game.)



(C) Configure a switch to be worth some extra points
----------------------------------------------------

Next pick a switch that will be the target of your skill shot. To keep
things simple right now, let's use a switch called *target1.* Add a
scoring entry to your skill shot mode's configuration that makes that
switch worth 10,000 points. In this case you can also add *|block* to
the end of the value which will prevent lower priority modes from
scoring this event:


::

    
    scoring:
        target1_active:
            score: 10000|block


Of course in the case of the skill shot, you might not actually want
to block the scoring. Maybe you want the player to get the 10,000
points from the skill shot and also to get the 1,000 points from the
base mode. In that case then don't add *|block*. But if you want the
player to only get the 10,000 points, then you can block the lower
priority modes from scoring this event.



(D)Add the skill shot mode to your machine config
-------------------------------------------------

Now go back to your machine-wide configuration (
*your_machine/config/config.yaml*) and add the skill shot mode to the
`Modes:` list. So now it should look like this:


::

    
    Modes:
      - base
      - skill_shot




(E) Run your game to make sure the skill shot is working
--------------------------------------------------------

Be sure to save both of your config files and go ahead and run your
game. Remember that your modes won't load until the first player's
first ball starts, but if you push start (or hit the S key), you
should see something like this in the console log:


::

    
    INFO : ModeController : =========== ACTIVE GAME MODES ==============
    INFO : ModeController : skill_shot : 300
    INFO : ModeController : base : 100
    INFO : ModeController : ============================================


Now if you hit the switch for *target1* (or whatever switch you
configured), you should see the score jump by 10,000 points: ` `_ Of
course what you might have noticed is that yes, the skill shot is
working, but it runs forever. How do we make it so it stops after a
few seconds? With a timer!



(F) Configure a timer to end the skill shot mode
------------------------------------------------

MPF has timers you can configure via your config files you can use to
do all sorts of useful things. If you haven't used MPF timers before,
you can read about them in the ` `timers:` section of the
configuration file reference`_. Let's set up the a timer like this:
(Set this up in the skill shot's configuration file,
*skill_shot.yaml*.)


::

    
    timers:
        skill_shot:
            start_value: 5
            direction: down
            control_events:
              - event: balldevice_playfield_ball_enter
                action: start


Like most sections of the config file, the `timers:` section is a list
of timers. Each sub-entry is the name of a timer, and then all the
entries under there are configuration settings for that specific
timer. When a timer completes, it posts an event
`timer_<timer_name>_complete`. This is why we configured the skill
shot mode's settings with `stop_events:timer_skill_shot_complete`. In
other words, this timer ending will post the
*timer_skill_shot_complete* event which will cause the mode to stop.
Taking another look at the skill_shot timer settings, notice that we
specified `balldevice_playfield_ball_enter` as a control event to
start the timer. But why *balldevice_playfield_ball_enter*? Why not
*mode_skill_shot_started*? In this case we don't want the timer to
actually start counting down until the ball has been plunged and is in
play. If we set the timer to start on `mode_skill_shot_started` then
it's possible the skill shot timer could end and the skill shot would
be unloaded before the player even had a chance to plunge! Of course
you could ask, "Then why start the mode with the *ball_starting*
event? Why not just configure the mode to start with
*balldevice_playfield_ball_enter*?" Good question, of course! The
reason we start the skill shot mode on *ball_starting* is because we
might want to do something with the skill shot mode before the player
has plunged the ball. For example:


+ Maybe we want to show a skill shot slide on the display?
+ Maybe we want to flash a light indicating a shot or lane that's
  available for the skill shot. (And if it's a lane, maybe we want the
  player to be able to use the flippers to rotate it even before they
  plunge.)
+ Maybe we want the skill shot to watch for a flipper button being
  held in or some other combination of pre-launch setting that would
  actually change how the skill shot behaves.


Of course if you don't want any of that, then yeah, you can change
your skill shot mode settings so it loads on
*balldevice_playfield_ball_enter*. (Just be sure to also change your
timer so that it starts ticking right away instead of waiting for a
start event.) Anyway, go ahead and test the skill shot mode again.
When you push start, you should see both the skill_shot and the base
modes show as active in the console log. Then after 5 seconds, you
should see the skill_shot mode unload, leaving just the base mode.
Here's a console log of that whole process *without* verbose logging:


::

    
    INFO : SwitchController : <<<<< switch: start, State:1 >>>>>
    INFO : SwitchController : <<<<< switch: start, State:0 >>>>>
    INFO : Game : Game Starting!!
    INFO : Game : Player added successfully. Total players: 1
    INFO : Mode.base : Mode Starting. Priority: 100
    INFO : Mode.skill_shot : Mode Starting. Priority: 300
    INFO : Mode.base : Mode Started. Priority: 100
    INFO : ModeController : ======== ACTIVE GAME MODES ===========
    INFO : ModeController : base : 100
    INFO : ModeController : ======================================
    INFO : Mode.skill_shot : Mode Started. Priority: 300
    INFO : ModeController : ======== ACTIVE GAME MODES ===========
    INFO : ModeController : skill_shot : 300
    INFO : ModeController : base : 100
    INFO : ModeController : ======================================
    INFO : SwitchController : <<<<< switch: target1, State:1 >>>>>
    INFO : SwitchController : <<<<< switch: target1, State:0 >>>>>
    INFO : Mode.skill_shot : Mode Stopping.
    INFO : Mode.skill_shot : Mode Stopped.
    INFO : ModeController : ======== ACTIVE GAME MODES ===========
    INFO : ModeController : base : 100
    INFO : ModeController : ======================================


So far, so good... right? We're almost done, but there are a few more
things we should tidy up first.



(G) End the skill shot once it's made
-------------------------------------

You might have noticed that if you keep hitting *target1*, the player
will keep getting 10,000 points (at least until the 5 second timer
expires). Maybe that's a cool thing that you want, but more likely you
want the shot to only be scored once. The easiest way to fix this is
to add *target1_active* to the skill shot mode's `stop_events`. So now
when a switch with the *points_please* tag is hit while the skill shot
is running, it will give the player 10,000 points and also stop the
mode. (And stopping the mode will remove the scoring event that was in
that mode, meaning additional hits to that target will only score
1,000 points since that's what's configured in the lower priority base
mode.) This also means that we have two stop_events for this mode—one
which will stop the mode when the timer runs out, and a second which
will stop the mode when that switch is hit. Either one will stop the
mode, and if the other event happens later it won't matter because the
mode will already be stopped and won't even know about it. At this
point, your entire
`your_machine/modes/skill_shot/config/skill_shot.yaml` file should
look like this:


::

    
    mode:
        start_events: ball_starting
        stop_events: timer_skill_shot_complete, target1_active
        priority: 300
    
    scoring:
        target1_active:
            score: 10000|block
    
    timers:
        skill_shot:
            start_value: 5
            direction: down
            control_events:
              - event: balldevice_playfield_ball_enter
                action: start




(H) Add some lights and display to advertise the skill shot
-----------------------------------------------------------

Really the sky's the limit with what you can do with this skill shot,
and you've already learned a bunch of different things you could do in
this tutorial so far. For example, what if you wanted to flash the
light at the target while the skill shot was running? How would you do
that? One way would be to create a show file which flashes that light.
Put this file in the shows folder in your skill shot mode folder, e.g.
`your_machine/modes/skill_shot/shows/flash_target1.yaml`. The file
could look like this:


::

    
    - tocks: 1
      lights:
        target1: ff
    - tocks: 1
      lights:
        target1: 00


Then in your skill shot's mode config file ( `skill_shot.yaml`), add a
`light_player:` section and configure this show to start and stop with
the mode, like this:


::

    
    light_player:
        mode_skill_shot_started:
          - show: flash_target1
            repeat: yes
            tocks_per_sec: 4
        mode_skill_shot_stopped:
          - show: flash_target1
            action: stop


Since this light show will run at a priority of 300 (since that's the
skill shot mode's priority), it will flash the light "on top" of what
any lower priority mode wants the light to do. You could also
configure a countdown timer on the display with a s `lide_player:`
entry in your skill_shot.yaml file, like this:


::

    
    slide_player:
        timer_skill_shot_tick:
            type: text
            text: "SKILL SHOT TIME: %ticks%"


Note that "SKILL SHOT TIME: %ticks%" is in quotes because colons have
special meaning in YAML files, and since we wanted the color after the
word "TIME" we had to wrap the whole thing in quotes. Also, we knew
that running timers post an event each tick called
*timer_<timer_name>_tick* with a parameter called *ticks* by searching
through the log files for event names. Now as soon as the ball goes
live on the playfield, the display will show a countdown like this:
(Assuming you don't hit the skill shot right away.) ` `_ Of course
this is all just scratching the surface of what you can do, but
hopefully you're starting to see how you can use modes and timers to
do some pretty cool things—all without any coding!

.. _ section of the configuration file reference: https://missionpinball.com/docs/configuration-file-reference/timers/


