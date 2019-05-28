Conditional Events
==================


So far we've talked about how events are just strings of text, for example:

* ball_started
* game_ending
* shot1_hit
* mode_jackpot_starting
* etc.

However, it's possible for events to have key/value parameters attached to them.

For example, when the "ball_started" event is posted, it has two parameters
attached to it: "ball" (which is the number of the ball that's
started), and "player" which is the number of the player whose ball just
started.

This means that the "ball_started" event isn't just MPF saying, "Hey, a ball
just started", rather, it's more like MPF saying, "Hey, a ball just started
for player 2, ball 3.".
You can also see that in your mpf log:

.. code-block:: console

   INFO : EventManager : Event: ======'ball_started'====== Args={'player': 2, 'ball': 3}

By the way, in case you're wondering how we know that the ``ball_started`` event
has those parameters (or even that ``ball_started`` is an event), they're
all in the :doc:`event reference guide </events/index>`, and the entry for
:doc:`/events/ball_started` lists the parameters it has along with an
explanation of what those mean.

In addition to parameters in your event you can also reference most devices in
your machine.
For instance, you might want to start a mode after a counter reached a certain
value.
You can reference any
:doc:`placeholder variable </config/instructions/dynamic_values>` in a condtion
and also apply arbitrary logic/conditions to them.

Using keyword arguments in your config files
--------------------------------------------

What's *really cool* about event parameters is that you can use them in your
config files when you enter things that take action on events.

For example, here's a section of a config file that would show a slide called
"lets_go" when the *ball_started* event was posted:

.. code-block:: mpf-config

   slide_player:
      ball_started: lets_go

The example above will show that slide any time that the *ball_started* event
was posted, regardless of what the values of the parameters are.

However, you can enter the event name in your config file a bit differently so
that the action only takes place if that event is posted AND if the parameters
have certain values.

For example:

.. code-block:: mpf-config

   slide_player:
      ball_started{ball==1}: first_ball_intro

In the above example, the slide "first_ball_intro" will only be posted when
the *ball_started* AND when the value of ball is 1. (Since this entry doesn't
mention "player", then this action would happen when ball 1 is started for
any player.)

Of course you can use multiple entries with different values, like this:

.. code-block:: mpf-config

   slide_player:
      ball_started{ball==1}: first_ball_intro
      ball_started{ball>1}: lets_go

In this case, when the *ball_started* event is posted for Ball 1, the
"first_ball_intro" slide will be shown. And if it's posted with a ball after
Ball 1, the "lets_go" slide will be posted.

You can also combine things here using ``and`` or ``or``. For example:

.. code-block:: mpf-config

   slide_player:
      ball_started{ball==1 or ball==3}: special_slide

Now the "special_slide" will be shown for either ball 1 *or* ball 3.

You can also combine with "and", for example:

.. code-block:: mpf-config

   slide_player:
      ball_started{ball==3 and player==1}: special_slide

Now the "special_slide" will only show when the *ball_started* event is posted
for player 1, ball 3 (but not player 2, ball 3, etc.).

Feeling crazy yet?

In addition to keyword arguments from events), you
can also use ``current_player.`` to access player variables,
``players[x]`` to access player variables from any player (x is the player index),
``machine.`` to access machine variables, ``game.`` game attributes,
and ``settings.`` to access operator settings.

.. code-block:: mpf-config

   slide_player:
      ball_started{current_player.score > 1000000}: you_rule
      ball_started{current_player.score < 10000 and ball == 3}: you_stink

The above config will show the slide "you_rule" any time the *ball_started*
event is posted and the player's score is more than 1 million. It will also
show the slide "you_stink" if ball 3 is starting and the player has less than
10,000 points.

But wait, there's more!

You can also use standard math operators (``+``, ``-``, ``*``, ``/``, etc.)
to evaluate whether the action should take place:

.. code-block:: mpf-config

   slide_player:
      ball_started{ball > 1 and current_player.score < ((ball - 1) * 10000)}: uh_oh

This will post the slide "uh_oh" if the player is starting a ball after Ball 1
and their score is less than an average of 10k points per ball. (Notice that
you can also use parentheses to control the order of operation stuff you
learned in school.)

Most likely you wouldn't get that complex, but it's nice to know that you
can if you want. :)

You can also reference devices in your machine.
The syntax for that is ``device.DEVICE_TYPE.DEVICE_NAME.PLACEHOLDER``.
For instance, to reference the ``value`` of a ``counter`` called
``your_mode_counter`` you would use
``device.counters.your_mode_counter.value``.
In the following example we show a slide when the value of the counter is
above ``5`` in ball ``3``

.. code-block:: mpf-config

   slide_player:
      ball_started{ball == 3 and device.counters.your_mode_counter.value > 5}: nearly_did_all_modes

You can use all :doc:`placeholder variables </config/instructions/dynamic_values>`.

Subscribed config players
-------------------------

Sometimes you want to play a show, display a slide or enable a light
when certain condition hold true and remove/disable it when the condition no
longer holds.
This would usually require two config player entries with two different events
to add and remove the show (or light).
However, MPF supports subscriptions in config players for certain (not all)
variables.

This is an example:

.. code-block:: mpf-config

   light_player:
     "{machine.test_machine_var == 23}":
       led4: red
     "{current_player.test_player_var == 42}":
       led5: red

If will turn ``led4`` to ``red`` once the machine variable ``test_machine_var``
becomes ``23`` and turns ``led4`` back to ``off`` once ``test_machine_var``
becomes something else.
Same for ``led5`` and player variable ``test_player_var``.

Comparisons
-----------

* ``==`` equal
* ``!=`` not equal
* ``>`` greater than
* ``>=`` greater than or equal to
* ``<`` less than
* ``<=`` less than or equal to

Operators
---------

* ``+`` add
* ``-`` subtract (or negative if there's no space after it)
* ``*`` multiply
* ``/`` divide
* ``^`` power (exponent)
* ``%`` modulus
* ``^=`` bit xor
* ``not``
* ``and``
* ``or``
