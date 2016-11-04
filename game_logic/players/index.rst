Player Variables
================

+------------------------------------------------------------------------------+
| Related Config File sections                                                 |
+==============================================================================+
| :doc:`/config/player_vars`                                                   |
+------------------------------------------------------------------------------+

MPF contains lots of features which make working with players easy.

Each player has "player variables" which are names and values that are stored
separately for each player.

Some simple examples of player variables include things like:

* ``number``: The player's number (1, 2, etc.)
* ``score``: The player's current score

You can create your own player variables which can be called anything you want
and can store anything you want. So you can use them to track player's progress
through the game, how many loops they've made, how many pop bumper hits they
have, etc.

MPF also uses player variables to keep track of all the other game logic
elements that are tracked on a per-player basis, like achievement status,
logic block states, extra balls, bonus, etc.

+------------------------------------------------------------------------------+
| Related How To Guides                                                        |
+==============================================================================+
| TODO                                                                         |
+------------------------------------------------------------------------------+

+------------------------------------------------------------------------------+
| Related Events                                                               |
+==============================================================================+
| :doc:`/events/player_var_name`                                               |
+------------------------------------------------------------------------------+
| :doc:`/events/player_add_request`                                            |
+------------------------------------------------------------------------------+
| :doc:`/events/player_add_success`                                            |
+------------------------------------------------------------------------------+
| :doc:`/events/player_turn_start`                                             |
+------------------------------------------------------------------------------+
| :doc:`/events/ball_save_name_saving_ball`                                    |
+------------------------------------------------------------------------------+
| :doc:`/events/player_turn_stop`                                              |
+------------------------------------------------------------------------------+
| :doc:`/events/multi_player_ball_started`                                     |
+------------------------------------------------------------------------------+
| :doc:`/events/single_player_ball_started`                                    |
+------------------------------------------------------------------------------+
