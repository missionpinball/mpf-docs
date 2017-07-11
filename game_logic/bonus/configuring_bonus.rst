How to configure End of Ball Bonus
==================================

This guide walks you through configuring an end-of-ball Bonus mode in MPF.

1. Add the bonus mode to your machine's list of modes
-----------------------------------------------------

MPF contains a built-in bonus mode that you can use which should contain
everything you need. To use it, first simply add ``- bonus`` to your
machine config's ``modes:`` section, like this:

.. code-block:: yaml

   #config_version=5

   modes:
      - base
      - some_other_modes
      - jackpot
      - credits
      - tilt
      - bonus  # just add bonus to this list, don't forget the dash

The bonus mode is automatically configured to start when the ball ends (as
long as the machine is not tilted), running at priority 500.

2. Create your bonus mode folders
---------------------------------

Even though the bonus mode is built-in, you'll still need to add a ``bonus``
folder to your machine's *modes* folder. Then in there, add a ``config``
folder, and finally, create a file in the config folder called ``bonus.yaml``.
(So this is just like any other mode so far.)

It should look something like this:

.. image:: /game_logic/images/bonus_folder.png

3. Add the bonus mode to your machine-wide modes list
-----------------------------------------------------

Remember that when you create a new mode, you need to add it to the ``modes:``
section of your machine-wide config. (Why doesn't MPF just automatically
detect modes based on what folders it finds? Because you might want to have
different sets of configs that use different modes, or you might want to
disable a mode you're testing, etc.)

So just add ``- bonus`` to the list of modes in the ``modes:`` section of your
machine-wide config, like this:

.. code-block:: yaml

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

4. Think about what you want to score bonus on
----------------------------------------------

Most modern pinball machines have bonus scores based on multiple things.

TODO finish this....

4. Add some settings to your bonus mode config
----------------------------------------------

Now go back into your bonus mode folder open up ``bonus.yaml`` config file
(which should be empty at this point), and enter a basic config:

.. code-block:: yaml

   #config_version=5

   mode_settings:
      bonus_entries:


TODO
