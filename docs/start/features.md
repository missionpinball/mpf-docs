---
title: MPF feature list
---

# MPF features & capabilities

MPF has been around for almost ten years and used in hundreds of
homebrew and commercial pinball machines.

## Major Features & Concepts

  * The vast majority of "programming" your game can be done with
    text-based config files that make it easy to get powerful and
    complex pinball features running in your game. They're also easy
    for non-programmers to use.
  * MPF is "event-driven" meaning that everything that happens in a
    pinball machine generates an event, and you can use those events to
    trigger actions (scoring, lights, starting a mode, etc.)
  * Advanced programmers and customization can be done via the API. (The
    API is fully documented at
    [developer.missionpinball.org](http://developer.missionpinball.org/).)
  * You can easily switch between hardware platforms, so if sometime
    down the road you want to switch hardware or the company whose
    hardware you're using goes out of business, all your effort is not
    lost as you can easily move everything to a new hardware platform
    with a few changed lines in your config file.

## Compatible pinball controllers

MPF supports the following pinball control systems &
electronics (which in turn control the physical pinball machine
hardware):

* FAST Pinball Modern & Retro controllers
* Open Pinball Project (OPP) open source hardware controllers
* CobraPin (Pre-built based on OPP)
* Multimorphic P-ROC & P3-ROC pinball controllers
* Stern SPIKE / SPIKE 2 pinball machines
* LISY controllers (Gottlieb System 1 and System 80)
* Arduino Pinball Controller (APC)
* Penny K PKONE pinball controller

See the [pinball controllers](../hardware/pinball_controllers.md) page for details.

## Compatible pinball accessories

MPF also supports the following pinball accessory and mod
electronics:

* Snux System 11 driver board
* SmartMatrix RGB LED DMD controllers
* RGB.DMD RGB LED-based DMD controllers
* PIN2DMD
* Raspberry Pi DMD
* MyPinballs segment display controllers

## Compatible hobby electronics boards

In addition to control systems designed specifically for pinball machines,
MPF also supports several "hobby" style electronics which people often use
in homebrew machines, including:

* Fadecandy RGB LED controllers
* Open Pixel Control (OPC) LED and lighting controllers
* I2C servo controllers
* Pololu Maestro servo controllers
* Pololu Tic stepper controllers
* StepStick stepper controllers
* Other native I2C devices
* MMA8451-based accelerometers
* OSC, DMX, and MIDI devices
* Trinamics Steprocker stepper motor controllers

See the [Hobbyist Electronics](../hardware/hobbyist.md) documentation for full details.

## Pinball mechanism support

MPF currently supports the following different types of pinball
playfield mechanisms:

  * Switches (normally open, normally closed, mechanical or opto, with
    configurable debounce settings)
  * Coils / drivers / solenoids (pulse, enable, disable, PWM)
  * Lamp matrix-based incandescent lights & LEDs
  * LEDs (RGB, GRB, RGBA, RGBW, RGBAW)
  * Accelerometers
  * GI (general illumination)
  * Flashers
  * Flippers
  * Pop bumpers / slingshots
  * Drop targets and drop target banks
  * Diverters
  * All forms of troughs (modern, System 11, early WPC, early '80s,
    Gottlieb System 3, etc.)
  * Ball devices (scoops, VUKs, saucers, locks, etc.)
  * Multiple playfields and playfield transfers (including head-to-head
    machines)
  * Driver-enabled devices (like flippers and pop bumpers in System 11
    machines)
  * Mechanical and coil-fired plungers, ball launchers, and catapults
  * EM score reels
  * Kickbacks
  * Magnets
  * Rollover switches
  * Servos
  * Stepper motors
  * Traditional motors

See the [Pinball Mechs](../mechs/index.md)
documentation for full details.

## Game logic

MPF includes built-in support for all the pinball machine and game logic
you need, including:

  * Modes and a mode stack (start / stop / restart / stacked modes)
  * Ball locks
  * Multiball
  * Ball saves
  * Ball search
  * Extra balls
  * Tilt
  * Credits / coin play
  * Audits
  * Bonus
  * High score
  * Full per-player variable and settings support. Save/restore anything
    on a per-player bases (shots, objectives, goals collected, targets
    hit, etc.)
  * Player achievements & achievement groups (groups of modes to start
    which progress towards wizard mode, etc.)
  * Ball tracking / automatic ball routing
  * Shots & shot groups (with full per-player state management, e.g.
    lit, unlit, flashing, etc.)
  * Shot rotation (lane change, etc.)
  * Attract mode
  * Logic blocks, which let you build complex pinball game logic out of
    reusable components via the config files
  * Score controller to assign points (or other progress) per-player for
    different events, with mode integration for blocking and blending
  * Timers (start / stop / pause / count down / count up)
  * Video modes
  * Switch combinations (flipper cancel, hold flipper button to start
    super skill shot, etc.)
  * Timed switches (hold the flipper for 2 seconds to show game stats,
    etc.)

See the [Game Logic](../game_logic/index.md)
documentation for full details.

## Displays, DMDs, & Graphics

  * On-screen LCD displays, either high-def or with a "dot" look

  * Physical mono-color DMDs

  * RGB LED DMDs

  * Segmented displays

  * Display "slides" with priorities, transitions in and out

  * Display "widgets" (things you put on displays), including:

      * Text (with fonts, styles, colors, dynamic text based on game
        state, etc.)
      * Images & animated images
      * Videos
      * Shapes
      * "Picture-in-picture" style sub-displays

  * Any property of any widget can be animated (opacity, size, position,
    etc.)

See the [Displays](../mc/displays/types.md) documentation for full details.

## Sounds & Audio

  * Multi-track sound system with automatic volume and ducking (e.g.
    voice, sfx, and background music tracks)
  * Per-track settings for simultaneous sounds and sound queues (e.g.
    let as many sfx sounds play at once as you want, but queue sounds on
    the voice track so only one plays at a time)
  * Advanced per-sound "tuning", including attack, attenuation,
    ducking, etc.
  * Sound pools and sound groups, so you can have multiple sounds for a
    single effect and cycle through them, with controls for whether they
    random, weighed random, rotation patterns, etc.

See the [Sounds](../mc/sound/index.md)
documentation for full details.

## Shows

  * A show controller which runs coordinated shows of LEDs, lights,
    coils, flashers, sounds, slides, videos, animations, etc.
  * Start/stop/pause/resume shows
  * Dynamic shows which change based on what's happening in the game.
  * Change the playback speed of shows (even while they're playing)

See the [Shows](../shows/index.md)
documentation for full details.

## Machine Management

  * Service mode / operator menus
  * Operator-configurable "settings" which you can use to expose any
    setting anywhere in MPF to game operators.
  * A data manager which handles reading and writing data from disk,
    including audits, earnings, machine variables, high scores, etc.
  * Power supply management (map drivers to power supplies to make sure
    not too many things fire at once)

See the [machine management](../machine_management/index.md) documentation for details.

## Tools

  * The [MPF Monitor](../tools/monitor/index.md) standalone app which is a graphical tool that connects
    to a live running instance of MPF and shows the status of various
    devices. You can interact with it by clicking on switches and see
    your game in action on your computer.
  * An "interactive" media controller which lets you interactively
    build and test display slides, widgets, and animations.
  * A switch player which lets you build automatically scripts to
    "replay" switches for testing your game.
  * A complete set of test functions which you can use to write your own
    automated tests for your machine.
  * A keyboard interface which lets you simulate switch actions with
    your computer keyboard. (Great for testing!)
  * Detailed logging, config file checking, and helpful error messages
    to help you troubleshoot issues.

## Professional-level features

MPF contains hundreds of the "little" things most people never think
about that help ensure machines running it are truly professional-level
machines that can be placed in revenue service in public locations. Here
are just a few random things that have caused people to say, "Hey,
that's cool!" over the years:

  * Power supply management: MPF knows how much current each power
    supply has and how much current various devices require, so it will
    intelligently manage and delay coil firings to ensure fuses don't
    blow. (For example, don't reset the drop targets at the same time
    the flippers are held on and a ball is being ejected.)
  * Tilt-through prevention: A sliding time window ensures that the tilt
    plumb-bob has settled before the next player's ball is started.
  * Automatic ball routing and retry logic:
  * Asset pools: Sound effects, images, and videos can be "pooled"
    (with various settings for randomness, weightings, etc.), ensuring
    that each "hit" of a target produces a different sound instead of
    the same one over and over.
  * Audio loops and break / resume points: Cue points for music and
    audio to ensure that music tracks are smoothly looped and advanced
    based on game play.
  * Advanced multi-track audio: Automatic ducking of music and sfx when
    voice tracks play, etc.
  * Auto leveling based on accelerometer: The machine knows when it's
    out of level and can post a credit dot or notify the operator.

## Developer-friendly

  * Fully open-source and well-documented code.
  * A plugin architecture which allows you to write your own plugins to
    extend baseline functionality.
  * Modular design that lets you write your own hardware interfaces.
  * A "scriptlet" interface which can be used to easily add Python
    code snippets to a game to extend the functionality you can get with
    the configuration files.
  * A mode "code" interface which lets you add custom Python code to
    game modes.

And the best part: Everything mentioned on this page (except for the
developer stuff) can be done via the text-based configuration files. If
you don't want to be a "coder," you don't have to be. (Though if you
are a coder, we'd love to have you help us write MPF!

By the way, if you'd like to see what we have in store for the future,
check out our [road map](../versions/roadmap.md).
