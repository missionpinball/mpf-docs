Scoops / Vertical up Kickers (VUKs) / Saucer holes
==================================================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/ball_devices`                                                  |
+------------------------------------------------------------------------------+
| :doc:`/config/switches`                                                      |
+------------------------------------------------------------------------------+
| :doc:`/config/coils`                                                         |
+------------------------------------------------------------------------------+

.. contents::
   :local:

Scoops usually capture balls from a playfield (sometimes via a subway) and
eject them back to the playfield after a short while.
Saucer holes work like scoops but the ball stays visible all the time and they
are sometimes used as a lock.
Similarly, vertical up kickers (VUKs) capture from the playfield but they
eject onto a ramp or a upper playfield.

Electronical details
--------------------

Electronically, all of those mechs consist of a switch or opto and a coil to
eject the ball.

.. image:: /mechs/images/scoop_front.jpg
   :scale: 25%
   :align: left
   :alt: Scoop from front

.. image:: /mechs/images/scoop_back.jpg
   :scale: 25%
   :align: left
   :alt: Scoop from back

.. image:: /mechs/images/scoop_side.jpg
   :scale: 25%
   :align: left
   :alt: Scoop from side

.. |clearfloat|  raw:: html

    <div style="clear: both;"></div>

|clearfloat|

Connect your switch according to :doc:`/mechs/switches/mechanical_switches`
or :doc:`/mechs/switches/optos` depending on its type.
Then connect your coil according to :doc:`/mechs/coils/index`.

Config
------

In MPF, you configure them as :doc:`ball devices </mechs/ball_devices/index>`
since they can count balls and choose to keep or eject it.

This is an example:

.. code-block:: mpf-config

    switches:
      s_scoop:
        number: 2
    coils:
      c_scoop_eject:
        number: 4
        default_pulse_ms: 20
    ball_devices:
      bd_scoop:
        ball_switches: s_scoop
        eject_coil: c_scoop_eject
        eject_timeouts: 1s

It is very common to delay the game when the ball is inside a scoop/VUK/saucer
to show animations and play sounds.
You can achieve this using a :doc:`queue_relay_player </config/queue_relay_player>`
in your mode (you might want to use
:doc:`conditional events </events/overview/conditional>` to only trigger it when
certain condition match):

.. code-block:: mpf-config

   switches:
     s_scoop:
       number: 2
   coils:
     c_scoop_eject:
       number: 4
       default_pulse_ms: 20
   ball_devices:
     bd_scoop:
       ball_switches: s_scoop
       eject_coil: c_scoop_eject
       eject_timeouts: 1s
   ##! mode: my_mode
   # in your mode
   queue_relay_player:
     balldevice_bd_scoop_ball_eject_attempt:
       post: start_mode_success_show
       wait_for: mode_success_show_ended
   show_player:
     start_mode_success_show:
       success_show:
         loops: 0
         events_when_completed: mode_success_show_ended
   shows:
     success_show:
       - duration: 10
   #!       events: test_event
         # add lights/sounds/slides here
   ##! test
   #! start_game
   #! mock_event test_event
   #! assert_balls_on_playfield 1
   #! hit_switch s_scoop
   #! advance_time_and_run .9
   #! assert_balls_on_playfield 0
   #! advance_time_and_run 2
   #! assert_balls_on_playfield 1
   #! assert_event_not_called test_event
   #! start_mode my_mode
   #! hit_switch s_scoop
   #! advance_time_and_run 2
   #! assert_event_called test_event
   #! assert_balls_on_playfield 0
   #! advance_time_and_run 10
   #! assert_balls_on_playfield 1

When your mode is running the eject will be delayed by 10s (duration of your
show). Add all your lights, shows and slides to this show.
After the show ends it will eject normally.

The same can be achieved using a :doc:`ball_hold device </config/ball_holds>`.
If you want your saucer/VUK/scoop to lock a ball for a
:doc:`multiball </config/multiballs>` use
a :doc:`ball_lock device </config/ball_locks>` instead (see
:doc:`multiball </game_logic/multiballs/index>` in the game design section for
more details).
