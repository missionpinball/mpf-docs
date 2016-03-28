
The `scoring:` section of the configuration files lets you increase
(or decrease) the value of a `tracked player variable`_ when some
event takes place. In most cases, you'll use the scoring section to
add a value to the player's score variable, but technically this
section can be used to add to any player variable. (So if you're
tracking the total number of loops a player gets via a player variable
called loops, you would use the scoring section to increase the value
of the loops player variable by one whenever a loop is made.) See the
`documentation on the Score Controller`_ for more details on this.
This section *cannot* be used in your machine-wide config files. This
section *can* be used in mode-specific config files. Here's an example
scoring section:


::

    
    scoring:
        inlane_hit:
            score: 1070
        outlane_hit:
            score: 930
        sw_playfield_active:
            score: 10
            total_switches: 1
        right_ramp_made:
            score: 1000000|block
            ramps: 1


Inside your scoring section, there are basically only two things you
have to configure:



<event_name>:
~~~~~~~~~~~~~

In your `scoring:` section, create an sub-entry for each event that
you'd like to use to trigger a player variable to change value.



<player_variable>:
~~~~~~~~~~~~~~~~~~

Then under each event_name: entry, create a sub-entry for one or more
player variables and add the numeric value you'd like added to (or
subtracted from) that player variable. For example:


::

    
    scoring:
        outlane_hit:
            score: 930


In the example above, whenever the event *outline_hit* is posted, the
player variable called *score* will be increased by 930.


::

    
    scoring:
        sw_playfield_active:
            score: 10
            total_switches: 1


In the example above, whenever the event *sw_playfield_active* is
posted, the player variable called *score* will be increased by 10,
and the player variable *total_switches* will be increased by 1. Note
that you can have as many player variables listed for an event as you
want, and you can also enter negative values if you want that event to
subtract from the associated player variable.



Blocking score events in lower-priority modes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The scoring: section of your config file is a mode-based configuration
setting. This means that you'll likely have scoring: sections in most
(if not all) of your modes, and each mode's scoring: section will
contain the scoring-related configuration for that mode only. (It also
means that the scoring events you enter are only processed if the mode
whose config they're in is running.) There are situations where you
might want a scoring event from one more to block a scoring entry from
a lower-priority mode. For example, you might have scoring for your
pop bumpers set to 75,000 in your base mode. But after 50 pop bumper
hits, you might want to enable a super jets mode where each shot to a
pop bumper is worth 1,000,000 points instead. If you just entered
score: 1000000 in your super jets mode config, then each pop bumper
hit would actually be worth 1,075,000 points since the scoring entry
would be processed by both your base and your super jets modes. To
address this, you can add |block to the end of a scoring entry. Doing
so will prevent that event from affecting that player variable in a
lower priority mode. For example, if you have this config in your base
mode:


::

    
    scoring:
        pop_bumper_hit:
            score: 75000
            total_pops: 1


And then this config in your super jets mode:


::

    
    scoring:
        pop_bumper_hit:
            score: 1000000|block


Now when your super jets mode is active, the super jets scoring of
1000000 will be added and it will prevent the *score: 75000* from the
base more from being added. Note that this *block* configuration is
player variable-specific, so in the above configuration example, the
base mode's *total_pops* value will still be increased by one when the
super jets mode is active since the super jets *scoring* config was
only set to block the *score*, not the *total_pops*.



Mode-based scoring
------------------

Whenever a tracked player variable changes (which is what player
variables in the scoring section of your config create), an event is
posted with the details of the change. You can use this to show slides
based on the new score or the score change. See the `score controller
documentation`_ for details. Also since all scoring is done in mode-
based configurations, the score controller also tracks the total
change of each player variable in a mode and posts mode-specific
scoring events. (This means you can set a mode that, for example, ends
when you get a certain number of points in that mode. Or you can base
bonus scores on specific score values achieved in modes.) Again see
the `score controller documentation`_ for details.

.. _score controller documentation: https://missionpinball.com/docs/mpf-core-architecture/system-modules/score-controller/
.. _tracked player variable: https://missionpinball.com/docs/mpf-core-architecture/player-management/


