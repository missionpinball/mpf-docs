Magnets
=======

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/magnets`                                                       |
+------------------------------------------------------------------------------+


.. contents::
   :local:

MPF supports the ability to control precise timing for magnets which you can
use to grab and release balls. It also includes the ability to set timings to
"fling" a ball by grabbing, releasing, then pulsing the magnet again.

.. image:: /mechs/images/magnet1.jpg
.. image:: /mechs/images/magnet2.jpg
.. image:: /mechs/images/magnet3.jpg

Hardware
--------

Magnets are quite strong :doc:`single wound coils </mechs/coils/index>` and
everything in the coils section also applies to them.
Especially, the Strength and Current calculations apply to them.
Expect a resistance in the range of 2 to 10 ohms for a magnet coil.

Connecting Magnets
~~~~~~~~~~~~~~~~~~

Please refer to the
:doc:`Connecting Coils section for single wound coils </mechs/coils/index>`.

If you do not have a diode on your magnet we recommend to add one.
Magnets are strong coils and they can easily fry your driver board otherwise.

Magnets often got a thermal fuse soldered inline to the connectors.
Those should not limit you in any way.

Part Numbers
~~~~~~~~~~~~

Assemblies:

* PBL-100-0007-00 (with 511-5065-ND coil)

Coils:

* 20-10197
* 20-9247
* 511-5065-ND
* 90-5064-02
* A-15685

Dedicated driver boards:

You can use a board such as ``520-5068-01`` to connect up to
three drivers to four logic level outputs (3 inputs + 1 clock).
The board contains FETs with flyback diode and a logic buffer for further
protection.

Config
------

This is an example:

.. code-block:: mpf-config

   coils:
     magnet_coil:
       number:
       default_pulse_ms: 100
       default_hold_power: 0.375

   switches:
     grab_switch:
       number:

   magnets:
     magnet:
       magnet_coil: magnet_coil
       grab_switch: grab_switch
       release_ball_events: magnet_release
       fling_ball_events: magnet_fling

Monitorable Properties
----------------------

For :doc:`dynamic values </config/instructions/dynamic_values>` and
:doc:`conditional events </events/overview/conditional>`,
the prefix for magnets is ``device.magnets.<name>``.

*active*
   Boolean (true/false) as to whether this magnet is actively on and
   in the powered state.

*enabled*
   Boolean (true/false) which shows whether this ball hold is enabled.

Related How To guides
---------------------

:doc:`stern_magnet_pcb`

Related Events
--------------

.. include:: /events/include_magnets.rst

.. toctree::
   :titlesonly:

   stern_magnet_pcb
