
The *auditor:* section of the machine configuration file lets you
control what events the `auditor module`_ audits. This sectioncan be
used in your machine-wide config files. This section *cannot* be used
in mode-specific config files. Here's an example which is the settings
we including in the default *mpfconfig.yaml* file. (So these are the
settings that are included by default with every game you run.) Also,
by default, the auditor saves its audits to */audits/audits.yaml*
inthe folder for each machine. (Check out the `documentation on the
Auditor`_ to see a sample audit log file.)


::

    
    auditor:
        save_events:
            ball_ended
            game_ended
        audit:
            shots
            switches
            events
            player
        events:
            ball_search_begin
            machine_init_phase_1
            game_started
            game_ended
            machine_reset
        player:
            score
        num_player_top_records: 10




save_events
~~~~~~~~~~~

A list of events trigger the auditor to update the audit file on disk.
We include *ball_ended*so we write out the audits after each ball, and
also *game_ended*so we capture the final scores of each player.



audit
~~~~~

This is a listof the various types of things you want to include in
your audit file. There are currently four options:


+ shots - tracks the number of times each shot has been made
+ switches - tracks the number of times each switch has been hit.
+ events - whether the auditor should audit certain events. (Add the
  events you want to track to the *events* section.)
+ player - includes player variables (score, maybe shots or goals
  they've achieved, etc.) See the *player* section below for details.




events
~~~~~~

A list of which events you want to audit. These are the names of any
events you want.



player
~~~~~~

This is a list of player variables you want to track. The auditor will
save a certain number (configurable via the
*num_player_top_records:*setting), as well as the total number of
entries and the current average.



num_player_top_records
~~~~~~~~~~~~~~~~~~~~~~

For player-specific variables, you have the option of track the "top"
number of each. So in the example above, since the only player item is
*score*, the auditor will track the top 10 highest scores, plus the
total count and the overall average.

.. _documentation on the Auditor: https://missionpinball.com/docs/mpf-core-architecture/plugins/auditor/


