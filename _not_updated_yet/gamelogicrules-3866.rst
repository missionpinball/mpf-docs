
In MPF, there's no single "feature" that's used to create game logic
and rules, rather, it's a combination of many different parts of MPF,
including:


+ MPF events
+ Player variables
+ Game modes
+ Logic blocks
+ Timers
+ "Real" programming


This section of the documentation explains the theory and general
approach to how you program game logic and rules. The nitty gritty
details for each section are covered in the full documentation for
each item. You can also follow our step-by-step tutorial for specific
instructions and examples on how to set all of this up.



MPF Events
----------

MPF makes *heavy* use of the concept of "events." An event is like a
message that one part of MPF can post that other parts of MPF can
respond to. (More info `here`_.) Events have quasi-friendly names like
"ball_started" or "ball_live_added" or "target_x_lit_hit." In MPF,
there are lots and lots and lots of events. Seriously. Dozens per
second. Maybe hundreds. Events are your key to creating your game
logic completely in config files without "real" programming. You'll
notice as you browse through the configuration file reference that
events are often the *result* of something happening, and/or that they
can be the *trigger*which causes something to happen. Some examples of
events that get posted as the result of things: (This is a tiny
fraction of the list. See `here`_ for more examples of events.)


+ A ball enters a device. Event is posted.
+ A shot is made. Event is posted.
+ Ball drains. Event is posted.
+ A switch is hit with a tag. Event is posted.
+ Shows can contain events which are posted when they get to a certain
  step.
+ etc.


Some examples of how you can use events to make things happen:


+ `Modes`_ have a list of one or more events that, when posted, cause
  them to start and stop.
+ Logic Blocks and Timers (both explained below) use events to start
  and stop and post events as they make progress.
+ `SlidePlayer`_ config entries show display content on the DMD or LCD
  based on events.
+ `SoundPlayer`_ config entries play sounds based on events.
+ `ShowPlayer`_ config entries play light/sound/display shows based on
  events.
+ `Scoring`_ is configured to assign points based on events.
+ etc.


So generally speaking, you'll be using events as the basis for the
bulk of your game logic.



Player Variables
----------------

A Player Variable is what we call a"per player" setting in MPF.
Basically these are used for everything you want to track per player
and remember from ball-to-ball. MPF automatically uses a few different
ones out of the box, including:


+ ball (what ball this player is on)
+ number (what player number this player is. e.g. *Player 1*, *Player
  2*, etc.)
+ score (the player's score)
+ extra_balls (how many extra balls this player has stacked up)


MPF's player system is very flexible. There is no central "list" of
player variables, rather, anything can be stored as a player variable
and it's automatically remembered for that player (and only that
player). Player variables are part of the game logic and rules
conversation because every time a player variable is changed, an event
is posted. (Seriously, events are really important!!) The event has
the name `player_<variable_name>`, and it's posted along with three
key/value pairs: *value* (the new value), *prev_value* (the previous
value), and *change* (the numeric change in the value, or if the
values are not numeric, a simple True/False as to whether the value
actually changed). For example, if the player's score is 1,000,000
points and something in MPF gives them 50,000 points, an event will be
posted called *player_score* with key/value pairs *value: 1050000*,
*prev_value: 1000000*, *change: 50000*. If you combine the fact that
*every player variable change causes an event to be posted* with the
fact that you can set lots of things in your config files to be
triggered by events, now you can start to see how this is used for
game logic. Some examples:


+ You can configure a score display via a SlidePlayer entry which
  shows and updates itself based on the player_score event.
+ You can configure an extra ball show to play based on the
  player_extra_balls event being posted with a change of 1.


Events posted by changing player variables will become even more
important as we dig into game modes and logic blocks



Game Modes
----------

In MPF, game modes are like little self-contained instances of an MPF
environment that only apply when a particular mode is active. (Full
details on game modes are`here`_.) In other words, you can add
scoring, shots, timers, light shows, display effects, logic blocks,
and many other things to a game mode, and when that mode is active,
everything you specified in that mode is active. When that mode ends,
everything you configured for that mode ends too. The trick with game
modes in MPF is that you can use them for a lot more than what you
might think of as a "traditional" mode. And you can have lots of them
running at the same time. The key is to break your game logic down
into lots of little pieces, and then create a mode for each piece.
Also each mode can run at a different priority which affects the
priority of display, lighting, and sound effects that come from that
mode. Higher priority modes can also block lower priority modes from
getting access to certain things. (Shots, for example.) For example,
we typically create a mode called "base" which we set to priority 100
which represents the base game mode. In it we'll configure all of our
shots as well as our default scoring values for everything. We'll also
configure default lighting, show, and sound effects. Let's imagine we
want to create a "super jets" game element where the pop bumpers are
worth 100 points each, but after the player has 50 pop bumper hits
then the "super jets" mode is enabled and the pop bumpers are worth
10,000 points each. To do that, we would configure the sound effect,
lighting effect, and pop bumper score as part of our base mode. We
would also create a Counter logic block which was triggered by a tag
added to each pop bumper. We would configure that logic block to start
at zero, count up by 1 when a pop bumper was hit, not reset between
balls, and finish when it got to 75. Then we'd also create a game mode
called "super_jets" which we would set to run at priority 200 and
configure to start based on the event posted by our counter logic
block finishing. We might configure a voice callout (via a
SoundPlayer: entry) and a display effect (via a SlidePlayer: entry)
which would play when the mode started. We would also configure a
scoring entry for the pop bumpers to award 10,000 points per hit, and
we would enable blocking so that scoring event was not passed down to
the base mode. (Otherwise a pop bumper hit when our super_jets mode
was active would be worth 10,100 points.) We could choose to keep this
mode running when the ball ends or to reset it. If we want to make the
second round to super jets require 75 hits instead of 50, we could
configure a second logic block in the base mode which would start
counting when the first logic block ended. This of course is just one
simple example, but it shows one way you can use modes to control game
logic. (All without programming!) You can imagine similar modes for
the skill shot, combos, extra ball lit and extra ball collected,
progress towards multiball, multiball itself, and pretty much anything
else you need to do.



Logic Blocks
------------

Logic Blocks are the logical "glue" you use to create game logic and
tie together shots, scoring, display, lighting, and sound effects.
They're based onMPF events. They watch for an event (or events) to
happen, and when they do, they post a "complete"event. Logic blocks
can be configured to start over when they're complete, reset between
balls, and enable and disable based on other events. There are three
types of logic blocks: *Sequence*, *Counter*, and *Accrual*.


+ Sequence logic blocks watch for a sequence of events to happen in
  order. e.g. Event A, then B, then C, then D, then it posts the
  "complete" event.
+ Accrual logics blocks watch for a bunch of different events to
  happen, but in any order. So once events A, B, C, and D happen, then
  the "complete" event is posted.
+ Counter logic blocks just count (up or down) the number of times an
  event happens.So after event A happens 15 times, post the "complete"
  event.


You can read the documentation on logic blocks for the full details of
how to use them, but in terms ofusing them for game logic, hopefully
it's pretty clear how simple and powerful they are. Someexamples:


+ To start a wizard mode, you could configure that mode's start event
  to be an accrual logic block which is based on the events posted by
  your 15 different game modes completing.
+ You can configure a target to light based on accrual logic block
  which is configured for 3 different ramp shots made in the same ball.
+ You can configure the a light extra ball mode to start based on the
  event posted by the bonus multiplier moving to 8x.
+ You can configure progress towards starting a multiball mode with a
  counter logic block based on ball_locked events being posted.




Timers
------

Timers are kind of like logic blocks except they run automatically
based on time rather than waiting for events to move them towards
completion. You can configure timers (also via the config files) which
start when a certain event is posted, then they post a "complete"
event when they end. Timers can run up or down, and you can specify
what the count is being ticks. You can also specify how fast they
tick. The default is 1 second per tick, but most pinball machines use
something we call "pinball time" where each "second" in a countdown
mode is actually more like 1.5 or 2 seconds of real world time. You
can also configure events which add, subtract, pause, restart, or
reset timers. So how do timers relate to game logic? Lots of ways:


+ If you want to create a timed mode, you can add a timer entry to
  that mode's config. Then also configure the mode to stop when the
  timer posts its "complete" event.
+ You can use timers in combination with counter logic blocks and a
  game mode to track "combo" shots:

    + Create a game mode called "combos" which has its start events based
      on a shot to a ramp or loop.
    + Within that mode, create a counter logic block that increments a
      combo count for each shot that's made.
    + Create a timer in the combomode that counts down (3 seconds or
      whatever you want) and set the mode's stop event to be that timer
      completing. When the timer ends, the mode will stop and unload, along
      with its counter logic block and any scoring, lighting, or display
      effects you had.
    + Since logic blocks are stored per-user, the next time the combo mode
      starts (based on the next ramp shot), the combo progress will be
      resumed. (Of course you can reset this per ball each time or whatever
      you want, if you want.)





"Real" programming
------------------

Even though we try to make it so you can do as much as possible with
your machine config files, it's possible that you'll eventually come
to a point where you have to do actual programming. (Though feel free
to post to our `MPF users forum`_ first to ask. Hopefully we can find
a way to do what you want to do or write the code for you.) This
section isn't meant to be a programming guide (`we do have that
though`_), rather, it's to help you figure out what how you might want
to approach your custom programming. First, the good news is that MPF
was designed to be extended with custom programming. You don't have to
"hack" or "break" anything to add some custom code. Second, we've
created a few different options for adding custom code, and they're
both really easy to use. You don't have to be a Python master or
understand anything about subclassing or method resolution order or
PEP 20. You can just write some very simple code to do what you need
to do and move on. The main thing when it comes to adding Python code
to your game is to decide whether your code is mode-specific or
machine-wide. If it's mode-specific, you'll add it to your mode's
`code`subfolder, and if it's machine-wide, you'll create a
`scriptlet`_. Examples of machine-wide scriptlets:


+ In *Judge Dredd*, the crane which unloads balls from the Deadworld
  orbit is a scriptlet to replace the Deadworld ball device's eject()
  method.
+ Same for the Cryo-Claw in *Demolition Man*.
+ In *Star Trek: The Next Generation*, a scriptlet is used to pre-
  stage the required number of balls in the VUKs after a game ends. (1
  ball in the left VUK, 1 in the left cannon VUK, 1 in the right cannon
  VUK.)


.. _we do have that though: https://missionpinball.com/forum/
.. _here: https://missionpinball.com/docs/events/
.. _ShowPlayer: https://missionpinball.com/docs/configuration-file-reference/showplayer/
.. _here: https://missionpinball.com/docs/game-modes/
.. _scriptlet: https://missionpinball.com/docs/programming-guide/scriptlets/
.. _Scoring: https://missionpinball.com/docs/configuration-file-reference/scoring/
.. _here: https://missionpinball.com/docs/events/built-in-events/
.. _SoundPlayer: https://missionpinball.com/docs/configuration-file-reference/soundplayer/
.. _SlidePlayer: https://missionpinball.com/docs/configuration-file-reference/slideplayer/


