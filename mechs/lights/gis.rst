GI (general illumination)
=========================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/lights`                                                        |
+------------------------------------------------------------------------------+
| :doc:`/config/light_player`                                                  |
+------------------------------------------------------------------------------+
| :doc:`/config/coils`                                                         |
+------------------------------------------------------------------------------+


.. contents::
   :local:

MPF includes support for GI (general illumination) light strings which are
common in existing Williams and Stern machines. You can specify GI
strings which you can then enable, disable, or (if the hardware supports it)
dim.
Typically, there are one to four GI strings.

.. note::

   In MPF 0.50 GIs became :doc:`/config/lights` with ``subtype`` gi. They behave
   like any other lights in MPF.

Hardware
--------

:doc:`TODO: Add a picture of a GI string </about/help_us_to_write_it>`
:doc:`TODO: Add a picture of GI LEDs </about/help_us_to_write_it>`

GI Strings are actually kind of complex. Many of them are AC (even in WPC
machines), and some Williams WPC machines include triacs (kind of like a
transistor for AC) and "zero cross" AC waveform detection circuits so they can
sync their dimming commands with the AC current wave. Later Williams WPC
machines split their GI into non-dimmable (which used still used AC) and
switched their dimmable to DC. Some machines also have "enable" relays that
must be activated first before certain GI strings will work.
In general those bulbs are the same models as used for inserts (#44 and #47
for EM and early SS; #444/#555/#249 for later SS; #906 for later machines).

GI string might also be
:doc:`connected to a driver <coils_as_lights>` and not part of a light matrix.
In recent machines LEDs are used but still driven in strings.

Config
------

MPF hides all this complexity from you. You just define your GI strings in
your machine :doc:`/config/lights` section and then you can enable, disable, and
dim the dimmable ones as you wish.

This is an example for a :doc:`light </config/lights>` with ``subtype: gi``:

.. code-block:: mpf-config

  lights:     
    gi_string_left:
      number: 3		# number depends on your platform
      subtype: gi

In modern machines (such as Spike) your GIs might just be handled as lights.
The details depend on your hardware platform and are outlined in the platform
documentation.

This is an example for a :doc:`light </config/lights>` in Spike:

.. code-block:: mpf-config

  lights:     
    gi_string_left:
      number: 3		# number depends on your platform
      subtype: led	# might be matrix in some platforms

In some cases GIs are connected to normal drivers on your driver board
(e.g. on a PD-16 on the P3-Roc).
If that is the case you should configure them as :doc:`coils </config/coils>`.
Then add them as :doc:`light </config/lights>` with ``platform: drivers``:

.. code-block:: mpf-config

  coils:
    gi_string_left:
      number: A1-B1-3		# number depends on your platform
      allow_enable: True	# this will allow 100% enable without pwm

  lights:     
    gi_string_left:
      number: gi_string_left	# map this light to a driver
      platform: drivers

Alternatively, you could also use :doc:`coil_player </config/coil_player>`
but this gives you the convinience of being able to use GIs in normal light shows.

Monitorable Properties
----------------------

For :doc:`dynamic values </config/instructions/dynamic_values>` and
:doc:`conditional events </events/overview/conditional>`,
the prefix for lights is ``device.lights.<name>``.

*color*
   The color of this string. If you set it to brightness values all color channels
   will have the same value. Brightness 100 (of 255) will be hex 64 and color 646464.

Related How To guides
---------------------

See the documentation of your platform on how to configure GIs.

+------------------------------------------------------------------------------+
| Platform related How To                                                      |
+==============================================================================+
| :doc:`P/P3-Roc leds </hardware/multimorphic/leds>`                           |
+------------------------------------------------------------------------------+
| :doc:`P/P3-Roc matrix light </hardware/multimorphic/lights>`                 |
+------------------------------------------------------------------------------+
| :doc:`FAST leds </hardware/fast/leds>`                                       |
+------------------------------------------------------------------------------+
| :doc:`FAST matrix light </hardware/fast/lights>`                             |
+------------------------------------------------------------------------------+
| :doc:`OPP leds </hardware/opp/leds>`                                         |
+------------------------------------------------------------------------------+
| :doc:`OPP matrix light </hardware/opp/lights>`                               |
+------------------------------------------------------------------------------+


Related Events
--------------

None
