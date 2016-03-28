
The `info_lights:` section of the configuration file allows you to
configure the `Info Lights`_ plugin to automatically set "status"
lights based on different things that are happening in the game. This
is very common in EM and older solid statemachines, since they uses
lights to tell you things like which player is up, what ball you're
on, etc. This sectioncan be used in your machine-wide config files.
This section *cannot* be used in mode-specific config files. Here's an
example `info_lights:` section froma machine configuration file:


::

    
    info_lights:
        match_00:
            light: match00
        match_10:
            light: match10
        match_20:
            light: match20
        match_30:
            light: match30
        match_40:
            light: match40
        match_50:
            light: match50
        match_60:
            light: match60
        match_70:
            light: match70
        match_80:
            light: match80
        match_90:
            light: match90
        ball_1:
            light: bip1
        ball_2:
            light: bip2
        ball_3:
            light: bip3
        ball_4:
            light: bip4
        ball_5:
            light: bip5
        player_1:
            light: player1
        player_2:
            light: player2
        tilt:
            light: tilt
        game_over:
            light: gameOver


The way info lights work is pretty simple. There are sub-sections that
represent different lights that may be in your machine, and then under
each of them you map them to the name of the light.



match_ *xx*:
------------

This section is for the match lights, with the "xx" replaced with the
number of the match light. In the example configuration above, the
machine has match lights that count up by tens (10, 20, 30...) which
is why the match_xx entries here are `match_10`, `match_20`,
`match_30`... If your machine matches by the ones digit, then you'd
enter these items at `match_1`, `match_2`, etc. The `light:`entry in
each of these is the light name from the `matrixlights:`section of
your config file.



ball_ *x*:
----------

This maps the ball-in-play number to the light.



player_ *x*:
------------

This maps the current player to the number in the light. This plugin
turns on each light when a new player joins a game. So it doesn't show
which player is up, rather, if you have a two-player game then both
the `player_1`and `player_2`lights are lit. (So how does a player know
that it's his turn? That's handled by the score reel lights.)



tilt:
-----

Turns this light on when the machine tilts.



game_over:
----------

Flashes this light when a game is not in progress at a rate of 1/2 sec
on, 1/2 sec off. This plugin is pretty basic, but it should meet the
needs for EM machines. Right now it only works with Matrix Lights, so
if you need it for LEDs then post a request to the forum and we can
change it. (Should be pretty simple.)

.. _Info Lights: https://missionpinball.com/docs/plugins/info-lights/


