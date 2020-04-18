Tutorial step 10: Run a real game
=================================

Holy Moly! It's actually time to run your first real game with MPF.
When we say a "real" game, we're talking about with multiple players
and balls machine flow from attract to game mode and back to attract
once the game is over.

1. Make one quick addition to your display configuration
--------------------------------------------------------

We know that at this point, you just want to run your game. The
problem is if we run it now, the display will continue to show "ATTRACT
MODE" throughout the entire game since we haven't configured it for
anything else.
So let's make a quick addition to the ``slide_player:``
section of your config so it will show the player and ball number when
a game is in progress. (Later in this tutorial we'll revisit this and
explain what's actually going on. For now just make this change.)
In
your config file, add a ``ball_started:`` entry with the following
information. Your complete ``slide_player:`` section should now look
like this:

.. code-block:: mpf-mc-config

   #! slides:
   #!   welcome_slide:
   #!     widgets:
   #!       - type: text
   #!         text: PINBALL!
   #!         font_size: 50
   #!         color: red
   #!       - type: rectangle
   #!         width: 240
   #!         height: 60
   #!   attract_started:
   #!     widgets:
   #!       - text: ATTRACT MODE
   #!         type: text
   slide_player:
     init_done: welcome_slide
     mode_attract_started: attract_started
     ball_started:
       widgets:
         type: text
         text: PLAYER (number) BALL (ball)
   ##! test
   #! advance_time_and_run .1
   #! assert_slide_on_top attract_started
   #! assert_text_on_top_slide "ATTRACT MODE"

2. Add initial active switches and bind trough switches to your keyboard
------------------------------------------------------------------------

If you are not using physical hardware you need some way to control the
ball inside your trough.
We will first make sure that the trough switches will be active (as if there
was a ball sitting on them) when your virtual machine starts up.
Additionally, we add keyboard bindings for ball switches to the numbers
``1`` to ``5`` and the plunger switch to ``p``.

.. code-block:: mpf-mc-config

  #! switches:
  #!   s_trough1:
  #!     number:
  #!   s_trough2:
  #!     number:
  #!   s_trough3:
  #!     number:
  virtual_platform_start_active_switches:
    - s_trough1
    - s_trough2
    - s_trough3

  keyboard:
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
      switch: s_plunger
      toggle: true

This way you can drain balls by activating trough switches.


3. Change your flipper config so they don't automatically enable on machine boot
--------------------------------------------------------------------------------

Almost there! The other quick change we need to make is to remove the
``enable_events:`` from the flipper configuration that we added back in
the *Get Flipping!* step.

This is because by default, MPF will
automatically enable your flippers when a ball starts and disable them
when a ball ends. But since we added a configuration setting to your
flippers that set them to automatically enable themselves immediately
when MPF loaded, that setting overwrote the default setting which
enables your flippers when a ball starts. So as your config file is
now, the flippers enable when MPF boots, then they disable when the
first ball ends, and that's it. They won't enable again for Ball 2.

To make this change, simply remove the ``enable_events: machine_reset_phase_3`` line
from each of your two flipper sections of your config file. So now
your ```flippers:`` section should look like this: (It might not be 100%
identical since you might have single-wound flipper coils and/or EOS switches.)

.. code-block:: mpf-config

    #! switches:
    #!   s_left_flipper:
    #!     number: 0
    #!   s_right_flipper:
    #!     number: 1
    #! coils:
    #!   c_flipper_left_main:
    #!     number: 0
    #!   c_flipper_left_hold:
    #!     number: 1
    #!     allow_enable: true
    #!   c_flipper_right_main:
    #!     number: 2
    #!   c_flipper_right_hold:
    #!     number: 3
    #!     allow_enable: true
    flippers:
      left_flipper:
        main_coil: c_flipper_left_main
        hold_coil: c_flipper_left_hold
        activation_switch: s_left_flipper
      right_flipper:
        main_coil: c_flipper_right_main
        hold_coil: c_flipper_right_hold
        activation_switch: s_right_flipper

4. Running your game with physical hardware
-------------------------------------------

If you have a physical machine attached, go ahead and run your game
without the ``-x`` or ``-X`` command line options. (If you don't have a physical
machine and you want to simulate a game using the keyboard keys,
skip to Step 4 below.)

.. code-block:: doscon

  C:\pinball\your_machine>mpf both -X

Make sure you have at least one ball in the trough and then run your
game. The display should display "ATTRACT MODE." Hit the start button.
A ball should be kicked out of the trough and into the plunger lane,
and the display should change to "PLAYER 1 BALL 1." If you have a coil-
fired plunger, you should be able to hit the launch button and the
coil should fire. If you have a manual plunger, you should be able to
plunge and flip. If you hit the start button a second time during Ball
1, a second player should be added. (The display won't show this since we
haven't configured it to show a message, but you can see this in the
logs and when the ball drains then it should go to Player 2 Ball 1
instead of Player 1 Ball 2.)

A few caveats to this early bare-bones game:

+ Since you haven't configured any scoring yet, this game will be
  boring and nothing will score. But hey, you're playing!
+ If your flippers, trough eject, or plunger coil is too weak or too
  strong, you can adjust them in the coil's ``default_pulse_ms:`` setting in the
  config file.
+ If you start MPF with a ball in the plunger lane and you
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
  game, with 3 balls per game. You can change this in the :doc:`/config/game`
  section of the machine config.

5. "Playing" a game without a physical machine attached
-------------------------------------------------------

If you've been adding keyboard switch map entries to your config file
as you've been going through this tutorial, you can actually "play" a
complete game on your computer keyboard. Here's how you do it:

#. Launch the MPF game engine and the MC. Note that in order for this
   to work, we want to use the "smart virtual" platform. This will be
   the default, but make sure you do not have ``platform: virtual`` in
   your config. (If you do have a platform entry in your config, make
   sure it's ``platform: smart_virtual``.) If you have a different
   platform setting for your physical hardware, you can still run without
   the hardware connected by using the ``-X`` (uppercase *X*) command
   line option to specify the smart virtual platform interface.
#. Push the "S" key to start a game. At this point MPF will eject a ball
   from the trough to the plunger
#. If you have a coil-fired plunger, push the "L" key (or whatever key
   you mapped to your launch button) to launch the ball.
#. If you do not have a coil-fired plunger, push the "P" key (or
   whatever key you mapped to your plunger lane switch) to un-toggle that
   switch which simulates the ball leaving the plunger lane.
   Note: The toggle option in the :doc:`/config/keyboard` section is useful for testing
   your game from your computer when you’re not around your physical machine.
#. Now you can "flip" with the "Z" and "?" keys.
#. After you get bored of this, push the "1" key to activate a trough
   ball switch. At this point MPF will think a ball drained and you
   should see the display switch to Ball 2 and the trough switch should
   open and the plunger lane switch should close as the "smart virtual"
   platform ejects a ball from the trough to the plunger.
#. Repeat until you're bored.
#. After Ball 3 is over the display will change back to the "ATTRACT MODE"
   text and you can push "S" again to start another game.
#. Congrats! You just played your first virtual pinball game. Yeah,
   it's boring, but you did it!

6. What if your game won't start?
---------------------------------

If your game doesn't start or doesn't work, hopefully we've given you
enough information in this tutorial to work out what the problem is.
That said, here's a list of things that could go wrong:

+ If you see a config error try running ``mpf both -t -v -V -X`` to disable
  the text ui and add verbose logging.
+ No ball in the trough. (If you are using the smart_virtual platform with
  ``-X`` press ``1`` and ``2`` to add balls to the trough via keyboard. Check
  that you got ``virtual_platform_start_active_switches:`` set.)
+ Ball in the trough, but not activating the switch.
+ Trough switches are optos but you didn't add ``type: NC`` to your
  switch configurations. (Mechanical trough switches do not need a
  ``type:`` setting.)
+ Trough is trying to eject, but the trough coil's ``default_pulse_ms:`` setting
  is too weak and the ball can't get out.
+ Incorrect switch or coil numbers which don't match up to your actual
  hardware inputs and outputs.
+ Some other setting isn't configured properly, which could lead to
  who-knows-what error? (Maybe compare your config file to the complete
  config from mpf-examples?)

If you're still having problems, feel free to post to the mpf-users
Google group.

Check out the complete config.yaml file so far
----------------------------------------------

If you want to see a complete ``config.yaml`` file up to this point, it's in the ``mpf-examples/tutorial/step_10``
folder.

You can run this file directly by switching to that folder and then running the following command:

.. code-block:: doscon

   C:\mpf-examples\tutorial>mpf both -X

Remember though that unless you're following this tutorial with an actual *Demolition
Man*, you'll have some differences in your config file.
