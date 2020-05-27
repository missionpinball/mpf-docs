Flippers
========

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/flippers`                                                      |
+------------------------------------------------------------------------------+

.. contents::
   :local:

.. include:: /hardware/voltages_and_power/common_ground_warning.rst

Flippers are probably the first thing you think of when you think about building
your own pinball machine. In fact when most people get their own hardware and
start drilling holes in a piece of plywood, the first visible thing they do is
to get their flippers flipping.

.. image:: /mechs/images/flippers.png
  :width: 400
  :alt: Pinball flippers

MPF has support for lots of different kinds of flippers (as there are many
different ways they've been wired over the years), as well as a lot of different
options for how flippers are fine tuned.

MPF also has support for various "novelty" flipper modes (no-hold flippers,
reversed flipper buttons, :doc:`weak flippers <weak_flippers>`, etc.)

We recommend you read the :doc:`/mechs/coils/dual_vs_single_wound`
guide to understand the difference between "dual wound" and "single wound"
coils, as flippers in pinball machines can be either type.

You should also probably read the EOS Switches guide if your machine has flipper
EOS switches. (In general EOS switches are not needed for flippers with MPF.)

See :doc:`coil hardware </mechs/coils/index>` for more details about the
current, resistance, number of windings and the strength of coils.

Debounce and Recycle on Flipper Coils
-------------------------------------

In MPF you can :doc:`configure debounce for each switch </mechs/switches/debounce>`
and :doc:`recycle for each coil </mechs/coils/recycle>`.
However, both will be overwritten when you enable flippers.
Debounce will be set to ``quick`` and ``recycle`` will be disabled.
In some platforms MPF might reconfigure your switch debounce settings when
activating the hardware rules (if the platform does not allow separate
settings) which might lead to more switch events when flippers are active.

Generally, this is how flipper work in most machines and this is how players
will expect flippers to behave.
If you want to change this let us know in the forum (or you could change it in
by overloading the flipper device class).

Default Events
--------------

MPF contains built-in support for the flipper cancel combo. If you
add the tag ``left_flipper`` to your left flipper switch, and ``right_flipper``
to your right flipper switch, then whenever the player hits both flippers at
the same time, an MPF event called *flipper_cancel* will be posted.
This is implemented as :doc:`combo switch </game_logic/combo_switches/index>`.

Additionally, MPF contains a default
:doc:`timed switch </game_logic/timed_switches/index>` for flipper cradle.
It will post ``flipper_cradle`` when a player cradles a ball for 3s.
Later it will post ``flipper_cradle_release`` when the player releases the
ball.

Monitorable Properties
----------------------

For :doc:`dynamic values </config/instructions/dynamic_values>` and
:doc:`conditional events </events/overview/conditional>`,
the prefix for flippers is ``device.flippers.<name>``.

*enabled*
   Boolean (true/false) which shows whether this ball hold is enabled.

Related How To guides
---------------------

.. toctree::
   :titlesonly:
   :caption: Flipper How To Guides

   dual_wound
   single_wound
   disabled_flippers
   enabling_secondary_flippers
   weak_flippers

Related Events
--------------

None

.. toctree::
   :titlesonly:
   :caption: Flipper Concepts

   eos_switches




