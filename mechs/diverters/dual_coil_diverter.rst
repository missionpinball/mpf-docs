Dual Coil Diverter
==================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/diverters`                                                     |
+------------------------------------------------------------------------------+
| :doc:`/config/dual_wound_coils`                                              |
+------------------------------------------------------------------------------+


In this example we use a standard flipper mechanism with a dual wound coil as
a diverter.
Much like a flipper, we'll want to control the main coil for enabling the
diverter, and then the hold coil to hold it in the active position for as long
as you need.

Config
------

First we need to define the coils in our hardware section:

.. code-block:: mpf-config

    coils:
      c_diverter_upper_right_main:
        number: 25
        default_pulse_ms: 4
        default_hold_power: 0.2
      c_diverter_upper_right_hold:
        number: 26
        allow_enable: true


Next we'll define the dual wound coil for the diverter to use:

.. code-block:: mpf-config

    #! coils:
    #!   c_diverter_upper_right_main:
    #!     number: 25
    #!     default_pulse_ms: 4
    #!     default_hold_power: 0.2
    #!   c_diverter_upper_right_hold:
    #!     number: 26
    #!     allow_enable: true
    dual_wound_coils:
      c_diverter_dualcoil:
        hold_coil: c_diverter_upper_right_hold
        main_coil: c_diverter_upper_right_main

Then we define the Diverter itself:

.. code-block:: mpf-config

    #! coils:
    #!   c_diverter_upper_right_main:
    #!     number: 25
    #!     default_pulse_ms: 4
    #!     default_hold_power: 0.2
    #!   c_diverter_upper_right_hold:
    #!     number: 26
    #!     allow_enable: true
    #! switches:
    #!   s_r_rampexit:
    #!     number:
    #!   s_l_rampexit:
    #!     number:
    #! dual_wound_coils:
    #!   c_diverter_dualcoil:
    #!     hold_coil: c_diverter_upper_right_hold
    #!     main_coil: c_diverter_upper_right_main
    diverters:
      ramp_diverter:
        activation_coil: c_diverter_dualcoil
        type: hold
        activation_time: .5s
        activation_switches: s_r_rampexit, s_l_rampexit
        enable_events: ball_started
        disable_events: ball_ended

+------------------------------------------------------------------------------+
| Related How To Guides                                                        |
+==============================================================================+
| :doc:`index`                                                                 |
+------------------------------------------------------------------------------+
