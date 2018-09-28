Understanding tags
==================

**General Theory**

A common definition of a tag is "a label attached to someone or something for the purpose of identification or to give other information".  This is the whole idea behind tags in MPF.  You can add one or more tags on to the various parts of your game.  These tags can be used in various ways such as firing events or identifying a device in some way.

**Tags and Events**

Some tags will cause events to be generated.  An example of this is a switch device.  You can tag a switch device with one or more tags.

.. code-block:: mpf-config

   switches:
     mygame_switch_button_start:
       number: 1
       tags: start, skyfall

In this case, whenever the start switch is activated, there will be two events.  sw_start and sw_skyfall.  They are both prefixed with "sw_" as a default.  You can overriide this with the :doc:`/config/mpf.rst` section.


**Power of Tags**

While most tags can be subsituted with events the power lies in multiple taggging whereby you use the same tags on multiple devices which can save you time and reduce your configurations.

Example 1 - Pop Bumpers

[Todo]

Example 2 - Playfield is active

[Todo]

**Reserved Tags in MPF**

MPF contains some reserved tags that are used for certain devices.  An example of this is a ball trough.

.. code-block:: mpf-config

   mygame_balldevice_trough:
     ball_switches: mygame_switch_trough_1, mygame_switch_trough_2, mygame_switch_trough_3
     eject_coil: mygame_coil_trough_eject
     eject_targets: mygame_balldevice_shooter_lane
     tags: trough, home
    
    
The two tags assist MPF in determine various characteristics of this device.  Namely that it is considered  a 'home' device where balls can come to rest when a game is not in play.  And the 'trough' tag to help MPF denote that this is a ball trough.

   
