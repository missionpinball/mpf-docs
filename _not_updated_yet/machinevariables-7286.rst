
MPF uses the concept of *machine variables* to track dynamically-
created variables that apply on a machine-wide basis. Machine
variables are similar in concept to `tracked player variables`_,
except machine variables are machine-wide instead of per-player.
Examples of things that are stored in machine variables include:


+ The number of credits on the machine (if you're using the credits
  mode and not set to free play)
+ The scores of the last game played (which are typically shown in the
  attract mode display loop)
+ The names and scores of the high scores (which are also shown in the
  attract mode display loop and in the "status" screen when a player
  holds a flipper button in during a game).


Machine variables can be set to "persist", meaning they are saved to
disk and available to MPF the next time it boots up. (For example, if
you first turn on a pinball machine, it will still show the scores of
the last game played in the attract mode.) These machine variables are
stored in the *<your_machine_folder>/data/machine_vars.yaml* file.
Machine variables that are saved to disk can optionally be written
with an expiration time which means they're cleared out if MPF boots
after the time has passed. (For example, the number of credits on the
machine might only persist for a few hours.)

.. _tracked player variables: https://missionpinball.com/docs/mpf-core-architecture/player-management/


