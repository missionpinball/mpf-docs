queue_event_player:
===================

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+

.. overview

.. note:: This section can also be used in a show file in the ``queue_events:`` section of a step.

The ``queue_event_player:`` section of your config file is similar to the ``event_player:``,
except it posts :doc:`queue events </events/overview/event_types>` instead of regular events.

This section is particularly useful with the :doc:`/config/queue_relay_player`.

Here's an example:

.. code-block:: mpf-config

   queue_event_player:
     some_event:
       queue_event: my_queue
       events_when_finished: my_queue_done

In the example above, when the regular event *some_event* is posted, a new queue event
called *my_queue* will be posted. After all the handlers for *my_queue* are done, the
event *my_queue_done* will be posted. (This could be immediately if none of the handlers
blocked it, or it could be awhile if one of those handlers is doing something else first.)

.. config


Required settings
-----------------

The following sections are required in the ``queue_event_player:`` section of your config:

queue_event:
~~~~~~~~~~~~
Single event. The device will add an handler for this event. Defaults to empty.

The name of the queue event that will be posted when the parent event is posted. (required)


Optional settings
-----------------

The following sections are optional in the ``queue_event_player:`` section of your config. (If you don't include them, the default will be used).

args:
~~~~~
One or more sub-entries. Each in the format of ``string`` : ``string``

A sub-configuration of key:value pairs that will be posted with the event. This setting
is optional.

events_when_finished:
~~~~~~~~~~~~~~~~~~~~~
Single event. This device will be posted by the device. Defaults to empty.

The event name that will be posted when all the handlers of this queue event are done
processing it. This setting is optional.


Related How To guides
---------------------

* :doc:`/game_design/game_modes/fake_ball_save`
* :doc:`/config_players/queue_event_player`
