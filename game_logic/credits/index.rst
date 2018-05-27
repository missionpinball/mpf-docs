Coins & Credits
===============

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/credits`                                                       |
+------------------------------------------------------------------------------+

MPF contains support for "coins & credits" which basically means you can configure
your machine to require money to play.

The credits system has several features and options, including:

+ Configuration of different coin/price values per coin switch.
+ Tracking money and/or tokens.
+ Set price tiers (1 credit for 50 cents, 5 credits for 2 dollars,
  etc.)
+ Specify max credits and credit expiration times
+ Retain credits even when the machine is powered off
+ Get access to a "credits string" machine variable that will show the
  number of credits (or configurable free play text) for use on your
  display.
+ Flexible events you can use to show display items based on credits
  being added, insert coin messages, max credits reached, etc.

This is an example:

.. code-block:: mpf-config

   switches:
       s_coin_left:
           number:
       s_service_coin:
           number:

   credits:
       max_credits: 12
       free_play: False
       service_credits_switch: s_service_coin
       switches:
           - switch: s_coin_left
             type: money
             value: .25
       pricing_tiers:
           - price: .50
             credits: 1
           - price: 2
             credits: 5
       fractional_credit_expiration_time: 15m
       credit_expiration_time: 2h
       persist_credits_while_off_time: 1h
       free_play_string: FREE PLAY
       credits_string: CREDITS

   ##! mode: attract
   # in modes/attract/config/attract.yaml
   # add credits string to your attract show
   show_player:
       mode_attract_started:
           attract_display_loop
   shows:
       attract_display_loop:
           - duration: 2s
             slides:
               press_start:
                 target: dmd
                 widgets:
                 - type: Text
                   text: PRESS START
                 transition:
                    type: move_in
                    duration: 1s
                    direction: top
           - duration: 2s
             slides:
               credits_slide:
                 target: dmd
                 widgets:
                 - type: text
                   text: (machine|credits_string)
                 transition:
                    type: move_in
                    duration: 1s
                    direction: bottom

   ##! mode: credits
   # in modes/credits/config/credits.yaml
   # add some credits slides
   slide_player:
       credits_added:
           credit_added_slide:
               expire: 2s
       not_enough_credits:
           not_enough_credits_slide:
               expire: 2s
       enabling_free_play:
           enabling_free_play_slide:
               expire: 2s
       enabling_credit_play:
           enabling_credit_play_slide:
               expire: 2s
       max_credits_reached:
           max_credits_reached_slide:
               expire: 2s

   slides:
       credit_added_slide:
           - type: text
             text: (machine|credits_string)
       not_enough_credits_slide:
           - type: text
             text: (machine|credits_string)
           - type: text
             text: INSERT COINS
       enabling_free_play_slide:
           - type: text
             text: ENABLING FREE PLAY
       enabling_credit_play_slide:
           - type: text
             text: ENABLING CREDIT PLAY
           - type: text
             text: (machine|credits_string)
       max_credits_reached_slide:
           - type: text
             text: MAX CREDITS REACHED

   ##! test
   #! assert_machine_variable 0 credit_units
   #! hit_and_release_switch s_coin_left
   #! hit_and_release_switch s_coin_left
   #! assert_machine_variable 2 credit_units
   #! start_game
   #! assert_machine_variable 0 credit_units

A game will always cost 1 credit per player.
In this example, 50ct will give you 1 credit and $2 will give you 5 credits.
When ``s_coin_left`` is hit 25ct are added (or 1/2 credit).

+------------------------------------------------------------------------------+
| Related How To guides                                                        |
+==============================================================================+
| :doc:`/game_design/index`                                                    |
+------------------------------------------------------------------------------+


+------------------------------------------------------------------------------+
| Machine Variables                                                            |
+==============================================================================+
| :doc:`/machine_vars/credit_units`                                            |
+------------------------------------------------------------------------------+
| :doc:`/machine_vars/credits_numerator`                                       |
+------------------------------------------------------------------------------+
| :doc:`/machine_vars/credits_string`                                          |
+------------------------------------------------------------------------------+
| :doc:`/machine_vars/credits_value`                                           |
+------------------------------------------------------------------------------+
| :doc:`/machine_vars/credits_whole_num`                                       |
+------------------------------------------------------------------------------+


+------------------------------------------------------------------------------+
| Related Events                                                               |
+==============================================================================+
| :doc:`/events/credits_added`                                                 |
+------------------------------------------------------------------------------+
| :doc:`/events/enabling_credit_play`                                          |
+------------------------------------------------------------------------------+
| :doc:`/events/enabling_free_play`                                            |
+------------------------------------------------------------------------------+
| :doc:`/events/max_credits_reached`                                           |
+------------------------------------------------------------------------------+
| :doc:`/events/not_enough_credits`                                            |
+------------------------------------------------------------------------------+
