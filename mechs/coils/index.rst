Coils (Solenoids)
=================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/coils`                                                         |
+------------------------------------------------------------------------------+
| :doc:`/config/coil_player`                                                   |
+------------------------------------------------------------------------------+

.. include:: /hardware/voltages_and_power/common_ground_warning.rst

In MPF, you typically list all the coils in your machine in the
:doc:`coils: section </config/coils>` of your machine configuration file, along
with default options for them, like pulse times, PWM values, whether they can
be enabled (held on), etc.

.. image:: /mechs/images/coil.jpg

You don't typically work with coils directly, rather, you tend to add them to
other devices once they've been defined (flippers, autofires, ball devices,
diverters, etc). You can configure :doc:`dual_wound_coils` on top of coils.

That said, it is possible to perform actions on coils directly, such as pulsing,
enabling, or disabling them. You can do this via the :doc:`/config/coil_player`
section of a config file or via the ``coils:`` section of a
:doc:`show </shows/index>`.

Hardware
--------

Coils vary in strength relative to the pulse time you use.
The strength of the magnetic field of a coil is a product of some constant (u),
the current (I) and the number of windings (N) divided by the length of the
coil (L): ``B = u * I * N / L``

The length of coils in pinball is almost the same for most coils (so ignore
that).
However, the number of windings is not.
Additionally, the thickness of the wire differs between coils which influences
how much current can flow though the coil.
Thicker wires generally means stronger coils.
Unfortunately, this is not generally true for windings even though the forumlar
above suggests it.
The reason is for that more windings also mean longer wires which will result
in higher resistance and less current.
At least for typical coils in pinball more windings means slighly less
powerful.

If you want to compare the strengh of different coils you can get the number of
windings and their resistance from one of the following pages:

* `Pinball Medic Coil Chart <https://www.pinballmedic.net/coilchart.html>`_
* `Flippers.com Coil Resistance <https://flippers.com/coil-resistance.html>`_

Get windings ``N`` and resistance ``R`` from the chart.
To get the current you can use ``I = U/R``.
Depending on your power supply ``U`` is either 48 or 70V.
Length is roughly ``3.5cm`` for most coils.

Relative strength: ``s = U / R * N / L``.
More is stronger.
In most cases you can leave out ``L`` as this is not terribly scientific
anyway (and there is slightly more to it but this should be a good start).


Related How To guides
---------------------

* :doc:`/tutorial/3_get_flipping`

.. toctree::
   :titlesonly:

   pulse_power
   hold_power
   recycle
   dual_wound_coils
   dual_vs_single_wound



+------------------------------------------------------------------------------+
| Related Events                                                               |
+==============================================================================+
| None                                                                         |
+------------------------------------------------------------------------------+
