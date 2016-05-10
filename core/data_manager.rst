Data manager
============

*MPF Module*

The MPF Data Manager is used to load and save data to files on disk.
it lives in the *mpf/core/data_manager.py* module.

There are many different types of data that are written to disk,
including audits, configurations, high scores, credits, and anything
else that MPF needs to "persist" when MPF is not running. The data
manager provides a centralized service for reading and writing data
which is used by several components of MPF. By default, machine-
specific data is saves in the ``<machine_folder>/data`` location. The
current data files you'll find are:

+ audits.yaml (audits)
+ earnings.yaml (earnings, if you're using the credits mode and your
  machine is not set to free play)
+ high_scores.yaml (high score names and values)
+ machine_vars.yaml (machine variables that are set to persist, including the scores of the last game played)
