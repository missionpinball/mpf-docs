Game Start Sequence
===================

This sequence document starts with the attract mode running and ends
with the running.

#. The player pushes a button tagged with "start". The time is noted.
#. The player releases that button. (This is important because in MPF
   it's possible to do different things based on a so-called "long press"
   of the start button. For example, you might start the machine in
   tournament mode, or allow players to select a player profile. So the
   game start process doesn't actually begin until the start button is
   released.)
#. The Attract mode posts the boolean event *request_to_start_game*.
   See the section below about the "How the *request_to_start_game*
   event works."

    #. The ball controller makes sure there are enough balls and that they
       are all gathered.
    #. Other modules make sure they are ready for the game to start and
       deny it if not.

#. The attract mode's ``result_of_start_request`` is the callback for
   the request event. If the result is True, this process continues.
#. The attract mode posts an event *game_start*.
#. The game mode is registered as a handler for the *game_start*
   event, so it starts.
#. The game mode posts a queue event called *game_starting*.

    #. The score reels reset themselves
    #. The auditor enables itself
    #. Info lights reset

#. The game mode's ``game_start()`` method is the callback for that
   queue event which is called when that event is finished.
#. The game mode calls its ``_player_add()`` method.

    #. The first player is created
    #. The number of players is updated

#. The game mode posts the event *game_started* .
#. The game mode calls its ``player_turn_start()`` method.

At this point we have a running game!

How the "request_to_start_game" event works
-------------------------------------------

When a player pushes (and releases) the start button during attract
mode, the Attract Mode code posts an MPF event called
*request_to_start_game*.This event is not a normal event that is just
posted and forgotten, rather, it's a special type of event called a
"boolean event." When a system component posts a boolean event, it
actually watches for responses from every other component that is
watching for that event. If this event is posted and nothing speaks up
to stop it, then the module that posted that event will continue. But
if anything "kills" that event, that will cause whatever module that
posted it to *not* proceed. This can be a bit confusing, so let's go
through this in plain English:

#. When a player pushes and releases the start button, the attract
   mode says, "Hey! I'd like to start a game now. Does anyone have a
   problem with that?
#. This gives other components a chance to pipe up and say, "Yeah! I
   have a problem with that. You're not starting a game!"
#. If no one speaks up, the attract mode will say, "Ok, I'm posting a
   follow up event to kick off the game start process."
#. But if any component denies the start, then the attract mode will
   do nothing, and the game doesn't start.

So what types of components might register to watch for and/or
interrupt the game start request? Lots of them.

The ball controller
watches for this event and will make sure that the game has the
minimum number of balls installed, and that those balls are all in
their "home" positions. If everything is ok when the game start
request comes in, then the ball controller will do nothing, allowing
the start to proceed. But if the start request comes in an the ball
controller doesn't have enough balls, it will "kill" the start
request, and the game won't start. (When something kills an event like
this, it's up to that component to make it obvious to the player
what's going on. For example, the ball controller might put a message
on the DMD which says something about balls being missing.)

Another
component that might care about this game start request is the credits
module. If the machine is *not* set to free play, then when the
*request_to_start_game* event is posted, the credits module will make
sure there's at least one credit on the machine. If not, then it will
kill the event and not allow the game to start.

At this point you
might be wondering what the point of all this is? Why have these start
request events? Isn't this overly complicated? Why not just have MPF
check all these things on its own?

The beauty of these types of events
is that it makes it easy to customize and add features and components
to MPF without the core MPF software knowing (or caring) what's
installed and what might be starting an event. The MPF core doesn't
know about credits or free play or any of that. It just says, "Hey, I
want to start a game. Is that cool?" If you don't have a credits
module, or if the credits module isn't active because the machine is
on free play, then the credits module isn't there to deny the start
and MPF can start the game no problem. But if then if you add or
enable the credits module,then this start request process is what
gives that random module a "hook" into the game starting process.

The
real power of this comes with future flexibility. You might want to
create some other type of component that we never thought of. (Maybe
you don't want any new games to start after 11pm or something?) Thanks
to this request event, you can write your own module as a simple snap-
in which "hooks" this game start event, and MPF doesn't need to know
about the details, and you don't have to resort to a "hack" of the MPF
core to hook in whatever future crazy module you have. It's very cool!
