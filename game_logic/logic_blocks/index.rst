Logic Blocks
============

MPF config files include the concept of "logic blocks" which let you perform
logic when certain events occur. Logic blocks can be thought of as the "glue"
that ties together all the different shows, shots, achievements, and other
parts of your game logic.

There are four types of logic blocks in MPF:

:doc:`counters <counters>`
   Count the number of times an event happens, and when a certain number is
   hit, a "complete" event is posted.

:doc:`accruals <accruals>`
   Watch for several different events to occur, and once they all do (no matter
   what order they happen in), a "complete" event is posted.

:doc:`sequences <sequences>`
   Watch for several different events that need to occur *in a specific order*,
   and once they do, a "complete" event is posted.

:doc:`state_machines <state_machines>`
   A generic state machine with arbitrary state transitions and state.

Logic blocks can be configured to store their state in player variables,
meaning that each logic block will remember where it was from ball-to-ball.

Logic blocks can be added to modes, and they can have events to enable, disable,
and reset them.

To help you understand how logic blocks might be used, here are some real
world examples from *Attack from Mars* (if we were building that game in MPF):

* A counter logic block can count the number of times a pop bumper is hit, and
  then when it hits a certain number, it posts an event to start a "Super Jets"
  mode.
* A counter can be used to track the three hits to the force field that are
  needed to lower it.
* A counter can be used (along with a timer) to track combos
* An accrual can be used in the Martian Attack mode to track all 4 of the
  martians being hit

You should also read about :doc:`integration of show and logic blocks <integrating_logic_blocks_and_shows>`.

.. toctree::
   :titlesonly:
   :hidden:

   Counters <counters>
   Accruals <accruals>
   Sequences <sequences>
   State Machines <state_machines>
   integrating_logic_blocks_and_shows
   scoring_based_on_logic_blocks
   integrating_logic_blocks_and_lights
   integrating_logic_block_and_slides
   persisting_state_in_a_player_variable
