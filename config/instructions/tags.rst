Understanding tags
==================

**General Theory**
------------------

A common definition of a tag is "a label attached to someone or something for the purpose of identification or to give other information".  This sums up the whole idea behind tags in MPF.  You can add one or more tags on to the various parts of your game.  These tag identifiers can then be used in various ways such as firing events or identifying a device in some particular way.

**Tags and Events**
-------------------

Some tags will cause events to be generated.  An example of this is a switch device.  You can tag a switch device with one or more tags.

.. code-block:: mpf-config

   switches:
     mygame_switch_button_start:
       number: 1
       tags: start, skyfall

In this case, whenever the start switch is activated, there will be two events fired.
You will see something like this in the log:

.. code-block:: console

   2018-09-26 20:32:14,215 : INFO : EventManager : Event: ======'sw_start'====== Args={}
   2018-09-26 20:32:14,215 : INFO : EventManager : Event: ======'sw_start_active'====== Args={}
   2018-09-26 20:32:14,215 : INFO : EventManager : Event: ======'sw_skyfall'====== Args={}
   2018-09-26 20:32:14,215 : INFO : EventManager : Event: ======'sw_skyfall_active'====== Args={}

Both events are prefixed with ``sw_`` as a default.
You can override this with the :doc:`/config/mpf` section.

.. note::

   Please note that those events will only show up if either a handler for them
   exists (i.e. an event_player) or when you set ``debug: True`` to your switch.
   This is purely a performance optimization and also will safe you a lot of
   log lines.


**Power of Tags**
-----------------

While tags and events can be used interchangeably at times, the real power lies in multiple tagging.
When you use the same tags on multiple devices it can save you coding time and reduce the size of your configurations.

Example 1 - Pop Bumpers
^^^^^^^^^^^^^^^^^^^^^^^

For this example, a game with 3 popbumpers will all behave in the same way.
To start we will give 100 points for every hit of a pop bumper.

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

Now we want to score 100 points every time a pop bumper is hit.
We have two ways of accomplishing this same goal.
One with pure events and one with tags.

Example with events:

.. code-block:: mpf-config

  ##! mode: my_mode
  variable_player:
    mygame_popbumper_left_active:
      score: 100
    mygame_popbumper_top_active:
      score: 100
    mygame_popbumper_right_active:
      score: 100

Now with tags:

.. code-block:: mpf-config

  ##! mode: my_mode
  variable_player:
    sw_mygame_popbumper:
      score: 100

As you can see, if you have a repeating event you can save yourself some time and coding by using tags.
Any switch tagged as *mygame_popbumper* will echo a *sw_mygame_popbumper* event.


Example 2 - Playfield is active
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Another example is tagging specific switches on a playfield to validate if a
ball is in play or not.
These would be any switches a ball could hit within regular game play which
are not part of a device.
Some devices such as drop targets will trigger their own switch during ball
search and we do not want them to end ball search doing that.
Therefore, they got built-in support for marking the playfield active and your
should not tag those switches (MPF will also complain if you do).

For our purposes we will check if a ball hits the roll over in the orbit
after it was plunged.
At that point it is obviously on the playfield and ball search should not
start.

All we need to do is add a tag:

.. code-block:: mpf-config

   switches:
     mygame_orbit_l:
       number: 55
       tags: playfield_active
     mygame_orbit_r:
       number: 56
       tags: playfield_active

**Reserved Tags in MPF**
------------------------

MPF contains some reserved tags that are used for certain devices.  An example of this is a ball trough.

.. code-block:: mpf-config

   #! switches:
   #!   s_test1:
   #!     number: 1
   #!   mygame_switch_trough_1:
   #!     number: 2
   #!   mygame_switch_trough_2:
   #!     number: 3
   #!   mygame_switch_trough_3:
   #!     number: 4
   #! coils:
   #!   mygame_coil_trough_eject:
   #!     number: 1
   ball_devices:
   #!   mygame_balldevice_shooter_lane:
   #!     ball_switches: s_test1
   #!     mechanical_eject: true
     mygame_balldevice_trough:
       ball_switches: mygame_switch_trough_1, mygame_switch_trough_2, mygame_switch_trough_3
       eject_coil: mygame_coil_trough_eject
       eject_targets: mygame_balldevice_shooter_lane
       tags: trough, home

The two tags on the ball trough device assist MPF in determining various
characteristics of this device.
Namely that it is considered  a 'home' device where balls can come to rest
when a game is not in play.
And the 'trough' tag to help MPF denote that this is a ball trough and not
some other style of captive device like a saucer.


