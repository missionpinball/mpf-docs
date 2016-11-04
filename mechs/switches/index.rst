Switches
========

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/switches`                                                      |
+------------------------------------------------------------------------------+
| :doc:`/config/switch_overwrites`                                             |
+------------------------------------------------------------------------------+

MPF's *switch* device represents a switch in a pinball machine. This device is
used for switches, including cabinet buttons, rollovers, targets, optos, trough
switches, DIP switches, etc.

MPF supports all types of switches found in all generations of pinball machines,
including matrix switches, direct switches, Fliptronics switches, switches
connected to I/O boards, etc.

Switches only have two states: *active* and *inactive*. (We don't say "open" or
"closed" because sometimes switches are normally-closed which mean they're
actually active when they're open.) In MPF, you configure your switches in the
``switches:`` section of your machine configuration file, including options
(like whether the switch is "active" when it's in the open state or the closed
state.)

You can also configure debounce settings for each switch, which controls how MPF
responds to switch events. Saying that a switch has to be "debounced" means that
the pinball controller makes sure the switch is actually in its current state
for a few milliseconds before it send the switch event to MPF. This can be
useful to filter out unwanted or phantom switch events which might happen due to
electrical interference or other little weird things.

Most switches in pinball machines are debounced except for the ones that you
absolutely want to fire instantly, like flipper switches and the switches
attached to automatically fired coils like slingshots and pop bumpers.

.. toctree::
   :titlesonly:
   :caption: Switch Concepts

   debounce

.. toctree::
   :titlesonly:
   :caption: Switch How To Guides

   optos

+------------------------------------------------------------------------------+
| Related How To Guides                                                        |
+==============================================================================+
| :doc:`/tutorial/3_get_flipping`                                              |
+------------------------------------------------------------------------------+

+------------------------------------------------------------------------------+
| Related Events                                                               |
+==============================================================================+
| :doc:`/events/switch_name_active`                                            |
+------------------------------------------------------------------------------+
| :doc:`/events/switch_name_inactive`                                          |
+------------------------------------------------------------------------------+
| :doc:`/events/sw_tag_name`                                                   |
+------------------------------------------------------------------------------+
