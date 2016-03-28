
In MPF, there are many situations where you might want to interrupt
the flow of progress in order to do something. For example, you might
want to hook the ball ending process to run a bonus mode, you might
want to hook the ball starting process to play some animation, you
might want to hook a ball entering a device to play a show before
multiball starts, etc. At first you might think, "No problem, I'll
just create a bonus mode that runs when the *ball_ending* event is
posted." Unfortunately that won't work because MPF will just start the
next ball, so your bonus mode will be running while the next player's
turn has started and the ball is sitting at the plunger. So how do you
handle this? This is done by leveraging MPF's "queue" events. A queue
event is just like other event in MPF with one key addition:
registered handlers of queue events can respond to the event by
telling it, "Hey, I've got some things to do, so don't proceed until I
tell you that I'm done." So that's what we're going to do in this
tutorial. (More info on queue events is `here`_.) This tutorial is
specifically about how you'd hook a bonus mode into the ball ending
process, but the techniques here can be used with any of the queue
events in MPF. Here are some examples of queue events:


+ game_starting
+ game_ending
+ ball_starting
+ ball_ending
+ mode_<name>_starting
+ mode_<name>_stopping


Notice that all of these event names end in *-ing*. These events are
all posted as queue events, and then when the queue is cleared, the
related *-ed* version of the event is posted. (So *ball_ending* is
posted as a queue event, and then when that queue is clear,
*ball_ended* is posted.)



Registering "waits" via the mode config file
--------------------------------------------

Fortunately it's easy to configure a mode so that it registers a wait.
You can do this right in the config file for your mode with the
`use_wait_queue: true` setting. For example, here's how we'd do this
in a bonus mode config that we want to hook the *ball_ending* event:


::

    
    mode:
      start_events: ball_ending
      stop_events: timer_bonus_complete
      priority: 500
      use_wait_queue: true


Since this mode has `start_events: ball_ending`, it will start when
the *ball_ending* event is posted. And since it has `use_wait_queue:
true`, it will "pause" the ball ending process as long as it's
running. To "release" the pause, all you have to do is end the mode.
Here's a very simple example, all done in the config (i.e. with no
custom mode code), that will display the word "BONUS" on the display
for 3 seconds during the ball ending process. This is the complete
mode config file:


::

    
    #config_version=3
    
    mode:
      start_events: ball_ending
      stop_events: timer_bonus_complete
      priority: 500
      use_wait_queue: true
    
    slide_player:
      mode_bonus_started:
        type: text
        text: BONUS
    
    timers:
      bonus:
        start_value: 3
        start_running: true
        direction: down


Of course this isn't terribly useful for a ball end bonus since you'd
probably want to do some math and add a score, but you get the idea.
(And you could use this exact same technique, for example, to play a
slide show and some sounds as an introduction to
*mode_<name>_starting* event.)



Working with "waits" in custom mode code
----------------------------------------

So now that you have a useless bonus mode that starts and stops, lets
look at adding some custom mode code to actually do something useful.
To do this, we'll add a `code/bonus.py` file into our bonus `mode`
folder. (Remember that you also have to add blank `__init__.py` files
to your `mode` and `code` folders.) Then update the config for your
bonus mode to specify that you're using custom code, like this:


::

    
    mode:
      start_events: ball_ending
      code: bonus.Bonus
      priority: 500
      use_wait_queue: true


(Note that we also removed the `stop_events:` entry from the mode
config since we'll stop our mode in code.) Next let's take a look at
the bonus.py mode code file. Here's a very simple (and fully
functional) file. In this example, we register an event to set the
player variable for the bonus multiplier to 1 when a new player is
created. We also set it to check for tilt when it starts and to
immediately stop if the machine is tilted. In this example, we're
pulling player variables for ramps, modes, and bonus_multiplier. Then
we spit out a series of events, one-by-one, along with the math to add
up the player's score. When we get to the end, we reset the player
variable for the bonus multiplier (after making sure the player
doesn't have hold bonus), and then we call `self.stop()` which ends
the mode. Since we have this mode configured with the
*use_wait_queue*, when the mode finishes its stop process the hold
will be released and MPF will move on. Here's the bonus.py code:


::

    
    from mpf.system.mode import Mode
    
    
    class Bonus(Mode):
    
        def mode_init(self):
            self.machine.events.add_handler('player_add_success',
                                            self.player_add)
    
        def player_add(self, player, **kwargs):
            player['bonus_multiplier'] = 1
    
        def mode_start(self, **kwargs):
    
            if self.machine.game.tilted:
                self.stop()
    
            self.bonus_score = 0
            self.bonus_start()
    
        def bonus_start(self):
            self.machine.events.post('bonus_start')
            self.delay.add(name='bonus', ms=2000, callback=self.total_ramps)
    
        def total_ramps(self):
            self.machine.events.post('bonus_ramps')
            self.bonus_score += self.player['ramps'] * 10000
            self.delay.add(name='bonus', ms=2000, callback=self.total_modes)
    
        def total_modes(self):
            self.machine.events.post('bonus_modes')
            self.bonus_score += self.player['modes'] * 50000
            self.delay.add(name='bonus', ms=2000, callback=self.subtotal)
    
        def subtotal(self):
            self.machine.events.post('bonus_subtotal', points=self.bonus_score)
            self.delay.add(name='bonus', ms=2000, callback=self.do_multiplier)
    
        def do_multiplier(self):
            self.machine.events.post('bonus_multiplier')
            self.delay.add(name='bonus', ms=2000, callback=self.total_bonus)
    
        def total_bonus(self):
            self.bonus_score *= self.player['bonus_multiplier']
            self.player['score'] += self.bonus_score
            self.machine.events.post('bonus_total', points = self.bonus_score)
            self.delay.add(name='bonus', ms=2000, callback=self.end_bonus)
    
        def end_bonus(self):
            if not self.player['hold_bonus']:
                self.player['bonus_multiplier'] = 1
            else:
                self.player['hold_bonus'] = False
    
            self.stop()


Next let's take a look at the bonus.yaml config file. It's pretty
straightforward, with slide_player settings that put slides on the
display for each event from the code. Note that some of the slides
pull their data from player variables (via the %variable_name%), and
others pull them from event parameters (via a single percent sign).


::

    
    #config_version=3
    
    mode:
      start_events: ball_ending
      code: bonus.Bonus
      priority: 500
      use_wait_queue: true
    
    slide_player:
      bonus_start:
        type: text
        text: END OF BALL BONUS
      bonus_ramps:
        type: text
        text: "RAMPS: %ramps%"
      bonus_modes:
        type: text
        text: "MODES: %modes%"
      bonus_subtotal:
        type: text
        text: "BONUS SCORE: %points"
        number_grouping: true
      bonus_multiplier:
        type: text
        text: "%multiplier%X"
      bonus_total:
        type: text
        text: "TOTAL BONUS: %points"
        number_grouping: true




Extending this code
-------------------

At this point you should have a fairly basic bonus structure in place,
and there are lots of ways you can extend it:


+ Add light shows and music.
+ Add some code to detect if the player presses both flippers at the
  same time to cancel or to hurry up the timing of the delays.
+ Decide which player variables you want to reset on each ball versus
  which ones you keep.
+ Add more flourish to the slide_player with different fonts, shapes,
  images, transitions, etc.


.. _here: https://missionpinball.com/docs/mpf-core-architecture/events/#queue


