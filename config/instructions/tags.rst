Understanding tags
==================

**General Theory**
------------------

A common definition of a tag is "a label attached to someone or something for the purpose of identification or to give other information".  This is the whole idea behind tags in MPF.  You can add one or more tags on to the various parts of your game.  These tags can be used in various ways such as firing events or identifying a device in some way.

**Tags and Events**
-------------------

Some tags will cause events to be generated.  An example of this is a switch device.  You can tag a switch device with one or more tags.

.. code-block:: mpf-config

   switches:
     mygame_switch_button_start:
       number: 1
       tags: start, skyfall

In this case, whenever the start switch is activated, there will be two events.  sw_start and sw_skyfall.  They are both prefixed with "sw_" as a default.  You can overriide this with the :doc:`/config/mpf.rst` section.


**Power of Tags**
-----------------

While most tags can be subsituted with events the power lies in multiple taggging whereby you use the same tags on multiple devices which can save you time and reduce the size of your configurations.

Example 1 - Pop Bumpers
^^^^^^^^^^^^^^^^^^^^^^^

For this example, a game with 3 popbumpers will all behave in the same way.  To start we will give 100 points for every hit of a pop bumper.

Firstly we define the popbumper switches.

.. code-block:: mpf-config

   switches:
     mygame_popbumper_left:
       number: 55
       tags: mygame_popbumper
     mygame_popbumper_top:
       number: 56
       tags: mygame_popbumper
     mygame_popbumper_right:
       number: 57
       tags: mygame_popbumper
       
Now we want to score 100 points every time a pop bumper is hit.  We have two ways of accomplishing this same goal.  One with pure events and one with tags.

Example with events:

.. code-block:: mpf-config

  scoring:
    mygame_popbumper_left_active:
      score: 100
    mygame_popbumper_top_active:
      score: 100
    mygame_popbumper_right_active:
      score: 100


Now with tags:

.. code-block:: mpf-config

  scoring:
    sw_mygame_popbumper:
      score: 100


As you can see, if you have a repeating event you can save yourself some time and coding by using tags.  Any switch tagged as mygame_popbumper will echo a sw_mygame_popbumper event.


Example 2 - Playfield is active
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Another example is tagging specific switches on a playfield to denote if a ball is in play or not.  These would be any switches a ball could hit within regular game play.

Building on the first example, we can add a second tag to the pop bumpers in case there is a loose ball on the playfield.  For our purposes we will check that if a pop bumper is hit, then the skill shot must be disabled.

First we add the tags.

.. code-block:: mpf-config

   switches:
     mygame_popbumper_left:
       number: 55
       tags: mygame_popbumper, playfield_active
     mygame_popbumper_top:
       number: 56
       tags: mygame_popbumper, playfield_active
     mygame_popbumper_right:
       number: 57
       tags: mygame_popbumper, playfield_active

Now we perform our logic based on this new tag.

.. code-block:: mpf-config

   event_player:
     sw_playfield_active: mygame_disable_skillshot

In this case whenever the playfield has an active ball if will fire the event mygame_disable_skillshot.  What you do with the event mygame_disable_skillshot is up to you.


**Reserved Tags in MPF**
------------------------

MPF contains some reserved tags that are used for certain devices.  An example of this is a ball trough.

.. code-block:: mpf-config

   mygame_balldevice_trough:
     ball_switches: mygame_switch_trough_1, mygame_switch_trough_2, mygame_switch_trough_3
     eject_coil: mygame_coil_trough_eject
     eject_targets: mygame_balldevice_shooter_lane
     tags: trough, home
    
    
The two tags assist MPF in determine various characteristics of this device.  Namely that it is considered  a 'home' device where balls can come to rest when a game is not in play.  And the 'trough' tag to help MPF denote that this is a ball trough.

   
