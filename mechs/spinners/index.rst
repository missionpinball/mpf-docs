Spinners
========

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/switches`                                                      |
+------------------------------------------------------------------------------+

Spinners are rotating metal plates which close a switch once per rotation.

Hardware
--------

.. image:: /mechs/images/spinner.jpg

Part numbers:

 * Stern: #511-5113-00 or #100-0014-00

Config
------

In MPF spinners are configured just like normal switches:

.. code-block:: mpf-config

   switches:
     s_my_spinner:
       number: 42    # number depends on your platform

It is very common to count the rotations of your spinner per player.
You can eiher use a player variable or a counter for that.
This is an example:

.. code-block:: mpf-config

   switches:
     s_my_spinner:
       number: 42   # number depends on your platform
   ##! mode: my_mode
   # in your base mode add 1 for every rotation to a player variable which you can use in slides
   variable_player:
     s_my_spinner_active:
       spinner_rotations: 1
   # in a game mode the player needs to spin the spinner 10 times
   counters:
     spinner_rotations:
       count_events: s_my_spinner_active
       count_complete_value: 10
       events_when_complete: mode_finished
   ##! test
   #! start_game
   #! start_mode my_mode
   #! hit_and_release_switch s_my_spinner
   #! mock_event mode_finished
   #! assert_player_variable 1 spinner_rotations
   #! hit_and_release_switch s_my_spinner
   #! hit_and_release_switch s_my_spinner
   #! hit_and_release_switch s_my_spinner
   #! hit_and_release_switch s_my_spinner
   #! hit_and_release_switch s_my_spinner
   #! hit_and_release_switch s_my_spinner
   #! hit_and_release_switch s_my_spinner
   #! hit_and_release_switch s_my_spinner
   #! assert_event_not_called mode_finished
   #! hit_and_release_switch s_my_spinner
   #! assert_event_called mode_finished
   #! assert_player_variable 10 spinner_rotations

