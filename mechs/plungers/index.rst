Plungers & Ball Launch Devices
==============================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/ball_devices`                                                  |
+------------------------------------------------------------------------------+

A Plunger is a type of ball device. MPF supports mechanical (traditional
"spring" plungers), coil-fired plungers, and combo auto/manual plungers.

Here are the options:

* :doc:`mechanical_with_switch`
* :doc:`mechanical_no_switch`
* :doc:`coil_fired`
* :doc:`auto_manual`

Since there are so many different options, you need to first identify which
type of plunger or ball launch system your machine has. So look at the following
pictures to match up what you have, and then follow the specific links to see
how to configure MPF to use it in your machine.

Option 1: Spring plunger with ball switch
-----------------------------------------

The most "traditional" style plunger is a spring-powered mechanical plunger lane.
In modern machines, there's a switch at the bottom of the plunger lane which is
activated by a ball sitting in the plunger lane waiting to be plunged.

Here's an example of this from a Pin*Bot machine:

.. image:: /mechs/images/plunger_with_switch.jpg

If you have this type of spring-powered plunger with a switch that's active when
a ball is sitting in it ready to be plunged, follow the :doc:`mechanical_with_switch`
guide to configure it in MPF.

Option 2: Spring plunger with no ball switch
--------------------------------------------

Older pinball machines (typically those that only have one ball) have what
appear to be traditional plungers like in Option 1, but if you look closely,
you'll notice that there is no switch which is active when the ball is sitting
in the plunger lane.

Here's an example of this from Gottlieb Big Shot:

.. image:: /mechs/images/plunger_no_switch.jpg

If you have this type of spring-powered plunger with **no** switch that's active when
a ball is sitting in it ready to be plunged, follow the :doc:`mechanical_no_switch`
guide to configure it in MPF.

Option 3: Combo spring plunger with coil-fired autolauncher
-----------------------------------------------------------

Many modern machines have a combination-style plunger which combines a
mechanical spring-powered plunger with an autolauncher coil. These types
of plungers allow game to decide whether the player should manually
pull back on the plunger handle to launch the ball with spring power or
whether the game should pulse a coil to eject the ball into play.

Here are two examples of slightly different versions of these, the left
from a Stern Star Trek Premium, and the right from a Gottlieb Brooks 'n Dunn machine:

.. image:: /mechs/images/auto_manual_plunger.jpg

If you have this type of auto/manual combo plunger, follow the :doc:`auto_manual`
guide to configure it in MPF.

Option 4: Coil-fired plunger (no mechanical spring option)
----------------------------------------------------------

The final plunger option is the fully automatic coil-fired option that has
no mechanical spring-based option.

There are a few different physical forms of this. Here's a typical example from
Judge Dredd where a coil shaft with a plastic tip is pulsed to launch the ball
directly:

.. image:: /mechs/images/coil_fired_plunger.jpg

And here's an example from Williams Star Trek: The Next Generation which uses
a catapult-style mechanism in order to launch the ball into play.

.. image:: /mechs/images/catapult_plunger.jpg

Note that both of these options are "identical" as far as MPF is concerned. They
both have switches which are active when a ball is able to be launched, they both
pulse coils to launch the ball, and neither one has a manual plunge option.

If you have this type of coil-powered plunger, follow the :doc:`coil_fired`
guide to configure it in MPF.

+------------------------------------------------------------------------------+
| Related How To Guides                                                        |
+==============================================================================+
| :doc:`/tutorial/8_plunger`                                                   |
+------------------------------------------------------------------------------+

+------------------------------------------------------------------------------+
| Related Events                                                               |
+==============================================================================+
| :doc:`/events/balldevice_ball_missing`                                       |
+------------------------------------------------------------------------------+
| :doc:`/events/balldevice_balls_available`                                    |
+------------------------------------------------------------------------------+
| :doc:`/events/balldevice_ball_device_ball_missing`                           |
+------------------------------------------------------------------------------+
| :doc:`/events/balldevice_captured_from_captures_from`                        |
+------------------------------------------------------------------------------+
| :doc:`/events/balldevice_ball_device_ball_eject_attempt`                     |
+------------------------------------------------------------------------------+
| :doc:`/events/balldevice_ball_device_ball_eject_failed`                      |
+------------------------------------------------------------------------------+
| :doc:`/events/balldevice_ball_device_ball_eject_success`                     |
+------------------------------------------------------------------------------+
| :doc:`/events/balldevice_ball_device_ejecting_ball`                          |
+------------------------------------------------------------------------------+

.. toctree::
   :titlesonly:
   :hidden:

   mechanical_with_switch
   mechanical_no_switch
   coil_fired
   auto_manual
