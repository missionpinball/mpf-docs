CobraPin Pinball Controller powered by OPP
============================================================

This page is under development...don't believe a word you read.

.. image:: /hardware/images/CobraPinV0_2_isoSmall.jpg

Features:
    * 24 solenoid outputs broken into 3 banks
    * 38 direct inputs <OR> 22 direct inputs + 8x8 switch matrix
    * Neopixel support for 512 RGB pixels (RGBW also possible but may be limited to ~460 pixels)
    * 24-50V power filter. Board also provides the common ground for the supplies.
    * Fuses for solenoid banks and Neopixels

Power Input and Filter
---------------------------------------------------------------------------------------------------------------

.. image:: /hardware/images/CobraPinV0_2_VIN.jpg

J9:
    Solenoid power input (24-50V).
J10:
    Neopixel 5V input.

The filter provides consistent power to solenoids while also protecting the power supply from sudden current surges that may otherwise cause a fault.

Solenoid Outputs
---------------------------------------------------------------------------------------------------------------

.. image:: /hardware/images/CobraPinV0_2_solenoids.jpg

J6, J7, J8:
    Solenoid outputs.

The 24 solenoids are broken up into 3 banks of 8 outputs. There is a ninth pin on the connector that can be used as a key. Each solenoid has a diode to help protect the transistor. You may still use coils with axial diodes installed, but you MUST ensure that you connect them with the correct polarity.

The solenoid outputs are labeled in silkscreen with the MPF compatible numbers. :doc:`OPP coils / drivers </hardware/opp/drivers>`.

Each bank has an LED next to it to indicate if that bank has power. Check these if you are concerned you have blown a fuse.  

Each solenoid has an associated LED to indicate it is being driven by the processor. It is highly recommended to test a new setup without high voltage power or without the coils plugged in. Using these LEDs, you can verify that each output is being driven correctly.

Solenoid Power Output and Fuses
---------------------------------------------------------------------------------------------------------------

.. image:: /hardware/images/CobraPinV0_2_HVout.jpg

J13:
    Solenoid power outputs.
F1, F2, F3:
    Solenoid power bank fuses.

The fuses are 5x20mm. Each fuse provides power to a bank of 8 solenoids. 

.. note:: Solenoids in bank A should only be powered by the HV_A pin, bank B should only be powered by HV_B, bank C should only be powered by HV_C. Failure to do so may confuse future troubleshooting and could eventually blow out a transistor.


Switch Inputs
---------------------------------------------------------------------------------------------------------------

.. image:: /hardware/images/CobraPinV0_2_switches.jpg

J1, J2, J3:
    Direct input switches.
J4, J5:
    Remaining direct input switches <OR> switch matrix input/output.

The switch inputs are labeled in silkscreen with the MPF compatible numbers. The two pins labeled "N/C" are not connected to anything.

Each connector also includes a logic ground pin. Use this for the direct input return. :doc:`OPP Switches </hardware/opp/switches>`.

Neopixel Support
---------------------------------------------------------------------------------------------------------------

.. image:: /hardware/images/CobraPinV0_2_NEO.jpg

J11, J12:
    Neopixel outputs
F4:
    5V fuse for neopixels
J14:
    Fused 5V output

There are two neopixel chains that support 256 RGB pixels each for a total of 512. RGBW pixels are also possible, but the number may be limited to 230 pixels per chain for a total of 460. :doc:`OPP LEDs </hardware/opp/leds>`.

The J14 fused output can be used to provide additional power taps in a neopixel chain. Each pin is rated for 7A continuous. The fuse holder is rated for 10A. The red D25 LED can be used to confirm you have a good fuse and are providing power for neopixels.

Microcontrollers
---------------------------------------------------------------------------------------------------------------

.. image:: /hardware/images/CobraPinV0_2_STM32.jpg

The brains of the CobraPin are two STM32 microcontroller boards programmed with OPP firmware. They are connected to the host computer via micro USB connectors.

.. note:: It is important to have your config file refer to the silkscreen board numbers (0 and 1) in the correct order, otherwise the labels on the solenoids, switches, etc. will refer to incorrect pin numbers.

The microcontrollers are removable so you can replace them if they fail for whatever reason. They are widely available and often referred to as "STM32 Blue Pill" boards. The right angle header that is normally used as a programming port is replaced with a vertical header so that those pins can be used on the CobraPin board.

Example Config
---------------------------------------------------------------------------------------------------------------

.. code-block:: mpf-config

    #config_version=5

    hardware:
      platform: opp
      driverboards: gen2

    opp:
      ports: /dev/ttyACM0, /dev/ttyACM1
      chains:
        0: /dev/ttyACM1
        1: /dev/ttyACM0

    switches:
        #DIRECT
      s_startButton:
        number: 0-0-25
        tags: start
      s_slingshot_left:
        number: 0-0-24
        tags: slings
      s_slingshot_right:
        number: 0-0-19
        tags: slings

        #MATRIX
      s_lowerDrop1:
        number: 1-0-32
      s_lowerDrop2:
        number: 1-0-33

    lights:
      l_15000Rollunder:
        number: 0-0-15
        type: grb
        subtype: led
        tags: inserts
      l_extraBall:
        number: 0-0-16
        type: grb
        subtype: led
        tags: inserts
      l_gi_17:
        number: 1-0-24
        subtype: led
        tags: gi
      l_gi_18:
        number: 1-0-25
        subtype: led
        tags: gi

    coils:
      c_flipper_left:
        number: 0-0-8
        allow_enable: true
        default_hold_power: 1.0
        default_pulse_ms: 50
      c_slingshot_left:
        number: 0-0-9
        default_pulse_ms: 30
        default_recycle: true
        platform_settings:
          recycle_factor: 4

