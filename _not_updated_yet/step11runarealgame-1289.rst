
Holy Moly! It's actually time to runyour first real game with MPF.
When we say a "real" game, we're talking about with multiple players
and balls machine flow from attract to game mode and back to attract
once the game is over.



(A) Make one quick addition to your display configuration
---------------------------------------------------------

We know that at this point, you just want to run your game. The
problem is if we run it now, the DMD will continue to display "PRESS
START" throughout the entire game since we haven't configured it for
anything else. So let's make a quick addition to the `slide_player:`
section of your config so it will show the player and ball number when
a game is in progress. (Later in this tutorial we'll revisit this and
explain what's actually going on. For now just make this change.) In
your config file, add a `ball_started:` entry with the following
information. Your complete `slide_player:` section should now look
like this:


::

    
    slide_player:
        mode_attract_started:
            type: text
            text: PRESS START
            slide_priority: 10
        ball_started:
            type: text
            text: PLAYER %number% BALL %ball%
            slide_priority: 10




(B) Change your flipper config so they don't automaticallyenable on
machine boot
------------

Almost there! The other quick change we need to make is to remove the
*enable_events:* from the flipper configuration that we added back in
the *Get Flipping!* step.This is because by default, MPF will
automatically enable your flippers when a ball starts and disable them
when a ball ends. But sincewe added a configuration setting to your
flippers that set them to automatically enable themselves immediately
when MPF loaded, that setting overwrote the default setting which
enables your flippers when a ball starts. So as your config file is
now, the flippers enable when MPF boots, then they disable when the
first ball ends, and that's it. They won't enable again for Ball 2. To
do that, simply remove the *enable_events: machine_reset_phase_3* line
from each of your two flipper sections of your config file. So now
your *flippers:* section should look like this: (It might not be 100%
identical since you might have single-wound flipper coils.)


::

    
    flippers:
        left_flipper:
            main_coil: c_flipper_left_main
            hold_coil: c_flipper_left_hold
            activation_switch: s_left_flipper
        right_flipper:
            main_coil: c_flipper_right_main
            hold_coil: c_flipper_right_hold
            activation_switch: s_right_flipper




(C) Running your game with physical hardware
--------------------------------------------

If you have a physical machine attached, go ahead and run your game
without the `-x` command line option. If you're using Windows, we
*highly recommend that you do not do verbose logging to the console
window*, since Windows' console screen updates are *very* slowand this
will screw up your game. (It's crazy. Console logging on Windows is so
slow that you might find your hardware controller's watchdog timer
expires and your whole machine turns off while Windows chugs along
spitting things out to the screen!) So if you're on Windows, and
you're using the batch file, launch your game like this:


::

    
    mpf your_machine -v


The `-v` (lowercase 'v') option still writes verbose logging
information to the log file while just putting basic logging
information on the screen. If you're on Mac or Linux, you can run it
withverbose console logging too, like this (both lowercase 'v' and
uppercase 'V'), but of course you'll need to have two windows open and
will have to launch both the MPF core engine and the media controller
separately. Launch the media controller first:


::

    
    python mc.py your_machine -v -V


Then launch the MPF core engine:


::

    
    python mpf.py your_machine -v -V


Make sure you have at least one ball in the trough and then run your
game. The DMD should display "PRESS START." Hit the start button.
Aball should be kicked out of the trough and into the plunger lane,
and the DMD should change to "PLAYER 1 BALL 1."If you have a coil-
fired plunger, you should be able to hit the launch button and the
coil should fire. If you have a manual plunger, you should be able to
plunge and flip. If you hit the start button a second time during Ball
1, a second player should be added. (The DMD won't show this since we
haven't configured it to show a message, but you can see this in the
logs and when the ball drains then it should go to Player 2 Ball 1
instead of Player 1 Ball 2.) A few caveats to this early bare-bones
game:


+ Since you haven't configured any scoring yet, this game will be
  boring and nothing will score. But hey, you're playing!
+ If your flippers, trough eject, or plunger coil is too weak or too
  strong, you can adjust them in the coil's *pulse_ms:* setting in the
  config file.
+ If you launch your game code with a ball in the plunger lane and you
  have a coil-fired plunger, MPF will immediately fire the plunger to
  kick out the ball. This is by design since you don't have a "home" tag
  in your plunger ball device's configuration, which means that MPF will
  automatically eject the ball to get all the balls into ball devices
  tagged with "home."
+ If you shoot a ball into a playfield lock or any other ball device,
  it will get stuck there since you haven't configured that device. (In
  this case you need to add configuration entries for those ball devices
  so MPF can know about them. Then it will automatically kick out any
  balls that enter. We'll get to that later.)
+ By default MPF is configured to allow a maximum of 4 players per
  game, with 3 balls per game. You can change this inthe ` *game:*
  section`_ of your config file.




(D) "Playing" a game without a physical machine attached
--------------------------------------------------------

If you've been adding keyboard switch map entries to your config file
as you've been going through this tutorial, you can actually "play" a
complete game on your computer keyboard. Before you do this Doing so
it somewhat complex, but it is technically possible. Here's how you'd
do it:


#. Once you launch MPF and the media controller and all the stuff
   stops scrolling by in the logs and you see the "PRESS START" message
   on the DMD, push the "S" key to start a game, and wait for all the
   stuff to scroll by. At this point MPF will eject a ball from the
   trough to the plunger
#. If you have a coil-fired plunger, push the "L" key (or whatever key
   you mapped to your launch button) to launch the ball. You should see
   the plunger lane switch deactivate based on the coil firing thanks to
   the smart virtual platform.
#. If you do not have a coil-fired plunger, push the "P" key (or
   whatever key you mapped to your plunger lane switch) to un-toggle that
   switch which simulates the ball leaving the plunger lane.
#. Now you can "flip" with the "Z" and "/" keys.
#. After you get bored of this, push the "1" key to activate a trough
   ball switch. At this point MPF will think a ball drained and you
   should see the display switch to Ball 2 and the trough switch should
   open and the plunger lane switch should close.
#. Repeat until you're bored.
#. After Ball 3 is over you can push "S" again to start another game.
#. Congrats! You just played your first virtual pinball game. Yeah,
   it's boring right now and kind of hard to understand, but it worked!
   (Later we'll show you how to write automated scripts to "play" the
   game for you. :)




(E) Look at your log files
--------------------------

Assuming everything went correctly, now let's look at the log files to
see what actually happened. Remember that you'll actually have two log
files—one from the MPF core and one from the media controller.These
will be the two newest files in your `<mpf project root>/logs` folder.
(One of them has "mpf" in the name and the other has "mc" in the
name.) Just take a look through it to start to get a feel for
everything that MPF is doing behind the scenes.



(F) What if your game won't start?
----------------------------------

If your game doesn't start or doesn't work, hopefully we've given you
enough information in this tutorial to work out what the problem is.
That said, here's a list of things that could go wrong:


+ No ball in the trough.
+ Ball in the trough, but not activating the switch.
+ Trough switches are optos but you didn't add *type: NC* to your
  switch configurations. (Mechanical trough switches do not need a
  *type:* setting.)
+ Trough is trying to eject, but the trough coil's *pulse_ms:* setting
  is too weak and the ball can't get out.
+ Incorrect switch or coil numbers which don't match up to your actual
  hardware inputs and outputs.
+ Some other setting isn't configured properly, which could lead to
  who-knows-what error? You can check out a complete config file in the
  next section.


If you're still having problems, feel free to post to the `MPF Users
forum`_ on this site. If you do post, please run MPF andthe media
controllerwith verbose logging enabled (via the `-v` lowercase "v"
option), and post your log files as well as your config file to the
forum. (Again, your log files will be automatically created in `<your
mpf project root>/logs` folder.)



Sample config file which should look similar to yours
-----------------------------------------------------

The config file below is the real one we use for the *Demolition
Man*machine connected to a P-ROC, and if you've been following all the
steps in this tutorial, it should look pretty close to yours. However,
unless you're following this tutorial with an actual *Demolition
Man*and a P-ROC, you'll have some differences in your config file,
including:


+ Your hardware and driver boards might be not be P-ROC, and your
  driver boards might not be `wpc`.
+ If you're using FASThardware, you'll have a `fast:` section in your
  config.
+ Your `number:` settings for all your switches and coils will be your
  actual hardware numbers and not the numbers for *Demolition Man*from
  this file.
+ Your flippers might be configured for single-wound coils instead of
  dual-wound (main + hold) like in this file.
+ Your trough might have fewer switches.
+ Your plunger lane might not have a coil-fired eject, which also
  means you might not have a launch button or
  `player_controlled_eject_tag`.
+ Your plunger lane might not have a switch which is activated when a
  ball is in it, meaning it won't be configured as a ball device.
+ Your trough might be a Williams System 11 or early Williams WPC
  style which would be configured as two separate ball devices.



::

    
    #config_version=3
    
    # Config file for Step 11 of our step-by-step tutorial.
    # https://missionpinball.com/docs/tutorial/
    
    # WARNING: The switch and coil numbers in this configuration file are for a Demolition Man machine.
    # Do not use this file with your own hardware unless you change the coil and switch numbers to match your actual
    # hardware!
    
    switches:
        s_left_flipper:
            number: SF4
        s_right_flipper:
            number: SF2
        s_trough1:
            number: s31
            label:
            tags:
            type: NC
        s_trough2:
            number: s32
            label:
            tags:
            type: NC
        s_trough3:
            number: s33
            label:
            tags:
            type: NC
        s_trough4:
            number: s34
            label:
            tags:
            type: NC
        s_trough5:
            number: s35
            label:
            tags:
            type: NC
        s_trough_jam:
            number: s36
            label:
            tags:
            type: NC
        s_plunger_lane:
            number: s27
        s_start:
            number: s13
            tags: start
        s_launch:
            number: s11
            tags: launch
        s_right_inlane:
            number: s17
            tags: playfield_active
    
    coils:
        c_flipper_left_main: 
            number: FLLM
            pulse_ms: 25
        c_flipper_left_hold: 
            number: FLLH
        c_flipper_right_main: 
            number: FLRM
            pulse_ms: 25
        c_flipper_right_hold: 
            number: FLRH
        c_trough_eject:
            number: c01
            pulse_ms: 25
        c_plunger_eject:
            number: c03
            pulse_ms: 25
    
    flippers:
        left_flipper:
            main_coil: c_flipper_left_main
            hold_coil: c_flipper_left_hold
            activation_switch: s_left_flipper
        right_flipper:
            main_coil: c_flipper_right_main
            hold_coil: c_flipper_right_hold
            activation_switch: s_right_flipper
    
    dmd:
        physical: yes
        width: 128
        height: 32
    
    window:
        elements:
          - type: virtualdmd
            width: 512
            height: 128
            h_pos: center
            v_pos: center
            pixel_color: ff6600
            dark_color: 220000
            pixel_spacing: 1
          - type: shape
            shape: box
            width: 516
            height: 132
            color: aaaaaa
            thickness: 2
          - type: text
            font: tall title
            text: MY AWESOME GAME
            h_pos: center
            v_pos: top
            y: 60
            size: 100
            antialias: yes
            layer: 1
            color: ee9900
    
    slide_player:
        mode_attract_started:
            type: text
            text: PRESS START
            slide_priority: 10
        ball_started:
            type: text
            text: PLAYER %number% BALL %ball%
            slide_priority: 10
    
    keyboard:
        z:
            switch: s_left_flipper
        /:
            switch: s_right_flipper
        1:
            switch: s_trough1
            toggle: true
        2:
            switch: s_trough2
            toggle: true
        3:
            switch: s_trough3
            toggle: true
        4:
            switch: s_trough4
            toggle: true
        5:
            switch: s_trough5
            toggle: true
        p:
            switch: s_plunger_lane
            toggle: true
        s:
            switch: s_start
        L:
            switch: s_launch
        q:
            switch: s_right_inlane
    
    ball_devices:
      bd_trough:
        tags: trough, home, drain
        ball_switches: s_trough1, s_trough2, s_trough3, s_trough4, s_trough5, s_trough_jam
        eject_coil: c_trough_eject
        entrance_count_delay: 300ms
        jam_switch: s_trough_jam
        eject_targets: bd_plunger
        debug: yes
      bd_plunger:
        ball_switches: s_plunger_lane
        entrance_count_delay: 300ms
        eject_timeouts: 3s
        tags: ball_add_live
        eject_coil: c_plunger_eject
        player_controlled_eject_event: sw_launch
    
    virtual_platform_start_active_switches:
        s_trough1
        s_trough2
        s_trough3
        s_trough4
        s_trough5


Once you've got everything working, congrats!

.. _MPF Users forum: /forum
.. _ section: https://missionpinball.com/docs/configuration-file-reference/game/


