Recipe: Modifying the game mode - Dual launch devices
=====================================================

While the following example adds a very unusual feature, it makes for a very simple and clean example of how to override default behavior in MPF.

One of the base assumptions that the MPF system makes is that there is only one launch device. While quite reasonable, what if you wanted both a left and right plugger?  You can add a ball device for each system, but MPF expects a *default_source_device* to be defined for the main playfield, and it won't take a list.  This means at the start of each player round, the game can only kick up a ball in the default device.

Here's what the hardware configuration for two plungers (and troughs) would look like:

.. code-block:: yaml

   #config_version=5
   switches:
     # Cabinet Buttons
     s_start_button:
       number:
       tags: start
     s_left_launch_button:
       number:
     s_right_launch_button:
       number:
     # Plunger Trough
     s_left_plunger_lane:
       number:
     s_right_plunger_lane:
       number:
     s_left_trough1:
       number:
     s_left_trough2:
       number:
     s_right_trough1:
       number:
     s_right_trough2:
       number:

   coils:
     c_left_plunger:
       number:
       default_pulse_ms: 20
     c_left_trough_eject:
       number:
       default_pulse_ms: 20
     c_right_plunger:
       number:
       default_pulse_ms: 20
     c_right_trough_eject:
       number:
       default_pulse_ms: 20

   ball_devices:
     bd_left_trough:
       ball_switches: s_left_trough1, s_left_trough2
       eject_coil: c_left_trough_eject
       tags: trough, home, drain
       eject_targets: bd_left_plunger
     bd_left_plunger:
       ball_switches: s_left_plunger_lane
       eject_coil: c_left_plunger
       player_controlled_eject_event: s_left_launch_button_active
       eject_timeouts: 1s
     bd_right_trough:
       ball_switches: s_right_trough1, s_right_trough2
       eject_coil: c_right_trough_eject
       tags: trough, home, drain
       eject_targets: bd_right_plunger
     bd_right_plunger:
       ball_switches: s_right_plunger_lane
       eject_coil: c_right_plunger
       player_controlled_eject_event: s_right_launch_button_active
       eject_timeouts: 1s

   playfields:
     playfield:
       default_source_device: bd_left_plunger
       tags: default

   virtual_platform_start_active_switches: s_left_trough1, s_left_trough2, s_right_trough1, s_right_trough2

It is the game mode that handles the ball start procedure and assumes a single launch device. Now MPF’s game mode does a lot more than that, so in most cases you probably don’t want to go through re-writing the whole thing just to change one behavior. Instead we will change the parts we need to.

First, see how the default game mode works.  Within the MPF source library you’ll see a directory called mpf/modes/game.  This is just like the modes directory in your own game definitions.  Let’s look at the config file first (`mpf/modes/game/config/game.yaml <https://github.com/missionpinball/mpf/blob/dev/mpf/modes/game/config/game.yaml>`_):

.. code-block:: yaml

   #config_version=5
   mode:
     start_events: game_start
     stop_events: game_ended, service_mode_entered
     priority: 20
     code: mpf.modes.game.code.game.Game
     game_mode: False  # this is the game so it is started outside of a game
     stop_on_ball_end: False

This is pretty straight-forward. First the standard mode settings, and then it points to the source for a Python module that defines a class called Game. We can look at that code in ``mpf/modes/game/code/game.py``. While we won’t repost the full source, you can look at it `here <https://github.com/missionpinball/mpf/blob/dev/mpf/modes/game/code/game.py>`_. We won’t get into all that it does, because we don’t need to. Looking through the file, we really only need to know where this mode adds a ball to the playfield. That can be found as the last line of the ``_start_ball()`` method. It makes the following call:

.. code-block:: python

   self.machine.playfield.add_ball(player_controlled=True)

Looking at the ``add_ball()`` method from the playfield class (`mpf/mpf/devices/playfield.py <https://github.com/missionpinball/mpf/blob/dev/mpf/devices/playfield.py#L169>`_) we can see that it can actually take a source device as an argument:

.. code-block:: python

   add_ball(self, balls=1, source_device=None, player_controlled=False) -> bool:
      """Add live ball(s) to the playfield.
      Args:
        balls: Integer of the number of balls you'd like to add.
        source_device: Optional ball device object you'd like to add the
            ball(s) from.
        player_controlled: Boolean which specifies whether this event is
            player controlled. (See not below for details)

This means that what we really want is the game class except with slightly different ``_start_ball()`` method.  To do that, we will define our own game mode.  Just like any other mode we add it to our folder of modes. Your file layout will become as follows::

 +-- config
     +-- config.yaml
 +-- data
 +-- logs
 +-- modes
     +-- game
         +-- __init__.py
         +-- config
             +-- game.yaml
         +-- code
             +-- __init__.py
             +-- game.py

Your ``game.yaml`` will look like this:

.. code-block:: yaml

   #config_version=5
   mode:
     start_events: game_start
     stop_events: game_ended, service_mode_entered
     priority: 20
     code: game.MyGameName
     game_mode: False  # this is the game so it is started outside of a game
     stop_on_ball_end: False

Now for our own game mode class that inherits everything it needs from the original Game mode class:

.. code-block:: python

   from mpf.modes.game.code.game import Game

   class MyGameName(Game):
     def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.log.debug("MyGameName init")

     async def _start_ball(self, is_extra_ball=False):
        """Perform ball start procedure.

        Note this method is called for each ball that starts, even if it's
        after a Shoot Again scenario for the same player.

        Posts a queue event called *ball_starting*, giving other modules the
        opportunity to do things before the ball actually starts. Once that
        event is clear, this method calls :meth:`ball_started`.
        """
        :
        # Cut and paste original game.py code for _start_ball() here.
        :
        # Replace self.machine.playfield.add_ball(player_controlled=True) with:
        self.machine.playfield.add_ball(source_device=self.machine.ball_devices['bd_left_plunger'], player_controlled=True)
        self.machine.playfield.add_ball(source_device=self.machine.ball_devices['bd_right_plunger'], player_controlled=True)


Notice that we’ve only had to define our ``_start_ball()`` method. It is really just a copy of the original, except the last line is changed to two ``add_ball()`` calls, one for each plunger defined.

Finally, the ``__init__.py`` files are all empty.

Now, when you hit the start button on your game, both sides will load a ball for each plunger. Again, a weird thing to do, but a simple example of customizing the game mode when you run up against a default that doesn't work for your design.
