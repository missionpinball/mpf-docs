---
title: Welcome to The Mission Pinball Framework!
---

# The Mission Pinball Framework (MPF) 0.57

*Open source software for powering real pinball machines!*

The **Mission Pinball Framework** (MPF) is a free Python-based pinball software
framework that's used to run real pinball machines. It's compatible with
virtually all modern pinball controllers and machines, and it's the most feature
complete pinball software environment you'll find.

MPF is a complete pinball software package which runs on a computer inside
your pinball machine. (It can run on Windows, Mac, Linux, or Raspberry Pi.)
MPF controls all the electronics in the machine,
including the lights, the solenoids (the things that make the balls move),
the DMD if your machine has one, the LCD if your machine has one, the
switches, and the motors. MPF uses simple configuration files to control
the game logic, sounds, videos, effects, and everything else you need to create
the rules for your game, including modes, multiballs, ball saves, scoring, and more.

MPF has been around since 2014, and it's been used to power hundreds of
homebrew pinball machines and a few commercially-released ones. It's
created by volunteers in their spare time.

Join in!

## Features

* Works with many modern pinball control systems, including FAST Pinball, CobraPin, P3-ROC, and many more.
* Runs on Windows, Mac, Linux, and Raspberry Pi.
* Supports many types of pinball machines, including solid state, EM, and custom homebrew machines.
* Built-in support for many types of pinball mechs, including flippers, pop bumpers, slingshots, drop targets, spinners, and more. (See the [complete list](mechs/index.md).)
* Supports many types of pinball displays, including DMDs, LCDs, segments, and mechanical score reels.
* Pinball logic built in for player management, game modes, multiballs, ball saves, tilt, shots, and more. (See the [complete list](game_logic/index.md).)
* Build your game with simple configuration files. (But you can also mix in your own custom code too, use as much or little of the config files as you want.)
* 100% open source and completely free to use.

See the [Features](start/features.md) page for a complete list of features.

[Installation Instructions](install/index.md){ .md-button } [Read the Tutorial](tutorial/index.md){ .md-button }

## Getting Started

What MPF is, how it works, how to install it, how to use it.

  * [How MPF works](start/index.md)
  * [Features](start/features.md)
  * [Installation](install/index.md)
  * [The MPF "Media Controller"](start/media_controller.md)
  * [Understanding MPF config files](start/config_files.md)
  * [Config files versus "real" programming](start/dsl_vs_programming.md)
  * [Troubleshooting](troubleshooting/index.md)
  * [Running MPF](running/index.md)

## Hardware

Pinball machines, control systems, and pinball mechs.

  * [Working with real pinball machines](machines/index.md)
  * [Pinball Controllers](hardware/pinball_controllers.md)
  * [Physical Machine Building](physical_building/index.md)

## Game Programming

  * [Tutorial](tutorial/index.md)
  * [Pinball Mechs](mechs/index.md)
  * [Game Elements](game_logic/index.md)
  * [Modes](game_design/index.md)
  * [Machine Management](machine_management/index.md)
  * [Testing](testing/index.md)
  * [Finalization](finalization/index.md)
  * [Cookbook](cookbook/index.md)
  * [Flowcharts](flowcharts/index.md)

## Media Controller(s)

  * [Media Controller](mc/displays/index.md)
  * [Displays](mc/displays/index.md)
  * [Slides](mc/slides/index.md)
  * [Widgets](mc/widgets/index.md)
  * [Sound & Audio](mc/sound/index.md)

## Tools

See the [Tools page](tools/index.md) for links to several tools that help you
work with MPF, including the [MPF Monitor](tools/monitor/index.md), a visual utility
that connects to a live running instance of MPF and shows you the stream of events,
device state, player variables, etc.

## Reference

  * [Machine Variables](machine_vars/index.md)
  * [Events](events/index.md)
  * [Config File Reference](config/index.md)
  * [Player Variables](player_vars/index.md)
  * [Game Variables](game_vars/index.md)
  * [Config Players](config_players/index.md)
  * [Assets](assets/index.md)
  * [Shows](shows/index.md)
  * [MPF Errors from Log Files](logs/index.md)
  * [Example Games](examples/index.md)

## Projects built on MPF

* [List of pinball machine projects running on MPF](showcase/index.md)
* [Add your machine to the list!](showcase/_add_yours.md)

## Community

* [Community](community/index.md)
* [MPF Users Google Group](https://groups.google.com/forum/#!forum/mpf-users)
* [MPF discussion group on GitHub](https://github.com/orgs/missionpinball/discussions)
* [PinDevCon](https://fastpinball.com/pindevcon) - The pinball developer conference, lots of MPF content!

## About MPF

  * [About](about/index.md)
  * [FAQs](faq/index.md)
  * [MPF Versions](versions/index.md)
  * [License & Copyright](about/license.md)
  * [MPF Documentation authors](about/authors.md)
  * [Contributing to MPF's Documentation](about/help_docs.md)
  * [Help us to write it](about/help.md)
  * [Contributing to MPF](about/contributing_to_mpf.md)
