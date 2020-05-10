How to use MPF with OSC Devices or Hardware
===========================================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/hardware`                                                      |
+------------------------------------------------------------------------------+
| :doc:`/config/osc`                                                           |
+------------------------------------------------------------------------------+
| :doc:`/config/switches`                                                      |
+------------------------------------------------------------------------------+
| :doc:`/config/lights`                                                        |
+------------------------------------------------------------------------------+

MPF can use the `Open Sound Control (OSC) <https://en.wikipedia.org/wiki/Open_Sound_Control>`_
to interface with other software or hardware devices.
As OSC messages are not standardized we define a few custom messages:

Incoming:

* ``/sw/switch_name`` with the state ``True`` or ``False`` as parameter to set
  the state of an OSC switch in MPF
* ``/event/event_name`` with parameters in the form
  ``key1, value1, key2, value2, ...`` to post events to MPF.

Outgoing:

* ``/light/light_name/color`` with the brightness of the color as float (0-1).
* ``/event/event_name`` with parameters in the form
  ``key1, value1, key2, value2, ...`` for all events configured in
  ``events_to_send`` in your ``osc`` config section.

This is an example:

.. code-block:: mpf-config

   hardware:
     platform: osc

   osc:
     remote_ip: 127.0.0.1
     remote_port: 8000

     events_to_send:
       - player_score
       - some_non_osc_switch_active
       - some_non_osc_switch_inactive

   lights:
     test_light1:
       channels:
         red:
           - number: light1/red
         blue:
           - number: light1/blue
         green:
           - number: light1/green
     test_light2:
       number: light2

   switches:
     switch_1:
       number: 1
     switch_2:
       number: 2
     some_non_osc_switch:  # not an OSC switch but used for the events above
       number: 23
       platform: virtual


You need to install python-osc to use the OSC platform:

.. code-block:: doscon

   pip3 install python-osc

What if it did not work?
------------------------

Have a look at our :doc:`hardware troubleshooting guide </hardware/troubleshooting_hardware>`.
