Random event player
===================

The *random event player* is a :doc:`config player </config_players/index>` that's used to post random events from a
list of events.

This is an example:

.. code-block:: mpf-config

   # in your global config:
   random_event_player:
       play_random_event_global:
         scope: machine
         events:
           - event1
           - event2
           - event3

   ##! mode: base
   # in your mode:
   random_event_player:
       play_random_event:
         events:
           - event1
           - event2
           - event3
       play_random_event_with_weight:
         events:
           unlikely_event1: 2
           unlikely_event2: 3
           likely_event1: 45
           likely_event2: 50

When `play_random_event` is posted a random event is posted out of the list `event1`, `event2` or `event3`.


Usage in config files
---------------------

In config files, the random event player is used via the ``random_event_player:`` section.

Usage in shows
--------------

In shows, the random event player is used via the ``random_events:`` section of a step.

Config Options
--------------

See :doc:`/config/random_event_player` for config details.
