
You can use the *random_event_player:* section of your config files to
cause a random event from a list to be posted when a specific event is
posted. This is very similar to the `event_player`_. If you add this
section to yourmachine-wide config file, the entries herewill always
be active. If you enter it into a mode-specific config file,
entrieswill only be active while that mode is active. This sectioncan
be used in your machine-wide config files. This sectioncanbe used in
mode-specific config files. Here's an example from Indiana Jones where
we use it to randomly advanced one of the top lane shots to light when
the skillshot starts:


::

    
    random_event_player:
      mode_skillshot_started:
        - indy_i_advance
        - indy_n_advance
        - indy_d_advance
        - indy_y_advance


The random event player is very basic. One of the events from the list
will be chosen and posted at random when the event entry above it is
posted.

.. _event_player: https://missionpinball.com/docs/configuration-file-reference/event_player/


