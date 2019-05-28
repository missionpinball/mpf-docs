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
as light):

.. code-block:: mpf-config

   digital_outputs:
       game_over_relay:
           number: 1
           type: light
           enable_events: ball_started
           disable_events: ball_will_end

This config will automatically enable the flippers on ball start and disable
them on ball end. You can add more events to enable/disable them during the
game.
