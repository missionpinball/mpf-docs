
In MPF, the "matrix light" device is anything that's connected to a
traditional lamp matrix, regardless of whether they're incandescent
lamps or "drop in" replacement LEDs like those from CoinTaker. (If
you're using RGB LEDs, those are covered `here`_.) MPF lets you turn
on and turn off individual matrix lights, as well as set levels of
brightness and fade rates. (Due to the realities of how lamp matrixes
strobe through all their columns, we can only get 12 levels of
brightness (between off and full on) for lamps or LEDs connected to a
lampmatrix, whereas we can get 255 levels per channel on LEDs
connected to an LED controller. You set up all your lights in the `
`matrix_lights:` section of your machine configuration file`_, and
they candriven, pulsed, flashed, and added to shows via the lighting
commands in the Hardware Show Controller module.

.. _ section of your machine configuration file: /docs/configuration-file-reference/matrixlights/
.. _here: https://missionpinball.com/docs/mpf-core-architecture/devices/low-level-devices/rgb-led/


