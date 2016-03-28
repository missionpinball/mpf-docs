
The `show_player:` section of your configuration file is used to
automatically play and stop shows based on different `MPF
events`_.(Remember that Shows are YAML files that contain synchronized
sequences of lights, display slides, sounds, events, and coil actions.
More information is available in the `Shows`_ section of this
documentation.) This sectioncan be used in your machine-wide config
files. This sectioncan be used in your mode-specific config files.
Here's an example


::

    
    show_player:
        attract_start:
          - show: random_blinking
            repeat: yes
            tocks_per_sec: 4
          - show: attract_display
            repeat: yes
            tocks_per_sec: 1
    
        attract_stop:
          - show: random_blinking
            action: stop
          - show: attract_display
            action: stop
    
        shot_jackpot:
            show: jackpot
            tocks_per_sec: 30


To configure shows to automatically play and stop, you create a
`show_player:` entry in your config file. Then create a sub-entry for
each MPF event where you'd like (one or more) shows to play or stop.
If you want to enter more than one show for each event, you have to
`enter them as a list`_. The easiest way to do that is to add a dash
("-") and a space before each show entry while keeping them at the
same level of indentation. (See the `attract_start:` section in the
example. Notice there are two sub-entries, one which starts with `-
show: random_blinking`, and one which starts with `- show:
attract_display`. Notice that you can enter any settings for shows you
want, including `repeat`, `priority`, `blend`, `hold`,
`tocks_per_sec`, `start_location`, and `num_repeats`. See the
documentation on `playing shows`_ for details. If you want to an event
to stop a show, add an setting `action: stop`, as shown in the example
above in the a `ttract_stop`: entry. Stopping a show can also take
settings `reset` and `hold`. If you add a ShowPlayer: section to a
mode-specific config files, shows that are playing as part of that
mode are automatically stopped when the mode ends.

.. _MPF events: https://missionpinball.com/docs/events/
.. _Shows: https://missionpinball.com/docs/shows/
.. _playing shows: https://missionpinball.com/docs/shows/playing-shows/
.. _enter them as a list: https://missionpinball.com/docs/configuration-file-reference/adding-lists-and-lists-of-lists-to-config-files/


