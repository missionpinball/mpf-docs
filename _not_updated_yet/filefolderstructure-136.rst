
When you download the latest `Mission Pinball Framework release from
GitHub`_ (click the *Source code* link in the "Downloads" section),
you'll get a file called *mpf-<branch>.zip* or *mpf-<branch>.tar.gz*,
(depending which link you click). When you unzip it you'll find a few
folders and files:


+ */mpf* (the main game framework)

    + */devices* (modules for different types of pinball hardware)
    + */media_controller* (our built-in media controller which handles the
      DMD, LCD windows, and audio)
    + */modes* (built-in modes for the game, attract, high score, credits,
      tilt, etc. You can extend, customize and/or replace these.)
    + */platform* (the hardware interface modules, for P-ROC, FAST, or
      virtual hardware)
    + */plugins* (default plugin modules that we include)
    + */system* (MPF game engine modules)
    + *mpfconfig.yaml* (holds the default and system configuration
      settings)

+ */machine_files* (contains sample game configurations. You'll put
  your own game files in a different location outside of MPF.)

    + */demo_man* (sample game config & code for our "`Demo Man`_" game)
    + */new_machine_template* (contains template files you can use to
      create your own game)
    + */tutorial* (contains configuration files from each step in our
      `getting started tutorial`_)

+ */tools* (contains helpful tools and utilities)
+ *mc.py* (the Python file you run to start the media controller which
  runs the DMD, LCD, and audio)
+ *mpf.py* (the python file you run to start your game)


Additional folders, such as */logs* will be automatically created
after you run your first game.

.. _Demo Man: https://missionpinball.com/blog/category/building-demo-man/
.. _getting started tutorial: /docs/tutorial
.. _Mission Pinball Framework release from GitHub: https://github.com/missionpinball/mpf/releases/latest


