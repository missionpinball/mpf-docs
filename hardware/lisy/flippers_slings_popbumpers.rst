Configuring and Enabling Flippers/Pop Bumpers/Slingshots in LISY
================================================================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/digital_outputs`                                               |
+------------------------------------------------------------------------------+

System 1/80 does not support rules in software for
flippers/pop bumpers/slingshots because CPUs were not fast enough at that time.
Instead, they installed a hardware relay to enable
flippers/pop bumpers/slingshots by connecting them physically to the
corresponding switches (similar to fliptronics).

All you have to do is to configure the ``game_over_relay`` (which is connected
as light) in LISY1 and LISY80:

.. code-block:: mpf-config

   digital_outputs:
     game_over_relay:
       number: 1
       type: light
       enable_events: ball_started
       disable_events: ball_will_end

In LISY35 the same relay is connected to a driver.
You can use this example to enable flippers:

.. code-block:: mpf-config

   digital_outputs:
     flipper_enabling_relay:
       type: driver
       number: 16
       enable_events: ball_started
       disable_events: ball_will_end

This config will automatically enable the flippers on ball start and disable
them on ball end. You can add more events to enable/disable them during the
game.

What if it did not work?
------------------------

Have a look at our :doc:`LISY troubleshooting guide <troubleshooting>`.
