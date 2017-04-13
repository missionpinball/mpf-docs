Machine Variables
=================

Machine variables are similar to
:doc:`player variables </game_logic/players/index>`, except that
machine variables are machine-wide and persist between games. (In fact,
machine variables can be configured to be saved to disk so they also persist
between reboots of MPF.)

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
   mpf_extended_version <mpf_extended_version>
   mpf_version <mpf_version>
   p_roc_revision <p_roc_revision>
   p_roc_version <p_roc_version>
   platform <platform>
   platform_machine <platform_machine>
   platform_release <platform_release>
   platform_system <platform_system>
   platform_version <platform_version>
   player(x)_score <playerx_score>
   python_version <python_version>
