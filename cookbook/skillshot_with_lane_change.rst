Recipe: Skillshot (with Lane Change)
==============================================

This guide shows you how to build an MPF config for a skillshot with rotating
rollover lanes (a.k.a "lane change").

For a description of rollover lanes, see
:doc:`Rollover Lanes with Lane Change <rollover_lanes_with_lane_change>`


Step 1. Create a skillshot mode and lane shots
----------------------------------------------

Skillshots are a self-contained set of rules, so it's wise to create a separate
mode that can be started when a player's ball starts and ended after the
skillshot is hit (or missed).

We'll assume that the machine has switches defined in the ``switches:``
config section for each of the lanes, called ``s_lane_left``, ``s_lane_middle``,
and ``s_lane_right``. We'll also use corresponding lights ``l_lane_left`` etc.
to indicate which lane is lit.


.. code-block:: mpf-config

  #config_version=5
  modes:
    - skillshot_with_lane_change
  switches:
    s_lane_left:
      number: 1
    s_lane_middle:
      number: 2
    s_lane_right:
      number: 3
  lights:
    l_lane_left:
      number: 1
    l_lane_middle:
      number: 2
    l_lane_right:
      number: 3
  shot_profiles:
    skillshot_profile:
      states:
        - name: off
        - name: on

  ##! mode: skillshot_with_lane_change
  #! mode:
  #!   start_events: start_mode_skillshot_with_lane_change
  #!   stop_events: stop_mode_skillshot_with_lane_change
  #!   priority: 1000

The first thing our mode needs is :doc:`/config/shots`. Each lane will count as
a shot, and for this example we'll have three lanes "left", "middle", and
"right".

.. code-block:: mpf-config

  #! switches:
  #!   s_lane_left:
  #!     number: 1
  #!   s_lane_middle:
  #!     number: 2
  #!   s_lane_right:
  #!     number: 3
  ##! mode: skillshot_with_lane_change
  #! shot_profiles:
  #!   skillshot_profile:
  #!     states:
  #!       - name: off
  #!

  mode:
    start_events: start_mode_skillshot_with_lane_change
    stop_events: stop_mode_skillshot_with_lane_change
    priority: 1000

  shots:
    skillshot_left:
      advance_events: advance_skillshot_left
      profile: skillshot_profile
      switch: s_lane_left
      show_tokens:
        led: l_lane_left
    skillshot_middle:
      advance_events: advance_skillshot_middle
      profile: skillshot_profile
      switch: s_lane_middle
      show_tokens:
        led: l_lane_middle
    skillshot_right:
      advance_events: advance_skillshot_right
      profile: skillshot_profile
      switch: s_lane_right
      show_tokens:
        led: l_lane_right


Step 2. Creating a profile for the lanes
----------------------------------------

We can create a :doc:`shot_profile</config/shot_profiles>` for the lanes that
starts with the light off and makes it flash if that lane is lit for the
skillshot.

By default, a shot will advance its profile when the shot is hit, but we don't
want that here so we'll set ``advance_on_hit: false``. Instead, we have explicit
``advance_events`` set on the shots so we can advance them for the lane change.

.. code-block:: mpf-config

  ##! mode: skillshot_with_lane_change
  shot_profiles:
    skillshot_profile:
      advance_on_hit: false
      states:
        - name: off
          show: off
        - name: lit
          show: flash


Step 3. Creating a shot_group for the lanes
-------------------------------------------

To tell MPF that the lane shots are related to each other, we create a
:doc:`shot_group</config/shot_groups>` with all the shots in it.

Shot groups are powerful because they control behavior of all the shots
together. In this case, we'll use our shot group to rotate the lit shots.

.. code-block:: mpf-config

  #! switches:
  #!   s_lane_left:
  #!     number: 1
  #!   s_lane_middle:
  #!     number: 2
  #!   s_lane_right:
  #!     number: 3
  ##! mode: skillshot_with_lane_change
  #! shots:
  #!   skillshot_left:
  #!     switch: s_lane_left
  #!   skillshot_middle:
  #!     switch: s_lane_middle
  #!   skillshot_right:
  #!     switch: s_lane_right

  shot_groups:
    skillshot:
      shots: skillshot_left, skillshot_middle, skillshot_right
      disable_rotation_events: s_plunger_lane_inactive
      rotate_left_events: s_flipper_left_active
      rotate_right_events: s_flipper_right_active


The ``rotate_left_events`` and ``rotate_right_events`` trigger the lane changes
based on the flipper events. The ``disable_rotation_events`` will prevent the
player from changing lanes after they plunge the ball, for a true "skill" shot.
(If you want to allow lane changes after plunge, just remove that line.)


Step 4. Light a random shot when the mode starts
------------------------------------------------

The starting state of the shot profile is "off", so we need to pick one
shot at random and advance it to its "lit" state. We'll use the
:doc:`/config/random_event_player` for this.

.. code-block:: mpf-config

  ##! mode: skillshot_with_lane_change
  random_event_player:
    mode_skillshot_started:
      events:
        - advance_skillshot_left
        - advance_skillshot_middle
        - advance_skillshot_right



Step 5. Rewards for Skillshot
-----------------------------

When the player hits the lit skillshot shot, they get an award of points.
We can use the :doc:`/config/variable_player` for this.

When a shot in a shot group is hit, the shot group will post an event with
the state name of the shot that was hit. By using the shot group events, we can
check when *any* shot is hit, rather than having to check each shot in the group
individually.

.. code-block:: mpf-config

  ##! mode: skillshot_with_lane_change
  variable_player:
    skillshot_lit_hit:
      score: 20_000


Step 6. Ending the mode on skillshot hit, or any other hit
----------------------------------------------------------

After any skillshot lane is hit, the skillshot mode should end. We can again
use the shot group to detect *any* shot being hit, but we'll use a hit event
*without* any state because it doesn't matter whether the shot was lit or not.

We also want to end the skillshot mode if any other switch on the playfield
was hit, which we can detect from the *playfield_active* event. However, when
the skillshot is hit the *playfield_active* event will post before the
*skillshot_lit_hit* event, so if we end the mode immediately then no score will
be awarded. Instead, we add a 1 second delay after playfield activation before
ending the mode.

.. code-block:: mpf-config

  ##! mode: skillshot_with_lane_change
  event_player:
    skillshot_hit: stop_mode_skillshot
    playfield_active: stop_mode_skillshot|1s


Full Example Code
-----------------

The full code from this example can be found as a fully-working game template in
the MPF Examples repository.

https://github.com/missionpinball/mpf-examples/tree/dev/cookbook/skillshot_with_lane_change


Related Docs
------------

* :doc:`/config/random_event_player`
* :doc:`/config/shots`
* :doc:`/config/shot_groups`
* :doc:`/config/shot_profiles`
* :doc:`/config/variable_player`
