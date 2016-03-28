
MPF has a robust system for managing the players in an active game.
Individual player objects are created (based on the Player class in
the *mpf/system/player.py* module), with one instance of that class
per player in the game. Players are automatically created as they're
added to a game and removed when the game ends. A key concept of
player management in MPF is *player variables*. A player variable is a
name/value pair of some attribute you want to store on a per-player
basis. (The most obvious example is *score*.) There are two types of
player variables— *tracked* and *untracked*.



Tracked player variables
------------------------

Tracked player variables automatically post events when they change,
and the event they post contains the name of the player variable, the
new value, the previous value, and the change in value. You can then
use the event generated from the player variable change to do anything
you want. (Start or stop a mode, update a timer, show something on the
display, play a show, etc.) Tracked player variables are also sent to
the media controller via BCP. The events posted for tracked player
variable changes are posted automatically in the form of player_<
*variable_name>* . For example, if player one's score is currently
10,000 and then they get 500 points, an MPF event will be posted
called *player_score* with parameters *value=10500, pre_value=10000,
change=500, player_num=1*. Default tracked player variables include
*score* (the player's score), and *number* (which player number they
are), and of course you can create lots more of them as you build-out
your game. (You can configure logic blocks, shot progress, and timers
all to use tracked player variables to store their settings.)



Untracked player variables
--------------------------

Untracked player variables are also stored on a per-player basis, but
they don't automatically post the events when they change, and they
are not sent out via BCP. Untracked player variables are used for the
"internal" things you might need to save on a per-player basis but
that you don't need to broadcast everywhere. For example, the states
of logic blocks are automatically stored on a per-player basis as
untracked player variables.



Accessing player variables in code
----------------------------------

(This is a thing for people writing Python code. If you're only using
config files, you can skip it.) Tracked player variables are used like
this:


::

    
    player.ball = 1


or


::

    
    player['ball'] = 1


Sometimes you don't want to go through all that gunk. Sometimes you
just need to store something (or several things) on a per-player basis
for your own use, but you don't need it being broadcast everywhere
(and running into BCP size limits, etc.). It was impossible to create
your own untracked attributes before because the Player class's
*__setattr__* method would store whatever you set as a tracked player
variable. Untracked player variables are accessed like this:


::

    
    player.uvars['some_name'] = whatever


You can have as many of these as you want per player, all with
separate names. You can store whatever you want (values, lists, dicts
. . . any Python object). Use them like you use a Python dictionary.
Loop, set, read, iterate, etc.



