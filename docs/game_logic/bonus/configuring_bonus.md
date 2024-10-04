---
title: How to configure End of Ball Bonus
---

# How to configure End of Ball Bonus


This guide walks you through configuring an end-of-ball Bonus mode in
MPF.

## 1. Create your bonus mode folders

Even though the bonus mode is built-in, you'll still need to add a
`bonus` folder to your machine's *modes* folder. Then in there, add a
`config` folder, and finally, create a file in the config folder called
`bonus.yaml`. (So this is just like any other mode so far.)

It should look something like this:

![image](../images/bonus_folder.png)

## 2. Add the bonus mode to your machine-wide modes list

Remember that when you create a new mode, you need to add it to the
`modes:` section of your machine-wide config. (Why doesn't MPF just
automatically detect modes based on what folders it finds? Because you
might want to have different sets of configs that use different modes,
or you might want to disable a mode you're testing, etc.)

So just add `- bonus` to the list of modes in the `modes:` section of
your machine-wide config, like this:

``` yaml
# this is your machine-wide config.yaml

modes:
  - base
  - jukebox_mode
  - skill_shot
  - jukebox_hurryup
  - managers_choice_base
  - managers_choice_multiball
  - managers_choice_timed_mode
  - managers_choice_lit
  - mystery_lit
  - wizard_advance_lit
  - mission_rotator
  - light_mission_select
  - play_poker
  - money_bags
  - world_tour
  - music_awards
  - jukebox_two_ball
  - bonus                  # just add bonus to the list of existing modes
```

The bonus mode is automatically configured to start when the ball ends
(as long as the machine is not tilted), running at priority 500.

## 3. Think about what you want to score bonus on

Most modern pinball machines have bonus scores based on multiple things.

Use a [variable_player:](../../config/variable_player.md) to count
some bonuses:

``` mpf-config
##! mode: mode1
variable_player:
  ramp_shot_hit:
    bonus_ramps: 1
  s_target1_active:
    some_variable: 1
```

## 4. Add some settings to your bonus mode config

Now go back into your bonus mode folder open up `bonus.yaml` config file
(which should be empty at this point), and enter a basic config:

``` mpf-mc-config
##! mode: bonus
#config_version=5
mode_settings:
  display_delay_ms: 1s
  hurry_up_delay_ms: 0
  bonus_entries:
    - event: bonus_ramps
      score: 400
    - event: bonus_math
      score: 1200 * (current_player.some_variable + 2)
slide_player:
  mode_bonus_started: bonus_start_slide
  bonus_ramps: bonus_ramp_slide
  bonus_math: bonus_math_slide
  bonus_total: bonus_total_slide
slides:
  bonus_start_slide:
    widgets:
      - type: text
        text: Bonus
  bonus_ramp_slide:
    - type: text
      text: "Ramps (player|level)"
    - type: text
      text: (score)
  bonus_math_slide:
    - type: text
      text: "Some variable (player|some_variable)"
    - type: text
      text: (score)
  bonus_multiplier_slide:
    - type: text
      text: "Multiplier"
    - type: text
      text: "(multiplier)X"
  bonus_total_slide:
    - type: text
      text: "Total Bonus"
    - type: text
      text: (score)
##! test
#! start_game
#! advance_time_and_run 1
#! drain_all_balls
#! advance_time_and_run .1
#! assert_text_on_top_slide "Ramps 0"
#! assert_text_on_top_slide "400"
#! advance_time_and_run 1
#! assert_text_on_top_slide "Some variable 0"
#! assert_text_on_top_slide "2400"
#! advance_time_and_run 1
#! assert_text_on_top_slide "Total Bonus"
#! assert_text_on_top_slide "2800"
#! stop_game 10
#! advance_time_and_run 1
```

You can use
[placeholder variables](../../config/instructions/dynamic_values.md) and math in all your score entries.
