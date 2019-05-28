flashers:
=========

*Removed in 0.50.*

In most cases flashers can be configured as :doc:`coils </config/coils>`.
You can use :doc:`coil_player </config/coil_player>` to pulse/flash them.
Alternatively, you can configure them as :doc:`lights </config/lights>`
and use :doc:`light_player </config/light_player>` or
:doc:`flasher_player </config/flasher_player>` to control them.


Here is an example:

.. code-block:: mpf-config

   # configure the flasher as coil
   coils:
       flasher_01:
           number: 4                # this number depends on your hardware
           default_pulse_ms: 40     # pulse duration to use if no specified elsewhere
           max_hold_power: 1.0      # needed if you want to use flasher and light_player

   # you can flash the flasher using flasher player
   coil_player:
     flash_coil:
       flasher_01:
         action: pulse              # will use the default 40ms pulse

   # create a light which is backed by a coil (optional if you want to use light_player and flasher_player)
   lights:
       flasher_01:
           number: flasher_01       # name of your coil
           platform: drivers        # use a coil

   # use the light to flash the flasher
   flasher_player:
      flash_flasher_01:
         flasher_01: 100ms
