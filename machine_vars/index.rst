Machine Variables
=================

MPF uses the concept of *machine variables* to track dynamically-
created variables that apply on a machine-wide basis. Machine
variables are similar in concept to :doc:`player variables </game_logic/players/index>`,
except machine variables are machine-wide instead of per-player.
Examples of things that are stored in machine variables include:

* The number of credits on the machine (if you're using the credits
  mode and not set to free play)
* The scores of the last game played (which are typically shown in the
  attract mode display loop)
* The names and scores of the high scores (which are also shown in the
  attract mode display loop and in the "status" screen when a player
  holds a flipper button in during a game).

Machine variables can be set to ``persist``, meaning they are saved to
disk and available to MPF the next time it boots up. (For example, if
you first turn on a pinball machine, it will still show the scores of
the last game played in the attract mode.) These machine variables are
stored in the ``<your_machine_folder>/data/machine_vars.yaml`` file.
Machine variables that are saved to disk can optionally be written
with an expiration time which means they're cleared out if MPF boots
after the time has passed. (For example, the number of credits on the
machine might only persist for a few hours.)

Like player variables, you can use machine variables in your config files,
particularly in text display widgets, to show things on your display.

You can create your own machine variables in your configs. There are also
several machine variables that are automatically created. Here's a list of
the machine variables that are "built in" and available for use in your
configs:

.. toctree::
   :maxdepth: 1

   credit_units <credit_units>
   credits_numerator <credits_numerator>
   credits_string <credits_string>
   credits_value <credits_value>
   credits_whole_num <credits_whole_num>
   credits_whole_num <credits_whole_num>
   fast_(x)_firmware <fast_x_firmware>
   fast_(x)_model <fast_x_model>
   (high_score_category)(position)_label <high_score_categoryposition_label>
   (high_score_category)(position)_name <high_score_categoryposition_name>
   (high_score_category)(position)_value <high_score_categoryposition_value>
   lisy_api_version <lisy_api_version>
   lisy_hardware <lisy_hardware>
   lisy_version <lisy_version>
   mc_extended_version <mc_extended_version>
   mc_version <mc_version>
   mpf_extended_version <mpf_extended_version>
   mpf_version <mpf_version>
   p_roc_hardware_version <p_roc_hardware_version>
   p_roc_revision <p_roc_revision>
   p_roc_version <p_roc_version>
   platform <platform>
   platform_machine <platform_machine>
   platform_release <platform_release>
   platform_system <platform_system>
   platform_version <platform_version>
   player(x)_score <playerx_score>
   python_version <python_version>


Related Events
--------------

.. include:: /events/include_machine_vars.rst
