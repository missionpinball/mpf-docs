Kickbacks
=========

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/kickbacks`                                                     |
+------------------------------------------------------------------------------+
| :doc:`/config/ball_saves`                                                    |
+------------------------------------------------------------------------------+

.. contents::
   :local:

A kickback mechanism is a type of :doc:`autofire coil </mechs/autofire_coils/index>`
that kicks the ball back into play, typically located in an outlane.
It is often paired with a :doc:`ball_save </config/ball_saves>` to compensate for
missed kickbacks.

This is an example:

.. code-block:: mpf-config

   switches:
       s_kickback:
           number: 5
   coils:
       c_kickback:
           number: 7
           default_pulse_ms: 15

   kickbacks:
       ac_kickback:
           coil: c_kickback
           switch: s_kickback

   ball_saves:
      kickback_ball_save:
        active_time: 5s
        enable_events: kickback_ac_kickback_fired
        auto_launch: yes
        balls_to_save: 1


Monitorable Properties
----------------------

For :doc:`dynamic values </config/instructions/dynamic_values>` and
:doc:`conditional events </events/overview/conditional>`,
the prefix for kickbacks is ``device.kickbacks.<name>``.

*enabled*
   Boolean (true/false) which shows whether this kickback is enabled.

Related Events
--------------
* :doc:`/events/kickback_name_fired`
