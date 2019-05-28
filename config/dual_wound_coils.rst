dual_wound_coils:
=================

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``dual_wound_coils:`` section of your config is where you configure
dual-would coils that are added to your "coils" device list which can
be used anywhere in MPF.

Here's an example:

.. code-block:: mpf-config

   coils:
       c_hold:
           number:
           allow_enable: True
       c_power:
           number:
           default_pulse_ms: 20

   switches:
       s_eos:
           number:

   dual_wound_coils:
       c_dual_wound:
           hold_coil: c_hold
           main_coil: c_power
           eos_switch: s_eos

In the configuration above, a new coil called ``c_dual_wound`` is created that,
when enabled, would energize both the ``c_hold`` and ``c_power`` coils. Then when
the ``s_eos`` switch is activated, the ``c_power`` coil would be de-energized, leaving
just the ``c_hold`` coil active until the ``c_dual_wound`` coil is
deactivated.

Required settings
-----------------

The following sections are required in the ``dual_wound_coils:`` section of your config:

<name>:
~~~~~~~

Create a sub-entry in your ``dual_wound_coils:`` section for each
dual-wound coil you want to define.

Note: Dual-wound flipper coils are configured in the ``flippers:``
section of the config, so you don't have to define them here. Other
dual-wound coils (like for diverters, etc.) should be defined here since
other MPF devices do not have explicit support for dual-wound coils.

hold_coil:
~~~~~~~~~~
Single value, type: string name of a ``coils:`` device.

The name of the hold coil winding. This coil must be a valid coil
defined in your ``coils:`` section.

main_coil:
~~~~~~~~~~
Single value, type: string name of a ``coils:`` device.

The name of the main (power) coil winding. This coil must be a valid coil
defined in your ``coils:`` section.

When this dual-wound coils is enabled, this coil will be pulsed for the
number of milliseconds specified in the original coil's ``default_pulse_ms:``
setting.

Optional settings
-----------------

The following sections are optional in the ``dual_wound_coils:`` section of your config. (If you don't include them, the default will be used).

debug:
~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

See the :doc:`documentation on the debug setting </config/instructions/debug>`
for details.

eos_switch:
~~~~~~~~~~~
Single value, type: string name of a ``switches:`` device. Default: ``None``

The name of a switch which, when activated, will disable the power to the main
coil winding.

.. todo::

   Verify whether this has been implemented?

label:
~~~~~~
Single value, type: ``string``. Default: ``%``

A descriptive name for this device which will show up in the service menu
and reports.

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

Special / reserved tags for dual-wound coils: *None*

See the :doc:`documentation on tags </config/instructions/tags>` for details.
