How to configure coils/drivers/magnets (P-ROC/P3-ROC)
=====================================================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/coils`                                                         |
+------------------------------------------------------------------------------+

To configure coils, drivers, motors, and/or magnets (basically anything
connected to PD-16 board's driver outputs) with P-ROC/P3-ROC hardware, you can
follow the guides and instructions in the :doc:`/mechs/coils/index` docs.

(If you're using a P-ROC with an existing machine's driver board, like a WPC
machine, then see the :doc:`existing machine documentation </hardware/existing_machines/index>`.)
If you are using the P-Roc with PDB drivers you can use the local drivers as number 0 to 31.

.. include:: /hardware/voltages_and_power/common_ground_warning.rst

The only specific thing you have to know for this platform is the number format:

number:
-------

.. image:: /hardware/images/multimorphic_PD-16.png

For PD-16-based devices, the numbering format is:

.. code-block:: yaml

   number: Ax-By-z

The “A” and “B” capital letters are required. (A means Address, B means Bank).
The lowercase x, y, and z letters should be replaced with numbers to represent
the following on a PD-16 driver board:

* x : Board address (0-31)
* y : Bank address (0 for A, 1 for B)
* z : Output number (0-7)

.. note::

   The output number is the logical number, *not* the pin number. For example, Output 0 is on Pin 1, and there is a key
   pin at 2 or 3. Check the manual for the exact mapping.

For example:

.. code-block:: mpf-config

   coils:
     some_coil:
       number: A0-B1-6
       default_pulse_ms: 30

Burst Switches as Local Outputs (P3-Roc only)
---------------------------------------------

.. image:: /hardware/images/multimorphic_p3_roc.png

If you want to use burst switches as local outputs set DIP switch 1 to ``on`` on the P3-Roc.
You can use those 64 output as direct outputs:

.. code-block:: mpf-config

   coils:
     local_output0:
       number: direct-0    # direct driver 0
     local_output20:
       number: direct-20   # direct driver 20

Make sure to assign IDs >= 2 to all PD-16 boards if you set DIP 1 (MPF cannot check this for you).
Local outputs behave just like any other output on the P3-Roc.
Hardware rules, pulse, hold, pwm etc. will behave exactly the same way.

You may also use outputs as ``digital_outputs``. For instance, to control a motor driver circuit:

.. code-block:: mpf-config

   digital_outputs:
     motor_left:
       number: direct-5
       type: driver
     motor_rigth:
       number: direct-6
       type: driver

.. note::

   You need at least Firmware version 2.6 to use burst switches as local outputs
   on the P3-Roc.

.. warning::

   There is no electronic protection on the P3-Roc for burst switches (neither as local outputs nor as burst optos).
   Additionally, there are no drivers attached to the outputs and they cannot drive any pinball mechs.
   Make sure not to draw too much current out of those outputs.
   Also, any voltage above 3.3V or below 0V will irrevisibly damage the P3-Roc.
   Make sure you know what you are doing before turning this on.
   We advise to use PD-16 for normal playfield/mech drivers and only use local outputs with additional
   circuits (not directly).

Pulse time
^^^^^^^^^^

The P-Roc, P3-Roc and/or PD-16 have the ability to specify the "pulse time".
Pulse time is the coil's initial kick time.
For example, consider the following configuration:

.. code-block:: mpf-config

    coils:
      some_coil:
        number:
        default_pulse_ms: 30

When MPF sends this coil a pulse command, the coil will be fired for 30ms.

Pulse Power
^^^^^^^^^^^

You can also set the power of pulses on your coil:

.. code-block:: mpf-config

    coils:
      some_coil:
        number:
        default_pulse_ms: 30
        default_pulse_power: 0.5

See the hold power section below for internal details about PWM times.
With the P-Roc and P3-Roc it is not possible to use ``default_hold_power`` and
``default_pulse_power`` at the same time.

Hold Power
^^^^^^^^^^

If you want to hold a driver on at less than full power, MPF does this by using
``default_hold_power`` parameter which works for all platforms.
It can range from 0.0 to 1.0 and defines the time share the coil is on
(0%-100%).

The P-Roc internally uses two parameters which determine how many milliseconds
the coil will be on (pwm-on time) and off (pwm-off time).
MPF will calculate those based on your power settings.

.. code-block:: mpf-config

    coils:
      some_coil:
        number:
        default_pulse_ms: 32
        default_hold_power: 0.5

When enabled, this driver will be pulsed for 32ms and then hold on at 50% duty
which will convert to 1ms on, 1ms off, 1ms on, 1ms off and so on.

With the P-Roc it is not possible to use ``default_hold_power`` and
``default_pulse_power`` at the same time.


Recycle
^^^^^^^

You can set :doc:`recycle time </mechs/coils/recycle>`
to your coil to prevent it from overheating by repeated pulses.
The recycle time is not configurable on the P-Roc but you can turn it on or
off (default on).
Default recycle time (called reload in the P/P3-Roc) is ``64ms``.

This is an example:

.. code-block:: mpf-config

    coils:
      some_coil_with_recycle:
        number:
        default_pulse_ms: 32
        default_recycle: true
      some_coil_without_recycle:
        number:
        default_pulse_ms: 32
        default_recycle: false

What if it did not work?
------------------------

Have a look at our
:doc:`troubleshooting guide for the P/P3-Roc <troubleshooting>`.

.. include:: ../driver_related_howto_guides.rst
