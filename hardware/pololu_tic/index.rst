How to use Pololu Tic in MPF
============================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/hardware`                                                      |
+------------------------------------------------------------------------------+
| :doc:`/config/pololu_tic`                                                    |
+------------------------------------------------------------------------------+
| :doc:`/config/tic_stepper_settings`                                          |
+------------------------------------------------------------------------------+
| :doc:`/config/switches`                                                      |
+------------------------------------------------------------------------------+
| :doc:`/config/steppers`                                                      |
+------------------------------------------------------------------------------+

The Pololu Tic is a stepper controller which can controll one stepper via USB.
Multiple versions with different power rating exist but they all work the
same from the perspective of MPF.

:doc:`TODO: Add a picture of a Pololu Tic </about/help_us_to_write_it>`

Installation
------------

To use the Pololu Tic you need to install ``ticcmd`` from Pololu.
Follow their `Installation instructions for ticcmd <https://www.pololu.com/docs/0J71/3>`_.

Connecting your stepper
-----------------------

Connect your stepper according to the Pololu manual.

Configuring your stepper
------------------------

Afterwards, you can use steppers from MPF.
This is an example:

.. code-block:: mpf-config

   #config_version=5
   hardware:
     stepper_controllers: pololu_tic

   switches:
     s_home:
       number: 1

   steppers:
     stepper1:
       number: 1
       homing_mode: switch
       homing_switch: s_home
       named_positions:
         10: test_00
         20: test_01
         50: test_10
       platform_settings:
         max_acceleration: 20000

You can set certain pololu-specific settings in ``platform_settings``.
See :doc:`/config/tic_stepper_settings` for details.

What if it did not work?
------------------------

Have a look at our :doc:`hardware troubleshooting guide </hardware/troubleshooting_hardware>`.
