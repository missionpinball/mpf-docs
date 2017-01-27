queue_event_player:
===================

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`shows </shows/index>`                                       | **YES** |
+----------------------------------------------------------------------------+---------+

.. versionadded:: 0.32

.. note:: This section can also be used in a show file in the ``queue_events:`` section of a step.

The ``queue_event_player:`` section of your config file is similar to the ``event_player:``,
except it posts :doc:`queue events </events/overview/event_types>` instead of regular events.

This section is particularly useful with the :doc:`/config/queue_relay_player`.

Here's an example:

.. code-block:: yaml

   queue_event_player:
      some_event:
         queue_event: my_queue
         events_when_finished: my_queue_done

In the example above, when the regular event *some_event* is posted, a new queue event
called *my_queue* will be posted. After all the handlers for *my_queue* are done, the
event *my_queue_done* will be posted. (This could be immediately if none of the handlers
blocked it, or it could be awhile if one of those handlers is doing something else first.)

Settings
--------

queue_event:
~~~~~~~~~~~~

The name of the queue event that will be posted when the parent event is posted. (required)

args:
~~~~~

A sub-configuration of key:value pairs that will be posted with the event. This setting
is optional.

events_when_finished:
~~~~~~~~~~~~~~~~~~~~~

The event name that will be posted when all the handlers of this queue event are done
processing it. This setting is optional.
