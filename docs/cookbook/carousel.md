---
title: Carousel Mode Selection
---

# Carousel Mode Selection


Related Config File Sections:

* [mode:](../config/mode.md)
* [mode_settings:](../config/mode_settings.md)
* [event_player:](../config/event_player.md)
* [slide_player:](../config/slide_player.md)
* [slides:](../config/slides.md)

A carousel allows you to create process for the player to select from a
list of items such as selecting a mode to play. The carousel is
implemented as a mode. The player can move through a list of items that
you provide on the display or cycle through playfield inserts.

This is just one way to select modes. More ways to implement mode
selection are described in the
[mode selection section](../game_design/mode_selection.md) of the
[game design documentation](../game_design/index.md).

A common use of the carousel is to create a mode selection process. For
example, the player can scroll through a list of modes on the display.
Each mode could be presented to the user as a slide. The player can move
from slide to slide using the flippers. Once the player decides which
mode to play, he can select the mode by hitting the start button or both
flippers at once. This is just one example of how you could implement a
carousel as a mode selection process.

There is a reference to a code file in here so be careful to include
that reference. You don't need to download any code as it is already in
you MPF installation. Here is the process of configuring a carousel:

Create a mode folder and config file

!!! note

    It is recommended to use the *flipper_inactive* events to rotate, rather
    than *flipper_active*. This allows the use of *flipper_cancel* to select
    items without accidentally rotating before the selection occurs.

Depending on your situation, especially if you use *flipper_cancel* as
the select event, you may notice that after cancelling the subsequent
*flipper_inactive* events still play sounds or change slides after
selection has been made. The Carousel's `block_events` can be used to
prevent carousel event handling until one of the `release_events` is
posted. If you don't need to do anything after selection, just
specifying `block_events` without any
`release_events` will help.

``` yaml
block_events: flipper_cancel
release_events: both_flippers_inactive
```

There are two events of importance here:

* carousel_\(item)\_highlighted
* carousel_\(item)\_selected

You can use the carousel_\(item)\_highlighted event to
display a slide showing the name of the mode to the player.

You can then use the carousel_\(item)\_selected event to
start the mode that was selected by the player.

``` yaml
##! mode: my_carousel
# in mode my_carousel
#config_version=5
mode:
  start_events: ball_starting
  stop_events: my_carousel_item_selected
  code: mpf.modes.carousel.code.carousel.Carousel
  use_wait_queue: true
mode_settings:
  selectable_items: terra, pyro, space, liquid
  select_item_events: s_start_inactive
  next_item_events: s_right_flipper_inactive
  previous_item_events: s_left_flipper_inactive
slide_player:
  my_carousel_terra_highlighted: select_terra
  my_carousel_liquid_highlighted: select_liquid
  my_carousel_space_highlighted: select_space
  my_carousel_pyro_highlighted: select_pyro
slides:
  select_liquid:
    widgets:
      - type: text
        text: LIQUID METAL
        font_size: 100
        color: yellow
    transition:
      type: move_in
      direction: right
  select_terra:
    widgets:
      - type: text
        text: TERAFORM
        font_size: 100
        color: yellow
    transition:
      type: move_in
      direction: right
  select_space:
    widgets:
      - type: text
        text: SPACE OUT
        font_size: 100
        color: yellow
    transition:
      type: move_in
      direction: right
  select_pyro:
    widgets:
      - type: text
        text: PYRO
        font_size: 100
        color: yellow
    transition:
      type: move_in
      direction: right
##! test
#! start_game
#! advance_time_and_run .1
#! assert_available_balls_on_playfield 0
#! assert_text_on_top_slide TERAFORM
#! post s_right_flipper_inactive
#! advance_time_and_run .1
#! assert_text_on_top_slide PYRO
#! post s_start_inactive
#! advance_time_and_run .1
#! assert_available_balls_on_playfield 1
```

## Doctor Who Carousel

The following example is based around Bally's Doctor Who. When the
player starts a game, the player is shown via a carousel the option to
pick eight modes, each representing a certain Doctor. The flipper
buttons control the carousel right and left. When the Launch Button is
pressed, the game starts the mode selected by the player and launches
the ball.

``` yaml
#config_version=5
##! mode: carousel
# put this in your modes/carousel/config/carousel.yaml
mode:
  start_events: ball_starting
  stop_events: carousel_item_selected
  code: mpf.modes.carousel.code.carousel.Carousel
  priority: 125
  use_wait_queue: true
mode_settings:
  selectable_items: Doctor1, Doctor2, Doctor3, Doctor4, Doctor5, Doctor6, Doctor7, Doctor8
  select_item_events: sw_launch_active
  next_item_events: sw_right_flipper_inactive
  previous_item_events: sw_left_flipper_inactive
slide_player:
  carousel_Doctor1_highlighted: select_Doctor1
  carousel_Doctor2_highlighted: select_Doctor2
  carousel_Doctor3_highlighted: select_Doctor3
  carousel_Doctor4_highlighted: select_Doctor4
  carousel_Doctor5_highlighted: select_Doctor5
  carousel_Doctor6_highlighted: select_Doctor6
  carousel_Doctor7_highlighted: select_Doctor7
  carousel_Doctor8_highlighted: select_Doctor8
slides:
  select_Doctor1:
    widgets:
      - type: text
        text: Doctor 1
        font_size: 10
        color: yellow
    transitions:
      type: move_in
      direction: right
  select_Doctor2:
    widgets:
      - type: text
        text: Doctor 2
        font_size: 10
        color: yellow
    transitions:
      type: move_in
      direction: right
  select_Doctor3:
    widgets:
      - type: text
        text: Doctor 3
        font_size: 10
        color: yellow
    transitions:
      type: move_in
      direction: right
  select_Doctor4:
    widgets:
      - type: text
        text: Doctor 4
        font_size: 10
        color: yellow
    transitions:
      type: move_in
      direction: right
  select_Doctor5:
    widgets:
      - type: text
        text: Doctor 5
        font_size: 10
        color: yellow
    transitions:
      type: move_in
      direction: right
  select_Doctor6:
    widgets:
      - type: text
        text: Doctor 6
        font_size: 10
        color: yellow
    transitions:
      type: move_in
      direction: right
  select_Doctor7:
    widgets:
      - type: text
        text: Doctor 7
        font_size: 10
        color: yellow
    transitions:
      type: move_in
      direction: right
  select_Doctor8:
    widgets:
      - type: text
        text: Doctor 8
        font_size: 10
        color: yellow
    transitions:
      type: move_in
      direction: right
event_player:
  select_Doctor1: mode_Doctor_1_start
  select_Doctor2: mode_Doctor_2_start
  select_Doctor3: mode_Doctor_3_start
  select_Doctor4: mode_Doctor_4_start
  select_Doctor5: mode_Doctor_5_start
  select_Doctor6: mode_Doctor_6_start
  select_Doctor7: mode_Doctor_7_start
  select_Doctor8: mode_Doctor_8_start
##! test
#! start_game
#! advance_time_and_run .1
#! assert_available_balls_on_playfield 0
#! assert_text_on_top_slide "Doctor 1"
#! post sw_right_flipper_inactive
#! advance_time_and_run .1
#! assert_text_on_top_slide "Doctor 2"
#! post sw_launch_active
#! advance_time_and_run .1
#! assert_available_balls_on_playfield 1
```

Then, each mode that the carousel can start is set up with the
following.

``` yaml
#config_version=5
##! mode: Doctor_1
##Example:  Doctor_1.yaml
mode:
  start_events: carousel_Doctor1_selected
  stop_events: ball_ended
  priority: 130
##Then the rest of the mode's code.
```

Related How To guides:

* [How to design a game in MPF using Modes](../index.md)
