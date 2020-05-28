Reducing light update rate
--------------------------

If you got a lot of lights you might run into bus contention issues.
You can reduce the light update rate in MPF:

.. code-block:: mpf-config

    mpf:
      default_light_hw_update_hz: 30   # defaults to 50

If you set this too low fades will be less smooth but otherwise it should not
affect your game.
