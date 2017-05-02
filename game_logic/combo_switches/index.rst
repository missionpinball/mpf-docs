Combo Switches ("flipper cancel", etc.)
=======================================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/combo_switches`                                                |
+------------------------------------------------------------------------------+

.. versionadded:: 0.32

.. contents::
   :local:

MPF contains support for "combo switches" which are special combinations of
switches that post events when they're hit together.

The most basic example of this is the "flipper cancel" combination, where a
player can cancel a show or bonus by hitting both flippers at the same time.
In fact MPF contains built-in support for the flipper cancel combo. If you
add the tag ``left_flipper`` to your left flipper switch, and ``right_flipper``
to your right flipper switch, then whenever the player hits both flippers at
the same time, an MPF event called *flipper_cancel* will be posted.

Combo switches are also used for things like different kinds of skill shots.
For example, in *Attack From Mars*, if the player hits the launch button, the
ball is launched into the pop bumper area, but if the player holds down the
left flipper button while pressing the launch button, a pin in the upper
playfield is lowered and the ball is delivered to the flippers for an attempt
at a super skill shot. The left flipper + launch button combination is something
you can enable with MPF's combo switches.

MPF's combo switches also generate events once both switches are hit together,
then one switch is tapped while the other is held in. This can be used to
scroll through certain information screens with one button while the combo is
active.

You can set various timing options for combo switches, including how close
together the two switches have to be hit to count as a combo, how long they
have to be held, and how long they have to be released.

Monitorable Properties
----------------------

For :doc:`dynamic values </config/instructions/dynamic_values>` and
:doc:`conditional events </events/overview/conditional>`,
the prefix for combo switches is ``device.combo_switches.<name>``.

*state*
   String which reflects what state this combo switch is in.
   Options wil be one of the following: *inactive*, *both* or *one*.

Related How To guides
---------------------

.. todo:: TODO

Related Events
--------------

* :doc:`/events/combo_switch_state`
* :doc:`/events/flipper_cancel`
