Recipe: Sequential Drop Target Banks
========================================

This guide shows you how to build an MPF config for a drop target bank with
targets that must be hit in a specific order.

The mode starts with one target flashing as the correct target to hit, and all
the rest off. Hitting the correct target will keep the hit target down, hold the
light on, and flash the next target. Hitting an incorrect target will reset that
target's coil and keep the light off.


Step 1. Create a sequential_drops mode and lane shots
-----------------------------------------------------

We'll create a separate mode called *sequential_drops* to manage the game logic.
Separate modes keep the code clean and make it easy to turn the drop sequence on
and off as needed (e.g. during a multiball or wizard mode).

The first thing our mode needs is :doc:`/config/shots`. Each drop target will be
a shot (in this example, we'll have four). Each shot has a switch, a light, and
a shot profile to track its state.

Each shot will also have unique ``advance_events`` configured, which will
advance the shot (from "off" to "lit") when its predecessor is hit, and again
advance the shot (from "lit" to "down") when it is hit. The final shot does not
need to advance from "lit" to "down" because the sequence resets when it's hit.

Each shot also has ``reset_events`` configured, so that the entire sequence can
be reset after completion.


.. code-block:: mpf-config

  #! switches:
  #!   s_drop_1:
  #!     number: 1
  #!   s_drop_2:
  #!     number: 2
  #!   s_drop_3
  #!     number: 3
  #!   s_drop_4:
  #!     number: 4
  #! lights:
  #!   l_drop_1:
  #!     number: 1
  #!   l_drop_2:
  #!     number: 2
  #!   l_drop_3
  #!     number: 3
  #!   l_drop_4:
  #!     number: 4
  #! shot_profiles:
  #!   drop_sequence:
  #!     states:
  #!       - name: off
  #!       - name: lit
  #!       - name: down
  ##! mode: sequential_drops

  mode:
    start_events: start_mode_sequential_drops
    stop_events: stop_mode_sequential_drops
    priority: 200

  shots:
    drop_1:
      advance_events: advance_drop_1, drop_1_lit_hit
      reset_events: reset_drop_sequence
      switch: s_drop_1
      profile: drop_sequence
      show_tokens:
        led: l_drop_1
    drop_2:
      advance_events: drop_1_lit_hit, drop_2_lit_hit
      reset_events: reset_drop_sequence
      switch: s_drop_2
      profile: drop_sequence
      show_tokens:
        led: l_drop_2
    drop_3:
      advance_events: drop_2_lit_hit, drop_3_lit_hit
      reset_events: reset_drop_sequence
      switch: s_drop_3
      profile: drop_sequence
      show_tokens:
        led: l_drop_3
    drop_4:
      advance_events: drop_3_lit_hit
      reset_events: reset_drop_sequence
      switch: s_drop_4
      profile: drop_sequence
      show_tokens:
        led: l_drop_4


Step 2. Create a profile for the targets
------------------------------------------

We can create a :doc:`shot_profile</config/shot_profiles>` for the targets that
starts with the light off, flashes it after one advancement, and keeps the light
on solid after a second advancement. By default, a shot will advance its profile
when the shot is hit, but we don't want that here so we'll set
``advance_on_hit: false``.

.. code-block:: mpf-config

  ##! mode: sequential_drops

  shot_profiles:
    drop_sequence:
      advance_on_hit: false
      states:
        - name: off
          show: off
        - name: lit
          show: flash
        - name: down
          show: on

Step 3. Create a Sequence Logic Block to track the progression
--------------------------------------------------------------

MPF includes a number of convenient ways for tracking progress called Logic
Blocks, including the :doc:`sequence</config/sequences>` that we can use to
require a series of events to occur in a specific order.

The below sequence requires all four drop target shots to be hit, but only
registers a hit if the shot is in the "lit" state. This allows us to track where
we are in the sequence without having to monitor each shot individually.

The sequence also has ``restart_events`` so we can restart when the mode starts
and when the sequence completes. All logicblocks have a default completion event
called *logicblock_(name)_complete* so we don't need to explicitly define any
completion event.

.. code-block:: mpf-config

  ##! mode: sequential_drops

  sequences:
    drop_sequence:
      restart_events: reset_drop_sequence
      events:
        - drop_1_lit_hit
        - drop_2_lit_hit
        - drop_3_lit_hit
        - drop_4_lit_hit


Step 4. Start, advance, and reset the shots
-------------------------------------------

We will use events to manage the behavior of the shots and the drop targets. The
first step is to identify all the rules of how the sequence and shots behave.

* Rule 1: When the mode starts, reset the drop sequence
* Rule 2: When the sequence is completed, reset the drop sequence

On a reset, all of the shots will be in their "off" state. We need the first
target to be "lit" in order for the sequence to start.

* Rule 3: When the sequence resets, advance the first target from "off" to "lit"

When a shot is in the "off" state and gets hit, we want to fire the reset coil
for the target so that the target stays up.

* Rule 4: When an "off" shot is hit, reset its coil

We can apply all of these rules based on the corresponding events, like follows.


.. code-block:: mpf-config

  ##! mode: sequential_drops

  event_player:
    # When the mode starts, reset the drop sequence
    mode_sequential_drops_started: reset_drop_sequence

    # When the sequence is completed, reset the drop sequence
    logicblock_drop_sequence_complete: reset_drop_sequence

    # When the sequence resets, advance the first target
    reset_drop_sequence: advance_drop_1

    # When an "off" shot is hit, reset its coil
    drop_1_off_hit: reset_drop_1
    drop_2_off_hit: reset_drop_2
    drop_3_off_hit: reset_drop_3
    drop_4_off_hit: reset_drop_4

The above configuration requires that each drop target coil has the
corresponding reset events, as configured below.

.. code-block:: mpf-config

  #! switches:
  #!   s_drop_1:
  #!     number: 1
  #!   s_drop_2:
  #!     number: 2
  #!   s_drop_3:
  #!     number: 3
  #!   s_drop_4:
  #!     number: 4
  #! coils:
  #!   c_drop_1:
  #!     number: 1
  #!   c_drop_2:
  #!     number: 2
  #!   c_drop_3:
  #!     number: 3
  #!   c_drop_4:
  #!     number: 4

  drop_targets:
    drop_1:
      switch: s_drop_1
      reset_coil: c_drop_1
      reset_events: ball_starting, machine_reset_phase_3, reset_drop_1
    drop_2:
      switch: s_drop_1
      reset_coil: c_drop_1
      reset_events: ball_starting, machine_reset_phase_3, reset_drop_2
    drop_3:
      switch: s_drop_1
      reset_coil: c_drop_1
      reset_events: ball_starting, machine_reset_phase_3, reset_drop_3
    drop_4:
      switch: s_drop_1
      reset_coil: c_drop_1
      reset_events: ball_starting, machine_reset_phase_3, reset_drop_4


Step 5. Rewards for progression and completion
----------------------------------------------

When a drop target is hit, The sequence logic block keeps track of whether it is
the part of the sequence or not. We can easily award points for progression with
the *logicblock_(name)_hit* event (when a lit target is hit) and the
*logicblock_(name)_complete* event (when the full sequence is completed).


.. code-block:: mpf-config

  ##! mode: sequential_drops

  variable_player:
    logicblock_drop_sequence_hit:
      score: 1000
    logicblock_drop_sequence_complete:
      score: 50_000


Full Example Code
-----------------

The full code from this example can be found as a fully-working game template in
the MPF Examples repository.

https://github.com/missionpinball/mpf-examples/tree/dev/cookbook/sequential_drop_banks


Related Docs
------------

* :doc:`/config/shots`
* :doc:`/config/shot_groups`
* :doc:`/config/shot_profiles`
* :doc:`/config/sequences`
* :doc:`/config/variable_player`
