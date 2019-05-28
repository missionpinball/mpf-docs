queue_relay_player:
===================

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+


The queue_relay_player lets you "pause" queue event processing until some other
event is posted, at which time the original queue event processing continues.

Here's an example:

.. code-block:: mpf-config

   queue_relay_player:
      game_ending:
         post: start_my_mode
         wait_for: my_mode_done

This entry will watch for the *game_ending* event to be posted. (*game_ending* is a
queue event.) When it's posted, the queue relay player will pause the processing of
the *game_ending* event and post a new event, the *start_my_mode* in this case.

You can use that new event to do whatever you want, like start some custom mode
you want to run at game end before the machine goes back to the attract mode.

When your mode is done, you would configure it to post *my_mode_done* (or whatever
the ``wait_for:`` is set to, and that will release the queue and progress will
continue. If your mode doesn't need to do anything, it can simply post the
``wait_for:`` event and exit.

.. warning::

   If the ``wait_for:`` event is never posted, you will break your game since
   MPF will wait forever.

Note that each entry under ``queue_event_player:`` (the ``game_ending:`` in the
example above) must be for a queue event. (You can see which events are queue
events in the :doc:`event reference </events/index>`.) You can also use the
:doc:`/config/queue_event_player` to "convert" a regular event into a queue event.

Settings
--------

post:
~~~~~

The name of the event to post to trigger your action once the queue event
has been posted. (required)

wait_for:
~~~~~~~~~

The name of the event this queue will wait for to continue. In other words,
this is the event you need to post for the queue event to continue. (required)

args:
~~~~~

A sub-configuration of key:value pairs that will be posted with the event. This setting
is optional.
