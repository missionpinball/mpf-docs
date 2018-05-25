Carousel
============

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/examples/carousel/index`                                              |
+------------------------------------------------------------------------------+

.. versionchanged:: 0.33

.. contents::
   :local:

A carousel allows you to create process for the player to select from a list
of items such as selecting a mode to play.
The carousel is implemented as a mode.
The player can move through a list of items that you provide on the display
or cycle through playfield inserts.

This is just one way to select modes. More ways to implement mode selection
are described in the :doc:`mode selection section </game_design/mode_selection>`
of the :doc:`game design documentation </game_design/index>`.

A common use of the carousel is to create a mode selection process.
For example, the player can scroll through a list of modes on the display.
Each mode could be presented to the user as a slide.
The player can move from slide to slide using the flippers.
Once the player decides which mode to play, he can select the mode by hitting
the start button or both flippers at once.
This is just one example of how you could implement a carousel as a mode
selection process.

There is a reference to a code file in here so be careful to include that
reference.
You don't need to download any code as it is already in you MPF installation.
Here is the process of configuring a carousel:

* Create a mode folder and config file ``<machine>/modes/carousel/config/carousel.yaml``
* Add the code to ``mode:`` section:

.. code-block:: yaml

    code: mpf.modes.carousel.code.carousel.Carousel

* Create your selectable items.  These could be your mode names but you can name them anything for now.

.. code-block:: yaml

   selectable_items: terra, pyro, space, liquid

* Select the event(s) that choose the item.  For example, the start button. You could think of this an the "enter key"

.. code-block:: yaml

   select_item_events: s_start_active

* Select the event that moves to the next item in the list of items

.. code-block:: yaml

  next_item_events: s_right_flipper_active

* Select the event that moves back to the previous item in the list of items

.. code-block:: yaml

   previous_item_events: s_left_flipper_active


There are two events of importance here:

* carousel_<item>_highlighted
* carousel_<item>_selected

You can use the carousel_<item>_highlighted event to display a slide showing the name of the mode to the player.

You can then use the carousel_<item>_selected event to start the mode that was selected by the player.

.. code-block:: mpf-config

  ##! mode: my_carousel
  #config_version=5
  mode:
    start_events: ball_starting
    stop_events: carousel_terra_selected  # not sure what event to use here????
    code: mpf.modes.carousel.code.carousel.Carousel

  mode_settings:
    selectable_items: terra, pyro, space, liquid
    select_item_events: s_start_active
    next_item_events: s_right_flipper_active
    previous_item_events: s_left_flipper_active

  slide_player:
    carousel_terra_highlighted: select_terra
    carousel_liquid_highlighted: select_liquid
    carousel_space_highlighted: select_space
    carousel_pyro_highlighted: select_pyro

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
