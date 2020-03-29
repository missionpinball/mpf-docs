Mystery Awards
==============

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/ball_holds`                                                    |
+------------------------------------------------------------------------------+
| :doc:`/config/event_player`                                                  |
+------------------------------------------------------------------------------+
| :doc:`/config/random_event_player`                                           |
+------------------------------------------------------------------------------+
| :doc:`/config/slide_player`                                                  |
+------------------------------------------------------------------------------+
| :doc:`/config/slides`                                                        |
+------------------------------------------------------------------------------+

Mystery awards provide a random award from a list of options while holding the ball.

Holding the Ball
----------------------------------------------

Any :doc:`ball_device </mechs/ball_devices/index>` can be used to hold a ball
while the mystery award display runs with
:doc:`ball_holds </game_logic/ball_holds/index>`.

Here is an example of how to use a scoop to hold a ball during a mystery award
animation:

.. code-block:: mpf-config

   #! switches:
   #!   s_ball1:
   #!     number:
   #!   s_ball2:
   #!     number:
   #! coils:
   #!   c_eject:
   #!     number:
   #! ball_devices:
   #!   bd_low_scoop:
   #!     ball_switches: s_ball1, s_ball2
   #!     eject_coil: c_eject
   ##! mode: mystery_mode
   event_player:
     upper_lanes_complete: enable_mystery

   ball_holds:
     mystery_scoop:
       balls_to_hold: 1
       hold_devices: bd_low_scoop
       enable_events: enable_mystery
       disable_events: end_mystery, multiball_active
       release_one_events: end_mystery

In the above example, the scoop will only hold the ball when it is enabled with
the enable_mystery event.
For example, the player needs to complete upper lanes to light mystery.
Only when those conditions are met will the scoop hold the ball.

Under disable_events, you can see that the example also prevents the mystery
award during multiball.
These events allow you to control when you don't want the device to hold on to
the ball.

At the end of the mystery award, the ball_hold is disabled and releases a ball.


Providing Random Awards
~~~~~~~~~~~~~~~~~~~~~~~

Once mystery has been lit and the ball enters the device, you can use
:doc:`random_event_player </config_players/random_event_player>` to control
which awards are chosen.

In the below example, there are four possible awards and the game will make
sure each one is provided to avoid doubling-up.

.. code-block:: mpf-config

    ##! mode: mystery_mode
    random_event_player:
      ball_hold_mystery_scoop_held_ball:
        events:
          mystery_award_1_event: 30 #numbers show probability of event
          mystery_award_2_event: 20
          mystery_award_3_event: 20
          mystery_award_4_event: 30
        force_all: true

A random award will only be selected after a ball has been held in the scoop.

Displaying Awards
~~~~~~~~~~~~~~~~~

You can use anything to display an award such as a slide or video.
In the below example, a video is used for each award and the scoop will eject
the ball after the video has completed.

.. code-block:: mpf-mc-config

  ##! mode: mystery_mode
  event_player:
    slide_award_1_slide_removed: end_mystery
    slide_award_2_slide_removed: end_mystery
    slide_award_3_slide_removed: end_mystery
    slide_award_4_slide_removed: end_mystery

  slide_player:
    mystery_award_1_event:
      award_1_slide:
        expire: 5s
    mystery_award_2_event:
      award_2_slide:
        expire: 5s
    mystery_award_3_event:
      award_3_slide:
        expire: 5s
    mystery_award_4_event:
      award_4_slide:
        expire: 5s

  slides:
    award_1_slide:
      - type: video
        video: award_1
    award_2_slide:
      - type: video
        video: award_2
    award_3_slide:
      - type: video
        video: award_3
    award_4_slide:
      - type: video
        video: award_4


Full Mystery Award Example
---------------------------

Here is the full example you can use in a mode as a template to start working
on your own mystery award.

.. code-block:: mpf-mc-config

   #! switches:
   #!   s_ball1:
   #!     number:
   #!   s_ball2:
   #!     number:
   #! coils:
   #!   c_eject:
   #!     number:
   #! ball_devices:
   #!   bd_low_scoop:
   #!     ball_switches: s_ball1, s_ball2
   #!     eject_coil: c_eject
   ##! mode: mystery_mode
   event_player:
     upper_lanes_complete: enable_mystery
     slide_award_1_slide_removed: end_mystery
     slide_award_2_slide_removed: end_mystery
     slide_award_3_slide_removed: end_mystery
     slide_award_4_slide_removed: end_mystery

   ball_holds:
     mystery_scoop:
       balls_to_hold: 1
       hold_devices: bd_low_scoop
       enable_events: enable_mystery
       disable_events: end_mystery, multiball_active
       release_one_events: end_mystery

   random_event_player:
     ball_hold_mystery_scoop_held_ball:
       events:
         mystery_award_1_event: 30 #numbers show probability of event
         mystery_award_2_event: 20
         mystery_award_3_event: 20
         mystery_award_4_event: 30
       force_all: true

   slide_player:
     mystery_award_1_event:
       award_1_slide:
         expire: 5s
     mystery_award_2_event:
       award_2_slide:
         expire: 5s
     mystery_award_3_event:
       award_3_slide:
         expire: 5s
     mystery_award_4_event:
       award_4_slide:
         expire: 5s

   slides:
     award_1_slide:
       - type: video
         video: award_1
     award_2_slide:
       - type: video
         video: award_2
     award_3_slide:
       - type: video
         video: award_3
     award_4_slide:
       - type: video
         video: award_4


More examples
-------------

See :doc:`/game_design/index` and :doc:`/game_design/other_modes` in particular
for more examples.
