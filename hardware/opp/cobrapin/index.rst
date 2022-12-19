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

Overview video about Cobrapin:

.. youtube:: UQNMaLv3woo

Overview video about OPP:

.. youtube:: WU98MRDeYeQ

Video about cobrapin extension board:

.. youtube:: lfxKcaiZyMs

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
    Remaining direct input switches or switch matrix input/output. 
    
If you do have either 38 direct inputs or 22 direct inputs + a 8x8 switch matrix depends on your Cobra board. You specify this as an option when you order your board. The switch inputs are labeled in silkscreen with the MPF compatible numbers. The two pins labeled "N/C" are not connected to anything.

Each connector also includes a logic ground pin. Use this for the direct input return. If you measure the voltage between GND and a switch (in below picture 0-0-16) you should measure 3.3V.

.. image:: /hardware/images/Cobra_Voltage_Switch.jpg

For that to measure only the micro controllers need to be powered up, no need to apply any other voltage on the Cobra board. To perform a simple test connect any kind of switch to one of the inputs and setup a little mpf test configuration.


.. image:: /hardware/images/Cobra_Switch_connected.jpg


For further details and fully working Cobra board configuration example please check :doc:`OPP Switches </hardware/opp/switches>`.

Neopixel Support
---------------------------------------------------------------------------------------------------------------

.. image:: /hardware/images/CobraPinV0_2_NEO.jpg

J10:
   Power input for Neopixels, most likely 5V, but if you use 12V Neopixels you need to provide 12V power here. Power input is used for both Neopixel chains.

J11, J12:
    Neopixel outputs
F4:
    5V fuse for neopixels
J14:
    Fused 5V output
    
The connectors J10, J11, J12 and J14 are JST connectors VH style. There are lots of Neopixels which come with a JST connector SM style. You might want to craft a little converter cable in such a case.

.. image:: /hardware/images/Cobra_Neopixel_JST_adapter_VH_SM.jpg

There are two neopixel chains that support 256 RGB pixels each for a total of 512. RGBW pixels are also possible, but the number may be limited to 230 pixels per chain for a total of 460. 

The J14 fused output can be used to provide additional power taps in a neopixel chain. Each pin is rated for 7A continuous. The fuse holder is rated for 10A. The red D25 LED can be used to confirm you have a good fuse and are providing power for neopixels. For the LED to light up there is no need to run any mpf configuration, you don't even have to power up the micro controllers.

.. image:: /hardware/images/Cobra_Power_LED_Neopixel.jpg

When you order the micro controllers you have various options, one option to choose from is Regular vs NoGlow. If you order the Regular version then after power is provided for the Neopixel and the micro controllers are powered up (still no need to run any mpf on them), the LEDs of your strip will glow blue, which is a good first test.

.. image:: /hardware/images/Cobra_Neopixel_blue_glow.jpg

In order to addess the LEDs in MPF you need to know their address

J11: 
   NEO 0 Neopixel output, all these lights have MPF numbers with the format 0-0-##. The first LED in the chain is 0-0-0.

J12: 
   NEO 1 Neopixel output, all these lights have MPF numbers with the format 1-0-##. The first LED in the chain is 1-0-0. 

Details on how to configure LEDs in your mpf project can be found here :doc:`OPP LEDs </hardware/opp/leds>`.

Two fully working example for the Cobra board can be found in the generic LED section :doc:`LEDs </mechs/lights/index>` where as well the more general concept is explained.

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

    #CobraPin Example Config

    hardware:
      platform: opp
      driverboards: gen2


    opp:
      #Use the USB ports defined by your OS for the two STM32 boards
      ports: /dev/ttyACM0, /dev/ttyACM1
      #USING SERIAL NUMBERS INSTEAD OF CHAINS
      #  Board 0 has serial number 0, Board 1 has serial number 1.
      #  This is convenient if your OS tends to reassign the serial port.
      #  MPF will automatically address the correct board even if the ports
      #     are swapped.

      #For multiple CobraPin boards in a game, you will either have to give
      #  the STM32 boards on the second CobraPin board new serial numbers
      #  (10 and 11 are suggested for the 2nd board since 2 is used by the
      #  CobraPin Xpansion Board)
      #  <OR> Use the chains section to assign a port to a board number.
      #  Mixing these up could cause blown FETs, coils, and fuses. Proceed
      #  with caution. Test without coil power and use the yellow coil LEDs
      #  for feedback.
      #chains:
         #0: /dev/ttyACM0
         #1: /dev/ttyACM1


    psus:
      default:
        #Gives the capacitors extra time to recharge after firing a coil
        #  and eases the load on the power supply. Doesn't affect autofire
        #  devices like flippers, pops, slings.
        release_wait_ms: 50


    #One giant config file can get difficult to manage. You can put any of
    #  these config sections in its own yaml file and link to it with the
    #  config section here
    config:
      #- switches_config.yaml
      #- lights_config.yaml
      #- coils_config.yaml
      # ...


    switches:

      #DIRECT SWITCHES
      #switch numbers are labelled in silkscreen on the board
      s_left_flipper:
        number: 0-0-27
        tags: left_flipper
      s_right_flipper:
        number: 0-0-26
        tags: right_flipper
      s_startButton:
        number: 0-0-25
        tags: start


      #MATRIX SWITCHES
      #valid numbers are 1-0-32 through 1-0-95
      s_lowerDrop1:
        number: 1-0-32

      # ...

      s_topRollunder:
        number: 1-0-95
        ignore_window_ms: 250ms    #tune to assist in debouncing


    lights:

      #SERIAL LEDS (neopixels)
      #NEO0 output supports 256 LEDs numbered 0-0-0 to 0-0-255
      l_shootAgain:
        number: 0-0-0
        subtype: led
        type: grb   #Most WS2812-based LEDs are grb color order.
                    #This line not required for rgb ordered LEDs like the
                    #  WS2811 LEDs shown below

      # ...

      #NEO1 output supports 256 LEDs numbered 1-0-0 to 1-0-255
      l_gi_1:
        number: 1-0-0
        subtype: led
        tags: gi    #you can group similar LEDs with user defined tags
      l_gi_2:
        number: 1-0-255
        subtype: led
        tags: gi


    coils:
      #coil numbers are labelled in silkscreen on the board

      #There are multiple ways to configure flippers, use the one that
      #  matches your hardware
      c_flipper_left:
        number: 0-0-8
        allow_enable: true
        default_hold_power: 1.0
        default_pulse_ms: 50
      c_flipper_right:
        number: 0-0-4
        allow_enable: true
        default_hold_power: 1.0
        default_pulse_ms: 50
      c_ballRelease:
        number: 1-0-1
        default_hold_power: 0.15
        default_pulse_ms: 30


    flippers:
      #Add your flipper config


    autofire_coils:
      #Add your autofire cofigs for pops, slings, etc.


    ball_devices:
      #Add your ball devices


    playfields:
      #Define your playfields


    machine:
      balls_installed: 3 #How many balls are physically in your game
      min_balls: 3 #How few balls can be accounted for before you can start a game


    game:
      balls_per_game: 3
      max_players: 4


    modes:
      #Add all your mode names here
      #- attract
      #- base
      #- etc


    keyboard:   #use to drive your game from the computer for testing
      z:
        switch: s_left_flipper
      "/":
        switch: s_right_flipper

