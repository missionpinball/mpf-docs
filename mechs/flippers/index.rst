Flippers
========

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/flippers`                                                      |
+------------------------------------------------------------------------------+

.. contents::
   :local:

Flippers are probably the first thing you think of when you think about building
your own pinball machine. In fact when most people get their own hardware and
start drilling holes in a piece of plywood, the first visible thing they do is
to get their flippers flipping.

MPF has support for lots of different kinds of flippers (as there are many
different ways they've been wired over the years), as well as a lot of different
options for how flippers are fine tuned.

MPF also has support for various "novelty" flipper modes (no-hold flippers,
reversed flipper buttons, weak flippers, etc.)

We recommend you read the :doc:`/mechs/dual_wound_coils/dual_vs_single_wound`
guide to understand the difference between "dual wound" and "single wound"
coils, as flippers in pinball machines can be either type.

You should also probably read the EOS Switches guide if your machine has flipper
EOS switches. (In general EOS switches are not needed for flippers with MPF.)

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

Related Events
--------------

None

.. toctree::
   :titlesonly:
   :caption: Flipper Concepts

   eos_switches




