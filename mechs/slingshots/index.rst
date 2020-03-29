Slingshots
==========

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/autofire_coils`                                                |
+------------------------------------------------------------------------------+

Slingshots are configured as :doc:`autofire_coils </config/autofire_coils>` in MPF.

Hardware
--------

.. image:: /mechs/images/slingshot_side.jpg
.. image:: /mechs/images/slingshot_front.jpg

A sling shot usually consists of two
:doc:`blade switches </mechs/switches/mechanical_switches>` and
one :doc:`coil </config/coils>`.
Those switches are wired in parallel because it does not matter which switch
was closed to fire to slingshot. Connect one side of each switch to ground and
the other side of both switches to the same input.

Part numbers:

* Data East/Sega/Stern: #500-5849-00
* Spooky/American Pinball/Suncoast: PBL-5849-01


Config
------

This is an example:

.. code-block:: mpf-config

   switches:
     s_sling_left:
       number: 5
   coils:
     c_sling_left:
       number: 7
       default_pulse_ms: 15
   autofire_coils:
     ac_slingshot_left:
       coil: c_sling_left
       switch: s_sling_left

Adjust ``default_pulse_ms`` and ``default_pulse_power`` in your coil
to control the strength and sound of your slingshots.
