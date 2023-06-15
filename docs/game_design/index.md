---
title: How to design a game in MPF using Modes
---

# How to design a game in MPF using Modes


This section assumes that you already configured all your hardware
devices (especially all your
[ball device](../config/ball_devices.md)). If
you did not configure your hardware please do that first. You can go
through the [tutorial](../tutorial/index.md)
or have a look a the [mechs section](../mechs/index.md).

Video about how to structure your modes:

<div class="video-wrapper">
<iframe width="560" height="315" src="https://www.youtube.com/embed/JLgeGBc03bM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

Video about
[state machines](../game_logic/logic_blocks/state_machines.md) (often used to implement logic in your mode):

<div class="video-wrapper">
<iframe width="560" height="315" src="https://www.youtube.com/embed/qakxTF1H57E" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

Video about events in MPF:

<div class="video-wrapper">
<iframe width="560" height="315" src="https://www.youtube.com/embed/G3UbVP8gFU0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

This section is about laying out your modes and actually designing your
game logic. It is structured into the following subsections:

## Mode Selection and Game Startup

Questions answered in this section:

* How to select modes/players during start?
* How to implement a (timed) skill shot?
* How does a player qualify for a mode?
* How to start the mode?
* Can multiple modes run at once?

* [Mode Selection](mode_selection.md)

## Game Mode

Questions answered in this section:

* How to track progress inside a mode?
* How does it end?
* Will it always succeed?
* Can it timeout?
* Can it restart if it failed?
* Where will it continue on restart?
* How to implement roll over lanes in a mode?
* How to implement a mystery award mode?
* How to implement a stand-up target bank mode?

* [Game Mode](../game_design/index.md)

## Wizard Modes

Questions answered in this section:

* How to track achievements towards one or multiple wizard modes?
* How to start a wizard mode?
* What to do after wizard mode?

* [Wizard Modes](wizard_modes.md)

## Ball End Modes

Questions answered in this section:

* How to start a mode after the ball for a player drained?
* How to implement a bonus mode?

* [Ball End Modes](ball_end_modes.md)

## Game End Modes

Questions answered in this section:

* How to start a mode after the last player drain his ball?
* How to implement a highscore mode?
* How to implement a match mode?

* [Game End Modes](game_end_modes.md)

## Other modes

Questions answered in this section:

* Which modes run outside of a game?
* How to control attract?
* How do credits work?
* How does tilt work?
* What is the service mode?

* [Other Modes](other_modes.md)

## Layering Modes Example

Examples given in this section:

* How to define mode categories and helper modes
* How to move in and out of game and wizard modes
* How to track and persist progress outside of modes

* [Layering Modes Example](mode_layering.md)
