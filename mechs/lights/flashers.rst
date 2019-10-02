Flashers
========

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/coils`                                                         |
+------------------------------------------------------------------------------+
| :doc:`/config/coil_player`                                                   |
+------------------------------------------------------------------------------+
| :doc:`/config/lights`                                                        |
+------------------------------------------------------------------------------+
| :doc:`/config/light_player`                                                  |
+------------------------------------------------------------------------------+
| :doc:`/config/flasher_player`                                                |
+------------------------------------------------------------------------------+

MPF includes support for flashers, which are essentially just really
bright lights that are controlled via high-power driver transistors instead
of low-power lighting circuitry.

.. image:: /mechs/images/flasher1.jpg
.. image:: /mechs/images/flasher2.jpg


MPF's flasher devices are only used in older machines (WPC, Stern SAM, System 11)
since modern LED-based machines typically use regular LED devices (or combinations
of them) as flashers. (So basically a "flasher" in MPF is any single-color
light that's connected to a driver output rather than a light output.

Hardware
--------

#89 bulbs are commonly used as flashers in pinball machines.
Those are rated at 13V but typically driven at higher voltages for only a very
short amount of time.
Turning them on permanently will burn quickly in most machines.


Config
------

Starting with MPF 0.50 flashers and lights have been unified. Depending on your
platform flashers might be :doc:`/config/lights` or :doc:`/config/coils`. In most
cases they are configured as :doc:`coil </config/coils>`:

.. code-block:: mpf-config

  coils:
    flasher_coil_4:
      number: 4
      allow_enable: True

Then add them as :doc:`light </config/lights>`:

.. code-block:: mpf-config

  #! coils:
  #!   flasher_coil_4:
  #!    number: 4
  #!    allow_enable: True
  lights:     
    flasher_4:
      number: flasher_coil_4
      platform: drivers


Now you can use them in :doc:`/config/flasher_player` (or also in
:doc:`/config/light_player` if you want to enable the flasher permanently).

.. code-block:: mpf-config

  flasher_player:
    flash:
      flasher_01: 100ms

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



+------------------------------------------------------------------------------+
| Related Events                                                               |
+==============================================================================+
| None                                                                         |
+------------------------------------------------------------------------------+
