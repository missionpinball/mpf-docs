Recipe: Rollover Lanes (with Lane Change)
==============================================

This guide shows you how to build an MPF config for rotating rollaver lanes,
as found in *Indiana Jones*, *Attack From Mars*, *Medieval Madness*,
and many, many more.

What are Rollover Lanes?
------------------------------

Rollover lanes are found where pinball machines
have a series of parallel lanes the ball can roll through. These are
commonly found at the top of the playfield, often above pop bumpers and accessed via
the outer orbit loop. Some games, like *Medieval Madness*, also use the
outlanes and return lanes together as a group of rollover lanes

Each lane in the rollover lane group has a switch and a light. To start,
all the lights are off. When the ball passes through a lane, that lane's
light turns on. When the player turns on all the lights, they are awarded
some prize and the lanes reset to off.

What is a Lane Change?
----------------------

Games that use rollover lanes usually incorporate a "lane change" feature
to make the completion easier. Lane changes use the flipper buttons to
rotate the lit and unlit lane shots, shifting them left and right according
to which button is pressed.

If a ball is about to enter a lane that's already been lit, the player can
use the flipper buttons to shift the lanes so that the lane with the ball
is unlit when the ball rolls over. By changing the lanes ahead of the ball,
the player can complete the lane set more frequently—and it also gives the
player more to do while the ball is away from the flippers!

Step 1. Create a lane change mode
---------------------------------

Lane changes are typically available at all times during a game, so it's
wise to create a separate mode for them. This mode can be run at the same
time as other modes (but stopped any time, maybe during wizard modes if
you want).

The first thing our mode needs is :doc:`/config/shots`. Each lane will count as a shot,
and for this example we'll use the I-N-D-Y lanes from the Indiana Jones
pinball game. We'll assume that the machine has switches defined in the
``switches:`` config section for each of the
top lanes, called ``s_top_lane_1`` through ``s_top_lane_4``.

.. code-block:: mpf-config

  #! switches:
  #!   s_top_lane_1:
  #!     number: 1
  #!   s_top_lane_2:
  #!     number: 2
  #!   s_top_lane_3:
  #!     number: 3
  #!   s_top_lane_4:
  #!     number: 4
  ##! mode: top_lanes
  mode:
    start_events: start_mode_top_lanes
    stop_events: stop_mode_top_lanes, ball_will_end

  shots:
    top_lane_i:
      switch: s_top_lane_1
    top_lane_n:
      switch: s_top_lane_2
    top_lane_d:
      switch: s_top_lane_3
    top_lane_y:
      switch: s_top_lane_4


Step 2. Creating a profile for the lanes
----------------------------------------


We can create a :doc`shot_profile</config/shot_profiles>` for the top lanes that starts with the
light on, and turns it off after the shot is hit.

.. code-block:: mpf-config

  ##! mode: top_lanes
  shot_profiles:
    top_lane_profile:
      states:
        - name:
          show: off
        - name: hit
          show: on

.. note:: In common pinball parlance, a shot is "lit" if the player should try an hit it. In almost all cases this means the light for the shot is on (i.e. "lit"), but rollover lane shots are the opposite:  the light is **off** when the shot is lit, and **on** after the shot is hit.

We can apply our shot profile to each of the ``shots`` we
defined earlier. Each lane has its own light, which we can specify
using ``show_tokens``. This tells MPF that when it plays the show (in this
case, the "on" show) for a specific shot, use the light that corresponds to
that shot.

We'll assume the machine has four lights defined in the ``lights:``
config section, called ``l_top_lane_1`` through ``l_top_lane_4``

.. code-block:: mpf-config

  #! switches:
  #!   s_top_lane_1:
  #!     number: 1
  #!   s_top_lane_2:
  #!     number: 2
  #!   s_top_lane_3:
  #!     number: 3
  #!   s_top_lane_4:
  #!     number: 4
  ##! mode: top_lanes
  #! shot_profiles:
  #!   top_lane_profile:
  #!     states:
  #!       - name:
  #!         show: off
  #!       - name: hit
  #!         show: on
  shots:
    top_lane_i:
      switch: s_top_lane_1
      profile: top_lane_profile
      show_tokens:
        led: l_top_lane_1
    top_lane_n:
      switch: s_top_lane_2
      profile: top_lane_profile
      show_tokens:
        led: l_top_lane_2
    top_lane_d:
      switch: s_top_lane_3
      profile: top_lane_profile
      show_tokens:
        led: l_top_lane_2
    top_lane_y:
      switch: s_top_lane_4
      profile: top_lane_profile
      show_tokens:
        led: l_top_lane_2


Step 3. Creating a shot_group for the lanes
-------------------------------------------

To tell MPF that the four lane shots are related to each other, we create a
:doc:`shot_group</config/shot_groups>` with all the shots in it.

Shot groups are powerful because they control behavior of all the
shots together. In this case, we'll use our shot group to:

* Rotate the lit and hit shots
* Trigger an event when all the shots are hit
* Reset all the shots to be lit

.. code-block:: mpf-config

  #! switches:
  #!   s_top_lane_1:
  #!     number: 1
  #!   s_top_lane_2:
  #!     number: 2
  #!   s_top_lane_3:
  #!     number: 3
  #!   s_top_lane_4:
  #!     number: 4
  ##! mode: top_lanes
  #! shots:
  #!   top_lane_i:
  #!     switch: s_top_lane_1
  #!     profile: top_lane_profile
  #!     show_tokens:
  #!       led: l_top_lane_1
  #!   top_lane_n:
  #!     switch: s_top_lane_2
  #!     profile: top_lane_profile
  #!     show_tokens:
  #!       led: l_top_lane_2
  #!   top_lane_d:
  #!     switch: s_top_lane_3
  #!     profile: top_lane_profile
  #!     show_tokens:
  #!       led: l_top_lane_2
  #!   top_lane_y:
  #!     switch: s_top_lane_4
  #!     profile: top_lane_profile
  #!     show_tokens:
  #!       led: l_top_lane_2
  #!
  #! shot_profiles:
  #!   top_lane_profile:
  #!     states:
  #!       - name:
  #!         show: off
  #!       - name: hit
  #!         show: on
  shot_groups:
    top_lane_group:
      shots: top_lane_i, top_lane_n, top_lane_d, top_lane_y
      reset_events: top_lane_group_hit_complete
      rotate_left_events: s_flipper_left_active
      rotate_right_events: s_flipper_right_active

The ``rotate_left_events`` and ``rotate_right_events`` allow the
lane changes based on the flipper events.

A shot group tracks the profile state of each shot, and will post
an event *(shot_group_name)_(state_name)_complete* event whenever
all shots in the group are the same state. In the profile "top_lane_profile"
we said that the second state is called "hit", so we can use the
*top_lane_group_hit_complete* event to know that all the shots are
hit. The name of the state is up to you.

When the *top_lane_group_hit_complete* event is triggered, the
shot group will reset all the shots to their initial state: the
"lit" state of the profile with the light off. Now the lanes are
ready for the player to complete again!

Step 4. Rewards for rollover lane completion
--------------------------------------------

Presumably when the player completes the rollover lanes, they should get
some reward: a bonus multiplier, a counter advance, some points...
it can be anything.

In this example, we'll use the :doc:`/config/variable_player` to
award the player 10,000 points for completing the rollover lanes, and
also increase a the bonus multiplier for the end-of-game bonus.

.. code-block:: yaml

  variable_player:
    top_lane_group_hit_complete:
      score: 10000
      bonus_multiplier: 1

See :doc:`/game_logic/bonus/index` for details on *bonus_multiplier*.

The full mode config code
-------------------------

.. code-block:: mpf-config

  #! switches:
  #!   s_top_lane_1:
  #!     number: 1
  #!   s_top_lane_2:
  #!     number: 2
  #!   s_top_lane_3:
  #!     number: 3
  #!   s_top_lane_4:
  #!     number: 4
  ##! mode: top_lanes
  mode:
    start_events: start_mode_top_lanes
    stop_events: stop_mode_top_lanes, ball_will_end

  shots:
    top_lane_i:
      switch: s_top_lane_1
      profile: top_lane_profile
      show_tokens:
        led: l_top_lane_1
    top_lane_n:
      switch: s_top_lane_2
      profile: top_lane_profile
      show_tokens:
        led: l_top_lane_2
    top_lane_d:
      switch: s_top_lane_3
      profile: top_lane_profile
      show_tokens:
        led: l_top_lane_2
    top_lane_y:
      switch: s_top_lane_4
      profile: top_lane_profile
      show_tokens:
        led: l_top_lane_2

  shot_groups:
    top_lane_group:
      shots: top_lane_i, top_lane_n, top_lane_d, top_lane_y
      reset_events: top_lane_group_hit_complete
      rotate_left_events: s_flipper_left_active
      rotate_right_events: s_flipper_right_active

  shot_profiles:
    top_lane_profile:
      states:
        - name:
          show: off
        - name: hit
          show: on

  variable_player:
    top_lane_group_hit_complete:
      score: 10000
      bonus_multiplier: 1


Related Docs
------------

* :doc:`/config/shots`
* :doc:`/config/shot_groups`
* :doc:`/config/shot_profiles`
* :doc:`/config/variable_player`
