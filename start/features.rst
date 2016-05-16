MPF features
============

Even though MPF is a work-in-progress that's not yet complete, the core dev team
has been working on it for over two years, with over 5,000 hours of combined
effort.

Major Features & Concepts
-------------------------

+ The vast majority of "programming" your game can be done with text-based
  config files that make it easy to get powerful and complex pinball
  features running in your game. They're also easy for non-programmers to use.
+ Advanced programmers and customization can be done via the API. (The
  API is fully documented at `api.missionpinball.com <http://api.missionpinball.com>`_
+ You can easily switch between hardware platforms, so if sometime down the road
  you want to switch hardware or the company whose hardware you're using
  goes out of business, all your effort is not lost as you can easily move
  everything to a new hardware platform with a simple config file change.

Hardware support
~~~~~~~~~~~~~~~~

+ Multimorphic P-ROC & P3-ROC pinball controllers, with either PD-8x8, PD-16,
  PD-LED, and SW-16 driver and accessory boards or installation in existing WPC,
  Stern Whitestar, or Stern SAM machines.
+ FAST Pinball Core, Nano & WPC controllers, with 3802, 1616, and 0804 I/O
  boards, FAST servo boards, or installation in existing WPC machines.
+ Mark Sunnucks's "Snux" System 11 driver board for use in System 11 and Data
  East machines, in concert with either a P-ROC or FAST WPC controller.
+ Fadecandy RGB LED controllers.
+ Open Pixel Control (OPC) LED and lighting controllers.
+ I2C servo controllers.
+ Pololu Maestro servo controllers.
+ SmartMatrix RGB LED DMD controllers

Pinball device support
~~~~~~~~~~~~~~~~~~~~~~

+ Switches (normally open, normally closed, mechanical or opto, with
  configurable debounce settings)
+ Coils / drivers (pulse, enable, disable, pwm)
+ Matrix-based lights
+ LED RGB-based lights
+ GI (general illumination)
+ Flashers
+ Flippers
+ Pop bumpers / slingshots
+ Drop targets and drop target banks
+ Diverters
+ All forms of troughs (modern, System 11, early WPC, early '80s, etc.)
+ Ball devices (scoops, VUKs, saucers, locks, etc.)
+ Multiple playfields and playfield transfers (including head-to-head machines)
+ Driver-enabled devices (like flippers and pop bumpers in System 11 machines)
+ Mechanical and coil-fired plungers and ball launchers
+ EM score reels

Pinball logic
~~~~~~~~~~~~~

+ Ball locks
+ Multiball
+ Ball saves
+ Ball search
+ Tilt
+ Credits / coin play
+ Audits
+ Full per-player variable and settings support. Save/restore anything
  on a per-player bases (shots, objectives, goals collected, targets
  hit, etc.)
+ Ball tracking / automatic ball routing
+ Shots & shot groups (with full per-player state management (e.g. lit, unlit,
  flashing, etc.)
+ Shot rotation (lane change, etc.)
+ Modes and a mode stack (start / stop / restart / stacked modes)
+ Attract mode
+ Logic blocks, which let you build complex pinball game logic out of reusable
  components via the config files
+ Score controller to assign points (or other progress) per-player for different
  events, with mode integration for blocking and blending
+ Timers (start / stop / pause / count down / count up)

Displays
~~~~~~~~

+ On-screen LCD displays, either high-def or with a "dot" look
+ Physical mono-color DMDs
+ RGB LED DMDs
+ Display "slides" with priorities, transitions in and out
+ Display "widgets" (things you put on displays), including:

    + Text (with fonts, styles, colors, dynamic text based on game state, etc.)
    + Images & animated images
    + Videos
    + Shapes
    + "Picture-in-picture" style sub-displays

+ Any property of any widget can be animated (opacity, size, position, etc.)

Sounds & Audio
~~~~~~~~~~~~~~

+ Multi-track sound system with automatic volume and ducking (e.g. voice,
  sfx, and background music tracks)
+ Per-track settings for simultaneous sounds and sound queues (e.g. let as many
  sfx sounds play at once as you want, but queue sounds on the voice track so
  only one plays at a time)
+ Advanced per-sound "tuning", including attack, attenuation, ducking, etc.
+ Sound pools and sound groups, so you can have multiple sounds for a single
  effect and cycle through them, with controls for whether they random, weighed
  random, rotation patterns, etc.

Shows
~~~~~

+ A show controller which runs coordinated shows of LEDs, lights, coils,
  flashers, sounds, slides, videos, animations, etc.
+ Start/stop/pause/resume shows
+ Dynamic shows which change based on what's happening in the game.
+ Change the playback speed of shows (even while they're playing)

Other stuff
~~~~~~~~~~~

+ A data manager which reads and writes data from disk, including
  audits, earnings, machine variables, high scores, etc.
+ A keyboard interface which lets you simulate switch actions with
  your computer keyboard. (Great for testing!)
+ A plugin architecture which allows you to write your own plugins to
  extend baseline functionality.
+ A "scriptlet" interface lets you add Python code snippets to extend
  the functionality you can get with the configuration files.
+ A mode "code" interface which lets you add custom Python code to game modes.
+ A switch "player" which lets you play back timed sequences of
  switches for automated testing and simulation.


And the best part: Everything mentioned on this page can be done via the text-
based configuration files. If you don't want to be a "coder," you don't have to
be. (Though the plugin, scriptlet, mode
coding, and `API documentation <http://api.missionpinball.com>`_ mean that if you want to use MPF for
your groundwork and code your game in "real" Python, that's fine too.
