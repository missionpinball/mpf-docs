Recipe: GADGET Targets from Stern Batman '66
============================================

This guide shows you how to build an MPF config for *Batman 66's*
GADGET targets. The idea is you can use this as a guide to 
implement a similar feature in your machine.

.. note::

   This recipe requires MPF 0.53 or newer.

This guide uses the following concepts in MPF:

* :doc:`/game_logic/modes/index`
* :doc:`/config_players/event_player.html`
* :doc:`/game_logic/logic_blocks/accruals`
* :doc:`events/overview/conditional.html`
* :doc:`/config_players/show_player.html`
* :doc:`/config_players/shows`


**TODO**
You can find the complete runnable machine config for this recipe in the
``cookbook/B66_Gadget`` folder of the
`mpf-examples repository <https://github.com/missionpinball/mpf-examples>`_
on GitHub.

What is GADGET mode?
--------------------

In Bataman '66, a player may hit each of the 6 stand-up targets representing the letters of the word "GADGET". When all letters have been hit, the player is awarded a "Gadget" which gives the players special ability in the game.

Here are the specific rules we need to implement:

**GADGET**

* Each letter begin unlit
* Letters become lit when hit individually
* When an already-lit letter is hit, award if there is an unlit letter adjacent to the already-lit letter, award one adjacent letter. (Friendly Neighbor)
* After all letters are hit, award a gadget and reset the letters to the beginning.
* Players may earn multiple gadgets
* Light the lockdown bar to indicate to the player that they have earned a gadget.

Using an earned Gadget is outside the scope of this document. This cookbook only covers earning gadgets.


Step 1. The machine-wide prerequisites
--------------------------------------

Before we dig into how to handle the mode itself, we need to create a
machine-wide config that has all the devices we'll need, including the switches for the targets.

Here's what our machine config looks like. (Note that this is complete in terms
of what we need to make this recipe work, but if you have a real Batman '66
then you'll probably have a lot more than this in your machine config file. Also, the coil, switch, and light numbers are generic and need to be changes for a real machine.)

Notice the "player_vars" section.  It has a two player variables named "gadgets_available" & "gadgets_earned". This exists outside of the mode to 'protect' earned, but unused gadgets from being reset in the rare cases when we may need to stop the mode that allows players to earn gadgets.

.. code-block:: yaml

  #config_version=5

  modes:
    - gadget

  player_vars:
    gadgets_available: 
      initial_value: 0
    gadgets_earned: 
      initial_value: 0

  switches:
    s_left_flipper:
      number: 0 
      tags: left_flipper, playfield_active
    s_right_flipper:
      number: 71
      tags: right_flipper
    s_credit:
      number: 6
      tags: start
    s_outhole:
      number: 8
      tags: 
    s_gadget_g1:
      number: 17
      tags: gadget_targets
    s_gadget_a:
      number: 18
      tags: gadget_targets
    s_gadget_d:
      number: 19
      tags: gadget_targets
    s_gadget_g2:
      number: 22
      tags: gadget_targets
    s_gadget_e:
      number: 23
      tags: gadget_targets
    s_gadget_t:
      number: 24
      tags: gadget_targets
    s_trough_6:
      number: 33
      tags: 
    s_trough_5:
      number: 36
      tags: 
    s_trough_4:
      number: 37
      tags: 
    s_trough_3:
      number: 38
      tags: 
    s_trough_2:
      number: 39
      tags:
    s_trough_1:
      number: 40
      tags: 
    s_start_button:
      number: 99
      tags: start, playfield_active

  keyboard:
    s:
      switch: s_start_button

  virtual_platform_start_active_switches: s_trough_1 s_trough_2 s_trough_3 s_trough_4 s_trough_5  s_trough_6

  coils:
    c_flipper_left_main:
      number: 0
      default_pulse_ms: 20
    c_flipper_left_hold:
      number: 1
      allow_enable: true
    c_flipper_right_main:
      number: 2
      default_pulse_ms: 20
    c_flipper_right_hold:
      number: 3
      allow_enable: true
    c_trough_eject:
      number: 4
      allow_enable: true
    c_ball_eject:
      number: c12
      label:
      tags:
      default_pulse_ms: 20
    c_outhole:
      number: c14
      label:
      tags:
      default_pulse_ms: 20

  lights:
    l_gadget_g1:
      number: 5
      tags: gadget_letter
    l_gadget_a:
      number: 6
      tags: gadget_letter
    l_gadget_d:
      number: 7
      tags: gadget_letter
    l_gadget_g2:
      number: 8
      tags: gadget_letter
    l_gadget_e:
      number: 9
      tags: gadget_letter
    l_gadget_t:
      number: 10
      tags: gadget_letter
    l_lockdown_bar:
      number: 11

  ball_devices:
    bd_drain:
      ball_switches: s_outhole
      eject_coil: c_outhole
      eject_targets: bd_trough
      tags: drain, outhole
    bd_trough:
      ball_switches: s_trough_1, s_trough_2, s_trough_3, s_trough_4, s_trough_5
      eject_coil: c_ball_eject
      tags: trough, home

  playfields:
      playfield:
          default_source_device: bd_trough
          tags: default


Step 2. Create the Gadget Mode Config File
------------------------------------------

Next, we can start setting up our gadget mode; below you see the contents of ``gadget.yaml``

.. code-block:: mpf-config

  config: 
  - logic_blocks.yaml
  - event_player.yaml
  - show_player.yaml
  - variable_player.yaml

  mode:
    #this mode starts when the ball starts
    start_events: ball_started

    priority: 500


Stepping through how we're using each setting:

.. code-block:: yaml

  config: 
    - logic_blocks.yaml

The config section imports other config files; this is often easier to manage than on long config file.

.. code-block:: yaml

  priority: 500

The Gadget mode in Batman '66 is nearly always running and rarely blocked, so we have assigned it a very high priority, but one that can still be superceded if the need arises.


Step 3. Create the Accrual Logic Block
--------------------------------------

Also in our mode config folder, we will add ``logic_blocks.yaml`` to hold our mode-specific logic_blocks. In this case, we're using an :doc:`/game_logic/logic_blocks/accruals` to track when all of the letters have been hit.

.. code-block:: yaml

  accruals:
    gadget_accrual:
        events:
          - gadget_g1_complete #index [0]
          - gadget_a_complete #index [1]
          - gadget_d_complete #index [2]
          - gadget_g2_complete #index [3]
          - gadget_e_complete #index [4]
          - gadget_t_complete #index [5]
        reset_on_complete: True
        disable_on_complete: False
        reset_events: mode_gadget_started
        events_when_complete: award_gadget, reset_gadget_lights


Stepping through once again:

.. code-block:: yaml

  accruals:
    gadget_accrual:

These two lines simply tell MPF that we have an accrual and we've named it "gadget_accrual".

.. code-block:: yaml

        events:
          - gadget_g1_complete #index [0]
          - gadget_a_complete #index [1]

Next, we have a list of events for the accrual to track. Accruals behave like arrays, so I added a comment after each event to help me remember the index of each event. We'll need to reference these events and their index later.

.. code-block:: yaml

          reset_on_complete: True

Once the player has hit all of the letters, we want the accrual to reset so that they can earn more Gadgets.

.. code-block:: yaml

        disable_on_complete: False

We also have to tell MPF to leave our accrual enabled, even after it's completed.

.. code-block:: yaml

  events_when_complete: award_gadget, reset_gadget_lights

When the accrual is complete, we want it to fire the two events in the list. We'll see what these events actually do a bit later.



Step 4. Create the 'Friendly Neighbor' Behavior
-----------------------------------------------

The Gadget targets exhibit a player-friendly behavior that makes them easier to complete. If the player hits a letter that is already complete, the game will award one of the neigbhoring targets if they are incomplete. To accomplish this, we'll use conditional events in our event player.

.. code-block:: yaml

  event_player:
    #plus one gadget when accrual is complete
    award_gadget:
      - gadgets_earned
      - gadgets_available
    
    s_gadget_g1_active:
      #if the g is hit, and unlit
      - gadget_g1_complete{device.accruals.gadget_accrual.value[0]==False}
      #award a if we already have g1
      - gadget_a_complete{device.accruals.gadget_accrual.value[0]==True}
    s_gadget_a_active:
      #if a is hit and unlit
      - gadget_a_complete{device.accruals.gadget_accrual.value[1]==False}
      #award g1 if we already have a
      - gadget_g1_complete{device.accruals.gadget_accrual.value[0]==False and device.accruals.gadget_accrual.value[1]==True}
      #award d if we already have a and g1
      - gadget_d_complete{device.accruals.gadget_accrual.value[0]==True and device.accruals.gadget_accrual.value[1]==True and device.accruals.gadget_accrual.value[2]==False}
    s_gadget_d_active:
      - gadget_d_complete{device.accruals.gadget_accrual.value[2]==False}
      - gadget_a_complete{device.accruals.gadget_accrual.value[1]==False and device.accruals.gadget_accrual.value[2]==True}
      - gadget_g2_complete{device.accruals.gadget_accrual.value[1]==True and device.accruals.gadget_accrual.value[2] and device.accruals.gadget_accrual.value[3]==False}
    s_gadget_g2_active:
      - gadget_g2_complete{device.accruals.gadget_accrual.value[3]==False}
      - gadget_d_complete{device.accruals.gadget_accrual.value[2]==False and device.accruals.gadget_accrual.value[3]==True}
      - gadget_e_complete{device.accruals.gadget_accrual.value[2]==True and device.accruals.gadget_accrual.value[3]==True and device.accruals.gadget_accrual.value[4]==False}
    s_gadget_e_active:
      - gadget_e_complete{device.accruals.gadget_accrual.value[4]==False}
      - gadget_g2_complete{device.accruals.gadget_accrual.value[3]==False and device.accruals.gadget_accrual.value[4]==True}
      - gadget_t_complete{device.accruals.gadget_accrual.value[3]==True and device.accruals.gadget_accrual.value[4]==True and device.accruals.gadget_accrual.value[5]==False}
    s_gadget_t_active:
      - gadget_t_complete{device.accruals.gadget_accrual.value[5]==False}
      - gadget_e_complete{device.accruals.gadget_accrual.value[4]==False and device.accruals.gadget_accrual.value[5]==True}

There's a lot happening here, so let's get the easy stuff out of the way first:

.. code-block:: yaml

  award_gadget:
    - gadgets_earned
    - gadgets_available
  
The "award_gadget" event - triggered by the accrual completion, simply adds one to both ``player_vars`` we configured in step one.

.. code-block:: yaml

  s_gadget_a_active:
    #if a is hit and unlit
    - gadget_a_complete{device.accruals.gadget_accrual.value[1]==False}

This is our first conditional event, which covers the case of "a" having not yet been hit.  When the "a" switch is active, trigger the event "gadget_a_complete" if it hasn't been seen by the accrual. 
Note the ``value[1]`` which refers to the 2nd index of our accrual. 

.. code-block:: yaml

    - gadget_g1_complete{device.accruals.gadget_accrual.value[0]==False and device.accruals.gadget_accrual.value[1]==True}

Now, we trigger gadget_g1_complete if it hasn't been seen by the accrual AND "a" is already complete. 

.. code-block:: yaml

    - gadget_d_complete{device.accruals.gadget_accrual.value[0]==True and device.accruals.gadget_accrual.value[1]==True and device.accruals.gadget_accrual.value[2]==False}

The final case for "a" is if "g1" and "a" are complete, then trigger the event for "d" if it hasn't been triggered yet. 

If all three cases "g1", "a" and "d" have all been captured by the accrual, then nothing happens.

We repeat this series of conditional events for all letters. "g1" and "t" have fewer events because they each only have one neighboring target.




Step 5. Add Your Light Shows
----------------------------

Now, we'll add some visual feedback for the player to know when they've been awarded a letter, or completed the "gadget_accrual". This show is "light_gadget_letter.yaml" and it's in the "shows" folder for the mode. It's pretty straightforward, but uses tokens and tags to be efficient.


.. code-block:: yaml

  - time: 0
    lights: 
      (gadget_letter_made_led): (gadget_letter_made_color)

  - time: +.05
    lights: 
      (gadget_letter_made_led): off

  - time: +.05
    lights: 
      (gadget_letter_made_led): (gadget_letter_made_color)

  - time: +.05
    lights: 
      (gadget_letter_made_led): off

  - time: +.05
    lights: 
      (gadget_letter_made_led): (gadget_letter_made_color)

  - time: +.05
    lights: 
      (gadget_letter_made_led): off

  - time: +.05
    lights: 
      (gadget_letter_made_led): (gadget_letter_made_color)

  - time: +.05
    lights: 
      (gadget_letter_made_led): off

  - time: +.05
    lights: 
      (gadget_letter_made_led): (gadget_letter_made_color)

  - time: +.05
    lights: 
      (gadget_letter_made_led): off

  - time: +.05
    lights: 
      (gadget_letter_made_led): (gadget_letter_made_color)

  - time: +.05
    lights: 
      (gadget_letter_made_led): off

  - time: +.05
    lights: 
      (gadget_letter_made_led): (gadget_letter_made_color)

  - time: +.05
    lights: 
      (gadget_letter_made_led): off

  - time: +.05
    lights: 
      (gadget_letter_made_led): (gadget_letter_made_color)

  - time: +.05
    lights: 
      (gadget_letter_made_led): off

  - time: +.05
    lights: 
      (gadget_letter_made_led): (gadget_letter_final_color)

    duration: -1



This show isn't terribly complicated, but let's look at some of the features.

.. code-block:: yaml

  - time: 0
    lights: 
      (gadget_letter_made_led): (gadget_letter_made_color)

  - time: +.05
    lights: 
      (gadget_letter_made_led): off

When the show starts, it accepts a token from the ``show_player`` (we'll configure that next), that tells MPF what corresponding light(s) we're going to flash, and what color to flash them. 

In a real Batman '66, we would simply flash the light because the inserts are yellow. However, since many custom games are using RGB LED, we'll allow for any color the builder prefers.


.. code-block:: yaml

  - time: +.05
    lights: 
      (gadget_letter_made_led): (gadget_letter_final_color)

    duration: -1

The last step is special for two reasons. We're passing in a second color that will be 'held' at the end of the show indefinitely as indicated by ``duration -1``. We've done this in order to allow for the same show to end in a 'lit' or 'unlit' state, depending on our need in a situation.



In the code you can download from the link at the beginning of this cookbook, there is another show that lights the LED on the lockdown bar, but it's not worth explaining here.

Step 6. Configure the Show Player
---------------------------------

Our show player is watching for events and triggering the appropriate shows.

.. code-block:: yaml

  show_player:
    gadget_g1_complete:
      light_gadget_letter:
        priority: 10
        key: gadget_g1_hit_show
        show_tokens:
          gadget_letter_made_led: l_gadget_g1
          gadget_letter_made_color: yellow
          gadget_letter_final_color: yellow

.. code-block:: yaml

    gadget_g1_complete:
      light_gadget_letter:

When the "gadget_g1_complete" event is triggered, start the "light_gadget_letter" show starts.

.. code-block:: yaml

  key: gadget_g1_hit_show

We'll add a key to the show so that we can keep re-using the same show for all the letters.

.. code-block:: yaml

        show_tokens:
          gadget_letter_made_led: l_gadget_g1
          gadget_letter_made_color: yellow
          gadget_letter_final_color: yellow

Finally, we pass show tokens to the show to tell it what light and what color we want for the on steps and the final step. This repeats for all of the individual letters.

.. code-block:: yaml

  reset_gadget_lights:
    light_gadget_letter:
      priority: 10
      show_tokens:
        gadget_letter_made_led: gadget_letter
        gadget_letter_made_color: yellow
        gadget_letter_final_color: 000000

"reset_gadget_lights" is fired by the accrual when it's complete. We make two small, but important changes. First "gadget_letter" is a ``tag`` from the machine config assigned to all the letters in GADGET. This will cause all of the letters to play the show simultaneously. Second, "gadget_letter_final_color" is now black/off. This effectively resets the lights and prepares the inserts for a new accrual to begin.


At this point, your Gadget mode is ready to go. You can add scoring in a ``variable_player`` and extend this by writing ways to use gadgets and reduce the "gadgets_available" player_vars. If any of this feels unclear or I've muddied up the explanation, feel free to join the discussion in the forums at https://groups.google.com/forum/#!topic/mpf-users/oVwBRQOgodY .
