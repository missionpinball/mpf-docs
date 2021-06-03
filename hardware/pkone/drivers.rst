How to configure coils/drivers/magnets (Penny K Pinball PKONE)
==============================================================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/pkone`                                                         |
+------------------------------------------------------------------------------+
| :doc:`/config/coils`                                                         |
+------------------------------------------------------------------------------+

To configure coils, drivers, motors, and/or magnets (basically anything connected to a
PKONE Extension board's driver outputs) with Penny K Pinball hardware, you can follow
the guides and instructions in the :doc:`/mechs/coils/index` docs.

.. include:: /hardware/voltages_and_power/common_ground_warning.rst

There are a few things to know about controlling drivers and coils
with PKONE hardware that are discussed here.

number:
-------

When you're using PKONE Extension boards, drivers plug into individual Extension boards.
Then the Extension boards are connected together in a chain to the controller.

.. image:: /hardware/images/pkone-extension.png

The ``number:`` setting for each switch is its board's Address ID number in the
PKONE chain, then the dash, then the coil/driver output number (1-10).

.. code-block:: mpf-config

   coils:
     my_coil:
       number: 0-1    # Extension board with Address ID 0, coil/driver 1
     some_other_coil:
       number: 2-10    # Extension board with Address ID 2, coil/driver 10

Notes:

   * The PKONE Extension board Address ID switches can be set from 0 to 7.

Pulse Power
-----------

In the :doc:`/mechs/coils/index` section of the documentation, we talked about
:doc:`how adjusting a coil's pulse time can affect its strength </mechs/coils/pulse_power>`.
Adjusting the coil's pulse times still assumes that 100% power will be applied
to that coil during that pulse time.

Penny K Pinball PKONE controllers allow you to specify the power that's applied
to the coil during the initial pulse time. This is similar to the
:doc:`/mechs/coils/hold_power`, except it applies to the initial pulse time
instead of the extended hold time.

You can configure the pulse power by adding a ``default_pulse_power:`` setting to
a coil definition and then specifying the power value from 0-1. (Like default_hold
power, 0% to 100%)

For example, consider the following configuration:

.. code-block:: mpf-config

    coils:
      some_coil:
        number: 1-3
        default_pulse_ms: 30
        default_pulse_power: 0.5

When MPF sends this coil a pulse command, the coil will be fired for
30ms at 50% power. You can even combine default_pulse_power and
default_hold_power, like this:

.. code-block:: mpf-config

    coils:
      some_coil:
        number: 1-3
        default_pulse_ms: 30
        default_pulse_power: 0.5
        default_hold_power: 0.25

In this case, if MPF enables this coil, the coil will be fired at 50%
power for 30ms, then drop down to 25% power for the remainder of the
time that it's on.

Setting Recycle Times
---------------------

Penny K Pinball controllers allow you to precisely control the
:doc:`recycle time </mechs/coils/recycle>` for coils or drivers.

A coil's ``recycle:`` setting is a boolean (True/False), which is
set to ``False`` by default. When using Penny K Pinball hardware, if you set
``recycle: true``, then the recycle time is automatically set to twice the
coil's ``default_pulse_ms:`` setting. (e.g. a coil with a
``default_pulse_ms: 30`` and ``recycle: true`` will have a 60ms recycle time).

With Penny K Pinball hardware, you can manually set a coil's recycle
time by adding a ``recycle_ms:`` setting, like this:

.. code-block:: mpf-config

   coils:
     slingshot_r:
       number: 1-4
       default_pulse_ms: 30
       platform_settings:
         recycle_ms: 100

If you manually specify a recycle_ms value, then that's the value that's used
and the coil's ``recycle:`` (true/false) setting is ignored.

What if it did not work?
------------------------

Have a look at our :doc:`PKONE troubleshooting guide <troubleshooting>`.

.. include:: ../driver_related_howto_guides.rst
