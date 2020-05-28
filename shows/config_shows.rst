Creating shows in config files
==============================

In addition to being able to :doc:`create standalone show files </shows/file_shows>`, MPF also lets you define your shows right
in-line in your config files.

You can do this in the ``shows:`` section of a config file. (This can be done in a mode-based config or in your
machine-wide config).

The actual format for a show in a config file is identical to the format of a standalone show file on disk.
Basically you add a ``shows:`` section to a config, create sub-sections based on show name, and then add normal
show items to the config. For example:

.. code-block:: mpf-config

   shows:
     flash_red:
       - time: 0
         lights:
           led1: red
       - time: +1
         lights:
           led1: off
       - time: +1
     blue_green_cycle:
       - time: 0
         lights:
           led2: blue
       - time: +1
         lights:
           led2: green
       - time: +1

The section above contains two shows: *flash_red* and *blue_green_cycle*.

Shows in files versus shows in configs
--------------------------------------

Now that you see it's possible to create shows as standalone YAML files in your *shows* folder and also in a *shows:*
section of a config file, you're probably wondering what the difference is and when you should use one versus the
other?

The answer is pretty simple: There is no difference.

When MPF boots up, it creates the shows objects from your show files and the show sections from configs. But once those
shows are created, they are identical. No difference whatsoever. So really you can uses whichever format you want (or
mix and match them). We typically create bigger and more complex shows as their own YAML files, and smaller, simpler
shows in-line in the machine or mode config. But again, it really doesn't matter.

The only real difference is that if you load shows from YAML files, you can dynamically load and unload shows throughout
the lifespan of MPF. (For example, you might configure it so a mode loads the shows it needs into memory when the mode
starts, and then unloads them when the mode ends.) If you have lots and lots of shows and not very much memory, this
could help conserve memory since shows are only loaded when they're needed. That said, individual shows don't take up
too much memory (certainly far less than sounds and images), so in most cases this is probably moot.

One "gotcha" to keep in mind is that MPF maintains a global list of shows, so you can't have the same show name twice
(even if one is loaded from a show file and one is in a config file). If you do this, then whichever show you load
last will be overwrite the previous one, and you'll be confused.
