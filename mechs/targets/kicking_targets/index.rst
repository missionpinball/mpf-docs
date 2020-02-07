Kicking Targets
===============

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/switches`                                                      |
+------------------------------------------------------------------------------+
| :doc:`/config/kickbacks`                                                     |
+------------------------------------------------------------------------------+

:doc:`TODO: Add a picture of a kicking target </about/help_us_to_write_it>`


Mission Pinball Framework's (MPF) *kicking target* device represents a switch in a pinball machine. This device is
used for kicking targets with a coil for kicking. Used rarely, these targets look like stationary targets, but when
hit they kick the back in the opposite direction much like a :doc:`slingshot </mechs/slingshots/index>` or
:doc:`bumper </mechs/pop_bumpers/index>`.

.. code-block:: mpf-config

   switches:
     s_kicking_target:
       number: 1
   coils:
     c_kicking_target:
       number: 1
       default_pulse_ms: 10ms
   kickbacks:
     kicking_target:
       coil: c_kicking_target
       switch: s_kicking_target

