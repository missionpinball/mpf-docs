OPP coils / drivers
===================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/coils`                                                         |
+------------------------------------------------------------------------------+


There are a few things to know about controlling drivers and coils
with OPP hardware.

.. include:: /hardware/voltages_and_power/common_ground_warning.rst

Number
^^^^^^

OPP coils are numbered sequentially depending on which wing board
is the coil output.  Wing position 0 contains coil numbers 0 to 3.
Wing position 1 contains coil numbers 4 to 7.  Wing position 2
contains coil numbers 8 to 11.  Wing position 3 contains coil
numbers 12 to 15. The coil is numbered using the position of the
OPP card (starting at 0), then a '-', and finally the coil number
on the card.

.. code-block:: mpf-config

    coils:
      some_coil:
        number: 0-12

The above example configures a coil output as the first OPP card, and
the third wing board, first output.  On the microprocessor card, the
output is marked as 3.4 (wing port 3, position 4).

Pulse time
^^^^^^^^^^

The OPP hardware also has the ability to specify the "pulse time".
Pulse time is the coil's initial kick time. For
example, consider the following configuration:

.. code-block:: mpf-config

    coils:
      some_coil:
        number: 0-12
        default_pulse_ms: 30

When MPF sends this coil a pulse command, the coil will be fired for
30ms.

Hold Power
^^^^^^^^^^
If you want to hold a driver on at less than full power, MPF does this by using
*default_hold_power* parameter which works for all platforms. It can range from
0.0 to 1.0 and defines the time share the coil is on (0%-100%).

The period is fixed at 16ms for OPP. To set the hold power to 25%, set
default_hold_power to .25 and OPP will use 4ms/16ms = 25%.

.. code-block:: mpf-config

    coils:
      some_coil:
        number: 0-3
        default_pulse_ms: 32
        default_hold_power: 0.5

This will configure OPP card 0, solenoid wing 0, last solenoid to
have an initial pulse of 32 ms, and then be held on at 50% power.


Recycle Factor
^^^^^^^^^^^^^^

OPP allows you to fine tune the
:doc:`recycle time of your coils </mechs/coils/recycle>`.
If you add ``recycle: True`` to your coil you can set ``recycle_factor``
in the ``platform_settings`` secton of your coil to set the recycle time.
The time will be ``default_pulse_ms * recycle_factor``.
For instance, if you set a pulse time of ``10ms`` and a recycle_factor of two
the coil will cool down for at least ``20ms``.
This is an example:

.. code-block:: mpf-config

    coils:
      some_coil:
        number: 0-3
        default_pulse_ms: 10
        default_recycle: true
        platform_settings:
          recycle_factor: 2

What if it did not work?
------------------------

Have a look at our :doc:`OPP troubleshooting guide <troubleshooting>`.


.. include:: ../driver_related_howto_guides.rst
