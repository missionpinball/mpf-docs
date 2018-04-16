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

MPF's flasher devices are only used in older machines (WPC, Stern SAM, System 11)
since modern LED-based machines typically use regular LED devices (or combinations
of them) as flashers. (So basically a "flasher" in MPF is any single-color
light that's connected to a driver output rather than a light output.

Starting with MPF 0.50 flashers and lights have been unified. Depending on your
platform flashers might be :doc:`/config/lights` or :doc:`/config/coils`. In most
cases they are configures as :doc:`coil </config/coils>`:

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


+------------------------------------------------------------------------------+
| Related How To Guides                                                        |
+==============================================================================+
| :doc:`/about/help_us_to_write_it`                                            |
+------------------------------------------------------------------------------+

+------------------------------------------------------------------------------+
| Related Events                                                               |
+==============================================================================+
| None                                                                         |
+------------------------------------------------------------------------------+
