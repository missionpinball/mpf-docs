
The Mission Pinball Framework uses `events`_ for many different
things. Here's a list of the events that framework uses out of the
box, along with notes about how they work. As you write your own game
code, feel free to add handlers to these events if you'd like to
interact with them in any way. Of course you're also free to create
your own events. By the way, don't be afraid to go nuts with events.
Even if you have lots of them firing every second, that's fine.
Computers are fast. Note that event names are not case sensitive. They
are all converted to lowercase before they're posted. (Event handlers
are also converted to lowercase when they're registered.)



ball_live_added
~~~~~~~~~~~~~~~

A ball was successfully added to the playfield. The number of live
balls in play has increased by one. This event passes a parameter
total_live which is the current number of balls that are live.



ball_drain
~~~~~~~~~~

A ball has just entered a ball device tagged with 'drain.' (i.e. a
ball has just drained from the playfield.) Note this does not
necessarily mean that a live ball was removed from play. For example,
if the machine has tilted, any live balls will still drain even though
they're no longer in play. This is a relay event. It will pass a
parameter called balls which is the number of balls that just drained.
Registered handlers can change this count if they don't want the
additional processing of the drained balls. (For example, the ball
save plugin will change the balls drained to zero since it will add
new live balls into play.)



ball_live_removed
~~~~~~~~~~~~~~~~~

A ball has been removed from live play. The number of live balls in
play has decreased by one. This event includes a paramenter
*total_live*which is the number of balls remaining live



ball_save_enable
~~~~~~~~~~~~~~~~

Ball save is now enabled.



ball_save_disable
~~~~~~~~~~~~~~~~~

Ball save is now disabled.



ball_saved
~~~~~~~~~~

A ball was just saved.



ball_search_begin_<phase>
~~~~~~~~~~~~~~~~~~~~~~~~~

A ball search has begun at the given `phase`_.



ball_search_end
~~~~~~~~~~~~~~~

The ball search is ending



ball_shoot_again
~~~~~~~~~~~~~~~~

The same player is shooting again.



ball_ended
~~~~~~~~~~

The ball has successfully ended.



ball_ending
~~~~~~~~~~~

The ball is in the process of ending. Any modules who want to do
something before the ball ends (like showing a failure animation or
something) should act on this. This is a *queue* event.



ball_started
~~~~~~~~~~~~

A new ball has successfully started. (This is called for each new
ball, including when the same player shoots again.) This event
contains two parameters: *ball,* which is the ball number that's
started, and *player,* which is the player number who's currently up.



ball_starting
~~~~~~~~~~~~~

If you want to do something that might take some time, respond to
this.This is a *queue* event.



balldevice_ *<name>*_ball_enter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A ball has entered the ball device called <name>. This event
represents one ball. If multiple balls enter then this posts multiple
times.



balldevice_ *<name>*_ball_eject_request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ball device <name> has received a request to eject a ball. This
event passes a parameter *balls* which is the number of balls for this
eject request.



balldevice_ *<name>*_ball_eject_attempt
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ball device <name> is attempting to eject a ball.This event passes
a parameter *balls* which is the number of balls for this eject
attempt.



balldevice_ *<name>*_ball_eject_failed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ball eject has failed and the device has given up trying



balldevice_ *<name>*_ball_eject_success
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ball device <name> has confirmed that it has ejected a ball.This
event passes a parameter *balls* which is the number of ballsthat were
ejected.



balldevice_<name>_ball_enter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A ball just entered this ball device.This event passes a parameter
*balls* which is the number of balls that just entered.



balldevice_<name>_ok_to_eject
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This ball device is ready to eject balls.This event passes a parameter
*balls* which is the number of balls ready to eject.



diverter_<name>_activating
~~~~~~~~~~~~~~~~~~~~~~~~~~

The diverter <name> is activating now.



diverter_<name>_deactivating
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The diverter <name> is deactivating now.



diverter_<name>_disabling
~~~~~~~~~~~~~~~~~~~~~~~~~

The diverter <name> is disabling itselfnow. A parameter *auto*=True is
passed if this diverter is disabling itself automatically based on a
request from one of its target devices.



diverter_<name>_enabling
~~~~~~~~~~~~~~~~~~~~~~~~

The diverter <name> is enabling itselfnow.A parameter *auto*=True is
passed if this diverter is enabling itself automatically based on a
request from one of its target devices.



extra_ball_awarded
~~~~~~~~~~~~~~~~~~

An extra ball was just awarded to this player.



game_ending
~~~~~~~~~~~

The game is ending. This is a *queue* event which allows handlers to
finish up anything they need to do before releasing the queue and
proceeding to game_ended.



game_ended
~~~~~~~~~~

A game has ended.



game_started
~~~~~~~~~~~~

A game has started. Used to reset variables and stuff.



game_starting
~~~~~~~~~~~~~

The game is in the process of starting.This is a *queue* event which
allows handlers to finish up anything they need to do before releasing
the queue and proceeding to game_started.



init_phase_ *x*
~~~~~~~~~~~~~~~

There are fivephases of machine initialization.



machine_flow_advance
~~~~~~~~~~~~~~~~~~~~

The machine isadvancing to the next machine mode. (Typically from
attract to game or from game to attract.)



machine_reset_phase_x
~~~~~~~~~~~~~~~~~~~~~

There are three phases of machine reset.



machineflow_ *<machine_mode>*_start
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The named <machine_mode> has started. This name is based on the class
you specify in the machine flow section of the configuration files.
For example 'machineflow_attract_start'.



machineflow_<machine_mode>_stop
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The named <machine_mode> has stopped.



player_turn_end
~~~~~~~~~~~~~~~

The player's turn has ended (including all their shoot agains). Next
will be either player_turn_start or game_end.



player_turn_start
~~~~~~~~~~~~~~~~~

A new player is up.



player_add_request
~~~~~~~~~~~~~~~~~~

This is a *boolean* event which is posted when the game wants to add a
player. Return False if you want to deny this



player_add_success
~~~~~~~~~~~~~~~~~~

A new player has successfully been added. This event passes a
parameter *player* which is the new Player classobject and *num* which
is the integer number of the player that was just added.



reel_ *<score reel group>*_advance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The score reel is advancing one position.



request_to_start_game
~~~~~~~~~~~~~~~~~~~~~

The machine is requesting to start a game. This is a boolean event, so
you can return False to deny it.



scorereelgroup_ *<name>*_valid
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The score real group has been validated against the assumed value
list. This event passes a parameter *value* which is the current
numerical value show on the reels.



*<score reel group>*_rollover
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The score reel group has just exceeded the limits of the value that it
can display and has rolled over. (Congrats to the player!)



*<score_reel>*_ready
~~~~~~~~~~~~~~~~~~~~

The score reel is ready to be advanced again.



*<score reel>*_hw_value
~~~~~~~~~~~~~~~~~~~~~~~

The score reel has confirmed its hardware value. These event passes a
parameter *value* which is the confirmed value of this reel.



shot_ *<name>*
~~~~~~~~~~~~~~

The shot <name> has been made



sw_ *<tag>*
~~~~~~~~~~~

A switch with the tag <tag> has just been activated.



<targetgroup>_<name>_unlit_complete
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Every member target in the target group <name> of type <targetgroup>
is now unlit. (In other words, this target group is now reset.)



<targetgroup>_<name>_lit_complete
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Every member target in the target group <name> of type <targetgroup>
is now lit. (In other words, this target group is now complete.)



<targetgroup>_<name>_unlit_hit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

One of the member targets in the group <name> of type <targetgroup>
was hit while it was unlit.



<targetgroup>_<name>_lit_hit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

One of the member targets in the group <name> of type <targetgroup>
was hit while it was lit.



target_<name>_lit
~~~~~~~~~~~~~~~~~

The target <name> is not lit



target_<name>_unlit
~~~~~~~~~~~~~~~~~~~

The target <name> is now unlit



target_<name>_lit_hit
~~~~~~~~~~~~~~~~~~~~~

The target <name> was in the lit state, and it was just hit.



target_<name>_unlit_hit
~~~~~~~~~~~~~~~~~~~~~~~

The target <name> was in the unlit state, and it was just hit.



tilted_ball_drain
~~~~~~~~~~~~~~~~~

A ball has just drained while the machine was tilted.



timer_tick
~~~~~~~~~~

Event posted every machine tick. (So... a lot!)

.. _events: https://missionpinball.com/framework/system-components/events/
.. _phase: /docs/configuration-file-reference/ballsearch/


