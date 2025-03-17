---
title: "Recipe: Modifying the game mode - Dual launch devices"
---

# Recipe: Modifying the game mode - Dual launch devices


While the following example adds a very unusual feature, it makes for a
very simple and clean example of how to override default behavior in
MPF.

One of the base assumptions that the MPF system makes is that there is
only one launch device. While quite reasonable, what if you wanted both
a left and right plugger? You can add a ball device for each system, but
MPF expects a *default_source_device* to be defined for the main
playfield, and it won't take a list. This means at the start of each
player round, the game can only kick up a ball in the default device.

Here's what the hardware configuration for two plungers (and troughs)
would look like:

``` yaml
##! no_fake_game
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
##! test
#! start_game
```

It is the game mode that handles the ball start procedure and assumes a
single launch device. Now MPF's game mode does a lot more than that, so
in most cases you probably don't want to go through re-writing the whole
thing just to change one behavior. Instead we will change the parts we
need to.

First, see how the default game mode works. Within the MPF source
library you'll see a directory called mpf/modes/game. This is just like
the modes directory in your own game definitions. Let's look at the
config file first
([mpf/modes/game/config/game.yaml](https://github.com/missionpinball/mpf/blob/dev/mpf/modes/game/config/game.yaml)):

``` yaml
##! mode: game
#config_version=5
mode:
  start_events: game_start
  stop_events: game_ended, service_mode_entered
  priority: 20
  code: mpf.modes.game.code.game.Game
  game_mode: false  # this is the game so it is started outside of a game
  stop_on_ball_end: false
##! test
#! start_game
```

This is pretty straight-forward. First the standard mode settings, and
then it points to the source for a Python module that defines a class
called Game. We can look at that code in `mpf/modes/game/code/game.py`.
While we won't repost the full source, you can look at it
[here](https://github.com/missionpinball/mpf/blob/dev/mpf/modes/game/code/game.py).
We won't get into all that it does, because we don't need to. Looking
through the file, we really only need to know where this mode adds a
ball to the playfield. That can be found as the last line of the
`_start_ball()` method. It makes the following call:

``` python
self.machine.playfield.add_ball(player_controlled=True)
```

Looking at the `add_ball()` method from the playfield class
([mpf/mpf/devices/playfield.py](https://github.com/missionpinball/mpf/blob/dev/mpf/devices/playfield.py#L169))
we can see that it can actually take a source device as an argument:

``` python
add_ball(self, balls=1, source_device=None, player_controlled=False) -> bool:
   """Add live ball(s) to the playfield.
   Args:
     balls: Integer of the number of balls you'd like to add.
     source_device: Optional ball device object you'd like to add the
         ball(s) from.
     player_controlled: Boolean which specifies whether this event is
         player controlled. (See not below for details)
```

This means that what we really want is the game class except with
slightly different `_start_ball()` method. To do that, we will define
our own game mode. Just like any other mode we add it to our folder of
modes. Your file layout will become as follows:

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

Your `game.yaml` will look like this:

``` yaml
#config_version=5
mode:
  start_events: game_start
  stop_events: game_ended, service_mode_entered
  priority: 20
  code: game.MyGameName
  game_mode: False  # this is the game so it is started outside of a game
  stop_on_ball_end: False
```

Now for our own game mode class that inherits everything it needs from
the original Game mode class:

``` python
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
     left_switch_pressed_future = self.machine.switch_controller.wait_for_switch(self.machine.switches["s_left_launch_button"])
     right_switch_pressed_future = self.machine.switch_controller.wait_for_switch(self.machine.switches["s_right_launch_button"])
     first_switch = await Util.race({left_switch_pressed_future: "left", right_switch_pressed_future: "right"})
     if first_switch == "left":
         self.machine.playfield.add_ball(source_device=self.machine.ball_devices['bd_left_plunger'], player_controlled=True)
     else:
         self.machine.playfield.add_ball(source_device=self.machine.ball_devices['bd_right_plunger'], player_controlled=True)
```

Notice that we've only had to define our `_start_ball()` method. It is
really just a copy of the original, except that we wait for one of the
two launch buttons and then eject a ball on that side.

Finally, the `__init__.py` files are all empty.

Now, when you hit the start button on your game, both sides will load a
ball for each plunger. Again, a weird thing to do, but a simple example
of customizing the game mode when you run up against a default that
doesn't work for your design.

Here is a complete example:

``` yaml
##! no_fake_game
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
    eject_timeouts: 1s
  bd_right_trough:
    ball_switches: s_right_trough1, s_right_trough2
    eject_coil: c_right_trough_eject
    tags: trough, home, drain
    eject_targets: bd_right_plunger
  bd_right_plunger:
    ball_switches: s_right_plunger_lane
    eject_coil: c_right_plunger
    eject_timeouts: 1s

playfields:
  playfield:
    default_source_device: bd_left_plunger
    tags: default

virtual_platform_start_active_switches: s_left_trough1, s_left_trough2, s_right_trough1, s_right_trough2

##! mode: game
#config_version=5
mode:
  start_events: game_start
  stop_events: game_ended, service_mode_entered
  priority: 20
  code: modes.game.code.game.MyGameName
  game_mode: false  # this is the game so it is started outside of a game
  stop_on_ball_end: false

##! code: modes/game/code/game.py
from mpf.modes.game.code.game import Game
from mpf.core.utility_functions import Util

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
     event_args = {
         "player": self.player.number,
         "ball": self.player.ball,
         "balls_remaining": self.balls_per_game - self.player.ball,
         "is_extra_ball": is_extra_ball}

     self.debug_log("***************************************************")
     self.debug_log("****************** BALL STARTING ******************")
     self.debug_log("**                                               **")
     self.debug_log("**    Player: {}    Ball: {}   Score: {}".format(self.player.number,
                                                                      self.player.ball,
                                                                      self.player.score
                                                                      ).ljust(49) + '**')
     self.debug_log("**                                               **")
     self.debug_log("***************************************************")
     self.debug_log("***************************************************")

     await self.machine.events.post_async('ball_will_start', **event_args)
     '''event: ball_will_start
     desc: The ball is about to start. This event is posted just before
     :doc:`ball_starting`.
     args:
     ball: The ball number
     balls_remaining: The number of balls left in the game (not including this one)
     is_extra_ball: True if this ball is an extra ball (default False)
     player: The player number'''

     await self.machine.events.post_queue_async('ball_starting', **event_args)
     '''event: ball_starting
     desc: A ball is starting. This is a queue event, so the ball won't
     actually start until the queue is cleared.
     args:
     ball: The ball number
     balls_remaining: The number of balls left in the game (not including this one)
     is_extra_ball: True if this ball is an extra ball (default False)
     player: The player number'''

     # register handlers to watch for ball drain and live ball removed
     self.add_mode_event_handler('ball_drain', self.ball_drained)

     self.balls_in_play = 1

     self.debug_log("ball_started for Ball %s", self.player.ball)

     await self.machine.events.post_async('ball_started', **event_args)
     '''event: ball_started
     desc: A new ball has started.
     args:
     ball: The ball number
     balls_remaining: The number of balls left in the game (not including this one)
     is_extra_ball: True if this ball is an extra ball (default False)
     player: The player number'''

     if self.num_players == 1:
         await self.machine.events.post_async('single_player_ball_started')
         '''event: single_player_ball_started
         desc: A new ball has started, and this is a single player game.'''
     else:
         await self.machine.events.post_async('multi_player_ball_started')
         '''event: multi_player_ball_started
         desc: A new ball has started, and this is a multiplayer game.'''
         await self.machine.events.post_async(
             'player_{}_ball_started'.format(self.player.number))
         '''event player_(number)_ball_started
         desc: A new ball has started, and this is a multiplayer game.
         The player number is the (number) in the event that's posted.'''

     if not hasattr(self.machine, "playfield") or not self.machine.playfield:
         raise AssertionError("The game did not define default playfield. Did you add tags: default to one of your "
                              "playfield?")

     left_switch_pressed_future = self.machine.switch_controller.wait_for_switch(self.machine.switches["s_left_launch_button"])
     right_switch_pressed_future = self.machine.switch_controller.wait_for_switch(self.machine.switches["s_right_launch_button"])
     first_switch = await Util.race({left_switch_pressed_future: "left", right_switch_pressed_future: "right"})
     if first_switch == "left":
         self.machine.playfield.add_ball(source_device=self.machine.ball_devices['bd_left_plunger'], player_controlled=True)
     else:
         self.machine.playfield.add_ball(source_device=self.machine.ball_devices['bd_right_plunger'], player_controlled=True)

##! test
#! start_game
#! assert_available_balls_on_playfield 0
#! hit_and_release_switch s_left_launch_button
#! hit_and_release_switch s_right_launch_button
#! assert_available_balls_on_playfield 1
```
