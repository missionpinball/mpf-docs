
The `game:` section of the configuration files holds settings related
to the game play. This sectioncan be used in your machine-wide config
files. This section *cannot* be used in mode-specific config files.
This list is very incomplete, but here's what's implemented now:


::

    
    game:
        balls_per_game: 3
        max_players: 4




balls_per_game:
~~~~~~~~~~~~~~~

How many balls the game is. Typically it's 3 or 3 but it can be
anything. The framework doesn't care.



max_players:
~~~~~~~~~~~~

Typically this is 4, but the core framework doesn't care what this
number is. (When we get to adding the display support, we'll probably
have to deal with certain limits, but for now it doesn't matter.)
start_game_switch_tag: add_player_switch_tag:



