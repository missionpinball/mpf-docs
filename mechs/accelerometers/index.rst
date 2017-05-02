Accelerometers
==============

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/accelerometers`                                                |
+------------------------------------------------------------------------------+

.. contents::
   :local:

An accelerometer is a device that measures proper acceleration; proper acceleration is not the same as coordinate
acceleration (rate of change of velocity). For example, an accelerometer at rest on the surface of the Earth will
measure an acceleration due to Earth's gravity, straight upwards (by definition) of g ~= 9.81 m/s2. By contrast,
accelerometers in free fall (falling toward the center of the Earth at a rate of about 9.81 m/s2) will measure zero.

Accelerometers in pinball could be used to measure a machine's TILT, replacing the tilt bob, to measure vibration, or
even the angle of the playfield at a given time.

Learn more at:
https://en.wikipedia.org/wiki/Accelerometer

Monitorable Properties
----------------------

For :doc:`dynamic values </config/instructions/dynamic_values>` and
:doc:`conditional events </events/overview/conditional>`,
the prefix for accelerometers is ``device.accelerometers.<name>``.

*value*
   A three-item tuple (x, y, z) of the current accelerometer values.

Related How To guides
---------------------

.. todo:: TODO

Related Events
--------------

*None*
  Varies based on the configured (you can configure events to be emitted when
  certain G-force thresholds are exceeded).
