Achievement Groups
==================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/achievement_groups`                                            |
+------------------------------------------------------------------------------+

.. versionadded:: 0.32

.. contents::
   :local:

Achievement groups are used to group together individual achievements.

If you look at the real-world examples we used in the achievements documentation,
each of the entries in that list is an achievement "group" that's made up of
individual achievements.

For example, in The Addams Family, the mansion awards would be individual
achievements, for example:

* 9 Mil
* 6 Mil
* 3 Mil
* Thing
* Quick Multiball
* Grave Yard at Max
* Raise the Dead
* Etc.

Each of those individual achievements has a state (enabled, started, completed,
etc.)

If you were building a config for *The Addams Family (TAF)* with MPF, you
would create an achievement group called "Mansion Awards", and then you would
add the individual achievements to that group.

The achievement group will let you perform group-level actions on the
achievements in the group. For example:

* Randomly select one of the incomplete achievements (so you can flash that
  achievement's light to indicate it's selected).
* Change which achievement is selected. (In *TAF*, each hit to a pop
  bumper changes the lit achievement, so you'd configure your achievement group
  to pick a new achievement when the pop bumper hit event was posted.)
* Post an event when all achievements are complete (to start a wizard mode, etc.)
* Post a "start" event for whichever achievement is lit (In *TAF*, you
  shoot the lit electric chair or the swamp to start the flashing achievement.)

Monitorable Properties
----------------------

For :doc:`config placeholders </config/instructions/placeholders>` and
:doc:`conditional events </events/overview/conditional>`,
the prefix for achievement groups is ``device.achievement_groups.<name>``.

*enabled*
   Boolean (true/false) as to whether this achievement group is enabled.

*selected_member*
   The achievement in the group that is currently in the selected state, or
   *None* if no achievement is selected.

Related How To guides
---------------------

* :doc:`/cookbook/TAF_mansion_awards`

Related Events
--------------
* Custom events as defined in the achievement's configuration in your config
  files.
