Switches
========

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/switches`                                                      |
+------------------------------------------------------------------------------+
| :doc:`/config/switch_overwrites`                                             |
+------------------------------------------------------------------------------+

.. contents::
   :local:

MPF's *switch* device represents a switch in a pinball machine. This device is
used for switches, including cabinet buttons, rollovers, targets, optos, trough
switches, DIP switches, etc.

There are two general switch types in pinball machines (read those for details):

* :doc:`Mechanical switches <mechanical_switches>`
* :doc:`Optical switches <optos>`

Typical switch applications in pinball machines are:

* :doc:`Rollover/lane switches <rollover_switches>`
* :doc:`Standup targets </mechs/targets/stationary_targets/index>`
* :doc:`Spinners </mechs/spinners/index>`
* :doc:`Flipper buttons </mechs/flippers/index>` and :doc:`Flipper end-of-stroke switches </mechs/flippers/eos_switches>`
* As part of a mech such as
  :doc:`Drop targets </mechs/targets/drop_targets/index>`,
  :doc:`Popbumpers </mechs/pop_bumpers/index>` or
  :doc:`Ball Devices </mechs/ball_devices/index>`/:doc:`Troughs </mechs/troughs/index>`
* :doc:`Service and door switches <service_and_door_switches>`

MPF supports all types of switches found in all generations of pinball machines,
including matrix switches, direct switches, Fliptronics switches, switches
connected to I/O boards, etc.

Switches only have two states: *active* and *inactive*. (We don't say "open" or
"closed" because sometimes switches are normally-closed which mean they're
actually active when they're open.) In MPF, you configure your switches in the
``switches:`` section of your machine configuration file, including options
(like whether the switch is "active" when it's in the open state or the closed
state.)

You can also configure :doc:`debounce settings <debounce>` for each switch,
which controls how MPF
responds to switch events. Saying that a switch has to be "debounced" means that
the pinball controller makes sure the switch is actually in its current state
for a few milliseconds before it send the switch event to MPF. This can be
useful to filter out unwanted or phantom switch events which might happen due to
electrical interference or other little weird things.

Most switches in pinball machines are debounced except for the ones that you
absolutely want to fire instantly, like flipper switches and the switches
attached to automatically fired coils like slingshots and pop bumpers.

This is an example:

.. code-block:: mpf-config

   switches:
     my_switch:
       number: 42    # number from your hardware platform

Switch Concepts
---------------
* :doc:`debounce`
* :doc:`switch_controller`

Monitorable Properties
----------------------

For :doc:`dynamic values </config/instructions/dynamic_values>` and
:doc:`conditional events </events/overview/conditional>`,
the prefix for switches is ``device.switches.<name>``.

*state*
   Numeric value which represents the logic state of this switch.
   0 is inactive, 1 is active.

*recycle_jitter_count*
   How many times this switch has activated within it's configured
   ``ignore_window_ms:``. (These activations are ignored.)

Related How To guides
---------------------

* :doc:`/tutorial/3_get_flipping`
* :doc:`optos`
* :doc:`mechanical_switches`
* :doc:`rollover_switches`
* :doc:`service_and_door_switches`
* :doc:`start_tournament_and_launcher_buttons`

Related Events
--------------

* :doc:`/events/switch_active`
* :doc:`/events/switch_inactive`

.. include:: /events/include_switches.rst


.. toctree::
   :titlesonly:
   :hidden:

   debounce
   switch_controller
   optos
   mechanical_switches
   service_and_door_switches
   rollover_switches
   start_tournament_and_launcher_buttons
   breakout_boards
