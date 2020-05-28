Combo Switches ("flipper cancel", etc.)
=======================================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/combo_switches`                                                |
+------------------------------------------------------------------------------+


.. contents::
   :local:

MPF contains support for "combo switches" which are special combinations of
switches that post events when they're hit together.

The most basic example of this is the "flipper cancel" combination, where a
player can cancel a show or bonus by hitting both flippers at the same time.
In fact MPF contains built-in support for the flipper cancel combo. If you
add the tag ``left_flipper`` to your left flipper switch, and ``right_flipper``
to your right flipper switch, then whenever the player hits both flippers at
the same time, an MPF event called *flipper_cancel* will be posted.

Combo switches are also used for things like different kinds of skill shots.
For example, in *Attack From Mars*, if the player hits the launch button, the
ball is launched into the pop bumper area, but if the player holds down the
left flipper button while pressing the launch button, the ball gate (Bally part A-17796) in the upper
playfield is raised and the ball is allowed to pass through and is delivered to the flippers for an attempt
at a super skill shot. The left flipper + launch button combination is something
you can enable with MPF's combo switches.

MPF's combo switches also generate events once both switches are hit together,
then one switch is tapped while the other is held in. This can be used to
scroll through certain information screens with one button while the combo is
active.

You can set various timing options for combo switches, including how close
together the two switches have to be hit to count as a combo, how long they
have to be held, and how long they have to be released.

Built-in flipper cancel combo
-----------------------------

MPF's ``mpfconfig.yaml`` (the built-in machine config that's merged in with
all machine configs) includes the following section:

.. code-block:: mpf-config

   combo_switches:
     both_flippers:
       tag_1: left_flipper
       tag_2: right_flipper
       events_when_both: flipper_cancel

This means if you tag add ``tags: left_flipper`` to your left flipper button
and ``tags: right_flipper`` to your right flipper button, you'll get an event
*flipper_cancel* posted anytime the player has both flipper buttons pushed in
which you can use to cancel shows or whatever else you want to do. If you want
to change or override this (perhaps you want to set a ``max_offset_time:`` to
make sure this event is only posted if the player hits the flipper buttons
within 500ms, then you can copy and add this section to your own machine
config file and it will overwrite this default config.

Here is an example of using flipper_cancel to cancel a show:

.. code-block:: mpf-mc-config

   switches:
     s_flipper_left:
       tags: left_flipper
       number:
     s_flipper_right:
       tags: right_flipper
       number:

   shows:
     mode_intro:
       - duration: 5
         slides:
           mode_intro_slide:
             widgets:
               - type: text
                 text: Hit 50 switches to light jackpot
                 color: white
                 font_size: 100
   show_player:
     start_mode_intro_show:
       mode_intro:
         loops: 0
         events_when_stopped: mode_intro_show_ended
     flipper_cancel:
       mode_intro:
         action: stop
   ##! test
   #! post start_mode_intro_show
   #! advance_time_and_run .1
   #! assert_slide_active mode_intro_slide
   #! hit_switch s_flipper_left
   #! hit_switch s_flipper_right
   #! advance_time_and_run .1
   #! assert_slide_not_active mode_intro_slide

The start_mode_intro_show will play for 5 seconds unless both flipper buttons are pressed which will cancel the show.


Monitorable Properties
----------------------

For :doc:`dynamic values </config/instructions/dynamic_values>` and
:doc:`conditional events </events/overview/conditional>`,
the prefix for combo switches is ``device.combo_switches.<name>``.

*state*
   String which reflects what state this combo switch is in.
   Options wil be one of the following: *inactive*, *both* or *one*.

Related How To guides
---------------------

* :doc:`Canceling ball end shows using flipper_cancel </game_logic/ball_start_end/index>`

Related Events
--------------

.. include:: /events/include_combo_switches.rst
