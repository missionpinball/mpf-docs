random_event_player:
====================

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`shows </shows/index>`                                       | **YES** |
+----------------------------------------------------------------------------+---------+

.. note:: This section can also be used in a show file in the ``randoms:`` section of a step.

.. overview

The ``random_event_player:`` section of your config is where you can play a random
event out of a list based on an event.

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

Required settings
-----------------

The following sections are required in the ``random_event_player:`` section of your config:

events:
~~~~~~~
List of one (or more) values, each is a type: ``string`` or dict of type ``string:int``.

List the events to choose from.
If you use a list all events will be equiprobable.
You can also use a dict with ``eventname: probablity``.
See the example above.

force_different:
~~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``True``

If set to true it will enforce that the same entry will never appear twice in a
row. When setting ``force_all`` to true this will prevent that the last event
is the same as the first of the next iteration.

force_all:
~~~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``True``

Enforce that all events are posted once before a event is posted a second time.

disable_random:
~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

Disable random.

scope:
~~~~~~
Single value, type: one of the following options: player, machine. Default: ``player``

The scope of the random selection for ``force_different`` and ``force_all``.
When setting to ``player`` this is enforced per player and persisted between
balls.



