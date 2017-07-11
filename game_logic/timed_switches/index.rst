Timed Switches
==============

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/timed_switches`                                                |
+------------------------------------------------------------------------------+

.. contents::
   :local:

MPF includes functionality to manage "timed_switches" which are scenarios when a single
switch is continuously active (or inactive, depending on the settings) for a set period
of time.

A classic example of this is the flipper "cradling" where a player holds a flipper button
in for a few seconds. In almost all modern machines, this is used to trigger a "player
info" screen that shows the player's score, how much bonus they have built up, high scores,
etc.

Flipper cradling is also used to reset (and pause) the ball search timer, since a player
could be holding a ball and drinking a beer, meaning no switch hits will happen, but the
ball search should not start.

In fact MPF's default config file (which is automatically used in all games) includes
a ``timed_switches:`` section for flipper cradling and automatically creates
*flipper_cradle* and *flipper_cradle_release* events (as long as you tag your flipper
switches with *left_flipper* and *right_flipper*).

Note that timed switches are similar to, but not the same as :doc:`combo switches </game_logic/combo_switches/index>`.

Monitorable Properties
----------------------

For :doc:`dynamic values </config/instructions/dynamic_values>` and
:doc:`conditional events </events/overview/conditional>`,
the prefix for timed switches is ``device.timed_switches.<name>``.

*active_switches*
   List of switches that are currently active past the time that this timed_switches: section is
   set for.

Related How To guides
---------------------

.. todo:: TODO

Related Events
--------------

* :doc:`/events/flipper_cradle`
* :doc:`/events/flipper_cradle_release`
