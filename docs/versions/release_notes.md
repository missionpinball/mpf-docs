---
title: MPF Release Notes
---

# MPF Release Notes


Here's the history of the various release versions and changes of the
Mission Pinball Framework.

Note you can also click the "Assets" section at the end of the notes
for each release to download the PDF or HTML versions of the
documentation for that specific release.

## 0.57.3

Release: September 15, 2024

MPF 0.57.3 includes quality of life changes with many small changes including more graceful error handling and mpf version enforcement.

### New Features
* FAST EXP Board Config option `ignore_led_errors` - setting `true` will log parsing/interpolation errors for LED colors but not crash the game.
* High Score "Filler" Initials/Names - provide defaults if a player chooses not to enter their own initials/name.
* Config option `min_mpf_version` - When specified, boot up will error out if the current MPF version is less than the config-specified one.

### Improvements
 * Bonus entries that use `player_score_entry` player variables will be zero if the player variable is unset (previously: one)
 * Active modes are logged at main loop start, with a warning if attract mode is not active
 * Platform Integration Test runner improved support for trough ball detection
 * Misc code cleanup and fixes

## 0.57.2

Release: July 17, 2024

MPF 0.57.2 includes substantial upgrades to ball search, and numerous bug fixes and improvements.

### New Features
* Switch `ignore_during_ball_search:` config option to prevent false positives during searches
* Switch support for `playfield:` config option to propagate to devices (drop targets, shots, etc.)
* Playfield `enable_ball_search:` now supports templates, e.g. `settings.enable_ball_search==1`
* OPP: Support for `WING_SOL_8` wings with up to 32 solenoids
* Virtual Pinball: Support for segment displays
* Spinners: `max_events_per_second:` config option to reduce event load during spins

### Improvements
* Playfield *playfield_active* event now includes the source of the active trigger
* Better (more reliable) suppression of switch hits from Drop Target firings during ball search with `switch.mute()`
* Better error messaging for ball search on a playfield without iterator devices
* Ball devices that mark playfield active can now inherit the playfield from their switch
* Switches no longer post active events during startup
* Shows now include debug logging for starting, stopping, and pausing

### Bug Fixes
* Fixed a bug in ball search phase/iteration counting that miscounted the number of phases and iterations to perform
* Fixed a bug in FAST LED channel numbering for rolling over channel offsets

## 0.57.1

Release: May 21, 2024

MPF 0.57.1 includes some important performance and stability updates and more functionality for machines running on-location.

### New Features
* Segment Displays `update_method:` to choose between stacked text and replace text
* Ball devices can attempt to re-order (knock around) balls to settle misalignments
* Service menu for displaying light chains
* Adjustable machine variable settings for per-track volume levels
* Restore FAST Audio Board volume levels during startup
* Auditor report for "missing" switches (i.e. switches not hit since some number of games)
* Platform Integration Test runner for automated testing on physical hardware platforms

### Improvements
* Re-enable Prospector linting checks at high strictness
* Use Python-preferred iteration over lists/dicts
* Re-raise validation errors to include more useful stacktraces
* Standardize all logging to use string substitution rather than f-strings
* Reduce FAST Segment Display bandwidth by only sending color changes instead of all color statements
* Better handling of missing balls and trough jams during startup

### Bug Fixes
* Fixed production bundle packaging with new ruamel syntax
* Fixed memory leak when using segment displays
* Fixed numerous bugs in managing FAST Audio Board through service menu
* Fixed random crash during light fades due to floating-point-rounding-error

## 0.57.0

Release: March 10, 2024

MPF 0.57 represents a major upgrade all across MPF, including a complete reworking of the
FAST platform layer and significant improvements in stability and auditing for machines
on-location.

Version 0.57 requires config file and show version 6, so machines running 0.56 and prior
will need to migrate their config files: namely, wrapping some colors and relative time
values in quotes. This process takes less than an hour and is documented in the
[migrating to config 6](../config/instructions/config_v6.md) guide.

### New Features
* Audio: New service menu for customizing audio volumes by track
* Audio: New service menu for managing hardware audio platforms
* Ball Locks: Customizable behavior for when a physical lock/hold loses a ball
* Bonus: Option to round bonus scores up or down to a nearest whole increment
* Coils: Coils now support `timed_enable_events` for automatic timed pulse-and-hold
* FAST: Support for FAST modern platform (Neuron) and retro platform (SYS11/WPC89/WPC95)
* Lights: Customizable RGBW behavior for managing how white pixel blends with colors
* Lights: New service menu for testing light chains
* Platform Integration Tests: new plugin for running automated test games on physical machines
* Steppers: More control with new config options `home_events` and `relative_positions`

### Improvements
* Animations: Support for `step` to throttle how many animation frames are calculated per second
* Auditor: More control over what is audited and when, including missing switches
* BCP: More fine-tune control of receiving settings and machine variables over BCP
* Dynamic Values: Support for `//` floor division
* FAST: Complete refactor of FAST serial connections by @toomanybrians
* FAST: Improve port autodetection and allow boards to be optional
* Framework: Only instantiate plugins that are enabled
* Framework: Use asyncio for managing async operations and loops
* Kivy: Support for `auto` and `fake` values in `fullscreen`
* Logging: Additional debug logs for drop targets by @wolfmarsh
* Logging: Improve logging statements and reduce logs written while in production mode
* Modes: New mode property `starting` for when a mode is starting up but not active
* Python: Support for Python up to 3.11, deprecate Python <= 3.7
* Shots: New event kwarg `elapsed` for sequence shots by @cobra18t
* Shots: Support for `priority` in shots to control multiple shots on the same switch
* Shows: Support for `start_step` in `show_tokens`
* Shows: Support for dynamic placeholders in `speed` by @cobra18t
* Sounds: Support for `ducking` in `sound_player` settings
* Text Input: Support for `bitmap_font` when using text input widget
* Timers: Support for event kwargs in evaluating dynamic timer values

### Bug Fixes
* Concurrent file writes would crash writing thread and silently fail subsequent writes
* Conditional asset pools would crash multiplayer games if players had different conditions
* FAST Nano RGB would hang when attempting a soft reset
* FAST serial comms would hang when awaiting a header with <3 characters
* Fix Windows audio crash due to cyclical dependencies by @ericselkpc
* Game ball count would break if a multi-ball device ejects more than one ball
* OPP `kick_coil` missing the EOM command by @mrechte
* Updating machine vars would erase previously-saved settings
* Verbose logging would not honor `-V` argument by @mrechte

### Breaking Changes
* Auditor: Uninitialized player variables will not be audited if zero
* Config files: `omap` deprecated; use `dict` instead
* Config files: Color values that are numeric with leading zeros (e.g. `005599`) and relative time values (e.g. `+1`)must be wrapped in quotes
* Config files: New `config_version` and `show_version` 6 to support updated YAML features
* Custom code: The `scriptlets` class is deprecated; use `custom_code` instead


## 0.56

Released: January 15, 2023

* BCP: Service test start events by @avanwinkle in https://github.com/missionpinball/mpf/pull/1589
* Adds hurry up and grace period features to multiball ball save by @atummons in https://github.com/missionpinball/mpf/pull/1590
* Adds Multiball Ball Save for Add A Ball by @atummons in https://github.com/missionpinball/mpf/pull/1592
* Blinkenlights by @densminger in https://github.com/missionpinball/mpf/pull/1591
* Adds a default show bl_color for blinkenlights by @atummons in https://github.com/missionpinball/mpf/pull/1594
* MultiballLock blocking_facility  by @avanwinkle in https://github.com/missionpinball/mpf/pull/1596
* Service list custom values for list_coils etc by @avanwinkle in https://github.com/missionpinball/mpf/pull/1597
* Production bundles: new options for MC and target machine path by @avanwinkle in https://github.com/missionpinball/mpf/pull/1598
* Add 'set_tick_interval' control event for Timers, with event kwargs by @avanwinkle in https://github.com/missionpinball/mpf/pull/1599
* handle autofire hw rules in a switch matrix by @cobra18t in https://github.com/missionpinball/mpf/pull/1600
* Enable ball saves to be sourced from a lock by @cobra18t in https://github.com/missionpinball/mpf/pull/1607
* Use source_playfield.add_ball for ball_locks in multiball by @cobra18t in https://github.com/missionpinball/mpf/pull/1608
* Posts update events for counter control_events by @atummons in https://github.com/missionpinball/mpf/pull/1606
* prevent ball search from marking playfield active by @cobra18t in https://github.com/missionpinball/mpf/pull/1610
* Service mode_setting to prevent device list sorting by @avanwinkle in https://github.com/missionpinball/mpf/pull/1602
* DropTarget config option max_reset_attempts to retry reset pulses by @avanwinkle in https://github.com/missionpinball/mpf/pull/1611
* Production bundle args: without MC, with custom machine_path by @avanwinkle in https://github.com/missionpinball/mpf/pull/1612
* Update 14 segment for better lowercase and symbols by @cobra18t in https://github.com/missionpinball/mpf/pull/1614
* feature: add empty_lock_devices_on_ball_end to multiball_locks by @jabdoa2 in https://github.com/missionpinball/mpf/pull/1615
* feature: service mode for segment displays by @jabdoa2 in https://github.com/missionpinball/mpf/pull/1616
* add 8 segment to display emulator by @borgdog in https://github.com/missionpinball/mpf/pull/1617
* Auditor checks if events exist before setting to 0 by @atummons in https://github.com/missionpinball/mpf/pull/1619
* Add check in RGBColor constructor to account for integer colors by @seanirby in https://github.com/missionpinball/mpf/pull/1609
* Allow kwargs or player variable events, default "source" kwarg in variable_player by @avanwinkle in https://github.com/missionpinball/mpf/pull/1620
* New coil option for timed_enable by @avanwinkle in https://github.com/missionpinball/mpf/pull/1613
* Cumulative drop_target reset delays for multi-coil banks by @avanwinkle in https://github.com/missionpinball/mpf/pull/1621
* Bugfix orphaned handlers on shot groups by @avanwinkle in https://github.com/missionpinball/mpf/pull/1622
* add OPP light subtype "incand" to VirtualHardware platform by @tp-ops in https://github.com/missionpinball/mpf/pull/1623
* Add priority to credits mode reset events by @avanwinkle in https://github.com/missionpinball/mpf/pull/1624
* Fix IMC Load Error by @atummons in https://github.com/missionpinball/mpf/pull/1625
* Post timer_(name)_tick event on restart when already running by @avanwinkle in https://github.com/missionpinball/mpf/pull/1626
* System11 AC Relay Improvements by @avanwinkle in https://github.com/missionpinball/mpf/pull/1628
* Text_UI: Updates player variables instantly by @atummons in https://github.com/missionpinball/mpf/pull/1632
* Update match.py to keep winner_number by @borgdog in https://github.com/missionpinball/mpf/pull/1630
* Simplifies attr check related to IMC by @atummons in https://github.com/missionpinball/mpf/pull/1627
* Adds a feature to jump to a state of shot profile by @atummons in https://github.com/missionpinball/mpf/pull/1633
* Correct delayed kick timing for OPP by @cobra18t in https://github.com/missionpinball/mpf/pull/1636
* FAST 2nd-Gen Hardware: Support for V2 Controllers by @avanwinkle in https://github.com/missionpinball/mpf/pull/1629
* Create flash duty for light segment displays by @cobra18t in https://github.com/missionpinball/mpf/pull/1637
* Fast segment display update hz by @toomanybrians in https://github.com/missionpinball/mpf/pull/1638
* Fixes issue with no player_vars in config by @atummons in https://github.com/missionpinball/mpf/pull/1635
* Add pulse_power support for OPP by @cobra18t in https://github.com/missionpinball/mpf/pull/1639
* Timer bugfix: set current player before updating tick values by @avanwinkle in https://github.com/missionpinball/mpf/pull/1640
* EventPlayer: Bugfix multiple conditionals by @avanwinkle in https://github.com/missionpinball/mpf/pull/1642
* Adds speed option to achievement shows by @atummons in https://github.com/missionpinball/mpf/pull/1643
* Add servo support for OPP by @cobra18t in https://github.com/missionpinball/mpf/pull/1641
* OPP Incand fix by @cobra18t in https://github.com/missionpinball/mpf/pull/1644
* Bugfix: FAST timed_enable hold ms/pwm inverted by @avanwinkle in https://github.com/missionpinball/mpf/pull/1647
* Add "use_dots_for_commas" setting to segment displays by @cobra18t in https://github.com/missionpinball/mpf/pull/1648
* Add support for NeoSeg display configuration by @cobra18t in https://github.com/missionpinball/mpf/pull/1649
* Update text_ui.py by @atummons in https://github.com/missionpinball/mpf/pull/1673
* Virtual_pinball LED Brightness by @4starpizza in https://github.com/missionpinball/mpf/pull/1666
* doc: remove double entries by @Stefku in https://github.com/missionpinball/mpf/pull/1677
* Add linear_gradient config spec by @nullbuilds in https://github.com/missionpinball/mpf/pull/1675
* Syncs up chimes with reel coil pulse by @atummons in https://github.com/missionpinball/mpf/pull/1634
* Add niceties to achievement_group by @Samdal in https://github.com/missionpinball/mpf/pull/1646
* Bump requests from 2.22.0 to 2.28.2 by @dependabot in https://github.com/missionpinball/mpf/pull/1678

## 0.55

Released: June 25, 2021

* Removed Python 3.5 support
* Added Python 3.8 and 3.9 support (default in Ubuntu 20.04)
* Flashing Segment Displays in P-Roc
* Segment Display Match Flashing
* Visual Pinball Engine (VPE) Support
* New argument "remaining" in counts
* Initial support for auto-generating wire harnesses
* Tilt improvements
* New hardware: Initial PKONE support
* Improved config validation
* More Service Mode Features
* Open Pinball Project 2.1 Firwmare (for Cobrapin)
* State Machines in non-game modes
* EOS repulse in software
* Better EOS support in FAST and P/P3-Roc
* Ball search only starts at boot when there is at least one ball
* Allow updating speed and manual_advance of shows
* Power management for enable on coils
* Production bundles for config in production machines
* RGB segment displays
* New hardware: FAST segment displays
* Segment displays emulator
* Animations for segment displays
* New command: "mpf hardware benchmark"
* Improved servo support
* Support switches in Pololu Tic
* Add more subscriptions and placeholders
* New spinner device
* New crash reporter
* More and better segment mappings
* Better drop target event behavior

### New Config Options

* New delay setting for all config players to delay execution
* New option enabled for displays
* New option max_hold_duration for coils to prevent burning your coils
    by accident
* Persist_frame on images
* logic_block_timeout for all logic blocks (counters, accruals and
    sequences)
* Added block in sound_player
* New option stop_timeout_after_last_move in servos

## 0.54

Released: November 7, 2020

This release contains incremental improvements and a lot of bugfixes. We
identified a few potential upgrade issues:

* Deprecated `ball_locks` device has been removed. Use
    `multiball_locks` or `ball_holds` instead.
* Space-separated lists have been removed. Use comma-separated lists
    or yaml lists instead (with or without spaces). MPF sticks to YAML
    conventions here and allows all kinds of legal YAML lists (which
    does not include space-separated lists).
* Deprecate `playfield_active` tags on shots. Those tags are only
    required for switches which are not part of shots or devices (so
    almost none). MPF will complain and you might have to remove the tag
    in that case.
* MPF will complain on event handlers with the same name as a switch.
    This should not happen in practice and has been done to catch
    typical user error (i.e. using the event `s_my_switch` instead of
    `s_my_switch_active`).
* Diagnostics menu (switch, coil, light) is now a sub-menu in service
    mode.

### New Features

* [Deduplicate asyncio
    code](https://github.com/missionpinball/mpf/pull/1488) - jab
* [Support more Pin2DMD hardware
    options](https://github.com/missionpinball/mpf/pull/1491) - jab
* [Do not flush in
    pypinproc](https://github.com/missionpinball/pypinproc/commit/b631d57265e35ea32618677cae79c8ad1e0d1ffc) -
    jab
* [Do not call flush on write_data in pypinproc to speed up LEDs on
    PD-LED](https://github.com/missionpinball/libpinproc/commit/5bb2146d3e655515c08e41d184f2a6bcce4667d4) -
    jab
* [Better default logging for ball
    devices](https://github.com/missionpinball/mpf/commit/22efb222f7b09a7dbd2d77590d444790d324b04e) -
    jab
* [Support event args in
    show_tokens](https://github.com/missionpinball/mpf/pull/1492) - jab
* [Log virtual time in unit
    tests](https://github.com/missionpinball/mpf/commit/5e3c61527607c863193410567385e78657e2755f) -
    jab
* [New "mpf format" command to format
    configs](https://github.com/missionpinball/mpf/pull/1499) - jab
* [Refactor hardware fades for
    performance](https://github.com/missionpinball/mpf/pull/1489) - jab
* [Driverboards per platform to support FAST and P-Roc in parallel in
    one
    machine](https://github.com/missionpinball/mpf/commit/3372fdfcfa57029fcc2803090151e829066f7af9) -
    jab
* [Crash asset loader thread on
    exception](https://github.com/missionpinball/mpf-mc/commit/c3d3116846bfc20ba16e53df10a6bfba1360b6dc) -
    jab
* [Validate widgets and targets in
    slide_player](https://github.com/missionpinball/mpf-mc/commit/d269acd57a2ee09f65c53c83c674cfa345e00c9a) -
    jab
* [Validate slides in
    widget_player](https://github.com/missionpinball/mpf-mc/commit/c458b9e6baa66a9d5aae2298f8fb0a7a81877dda) -
    jab
* [Refactor pypinproc to use
    PRWriteDataUnbuffered](https://github.com/missionpinball/pypinproc/commit/a34a26a39a93ca50da92f795f60fa157b5979c2c) -
    jab
* [Refactor libpinproc to use
    PRWriteDataUnbuffered](https://github.com/missionpinball/libpinproc/commit/031109f5ecabca594ee934423d4183b82b147f27) -
    jab
* [Util
    cleanup](https://github.com/missionpinball/mpf/commit/96b628496d0ff7d01b1c0a36cbefc81931d849dc) -
    jab
* [Turn off incands at start for
    OPP](https://github.com/missionpinball/mpf/commit/e0e711d1a7c525474aa12e09a98a86bd043895cc) -
    jab
* [Remove space separated
    lists](https://github.com/missionpinball/mpf/pull/1505) - jab
* [Support delayed pulses in autofires and kickbacks and implement it
    for OPP](https://github.com/missionpinball/mpf/pull/1507) - jab
* [Refactor config
    loading](https://github.com/missionpinball/mpf/pull/1506) - jab
* [Support serial LEDs in OPP on new
    boards](https://github.com/missionpinball/mpf/pull/1508) - jab
* [Enable dot priority syntax
    everywhere](https://github.com/missionpinball/mpf/commit/9fda4065f8084781c47f65c61a47ba0d9fd8ddef) -
    jab
* [Remove dash syntax for control
    events](https://github.com/missionpinball/mpf/commit/27833c715a22f2a9f430b5d18db7161a1b2895f4) -
    jab
* [Unity config spec loading for mpf and
    mc](https://github.com/missionpinball/mpf/commit/c9802a7f65da2e7184c67eefad3f3a05b0f1cc5a) -
    jab
* [Remove ball locks as they have been replaced by multiball_locks and
    ball_holds](https://github.com/missionpinball/mpf/commit/ab45e683e9b434cde420b001236051587cec7fe3) -
    jab
* [Dynamic value for keep_multiplier in bonus
    mode](https://github.com/missionpinball/mpf/pull/1510) - seanirby
* [Batch commands for
    PD-LED](https://github.com/missionpinball/mpf/commit/9b08f849ad88e1f6d810a54235dc2da5696961a0) -
    jab
* [Inputs on Neopixel wings in
    OPP](https://github.com/missionpinball/mpf/commit/65615b2d36b0741d6f029e47ea28e89bdd208446) -
    jab
* [Add mpf build
    production_bundle](https://github.com/missionpinball/mpf/commit/2a91b5f436c9e3c745eb6127f056b40e5f3aad1e) -
    jab
* [Log config load
    times](https://github.com/missionpinball/mpf/commit/81e9750f4ea0c0b2c5fb42ee4cb59cdf7d97f84e) -
    jab
* [Interface for binary data storage (instead of yaml) for high scores
    and
    audits](https://github.com/missionpinball/mpf/commit/32221dcb6b108fb8f655950aa8c88a8f6fa26769) -
    jab
* [Test software update in service
    mode](https://github.com/missionpinball/mpf-mc/commit/cce63720ef5c09140b427cff156721f459deb260) -
    jab
* [Fix asset loading in overloaded
    modes](https://github.com/missionpinball/mpf-mc/commit/d0095cb6825a783cecbe91513ea0c7e22879ece8) -
    jab
* [Remove space separated lists in
    MC](https://github.com/missionpinball/mpf-mc/pull/396) - jab
* [Refactor Config Loading in
    MC](https://github.com/missionpinball/mpf-mc/pull/398) - jab
* [Build MC on Python 3.5 to
    3.7](https://github.com/missionpinball/mpf-mc/commit/1843582c154bc5db0a7ada04a0c0508d8013b519) -
    jab
* [Support Production Config Bundles in
    MC](https://github.com/missionpinball/mpf-mc/commit/f55b7ee8a7247654858b5d90e0f33896730bae58) -
    jab
* [Better error messages for incorrectly formatted
    shows](https://github.com/missionpinball/mpf/commit/6c4878cfa4fc3b56c3eb68e04137a881b259a450) -
    jab
* [Retry connect to LISY/APC
    serial](https://github.com/missionpinball/mpf/commit/b5549ca2084734abc47c310ae3965106160e7129) -
    jab
* [Validate shows in
    achievements](https://github.com/missionpinball/mpf/commit/e89e71d18968f6f744c633b9ceb261a46d03bd42) -
    jab
* [Improve smart_virtual
    errors](https://github.com/missionpinball/mpf/commit/cfb5467351f7ad2880a6560f8828a08ef67169af) -
    jab
* [Improve error when a required setting is
    missing](https://github.com/missionpinball/mpf/commit/4d95608d06091909c0fbbf9f1da2c40659756958) -
    jab
* [Improve generic validator
    errors](https://github.com/missionpinball/mpf/commit/27d337f67adaac2a15d7d6409770c11507aab4fd) -
    jab
* [Support switches in OSC
    platform](https://github.com/missionpinball/mpf/commit/723de4b177de3fb9ff2fc2768108668a555c25df) -
    jab
* [Implement events in OSC
    platform](https://github.com/missionpinball/mpf/commit/c19b087764592b7d342ec4d49bb792c359f8a49c) -
    jab
* [Support BCD, 14-segment and 16-segment displays as
    segment_display](https://github.com/missionpinball/mpf/commit/22827621831d34dc9397ebdc0898602d8f698b73) -
    jab
* [Improve empty device collection
    error](https://github.com/missionpinball/mpf/commit/5a6ae34d4763bcb3e4bbc82f764f9f3787bcb677) -
    jab
* [Validate playfield_active tags on shot
    switches](https://github.com/missionpinball/mpf/commit/2a6615cf80bb8c09ec2823816db4d115d63eb2d5) -
    jab (breaking change - you have to remove those tags)
* [Point users to our fork of apigpio (called
    apigpio-mpf)](https://github.com/missionpinball/mpf/commit/bd05b7531568a7e6213a6b5e5583d05f37760038) -
    jab
* [Validate platforms and prevent configuring features which do not
    exist on
    platform](https://github.com/missionpinball/mpf/commit/938a678c216390794ac20ae2bfd2f470d29a0761) -
    jab
* [Runtime errors with documentation
    links](https://github.com/missionpinball/mpf/commit/8132de4f18ffcc03c5ae32eca5e181727d2f6d37) -
    jab
* [Add glow effect](https://github.com/missionpinball/mpf/pull/1513)
    and [2](https://github.com/missionpinball/mpf-mc/pull/400) -
    seanirby (see blog post about glow effect)
* [Add font for 14-segment displays similar to Williams System 11
    displays](https://github.com/missionpinball/mpf-mc/pull/399) -
    seanirby
* [Pin all
    dependencies](https://github.com/missionpinball/mpf/commit/07d49d17945e6b307f853ea583b1ca1401918772) -
    jab
* [Commandline config
    generator](https://github.com/missionpinball/mpf/pull/1514) - F4b1-
* [Add end_ball and end_game events to
    game](https://github.com/missionpinball/mpf/commit/8f23cc83814bf39e4f8e8ae2daed050ab370b8b3) -
    jab
* [Prevent true and false in placeholder (use True and
    False)](https://github.com/missionpinball/mpf/commit/90ac1dee0fcb76c1eea9880fea2563a2437311c1) -
    jab
* [Expose more P/P3-Roc
    errors](https://github.com/missionpinball/mpf/commit/8a8348ed66c3c112e767d96edb312cf0f838bcce) -
    jab
* [mpf hardware scan for
    LISY](https://github.com/missionpinball/mpf/commit/81f64ca9fea2b53f9cb87ae4e90a8c3aa4aba816) -
    jab
* [Refactor driver lights to properly encapsulate
    internals](https://github.com/missionpinball/mpf/commit/8c9b9bdc7960d9bd45aa92a76d69e5ba105084eb) -
    jab
* [Parallel device
    initialisation](https://github.com/missionpinball/mpf/commit/6fc6b4a8a512d23d8cc840477181a531f975e152) -
    jab
* [Implement chained
    lights](https://github.com/missionpinball/mpf/commit/ae3e322fd25b275abe1f8500c1bc742b6990b655) -
    jab (see separate blog post)
* [Add spread spectrum modulation (SSM) PWM for fast coil for
    low-noise
    hold](https://github.com/missionpinball/mpf/commit/1b7f608a56fd902d6d4cb95edd6d9383c0d8e94c) -
    jab
* [Improve error message on failed template
    evaluation](https://github.com/missionpinball/mpf/commit/feb86c8dc5ed3696da82b27f848a123acd4af5c2) -
    jab
* [Add debug output to
    state_machines](https://github.com/missionpinball/mpf/commit/fe1fc1c4c469dfb5ae239355df0cb02574a1d589) -
    jab
* [Better config validator error
    paths](https://github.com/missionpinball/mpf/commit/6ddc1b731789e437eb776f6ad8899bb650fe8231) -
    jab
* [Support new templates syntax for all
    template_str](https://github.com/missionpinball/mpf/commit/ddb54c91c82cd67ab6d77ae03adbd23d5ba85756) -
    jab
* [Add subscriptions in
    variable_player](https://github.com/missionpinball/mpf/commit/eda7286918008b67d2b077a66365ced2971fba4d) -
    jab
* [Pass timestamps from platform for switch
    changes](https://github.com/missionpinball/mpf/commit/2273b27c371a859c531595839cc6ddfe4fca4dec) -
    jab
* [Refactor hot switch path for
    performance](https://github.com/missionpinball/mpf/commit/bd6dc68194e909886ff1c180e346e11874645f4c),
    [2](https://github.com/missionpinball/mpf/commit/90feacf79b3db24335205d6cc6e6ef5f8141161c),
    [3](https://github.com/missionpinball/mpf/commit/7d256ad27acd97430caec4791ca22517852b1b81),
    [4](https://github.com/missionpinball/mpf/commit/8ae14a17cd5b06589efc94a5ec5d83da0276d5ec) -
    jab
* [Add
    sound_loop_start_at/end_at](https://github.com/missionpinball/mpf/pull/1517)
    and [implement them in
    MC](https://github.com/missionpinball/mpf-mc/pull/403) - qcapen
* [Allow multiple
    entrance_switches](https://github.com/missionpinball/mpf/commit/376ddf05118bf4f24c033390f50b25b25c7d06c0) -
    jab
* [Prevent event handler with the same name as switches (to catch
    common beginner
    mistakes)](https://github.com/missionpinball/mpf/commit/87b61e04f26e8f683b99a0f5263cce27a3888f3d) -
    jab (breaking change in theory but unlikely for real machines)
* [Performance
    improvements](https://github.com/missionpinball/mpf/commit/f023ce2c8ac1d55337c3d64455c0ff1fe120518d) -
    jab
* [Add show_queues to serialize
    shows](https://github.com/missionpinball/mpf/commit/ab192b62a398cbba3443bcca25a5ad323a1ec083) -
    jab
* [Support pinproc in Python 3.7 and 3.8 on
    Windows](https://github.com/missionpinball/mpf/pull/1520) - qcapen
* [Recompiled pinproc for Python 3.5 and 3.6 on Windows to include
    recent
    improvements](https://github.com/missionpinball/mpf/pull/1522) -
    qcapen
* [Improve memory leak
    finder](https://github.com/missionpinball/mpf-mc/commit/e95f33e7e7d734142e29efd9b2777cc32aaed25d) -
    jab
* [Add debug button in
    iMC](https://github.com/missionpinball/mpf-mc/commit/aa3d54809cbc449cc3f7781057a39bd5c4ace46f) -
    jab
* [Load named_colors in mc and test
    them](https://github.com/missionpinball/mpf-mc/commit/1d4d87aaaf6c0594e833e307c4d3851dab9ee759) -
    jab
* [Require ffpyplayer for all platforms as it seems to solve video
    issues](https://github.com/missionpinball/mpf-mc/commit/694f356d3d926457423d80ad75ea585e2d18414e) -
    jab
* [Better type hints in
    mpf-ls](https://github.com/missionpinball/mpf-ls/commit/a8c496120b0e176fb5f5db4f313adda756facc57) -
    jab
* [Autocomplete events and go to definition for
    events](https://github.com/missionpinball/mpf-ls/commit/eec997a618dd5573d1e7f7b4a0a42abff944cd95) -
    jab
* [Support more events in
    mpf-ls](https://github.com/missionpinball/mpf-ls/commit/c9413e669d0da64076d08f43a078dbb83fc8f8f6) -
    jab
* [Install latest kivy in debian
    installer](https://github.com/missionpinball/mpf-debian-installer/commit/cfd0b5acce2091ea5e0fccd815bb82863d0a19e9) -
    jab
* [Better error handling in debian
    installer](https://github.com/missionpinball/mpf-debian-installer/commit/3409ea6c191d13b3bec0ef606971441a80c496d2) -
    jab
* [Add source_devices to
    multiball_locks](https://github.com/missionpinball/mpf/commit/20f35f692d2cb7b7d02bf4ab8c5a0c92fd6be08f) -
    jab
* [Select pulse_ms based on ball count during
    eject](https://github.com/missionpinball/mpf/pull/1525) - jab
* [Add start_running option to
    shows](https://github.com/missionpinball/mpf/pull/1524) - avanwinkle
* [Support pulse_power in P/P3-Roc where
    possible](https://github.com/missionpinball/mpf/commit/d08885983bbbfd23e92ae9061d44651481801ac6) -
    jab
* [Better log output for
    P/P3-Roc](https://github.com/missionpinball/mpf/commit/1c6df104f222be640934d01a7e9cefaa282d26db) -
    jab
* [Always log OPP chain
    serial](https://github.com/missionpinball/mpf/commit/c32220ea0139d62ccbd3fa10b9d4519cb4cf6ec7) -
    jab
* [Support GPIO inputs on
    P3-Roc](https://github.com/missionpinball/mpf/commit/a07e4a26863c85fc8cbe82a6ae6f6581bff5e314) -
    jab
* [Faster and better light
    batching](https://github.com/missionpinball/mpf/commit/e4c7355544ddc04fb5364fc9f53af14dde3c6ca1) -
    jab
* [Support Neopixel Wings on
    OPP](https://github.com/missionpinball/mpf/commit/de1b6f24b7543e945fe1fad65dc627c07e302e36) -
    jab
* [Prevent fades to the previous
    color](https://github.com/missionpinball/mpf/commit/80d2c9247634248c4995fab4e281ab43c5228c75) -
    jab
* [Deterministic
    fades](https://github.com/missionpinball/mpf/commit/d5bf5923be7d45d4b6594ac72ca556c19cf7b9fe) -
    jab
* [Allow platforms to set batch granularity for
    fades](https://github.com/missionpinball/mpf/commit/9418baeada0912060644d4c9dc5c61125f027da0) -
    jab
* [Improve ball
    counters](https://github.com/missionpinball/mpf/pull/1527) - jab
* [Python 3.8 compatibility (only MPF not MC because of
    kivy)](https://github.com/missionpinball/mpf/commit/264b0dc9e25b74526a7521facefd74f5eb60b338) -
    jab
* [Support Repulse on EOS in MPF (only supported in Spike so
    far)](https://github.com/missionpinball/mpf/commit/64b60e0777d7ff3b03a44bd86d97d1036903ff88) -
    jab
* [Event to reset high
    scores](https://github.com/missionpinball/mpf/commit/b89543732f6d051234dcf99eb8e0a014ac2e74c2) -
    jab
* [Event to reset
    audits](https://github.com/missionpinball/mpf/commit/5a07acaa3fac8330f1ef60d27d200350c585e34c) -
    jab
* [Event to reset earnings
    records](https://github.com/missionpinball/mpf/commit/cdfe1b5076bae28b5ba776b2d4754e73b69227a2) -
    jab
* [Event to reset
    credits](https://github.com/missionpinball/mpf/commit/52453e29fb064c0509d19503f62b7b5dea56d52d) -
    jab
* [More modern service
    mode](https://github.com/missionpinball/mpf/commit/2c689a7e0fe04c47f60aa65a5bae42b3b3d36322) -
    jab
* [Add twitch bot
    support](https://github.com/missionpinball/mpf/pull/1530) - Mark
    Seiden
* [Improve twitch
    bot](https://github.com/missionpinball/mpf/pull/1531) - Mark Seiden
* [Add advance_random_events to
    accruals](https://github.com/missionpinball/mpf/commit/10f55b2ca93e1ed2bc9c4c547651d48c45bca97d) -
    jab
* [Show a nice error when communication with P/P3-Roc breaks
    down](https://github.com/missionpinball/mpf/commit/f01f9da7595db4440135d0c77c581951b4fc0da6) -
    jab
* [Support more than 256 lights in LISY API >
    10](https://github.com/missionpinball/mpf/commit/4f9c04d357db47e586d051e8823e1d31f65f2059) -
    jab
* [Extend motor
    device](https://github.com/missionpinball/mpf/commit/2bcd15d42148e62bcc9d048e502b24f80a2ed48b) -
    jab
* [Add shop jump](https://github.com/missionpinball/mpf/pull/1532) -
    avanwinkle
* [Add settle_time_ms to entrance switch counter to prevent ejecting
    thin
    air](https://github.com/missionpinball/mpf/commit/78d5790f7c37b1c96844c002a918463cada3246d) -
    jab
* [First version of VPE platform (not finished
    yet)](https://github.com/missionpinball/mpf/commit/c1742f36ef714c7783250313b8bb51644f34d2f4) -
    jab
* [Test and build on Ubuntu
    20.04](https://github.com/missionpinball/mpf/pull/1534) - jab
* [Support conditional events and fallback for
    random_event_player](https://github.com/missionpinball/mpf/pull/1536) -
    avanwinkle
* [Python 3.8 support in MPF-MC (except
    kivy)](https://github.com/missionpinball/mpf-mc/commit/10bed3e964f9ad2d44b8d481e10e95609584feae) -
    qcapen
* [Faster image loading in
    sequences](https://github.com/missionpinball/mpf-mc/commit/4d866b929caf59efe7a87a8814fa05fa144e8937) -
    jab
* [Add block events to text_input and use them in
    carousel](https://github.com/missionpinball/mpf-mc/pull/406) -
    avanwinkle
* [Nicer errors in
    MC](https://github.com/missionpinball/mpf-mc/pull/408) - avanwinkle
* [Expose switch config in
    pypinproc](https://github.com/missionpinball/pypinproc/pull/6) - jab
* [Support loading light shapes from MPF Monitor in
    showcreator](https://github.com/missionpinball/showcreator/commit/06f712161b77ae34f1095ad9bc5ecf173a187267) -
    markinc
* [Add Mac build for
    showcreator](https://github.com/missionpinball/showcreator/commit/4c411ef810a36f6e5a2c207b0cb6cdc891b5b72b) -
    markinc
* [Improve logging in MPF Spike
    Bridge](https://github.com/missionpinball/mpf-spike/commit/e4fa12564954672f83fe9c4ba4299c54c0c26e9e) -
    jab
* [Extend MPF Monitor with a lot of new
    features](https://github.com/missionpinball/mpf-monitor/pull/29) -
    kylenahas
* [Monitor performance
    improvements](https://github.com/missionpinball/mpf-monitor/commit/2ad4b836cb483e5b4b8e74a395b0a913a8647867) -
    kylenahas
* [More monitor perf
    improvements](https://github.com/missionpinball/mpf-monitor/commit/26fe7e016b5232bfa0856b27cc3df93ced5f5a50) -
    jab
* [Add config arg to MPF
    Monitor](https://github.com/missionpinball/mpf-monitor/pull/32) -
    avanwinkle

## 0.53

Released: January 11, 2020

This is a 0.52 maintenance release with cleanups and some refactorings.
We identified a few potential upgrade issues:

* We fixed validation of animations. You might get a validation error
    with [repeat: -1](#). Change it to [repeat:
    false](#). See the [change in the
    docs](https://github.com/missionpinball/mpf-docs/commit/6a141ec4434a0904d92f05bcbce1fe345513c018).
* We changed [active_time](#) of ball_save from ms to secs.
    In case you did not use a unit here this might change the time.
    [Details](https://github.com/missionpinball/mpf/pull/1463).
* [Machine variables
    changed](https://github.com/missionpinball/mpf/pull/1394) if you
    accessed them from code (but not via config).
* [Achievement state
    changed](https://github.com/missionpinball/mpf/pull/1429) if you
    accessed it from code (but not via config or placeholders).

**MPF and MPF-MC**

### New Features

* [Support segment displays connected to normal light of a
    platform](https://github.com/missionpinball/mpf/pull/1305) - jab
* [Batch LED updates for PD-LED and P/P3-Roc to prevent bus
    overflows](https://github.com/missionpinball/mpf/pull/1310) - jab
* [Make separate thread configurable in P/P3-Roc and reduce IPC
    overhead](https://github.com/missionpinball/mpf/pull/1311) - jab
* [Highlight settings in service
    mode](https://github.com/missionpinball/mpf/pull/1309) - avanwinkle
* [Spike-MPF bridge in
    Rust](https://github.com/missionpinball/mpf-spike/commit/529ac6d7d047ef8d74ce2e4555a910a4ddf190c5) -
    jab
* [Use new Spike-MPF bridge in
    MPF](https://github.com/missionpinball/mpf/commit/089f7e48008ab0e82d3d8712ef812ea636975933) -
    jab
* [Use a better default for max_servo_value on
    PD-LEDs](https://github.com/missionpinball/mpf/commit/9fbbd9bbe1367566e5defda0a2914f75db1635d2) -
    jab
* [Allow reverse sorted highscore
    categories](https://github.com/missionpinball/mpf/pull/1296) -
    yensho
* [Light batching in Spike for better light
    sync](https://github.com/missionpinball/mpf/pull/1313) - jab based
    on [request by
    Dave](https://groups.google.com/forum/#!topic/mpf-users/WHRLH0lGZL0)
* [Read ticks_per_second per node for
    Spike](https://groups.google.com/forum/#!topic/mpf-users/WHRLH0lGZL0) -
    jab
* [Reliable speed/flow control in
    Spike](https://github.com/missionpinball/mpf/pull/1314) - jab
* [Initial Spike 2 support for the mpf-spike
    bridge](https://github.com/missionpinball/mpf-spike/commit/e234336f504c40a5050220e00b5baa049d659819) -
    jab
* [Limit light batch size in Spike to prevent bus
    desync](https://github.com/missionpinball/mpf/commit/f64d46689235bb1e4d5abaa63de6d5cf39a4c661) -
    jab
* [Ignore duplicate handler warnings during
    init](https://github.com/missionpinball/mpf/pull/1316) - avanwinkle
* [Add support for steppers in
    Spike](https://github.com/missionpinball/mpf/pull/1317) - jab
* [Support Spike 2
    backlight](https://github.com/missionpinball/mpf/commit/3bd30788613c687674d4e3c8bbace77691e0d1f5) -
    jab
* [Support Spike 1 and Spike 2 backlight in
    bridge](https://github.com/missionpinball/mpf-spike/commit/9ee733992c127050cb31fe79d8ab0f8d89871467) -
    jab
* [Servo and Steppers as
    Diverters](https://github.com/missionpinball/mpf/pull/1321) - jab
* [Separate event handlers and code to catch incorrect arguments in
    custom code](https://github.com/missionpinball/mpf/pull/1327) - jab
* [Auto launch when machine is
    tilted](https://github.com/missionpinball/mpf/pull/1330) - jab based
    on [question from Philip
    D](https://groups.google.com/forum/#!topic/mpf-users/rjDghM-2XXk)
* [Show player and machine variables in the Text
    UI](https://github.com/missionpinball/mpf/pull/1328) - woosle1234
* [Allow dynamic values in timer control
    events](https://github.com/missionpinball/mpf/pull/1337) -
    avanwinkle based on report by wilder
* [Reduce default batch size for Spike
    LEDs](https://github.com/missionpinball/mpf/commit/e3ad5dded06c820db2ec38cbccdc3ed8f683480a) -
    jab based on tests by Dave
* [Custom events_when_added and events_when_removed for
    widgets](https://github.com/missionpinball/mpf-mc/pull/372)
    [\[2\]](https://github.com/missionpinball/mpf/pull/1338) - qcapen
    based on [feature request by
    cfbenn](https://github.com/missionpinball/mpf/issues/1332)
* [Better cache invalidation of config_spec
    cache](https://github.com/missionpinball/mpf/commit/d806ceecb0a53e61d3726471008611b229fb4fd7) -
    jab
* [Refactor Text UI to prevent text
    clutter](https://github.com/missionpinball/mpf/pull/1339) - jab
* [Allow user to disable ball search in a ball
    device](https://github.com/missionpinball/mpf/pull/1341) - dziedada
* [Better signal handlers and shutdown logging during
    crashes](https://github.com/missionpinball/mpf/pull/1347) - jab to
    fix [some exit
    issues](https://groups.google.com/forum/#!topic/mpf-users/98apwhX_rMo)
* [Improve show and lights
    performance](https://github.com/missionpinball/mpf/pull/1346) - jab
* [Refactor
    DelayManager](https://github.com/missionpinball/mpf/pull/1344) - jab
* [Exit MPF when the FAST Nano reboots/crashes during a
    game](https://github.com/missionpinball/mpf/pull/1343) - jab
* [Add a setting for free play to service mode when credits mode is
    loaded](https://github.com/missionpinball/mpf/pull/1354) - jab based
    on [request by
    Greg](https://groups.google.com/forum/#!topic/mpf-users/Q18AvoEaVRw)
* [Allow newer FAST firmware
    versions](https://github.com/missionpinball/mpf/pull/1356) - jab
    based on problems with Firmware 1.05 by Brian Cox
* [Support inverted switches and non-numeric drivers in Virtual
    Pinball](https://github.com/missionpinball/mpf/pull/1360) -
    mfuegemann
* [Extend README and add hardware rules to VPX
    Bridge](https://github.com/missionpinball/mpf-vpcom-bridge/pull/1)
    and
    [Test](https://github.com/missionpinball/mpf-vpcom-bridge/pull/2)-
    mfuegemann
* [Placeholders in credits
    mode](https://github.com/missionpinball/mpf/pull/1357) - jab
* [Placeholders in tilt
    mode](https://github.com/missionpinball/mpf/pull/1358) - jab
* [RGB LEDs and flashers in Virtal
    Pinball](https://github.com/missionpinball/mpf/pull/1363) -
    mfuegemann
* [Update
    asciimatics](https://github.com/missionpinball/mpf/pull/1362) - jab
* [Add --vpx commandline option to
    mpf](https://github.com/missionpinball/mpf/pull/1364) and
    [mc](https://github.com/missionpinball/mpf-mc/pull/373)- jab
* [Add VPX demo table with MPF
    config](https://github.com/missionpinball/mpf-vpcom-bridge/pull/3) -
    mfuegemann
* [Placeholders for StateMachine
    devices](https://github.com/missionpinball/mpf/pull/1365) - jab
* [Initial support for the Arduino Pinball
    Platform](https://github.com/missionpinball/mpf/commit/0021aa4c80c3f5c4db02c7ed0e797f0f2419340e) -
    jab, bontango and blackknight
* [More debug in FAST
    platform](https://github.com/missionpinball/mpf/commit/c79a36b312d33c5cc546e4d9637f51ccef3ddcaf)
    and [longer wait
    times](https://github.com/missionpinball/mpf/commit/e031cb047dcecaaeb9eb37fc11422ea657e2ed71) -
    jab to support more FAST firmwares
* [Generic System 11 A/C Relay handling (for APC and
    Snux)](https://github.com/missionpinball/mpf/pull/1370) - jab
* [Improve duplicate event handler
    message](https://github.com/missionpinball/mpf/commit/bebf593f97b068f07b3af69e93f48b3c8e595974) -
    jab as it [caused confusion for
    Sepp](https://groups.google.com/forum/#!topic/mpf-users/epVKlaU9Yo8)
* [Better error message when number is
    empty](https://github.com/missionpinball/mpf/pull/1376) - jab based
    on [report by
    Sepp](https://groups.google.com/forum/#!msg/mpf-users/oHsUeEJr2yI/Y1hg21iNBAAJ)
* [Placeholders in show_tokens in
    show_player](https://github.com/missionpinball/mpf/pull/1379) - jab
    to [allow dynamic values in all
    widgets](https://groups.google.com/forum/#!topic/mpf-users/lUd6Z2lU_eo)
* [More useful and accurate validation errors in
    dicts](https://github.com/missionpinball/mpf/commit/240c4f9faabd58b8e96b3509b9a7d28ad0fc13fc) -
    jab
* [Add links to the docs to warnings and
    errors](https://github.com/missionpinball/mpf/pull/1380) - jab
* [Improve fake game in tests to handle multiball
    drains](https://github.com/missionpinball/mpf/commit/458927fca909510ef5df643e6947a886862a2aa9) -
    jab
* [Remove Windows Python 3.4 build of
    MPF-MC](https://github.com/missionpinball/mpf-mc/commit/ad6e0fdb5bcd4bdad142b1ac563696f61b60733d) -
    qcapen
* [Improve sound_loop_player
    design](https://github.com/missionpinball/mpf-mc/pull/374) - qcapen
* [Python 3.7 support for Windows in
    MPF-MC](https://github.com/missionpinball/mpf-mc/commit/4dda4261fe527fec829e9e3e3488af8e407a7daf) -
    qcapen
* [Add placeholder conditions for items in carousel
    mode](https://github.com/missionpinball/mpf/pull/1381) - avanwinkle
* [Add control events to
    counters](https://github.com/missionpinball/mpf/pull/1342) -
    dziedada
* [Support for the APC
    platform](https://github.com/missionpinball/mpf/issues/1345) - jab,
    bontango and blackknight
* [Validate switch numbers in
    LISY/APC](https://github.com/missionpinball/mpf/commit/b39bc2759eb83bb1160ca0b3a70247ddeb4aa7a9) -
    jab
* [Set DTS to low on connect for
    APC](https://github.com/missionpinball/mpf/commit/43f0585fcc75535435085189ec1f66128c308db5)
    and [clear serial after
    reset](https://github.com/missionpinball/mpf/commit/4f1198fd3302ebd1fe8aefa2455056975ac1d065) -
    jab
* [Modern lights for
    LISY/APC](https://github.com/missionpinball/mpf/commit/39642c7b3540005e8a4f775805302a8e4dadb484) -
    jab
* [Refactor sound
    loop](https://github.com/missionpinball/mpf-mc/pull/374) - qcapen
* [Allow tokens for widgets in
    shows](https://github.com/missionpinball/mpf/commit/4782dde5fca0f57603d0c82d221a1947887a6cd6) -
    jab based on [request from
    Sean-Paul](https://groups.google.com/forum/#!topic/mpf-users/lUd6Z2lU_eo)
* [Don't activate diverter if activate_event
    present](https://github.com/missionpinball/mpf/pull/1386) -
    GabeKnuth
* [Add enabled and rotation_enabled to placeholders for
    shots/shot_groups](https://github.com/missionpinball/mpf/pull/1387) -
    jab based on [request from
    Mike](https://groups.google.com/forum/#!topic/mpf-users/_EBF2tkfabI)
* [Throws Error when attempting to define more than one default
    display](https://github.com/missionpinball/mpf-mc/pull/376) -
    GranolaDaniel
* [Update unity-bcp-server to latest
    version](https://github.com/missionpinball/unity-bcp-server/commit/61a827fcf6136bd9237678f6b9ccebecc8356737) -
    qcapen
* [Segment display support for
    APC](https://github.com/missionpinball/mpf/pull/1388) - jab
* [Add token to slide_player to pass
    variables](https://github.com/missionpinball/mpf/pull/1389) and
    [MC](https://github.com/missionpinball/mpf-mc/pull/377) - jab based
    on [request in the forum by
    Greg](https://groups.google.com/forum/#!topic/mpf-users/ln2y_qxGRg4)
* [Increased light update
    throughput](https://github.com/missionpinball/mpf/pull/1390) - jab
* [Add express syntax for
    sound_player](https://github.com/missionpinball/mpf-mc/pull/378) -
    jab
* [Refactor machine
    variables](https://github.com/missionpinball/mpf/pull/1394) -
    pmansukhani
* [Tune shows and
    events](https://github.com/missionpinball/mpf/pull/1392) - jab
* [Setup improvements and wheels for
    OSX](https://github.com/missionpinball/mpf-mc/pull/379) - qcapen
* [Nicer errors on syntax errors in
    conditions](https://github.com/missionpinball/mpf/commit/5ce27ba9d7c2392d47fd1598790a89fdd43d9063) -
    jab
* [Improve debug log of early messages in
    OPP](https://github.com/missionpinball/mpf/commit/9262983dd8b207aa5ae546cd6d9e7672b1b9d64c) -
    jab
* [Option to send length bytes in LISY
    protocol](https://github.com/missionpinball/mpf/commit/e61c548efd3f2bfdc3af70338f4016f1ceab28ea) -
    jab
* [Better error message on invalid displays in
    LISY](https://github.com/missionpinball/mpf/commit/2bbc750cfc27df04b83f57680fe27003484b1ef1) -
    jab
* [Load modes from
    subfolders](https://github.com/missionpinball/mpf/pull/1396) -
    pmansukhani
* [Move code out of the hot path for light
    updates](https://github.com/missionpinball/mpf/pull/1397) - jab
* [Reserve all show_player options in show_tokens to prevent indent
    mistakes](https://github.com/missionpinball/mpf/pull/1399) - jab
    based on [bug report by
    Alex](https://groups.google.com/forum/#!topic/mpf-users/J0UBP81ppfg)
* [Improve linter and remove previously undetected unused
    imports](https://github.com/missionpinball/mpf/pull/1400) - jab
* [Better debug output for LISY
    platform](https://github.com/missionpinball/mpf/commit/b28c83fdcf860a3da90e3791d6ae82e1211db1b2) -
    jab
* [Fix segment display mapping for
    APC](https://github.com/missionpinball/mpf/commit/d8232883fc614177b188bc33f6794bc1fb72ce81) -
    jab
* [Configuration setting for player_vars and machine_vars to show in
    text ui](https://github.com/missionpinball/mpf/pull/1406) -
    avanwinkle
* [Better command logging for the
    P/P3-Roc](https://github.com/missionpinball/mpf/commit/163e769fa63bc745ffecce1497458942339212e6) -
    jab
* [Support daisy chaining in the Pololu
    Maestro](https://github.com/missionpinball/mpf/pull/1410) - jab
* [Expose P-Roc hardware version as machine
    variable](https://github.com/missionpinball/mpf/commit/7be95d1cc79dfee12d44ff25b0972444121ff6bc) -
    jab
* [Placeholders for shoot_again in
    multiball](https://github.com/missionpinball/mpf/pull/1404) -
    pmansukhani
* [Support show_tokens with placeholders in
    shot_profiles](https://github.com/missionpinball/mpf/pull/1414) -
    jab
* [Regression Test for Diverters (for a bug which was fixed during
    refactoring)](https://github.com/missionpinball/mpf/commit/4a9251b819e470b2072dbf634e26d1b4c1e5daec) -
    jab
* [Expose MPF and MC version in MPF-MC on
    connect](https://github.com/missionpinball/mpf-mc/commit/732cf02e5aefedbba4e9af72d7c0c7f1aa8b93a5) -
    jab
* [Support pulse power in
    P/P3-Roc](https://github.com/missionpinball/mpf/pull/1418) - jab
* [Add Scaffolding CLI to
    MPF](https://github.com/missionpinball/mpf/pull/1419) - jab
* [Optimized Service Mode for
    LCDs](https://github.com/missionpinball/mpf/commit/6e09beca89f18f718402f3780cd42fb624b3d948) -
    jab
* [Suggestions on config
    typos](https://github.com/missionpinball/mpf/pull/1424) - jab
* [Copy light positions in scaffolding CLI from monitor to MPF for
    display_light_player](https://github.com/missionpinball/mpf/pull/1423) -
    jab
* [Add start_enabled to achievements and refactor
    code](https://github.com/missionpinball/mpf/pull/1426) - jab
* [Add unselect_events to achievements and more
    cleanup](https://github.com/missionpinball/mpf/pull/1429) - jab
* [More achievement
    refactoring](https://github.com/missionpinball/mpf/pull/1431) - jab
* [Refactored test
    cases](https://github.com/missionpinball/mpf/pull/1432) - jab
* [Drop Python 3.4
    support](https://github.com/missionpinball/mpf/pull/1433) - jab
* [Turn device collections into native
    dicts](https://github.com/missionpinball/mpf/pull/1435) - jab
* [Led_color default show now supports all default
    show_tokens](https://github.com/missionpinball/mpf/pull/1441) - jab
* [Log asset loading times for
    tuning](https://github.com/missionpinball/mpf/pull/1442) - jab
* [Show shot state in
    MPF-monitor](https://github.com/missionpinball/mpf/pull/1446) - jab
* [Validate transitions in
    state_machines](https://github.com/missionpinball/mpf/pull/1445) -
    jab
* [Improve config
    parsing/validation](https://github.com/missionpinball/mpf/pull/1452) -
    jab
* [Nicer errors and suggestions in
    shows](https://github.com/missionpinball/mpf/pull/1453) - jab
* [Improve install and dependency manangement for Max and
    Linux](https://github.com/missionpinball/mpf-mc/pull/387) - jab
* [Improve build and install on
    Windows](https://github.com/missionpinball/mpf-mc/pull/388) - jab
* [Lazy loading for zipped image sequences to speed up game
    startup](https://github.com/missionpinball/mpf-mc/pull/389) - jab
* [New experimental language server support for
    IDEs](https://github.com/missionpinball/mpf-ls/) - jab
* [Generic high score mode which works for DMD and
    LCD](https://github.com/missionpinball/mpf/pull/1447),
    [2](https://github.com/missionpinball/mpf-mc/commit/efb6bfe5e58826e6545998a0ae9d7108e51ca1e3) -
    jab
* [Improve correctness, speed and error messages of config
    validation](https://github.com/missionpinball/mpf/pull/1455) - jab
* [Option to ignore checksum errors in
    Spike](https://github.com/missionpinball/mpf/pull/1456) - jab
* [Support new input command for Spike FW
    0.49+](https://github.com/missionpinball/mpf/pull/1457) - jab
* [Implement over current detection for
    Spike](https://github.com/missionpinball/mpf/commit/f8da2cf9b063a342f9ca15c7d84090f853a3465c) -
    jab
* [Arbitrary start state for
    state_machines](https://github.com/missionpinball/mpf/pull/1458) -
    avanwinkle
* [Configurable debounce times and FW 0.49+ for
    Spike](https://github.com/missionpinball/mpf/pull/1460) - jab
* [Coil priorities in hw rules for Spike FW
    0.49+](https://github.com/missionpinball/mpf/pull/1462) - densminger
    and jab
* [Placeholders in ball save
    active_time](https://github.com/missionpinball/mpf/pull/1463) -
    avanwinkle
* [Autodetect FAST
    ports](https://github.com/missionpinball/mpf/pull/1464) - avanwinkle
* [Improve robustness of LISY
    protocol](https://github.com/missionpinball/mpf/pull/1466) - jab
* [Emacs
    instructions](https://github.com/missionpinball/mpf-ls/pull/6) -
    seanirby
* [Support goto definition and hover + mode
    support](https://github.com/missionpinball/mpf-ls/pull/7) - jab
* [Basic
    diagnostics](https://github.com/missionpinball/mpf-ls/pull/8) - jab
* [Improve placeholder performance by evaluating them only when
    needed](https://github.com/missionpinball/mpf/pull/1469) - jab
* [Update ruamel.yaml to improve the install experience on
    Windows](https://github.com/missionpinball/mpf/pull/1476) - jab
* [Benchmark and tune/cache placeholder
    parsing](https://github.com/missionpinball/mpf/pull/1478) - jab
* [Priorities in ball_holds and
    ball_locks](https://github.com/missionpinball/mpf/pull/1479) -
    avanwinkle
* [Batch light for
    PD-LED](https://github.com/missionpinball/mpf/pull/1481) - jab
* [Benchmark and tune event
    performance](https://github.com/missionpinball/mpf/pull/1483) - jab
* [Extend combo_switches to include the triggering switch in the
    event](https://github.com/missionpinball/mpf/pull/1480) - avanwinkle
* [Initial Pin2DMD support (not yet
    working)](https://github.com/missionpinball/mpf/pull/1484) - jab
* [Option to ignore FAST RGB CPU
    crashes](https://github.com/missionpinball/mpf/pull/1482) -
    avanwinkle
* [Tracing for libpinproc
    calls](https://github.com/missionpinball/mpf/commit/9c7f3af27d4bdb91a67d80f6f0b43550d4607a3b) -
    jab
* [Software update via Service
    mode](https://github.com/missionpinball/mpf/pull/1487) - jab
* [Add tests for accrual
    restarts](https://github.com/missionpinball/mpf/pull/1470) - jab

## 0.52

Released: February 02, 2019

This is a 0.51 maintenance release with cleanups and some refactorings.
There should not be any breaking changes but a lot of bug fixes.

**MPF**

### New Features

* [OSC platform to control external
    lights](https://github.com/missionpinball/mpf/pull/1260) - jab based
    on [request in
    forum](https://groups.google.com/forum/#!topic/mpf-users/8JZbb_X__Rc)
* [Validate variables in
    variable_player](https://github.com/missionpinball/mpf/pull/1261) -
    jab based on [config in
    example](https://groups.google.com/forum/#!topic/mpf-users/v4b75FEQU70)
* [Placeholders for shots and
    shot_groups](https://github.com/missionpinball/mpf/pull/1262) - jab
    based on [question from mike
    wiz](https://groups.google.com/forum/#!topic/mpf-users/_EBF2tkfabI)
* [Better error messages for
    placeholders](https://github.com/missionpinball/mpf/commit/418b210e0e2bf847dcd66dbec5950d277828080c) -
    jab
* [Show proper error when fadecandy server is not
    running](https://github.com/missionpinball/mpf/pull/1263) - jab
    based on request from Brian Cox
* [Nicer output on startup
    errors](https://github.com/missionpinball/mpf/commit/55f449407d832e0bfa6f3403c19a3572ea621ee2) -
    jab
* [Show shutdown reason on exit of
    MPF](https://github.com/missionpinball/mpf/pull/1265) - jab
* [Show import error for
    pinproc](https://github.com/missionpinball/mpf/pull/1267) - jab
* [Upstream Raspberry Pi DMD
    support](https://github.com/missionpinball/mpf/pull/1269) - jab
    based on [external platform from Michael
    Betz](https://github.com/yetifrisstlama/Fan-Tas-Tic-platform)
* [Support for Spike Trough via SPI Bit
    Bang](https://github.com/missionpinball/mpf/pull/1270) - jab
* [Move libpinproc to a separate
    thread](https://github.com/missionpinball/mpf/pull/1195) - jab
* [Score Queues for SS style
    scoring](https://github.com/missionpinball/mpf/pull/1273) - jab
    based on [request in
    forum](https://groups.google.com/forum/#!topic/mpf-users/4Ecj6xtveHo)
* [Check for OPP firmware mismatch on
    start](https://github.com/missionpinball/mpf/pull/1276) - jab based
    on [bug report in
    forum](https://groups.google.com/forum/#!topic/mpf-users/umg2ZmDElog)
* [Evaluate placeholders from service
    cli](https://github.com/missionpinball/mpf/pull/1277) - jab
* [Improve USB latency for I2C in
    pypinproc](https://github.com/missionpinball/pypinproc/pull/5) - jab
    based on suggestion by rosh
* [Only enable AC relay by default during the game. Keep it off in
    attract](https://github.com/missionpinball/mpf/pull/1289) - snux
* [Ball Routing device to route balls to certain
    devices](https://github.com/missionpinball/mpf/pull/1291) - jab
* [Support for the Pololu Tic stepper
    controller](https://github.com/missionpinball/mpf/pull/1293) -
    wolfmarsh
* [Update Smartmatrix Teensy Code Example for New
    Cookie](https://github.com/missionpinball/mpf/pull/1295) -
    aaronmatthies and eli
* [Placeholders in event_player based on event
    parameters](https://github.com/missionpinball/mpf/pull/1297) -
    avanwinkle
* [Update ruamel yaml
    parser](https://github.com/missionpinball/mpf/pull/1298) - jab
* [Use newer cython to support Python
    3.7](https://github.com/missionpinball/mpf-debian-installer/commit/532d8757c078ef568b6a9d3473a1db63d35e84ef) -
    jab
* [Add Python 3.7 support to
    MPF](https://github.com/missionpinball/mpf/pull/1300) - jab

**MPF-MC**

### New Features

* [Add a segment display
    font](https://github.com/missionpinball/mpf-mc/commit/0dadad10eeaf01188e92016c90006ebb8b5b5933) -
    jab based on [example from
    BorgDog](https://groups.google.com/forum/#!topic/mpf-users/1wzjCo5pL0U)
* [Conditionals on add_to_slide
    animations](https://github.com/missionpinball/mpf-mc/pull/357) -
    avanwinkle

## 0.51

Released: November 24, 2018

This is a 0.50 maintenance release with cleanups and some refactorings.
Breaking changes in common features are minimal but some minor changes
might be required in some cases (e.g. we removed some defunctional
options). It comes with lots of performance improvements and new
settings for production machines.

**MPF**

### New Features

* [Configurable match
    number](https://github.com/missionpinball/mpf/pull/1150) - jab
* [Support I2C on the RPi via
    pigpio](https://github.com/missionpinball/mpf/pull/1159) - jab
* [Improve event
    order](https://github.com/missionpinball/mpf/pull/1160) - jab
* [Refactor
    accelerometers](https://github.com/missionpinball/mpf/issues/1155) -
    jab (breaking change)
* [Support burst IRs and local inputs/outputs on the
    P3-Roc](https://github.com/missionpinball/mpf/pull/1167) - jab
* [Validate P-Roc direct input
    numbers](https://github.com/missionpinball/mpf/pull/1172) - jab
* [Rename scriptlets to
    custom_code](https://github.com/missionpinball/mpf/pull/1148) - jab
* [Add json
    logging](https://github.com/missionpinball/mpf/pull/1178) -
    muffler-aus
* [Improve startup
    performance](https://github.com/missionpinball/mpf/pull/1179) - jab
* [Allow lists of
    flashers](https://github.com/missionpinball/mpf/pull/1183) -
    avanwinkle
* [Prevent spaces in event
    handlers](https://github.com/missionpinball/mpf/pull/1191) -
    avanwinkle (breaking change)
* [Allow float in
    timers](https://github.com/missionpinball/mpf/issues/1187) - jab
* [Major performance improvements for switch
    handlers](https://github.com/missionpinball/mpf/pull/1196) - jab
* [Major performance improvements in lights and
    shows](https://github.com/missionpinball/mpf/commit/9148c8ebc568706d1c30ef2a64710993c05d2aec) -
    jab
* [Add option to disable sound
    output](https://github.com/missionpinball/mpf/pull/1199) -
    avanwinkle
* [Support multiple I2C servo
    controllers](https://github.com/missionpinball/mpf/pull/1206) - jab
    (breaking change)
* [Improve performance without
    logging](https://github.com/missionpinball/mpf/commit/b870147b3031f4ab5cea90911269013b8d86f3ac) -
    jab
* [Add support for P3-Roc burst
    optos](https://github.com/missionpinball/mpf/commit/c98832f4e175a4cc2d1de0c546a3b9d65432aedb) -
    jab
* [Allow users to disable ball search
    rounds](https://github.com/missionpinball/mpf/commit/2ded24ac3076c877a53ed575205fe124378888e0) -
    jab
* [Define alignment for segment
    displays](https://github.com/missionpinball/mpf/issues/1201) - jab
* [Add restart_events to shots and shot
    groups](https://github.com/missionpinball/mpf/pull/1213) -
    avanwinkle
* [Add placeholder support to
    event_player](https://github.com/missionpinball/mpf/pull/1212) -
    avanwinkle
* [Prevent warnings during init and batch incandescant update for
    OPP](https://github.com/missionpinball/mpf/pull/1220) - jab
* [Improve FAST behavior during MPF
    init](https://github.com/missionpinball/mpf/pull/1221) - jab
* [Entrance switch ignore
    window](https://github.com/missionpinball/mpf/pull/1216) -
    avanwinkle
* [Improved README.md for the MPF
    project](https://github.com/missionpinball/mpf/pull/1219) -
    austinbgill
* [Prevent bad switch config for drop_targets, shots and
    autofires](https://github.com/missionpinball/mpf/pull/1227) - jab
* [Validate that ball_count for multiballs is the right
    range](https://github.com/missionpinball/mpf/pull/1229) - jab based
    on [question from
    Alex](https://groups.google.com/forum/#!topic/mpf-users/jQTwpofBysA)
* [Allow variable_players outside game modes for machine
    variables](https://github.com/missionpinball/mpf/pull/1231) - jab
* [Only reset drop target banks if a target is
    down](https://github.com/missionpinball/mpf/pull/1236) - jab based
    on [request from Mark
    M](https://groups.google.com/forum/#!topic/mpf-users/kHq3dM1PMyo)
* [Add support for flipper tapping for
    OPP](https://github.com/missionpinball/mpf/pull/1238) - jab and Hugh
    based on [forums
    discussion](https://groups.google.com/forum/#!topic/mpf-users/pKfmv_lmuDc)
* [Serial LEDs support for
    PD-LED](https://github.com/missionpinball/mpf/pull/1239) - jab with
    help from gstellenberg
* [Only send lamp updates when lamps change in
    LISY](https://github.com/missionpinball/mpf/commit/a4cd700c488f9290bd4a62cb198d188d75c30da2) -
    jab
* [mpf test can now parse example/tests from rst
    files](https://github.com/missionpinball/mpf/commit/89f05214e22bce03b7bcb2047600a11f338053ab) -
    jab
* [sw_flip_events and sw_release_events for flipper to flip from
    software](https://github.com/missionpinball/mpf/commit/9a1e6c0f41ccf53645d02804dd0f66eb387a1ee8) -
    jab based on [request from Philip
    D](https://groups.google.com/forum/#!topic/mpf-users/76BQAtIfsZc)
* [Add event handlers to start game and add
    players](https://github.com/missionpinball/mpf/pull/1244) - jab
    based on [request from Cole
    M](https://groups.google.com/forum/#!topic/mpf-users/vuUJMdSI2_A)
* [Add new mode_will_start hook for custom
    code](https://github.com/missionpinball/mpf/pull/1247) - Lamoraldus
    based on [discussion in
    forum](https://groups.google.com/forum/#!topic/mpf-users/D0W3pacTGUg)
* [Support external platforms via
    entry_points](https://github.com/missionpinball/mpf/pull/1248) - jab
* [Refresh Smartmatrix DMDs
    periodically](https://github.com/missionpinball/mpf/pull/1250) - jab
* [Support Servos on
    PD-LED](https://github.com/missionpinball/mpf/pull/1253) - jab with
    help from gstellenberg
    ([announcement](https://www.multimorphic.com/news/servo-and-stepper-motor-control-in-pd-led-v3/))
* [Support Steppers on PD-LED/New stepper device
    interface](https://github.com/missionpinball/mpf/pull/1255) - jab
    with help from gstellenberg
* [Support config specs for external platforms via
    entry_points](https://github.com/missionpinball/mpf/pull/1252) - jab

**MPF-MC**

### New Features

* [Disable multi
    touch](https://github.com/missionpinball/mpf-mc/commit/f4c19ea3ddb8a3d76351f4c7555abb35f5dae722) -
    qcapen
* [Add json logging to
    MC](https://github.com/missionpinball/mpf-mc/pull/335) -
    mfulleratlassian
* [Improve startup
    performance](https://github.com/missionpinball/mpf-mc/pull/337) -
    jab
* [Add animations based on event
    parameters](https://github.com/missionpinball/mpf-mc/commit/fc60d636409ed50ba2e8f9c03695b7b01c45d09d) -
    jab
* [Add option to disable sound
    output](https://github.com/missionpinball/mpf-mc/pull/340) -
    avanwinkle
* [Rename mc_scriptlets to
    mc_custom_code](https://github.com/missionpinball/mpf-mc/pull/347) -
    jab
* [Support other channel orders than RGB for all RGB
    DMDs](https://github.com/missionpinball/mpf-mc/issues/345) - jab
    based on [request from
    Cadrion](https://groups.google.com/forum/#!topic/mpf-users/1EtJxmAZiow)
* [Update kivy to version
    1.10.1](https://github.com/missionpinball/mpf-mc/pull/346) - jab
* [Support multiple (stacked) style values for
    widgets](https://github.com/missionpinball/mpf-mc/pull/349) -
    avanwinkle
* [Better error when showing images too
    early](https://github.com/missionpinball/mpf-mc/pull/350) - jab
    based on [question from Brian
    C](https://groups.google.com/forum/#!topic/mpf-users/iMivocg70BQ)
* [Allow widget styles to set z
    values](https://github.com/missionpinball/mpf-mc/pull/351) -
    avanwinkle
* [Update kivy
    dependencies](https://github.com/missionpinball/mpf-mc/pull/354) -
    jab
* [Reusing named
    widgets](https://github.com/missionpinball/mpf-mc/pull/353) -
    avanwinkle

**MPF-Monitor**

### New Features

* [Add config option for device size in
    monitor](https://github.com/missionpinball/mpf-monitor/commit/a348117131ae93904ef8c265eb4253b225876a8e) -
    jab
* [Improve monitor
    performance](https://github.com/missionpinball/mpf-monitor/commit/6e70bf76462a0bb21a4d272a5a4057aa3b67d3c9) -
    jab

**Others**

### New Features

* [Experimental external Philips Hue
    platform](https://github.com/missionpinball/mpf-hue-platform) - jab
    based on [code from Philip
    D](https://groups.google.com/forum/#!topic/mpf-users/e5dv9j71BUE)

## 0.50

Released: April 23, 2018

**MPF**

### New Features

* Consolidated LEDs, matrix lights, GI, and flashers into a single
    "light" device. Much cleaner, less code, and unified features
    across all light types.
* Added RGBA color support (RGB colors plus an alpha channel)
* Hardware fade support for all light (fade-in and fade-out).
* Added segmented displays support
* Added LISY hardware platform support (for Gottlieb System 1 and
    System 80 machines)
* Added MyPinballs 7 segment display support
* Added P-Roc alphanumeric displays support
* Added Raspberry Pi as a platform (remote via ethernet or local using
    pigpio)
* Added stepper motor device
* Added motor device (with position and/or end switches)
* Added Trinamics Steprocker platform
* Added SPIKE DMD support
* Support for FAST RGB DMD support
* Added digital output support (either mapped as drivers or lights)
* Added native I2C support on linux (via SMBus)
* Added NXP MMA8451 accelerometer support (via I2C)
* Support fuzz testing (to find crashes in a machine without playing
    it)
* Added PSU support to manage maximum power usage. Coil pulses can
    specify a maximum delay which is used to reorder pulses (used by
    ball devices, score reels and drop targets).
* Improved and broke out game lifecycle events (will start, starting,
    started, etc.) for game, ball, and turn starts and stops.
* Made many more settings "templatable"
* Logging to syslog
* Cleaned up and simplified shots
* Added Text UI
* Added replay credits
* Added developer documentation website (developer.missionpinball.org)
* Added support for custom named colors
* Added pluggable ejectors and ball counters in ball devices
* Added "mpf service" command to spawn a service cli (similar to
    service mode or SPIKE game cli)
* Added "mpf hardware scan" to enumerate all hardware platforms
* Added "mpf hardware update_firmware" to send firmware updates to
    all hardware platforms

**MPF-MC**

### New Features

* Major display refactoring
* Bitmap fonts
* Relative animation values
* Added widget rotation & scale animations
* Animation values respect initial anchor points
* Simplified, consolidated, & unified DMD, color DMD, and slide frame
    widgets into displays and display widgets
* New 'sound_loop' audio track type optimized for live looping music
    control driven by events. This specialized audio track type can
    synchronize playback of multiple looping sounds simultaneously in
    layers and provides gapless switching to a new set of loops. It is
    designed to build music that dynamically changes based on events in
    your game. Only supports in-memory sounds (no streaming).
* New 'sound_loop_set' asset type. A sound_loop_set is an asset used
    to play sounds in a sound_loop track that is basically a grouping of
    one or more sound assets. The sounds in a loop set are arranged in
    layers. The master layer contains the sound that establishes the
    length of the entire loop set. Whenever the sound in the master
    layer loops, all other sounds in the sound_loop_set will also loop
    back to the beginning.
* New 'sound_loop_player' config_player. The sound_loop_player is a
    config player that is used to control the playback of
    sound_loop_sets in a sound_loop audio track. The track_player can
    also be used with a sound_loop track to control volume and playback
    state.
* New 'playlist' audio track type is designed to provide a
    comprehensive set of music playing capabilities that include named
    playlists, playback mode (sequence, random, etc.), cross-fades
    between sounds/songs/playlists, and more.
* New 'playlist' asset type. A playlist is an asset used to group
    and play sound assets on a playlist track. A playlist is basically
    an ordered group of sounds/songs typically used to playback music.
* New 'playlist_player' config player. The playlist_player is a
    config player that is used to control the playback of playlists (and
    their component sounds) in a playlist track. The track_player can
    also be used with a playlist track to control volume and playback
    state.
* New sound 'about_to_finish' events (configurable for each sound).
    These post events at a specified time before the sound ends.
* New display_light_player to use your playfield lights as display
    in MC. Also supports transparency to overlay a graphic/animation
    above your light shows.

**MPF-Monitor**

### New Features

* Device list shows all monitorable attributes

## 0.33

Released: April 10, 2017

**MPF**

### New Features

* "Ball hold" device (Temporarily hold a ball while something else
    is happening)
* "Multiball lock" device (Track ball locks towards multiball,
    including virtual locks, across balls and players)
* Multiball "add a ball" feature
* Added support for Stern SPIKE platform
* [Revamped logging](../config/logging.md)
* Additional achievements control events
* BCP ports & interfaces are now configurable
* Drop target "keep up" feature (PWMs reset coil to "lock" target
    up)
* "Async" events (Events that wait for all handlers to finish before
    continuing)
* Additional multiball events
* More functions for people building games to use to write tests
* Built-in modes with code can have their code overloaded
* Added score reels to the smart virtual platform
* Allow machine variables to be set via BCP
* Allow setting default high scores
* Add "early save" events to ball saves
* Add all monitorable device properties to conditional events
* Use placeholders in mode timer start & end values
* More options for bonus (hurry ups, skip slides with 0 value,
    placeholders for score calculations, etc.)
* Improved ball search
* OPP - support for firmware 2.0 and dual wound coils
* MC scriptlets for video modes and code on the MC side
* Support for conditional events
* Template variables which are evaluated during runtime and can use
    placeholders (timers, logic_blocks, tilt, scoring, bonus_mode, and
    more)
* Early ball save
* Advanced bonus_mode
* TimedSwitch device - built-in event for flipper cradling and
    releasing
* Asynchronous logging - This is especially important on windows
    because logging previously slowed down the game. However, also
    important in production when under high I/O load or with slow discs.
* Timers work outside of the game now
* New "mpf diagnosis" command
* Scoring to machine variables
* Scoring for other players
* Weights in random_event_player
* Unlimited delay in ball_save to allow video modes or mode selection
* Added Machine vars for all kinds of versions
* Drop Target keep up support
* Multiball add a ball support
* New multiball_lock device which handles virtual saves for
    multiplayer game
* Allow BCP to bind on all IPs

**MPF-MC**

### New Features

* Added a camera widget (live video)
* Allow placeholders and settings
* Added keyboard debugging
* Added warnings if window size & display size aspect ratios are not
    the same
* MPF-MC now checks to make sure the MPF version it's talking to is
    compatible
* Change the default display size to 800x600 if a displays: section is
    not in the config
* Re-vamped Mac installation procedure. It's now a "real" install
    and does not use MPF.app anymore.
* Added a "volume" machine variable
* Added Interactive Media Controller (iMC)
* Added "anchor_y: baseline" option for text widgets
* Added gamma setting for physical DMDs
* Added new relative animation target values

## 0.32

Released: Dec 1, 2016

**MPF**

* Improved
    [achievements](../game_logic/achievements/index.md) and added
    [achievement groups](../game_logic/achievements/achievement_groups.md).
* Added relay events and relay queues
* Improved
    [smart virtual platform](../hardware/virtual/smart_virtual.md)
* Improved support for
    [System 11](../mechs/troughs/two_coil_multiple_switches.md) and
    [Gottlieb System 3 style](../mechs/troughs/two_coil_one_switch.md) troughs (including using the ball drain as a ball
    storage location to get one additional ball capacity with no
    hardware changes).
* Verify that duplicate sections don't exist in config files
* Check that event handlers are properly formatted before they're
    registered
* Added conditional events (handlers that only fire if certain
    conditions are met)
* You can
    [set starting values for player variables](../config/player_vars.md)
* Fixed the
    [physical mono DMD](../mc/displays/dmd.md) and
    [physical RGB (color) DMD](../mc/displays/rgb_dmd.md)
* Added
    [multiball lost event](../events/multiball_multiball_lost_ball.md)
* Allow devices to have inline config specs
* Added shots with events
* Better OPP platform parsing
* Fixed & improved the high score mode
* Improved service mode
* Added options for "random" events (force next, force all, save
    per-player, etc.)
* Added events to the BCP monitor (meaning they can be viewed in the
    MPF Monitor app)
* Added `-f` command line option to force all assets to load on boot
    for testing purposes
* Added scoring options (add, replace, block)
* Use color "on" for LED default colors
* Allow multiple config player entries to fire from the same event
* Ensure that events created by the MC are sent to MPF
* Added machine vars for P-ROC and FAST hardware revisions
* Added
    [combo switches](../game_logic/combo_switches.md) (for "flipper cancel", two-button skill shots, etc.)
* Lots of little bug fixes...

**MPF-MC**

* Fixed the widget z-order layering bug (this has been backported to
    0.31). Widget orders are now higher value z: settings are on top of
    lower value ones.
* Negative z: values are no longer used to target parent slide frames.
    Instead, `target: (name)` is used.
* Cleaned up debug logging so BCP frames are not included in it by
    default
* Events that are natively posted in the MC are now sent to MPF
* Fixed a bug to ensure that the slide_active event is only posted
    once per frame
* Fixed a bug that prevented slide frames from being animated
* Fixed a bug where videos were not stopping
* Allow the same slide to be used on multiple displays
* Switch to GStreamer instead of SDL_Mixer for loading and streaming
    sounds. (SDL2 still used for all sound output.)
* Sound file streaming is now supported from any track (streamed from
    disk instead of preloaded into memory)
* New "track_player" config controls sounds at the track-level
    (fade, volume, play, pause, stop, etc.)
* Custom loading & unloading events at the individual sound level.
* Lots of little bug fixes...

## 0.31

Released: Sept 19, 2016

**MPF**

* MPF is now "tickless", meaning everything runs faster, but with
    less overhead
* Improved flow control for FAST hardware serial communication
* Improved BCP communications
* Improved serial communications for all devices which use serial
* Additional options for ball saves
* Removed many threads which makes everything simpler and faster under
    the hood
* Improved "virtual" and "smart virtual" platforms
* Prevent broken data files from crashing MPF
* Added a basic service mode (this is just a start, much more to come)
* Detect balls that jump between playfields
* Prevent duplicate rules being written to P-ROC and P3-ROC
    controllers
* Allow mode config files to be broken into multiple files
* Allow multiple multiball modes to run at once and add options for
    how it tracks them
* Allow ball locks to wait for a ball to drain before releasing their
    locked balls
* Added the ability to use matrix lamps/LEDs at individual channels
    for RGB LEDs
* Re-added high score mode (Which was in 0.21 and removed in 0.30)
* OPP platform improvements
* Improved error messages for config file errors
* Improved the way the "mpf both" command works on all platforms
* Added ability to step backwards in shows
* Refactored and improved show player
* Added ball search for servos
* Added default colors to RGB LEDs
* Added support for nested shows
* Added the "LED Group" device (am easily-configured strip of LEDs
    which can be strobed, pulsed, etc.)
* Added kickback mechanisms
* Added magnets
* Added blocking show queues
* Many bug fixes...

**MPF-MC**

* Audio library improvements (sound fading, markers, start position,
    instance limiting, ducking improvements)
* Allow widget events based on when slides are shown, hidden, etc.
* Improved error if you try to target a widget to an invalid slide
* Added default DMD fonts
* Many bug fixes...

## 0.30

Released: July 15, 2016

* Python 3 required
* Mac OS X support
* The Media Controller is now a separate package from MPF
* The MPF-MC has been completely rewritten from scratch (based on
    Kivy, SDL2, OpenGL, and Gstreamer)
* GPU is used for graphics
* Brand-new audio interface specifically written for pinball audio,
    which includes advanced feature like ducking, attack, attenuation,
    etc.
* Proper Python package installers, and inclusion in PyPI so install
    can be done via *pip*.
* System-wide *mpf* launcher utility with pluggable commands
* New MPF clock module replaces the old timing and timers
* All shows are driven by MPF
* Show content is "played" by the standard config_players
* Playlists become shows
* "Tocks" are gone, shows now operate on real-world time
* Light scripts are gone, replaced by placeholder "tokens" in shows
* Named colors
* Hardware accelerated LED fades
* Asset Pools
* Ball Search
* Accelerometer-based tilts
* Servo support
* Text string support
* Player achievements

## 0.21

Released: Dec 1, 2015

* SmartMatrix "real" RGB LED Color DMD support.
* System 11 support.
* High Score mode.
* Credits mode.
* Tilt mode.
* Smart virtual platform. (This is the new default platform.)
* New display elements: Character Picker and Entered Characters.
* Devices can be created and changed per mode.
* Machine variables.
* Untracked player variables.
* Central config processor, data manager, file manager, and file
    interfaces. This paves the way for config files in formats other
    than YAML.
* Added support for combo manual/auto plungers.
* Events for ball collection process.
* Driver-enabled devices.
* External light shows, controllable via BCP. (Thanks Quinn Capen!)
* Created a starter game machine config template you can use for your
    own machines.
* Started adding unit tests. (We're at the very beginning of this,
    but we have full coverage of the ball device, the event manager, and
    the tutorial configuration files.)
* Rewritten driver/coil device interface.
* Rewritten ball device and ball controller code. (Thanks Jan
    Kantert!)
* Rewritten score controller.
* Rewritten display & slides modules.
* Many improvements and features added to ball saves.
* Python 2.7 is now required. (Previous releases would also run on
    Python 2.6)
* Logic blocks can now persist between balls
* Fixed & enhanced the asset loading process.
* Many improvements and features added to modes and the mode
    controller
* Multiple config files can be chained together at the command line
* Improved text display element.
* Improved event manager and event dispatch queue
* Moved all utility functions to their own class.

## 0.20

Sept 14, 2015

* The *targets* and *shots* modules have been combined into a single
    module called *shots*.
* The new shots module adds several new features, including:
    * Shots can be members of more than one shot group, and added and
        removed dynamically.
    * Sequence shots can track more than one simultaneous sequences.
        (e.g. two balls going into an orbit at essentially the same time
        will now count as two shots made.)
    * Shots are mode-aware and will automatically enable or disable
        themselves based on modes starting and stopping.
* Modes now work outside of a game.
    * "Machine modes" have been removed. Attract and game machine
        modes are now regular modes.
    * This makes it easier to have always-running modes (volume
        control, coin door open, coin & credit tracking).
    * This makes it possible to configure custom branching of
        mode-flow logic. (i.e. long-press the start button to load a
        different game mode, etc.)
* Significant performance improvements for both starting MPF and
    starting a game:
    * Reading the initial states of switches on a P-ROC is
        significantly faster.
    * The auditor now waits a few seconds before writing its audit
        file, and it does it as a separate thread. Previously this was
        slowing down the game start and player rotation events.
    * The way modules that need to track "all" the switches (like the
        auditor and OSC) was changed and now it doesn't bog things down.
* A device manager now manages all devices. (This will enable future
    GUI apps to easily be able to browse the device tree.)
* Devices can be "hot added" and removed while MPF is running. This
    includes automatic support to add and remove devices per mode.
* All device configuration is specified and validated via a central
    configuration service. This has several advantages:
    * The config files are now validated as they're loaded. For
        example, if there a device has a settings entry for "switches",
        MPF will now validate that the strings you enter in the are
        actual switch names. It will give you a smart error if not.
    * This paves the way for supporting config files in formats other
        than YAML. (JSON, XML, INI, etc.)
    * This led to the removal of about 500 lines of code since all the
        config processing was done manually in each module before.
    * The config processing is more efficient and less-error prone
        since it's not written from scratch for each module.
    * There's now a master list (in [mpfconfig.yaml](#)) of
        all config settings for all device types.
    * The config processor and validator can run as a service to
        support the back-end business logic behind future GUI tools
        which could be used to build machines.
    * If you're configuration has an unrecognized setting, the config
        validator will load the config file migrator to tell you what
        the updated name is for the section it doesn't recognized.
* Shot rotation has been improved:
    * You can now specify the states of shots you'd like to include or
        exclude. (i.e. only rotate between incomplete shots.)
    * You can specify custom rotation patterns (i.e. a "sweep"
        back-and-forth instead of a simple left or right rotation)
* A ball lock device was added to make it easy to specify ball locks.
* A multiball device was added.
* A simple ball save device was added.
* Created a "random_event_player" that lets you trigger random events
    based on another event being posted.
* Centralized debugging
* Drop targets and drop target banks have been simplified and
    separated from shots.
* The states of switches tagged with 'player' will be passed to the
    game start mode, allowing branching based on which combinations of
    switches were held in when the start button was pressed. (The amount
    of time the start button was held in for is also sent.)
* Official support for multiple playfields via config files
* Added x, y, and z positions to lights and leds
* Exposed wait queue events to mode configs, allowing code-less
    creation of modes that can hook into game flow (bonus, etc.)

## 0.19

Released: August 6, 2015

* Completely rewritten target and drop target device module,
    including:
    * Per-player state tracking for targets
    * Target "profiles" that control how targets behave, completely
        integrated with the mode system
* Light show "sync_ms" which allows new light shows to sync up with
    existing running shows.
* Timed switch events can be set up via the config files.
* Added "recycle_time" to switches. (Switches can be configured to not
    report multiple events until a cool-down time has passed.)
* Created an events_player module
* Player variables in slides automatically update themselves when they
    change. (No more need to find an event to tie the slide to in order
    for it to update!)
* Device control events exposed via the config files
* Automatic control of GI
* Activation and deactivation events can be automatically created for
    every switch.
* Allow multiple playfield objects to be created at once (for
    head-to-head pinball)
* Added support for FAST Pinball's new WPC controller
* Added a Linuxshell script to launch mc.py and mpf.py
* Created the config file migration tool
* Added per-timer debug loggers
* Standardization of many non-standard config file naming conventions
* Color logging to LEDs
* Added P3-ROC switch test tool
* Added reset to mode timer action list
* Added restart feature to mode timers
* Flipper Device: Add debug logging to rules
* FAST:Added minimum firmware version checking for IO boards
* Added "restart" method to logic blocks
* Text display element min_digits
* Allow system modules to be replaced and subclassed
* Added configurable event names for switch tag events
* Added callback kwargs to switch handlers
* Added light and LED reset on machine mode start
* Added default machine and mode delay managers

## 0.18

Released: June 2, 2015

* FadeCandy and Open Pixel Control (OPC) support. This means you can
    use a FadeCandy or other OPC devices to control the LEDs in your
    machine.
* Rewritten FAST platform interface. It's now "driverless," meaning
    you no longer need to download and compile drivers to make it work.
* Added support to allow multiple hardware platforms to be used at
    once. (e.g. LEDs can be from a FadeCandy while coils are from a
    P-ROC.) You can even use multiple different platform interfaces for
    the same types of devices at once (e.g. some LEDs are FadeCandy and
    others are FAST).
* Added support for GI and flashers to light shows
* Added activation and deactivation events to switches
* Added support for sounds in media shows
* Added per-sound volume control
* Added support for P-ROC / P3-ROC non-debounced switches
* Exceptions and bugs that causeMPF to crash are now captured in the
    log file. (This will be great for troubleshooting since you can just
    send your log. No more needing to capture a screenshot of the
    crash.)
* If a child thread crashes, MPF will also crash. (Previously child
    threads were crashing but people didn't know it, so things were
    breaking but it was hard to tell why.)
* MPF can now be used without switches or coils defined. (Makes
    getting started even easier.)
* "Preload" assets loading process is tracked as MPF boots, allowing
    display to show a countdown of the asset loading process
* Added *restart_on_complete* to mode timers
* Smarter handling of player-controlled eject requests while existing
    eject requests are in progress
* *eject_all()* returns *True* if it was able to eject any balls
* Playfield "add ball" requests are queued if there's a current player
    eject request in progress
* Created a smarter asset loading process
* The attract mode start is held until all the "preload" assets are
    loaded
* Updated how the game controller tracks balls in play

## 0.17

Released: May 4, 2015

* Broke MPF into two pieces: The MPF core engine and the MPF media
    player
* Added support for the Backbox Control Protocol (BCP)
* Added device-specific debugging for LEDs.
* Added version control to config files.
* Added volume control.
* Switches that you want to start active when using virtual hardware
    are now added to the [virtual platform start active
    switches:](#) section instead of being a property of the
    [keyboard:](#) entry.
* Converted several former plugins to system modules, including shots,
    scoring, bcp, and logic blocks.
* General performance improvements. (Running MPF on my machine used to
    take about 50% CPU. Now it's down to 15%.)

## 0.16

Released: April 9, 2015

* Added slide "expire" time settings to the Slide Player.
* Added *Demo Man* as the sample game code.
* Added start_time configuration parameter for music in the
    StreamTrack
* Added the SocketEvents plugin
* Created the LightScripts and LightPlayer functionality.
* Change light script "time" to "tocks"
* Created a centralized config processing module

## 0.15

Released: March 9, 2015

* Added support for game modes.
* Converted several existing modules to be mode-specific, including:
    * LogicBlocks
    * SoundPlayer
    * SlidePlayer
    * ShowPlayer
    * Scoring
    * Shots
* Created an Asset Manager and converted the images, animations,
    sound, and show modules to use it instead of each handling their own
    assets.
* Created an asset loader which creates a background thread to load
    each type of asset.
* Added an AssetDefaults section to the asset loader to specify
    per-folder asset settings
* Created a universal player variable system
* Added movie support (for playing MPEG videos on the LCD and DMD).
    They're available as a standard display element type which means
    they can be positioned, layered as backgrounds, etc.
* Created a generic ModeTimers class that can be used for timed modes
    and goals. (With variable count rates, support for counting up and
    down, multiple actions which can start, stop, pause, and add time,
    etc.)
* Changed logic blocks so they maintain all their states and progress
    on a per-user basis.
* Added a "double zero" text filter. (Used to show zero-value scores
    as "00" instead of "0".)
* Updated the display code so that it doesn't show a slide until all
    that slides assets have been loaded.
* Renamed the "sphinx" folder to "docs".
* Broke the three phases of machine initialization into 5 phases.
* Created the mode timer
* Renamed the "HitCounter" logic block to "Counter" and updated it
    to be more flexible so it can track general player-specific counts
    (both up and down), for example, total shots made, combos, progress
    towards goals, etc.
* Changed window section of config so it uses the slide builder.
* Added the ability to control lights and LEDs by tag name in shows.
* Modified the switch controller so events from undefined switches
    simply log a warning rather than raises an exception and halting
    MPF.

## 0.14

Released: February 9, 2015

* Completely rewritten ball controller.
* Completely rewritten ball device code.
* Major updates to the diverter device code.
* Creation of a new playfield module that's responsible for managing
    the playfield and any balls loose on it.
* Completely rewrote the "player eject" logic. (This is what happens
    when the game needs to wait for the player to push a button to eject
    a ball from a device.)
* The ball search code was moved from the game controller to the
    playfield device module.
* Different types of events were broken out into their own methods.
    For example, to post a boolean event, instead of calling
    [event.post(type='boolean')](#), you now use
    [event.post_boolean()](#). There are similar new methods
    for other event types, like [post_relay()](#) and
    [post_queue()](#).
* Added a debug option for ball devices which enables extra debug
    logging for problem devices.
* Tilt status was removed from the machine controller. (It was
    inappropriate there. Tilt is a game-specific thing, not a
    machine-specific thing.)
* Virtual Platform: default NC switch states fixed

## 0.13

Released: January 16, 2015

* Major update to the sound system, including:
    * Support for multiple sound tracks ("voice", "sfx",
        "music", etc.), each with their own channels, settings,
        volume, etc.
    * Using background threads to automatically load sound files from
        disk in the background without slowing down the main game loop.
    * Support for streaming sounds from disk versus preloading the
        entire sounds in memory.
    * Support for sound priorities and queues, so sounds can pre-empt
        other sounds if they have a higher priority.
    * System-wide volume control with settable steps.
* Support for the v1.0 update of FAST Pinball's libfastpinball
    library. (Basically we updated the FAST platform interface to
    support their latest firmware and drivers)
* Support for flashers. (Previously flashers were just driven like any
    other driver. Now they are their own device with their own
    flasher-specific settings.)
* Game Controller: Changed the player rotate routine to be driven from
    the game_started event so the player object isn't actually set up
    until the game has finished being set up.
* Pygame: Moved the Pygame event loop to the machine controller and
    out of the window manager. This lets us use Pygame events even if we
    don't have an on screen window. (This is needed for the sound
    system.)
* Display: Moved the SlideBuilder instantiation earlier in the boot
    process so it's available to other modules who want to use it when
    they're starting up. This will let us get the "loading" screen up
    earlier in the boot process.
* Switch Controller: Added a method to dump the initial active states
    of switches to the log. This is needed for our automated log
    playback utility so it can set the initial switches properly.
* Ball Devices: fixed a typo on the cancel ball request event

## 0.12

Released: December 31, 2014

* Added full display and DMD support, with support for physical DMDs,
    on screen virtual DMDs, color DMDs, and high res LCD displays.
* Added transitions which flip between display slides with cool
    effects.
* Added decorators which are used to "decorate" display elements
    (make them blink, etc.)
* Added display support to shows so that shows can now combine display
    and lighting effects
* Added a Slide Builder which can assemble slides from text, image,
    animation, and shapes from shows and the config files.
* Added a SlidePlayer config setting which can show slides based on
    MPF events
* Modified the Virtual DMD display element so that it can render on
    screen DMDs that look more like real pixelated DMDs
* Added a font manager that lets you define font names and specify
    default settings (sizes, antialias, color, etc.)
* Added TrueType font support
* Added support for stand image types to be displayed on the DMD
* Added .dmd file type support for images and animations
* Addedthe OSC Sender tool
* Added the Font Tester tool
* Added the multi-language module which can replace text strings with
    alternate versions for multi-language environments and other (e.g.
    "family-friendly") text replacements
* Improved the diverter devices so they have knowledge of what ball
    devices and diverters are upstream and downstream, allowing them to
    automatically activate and deactivate based on where balls need to
    go.
* Improved the ball device class so ball devices are smarter about how
    they interact with target devices. (e.g. a ball device will
    automatically eject a ball if its target device wants a ball.)
* Added support for the P3-ROC
* Added many more events
* Modified displays so they can each have independent refresh rates

## 0.11

Released: December 1, 2014

* Created a Display Controller module which is responsible for
    handling all interactions with all types of displays, including DMD,
    LCD, alphanumeric, 7-segment, etc.
* Created a DMD display module which controls both physical DMDs as
    well as on screen representations of physical DMDs
* Created a Window Manager, a centralized module which manages the on
    screen window, including full screen and resizable support
* P-ROC platform interface: Built the DMD control code
* FAST platform interface: Built the DMD control code
* Switched from Pyglet to Pygame
* Created a Sound Controller
* Created a Game Sounds plug-in that lets you control which sounds are
    played and looped based on MPF events
* Added PD-LED support
* Added support for P3-ROC SW-16 switch boards
* Switch Controller: Added verify_switches() method which verifies
    that switches are in the hardware state that MPF expects.
* Switch Controller: Adding logging so it can track when duplicate
    switch events were received
* LEDs: added on() and off() methods and "default color" support
* Ball Device: created _ball_added_to_feeder() and made it so the
    device watches for a ball entering and will request it if it needs
    it.
* Changed the command line options so you don't have to specify the
    .yaml extension for your configuration file
* Changed the command line options so you (optionally) don't have to
    specify the "machine_files" folder location
* Created default machine_files folder location settings in the config
    file
* Added support for absolute or relative paths in the command line
    options
* Added support for X/Y coordinates to LEDs and Lights for future
    light show mapping awesomeness.
* Created an early, early version of the Playfield Lights display
    interface which lets you "play" Pygame shows on your playfield
    lights
* Added system default font support
* Added a player number parameter to the player_add_success event
* Added a default MPF background image for the on screen window
* Added many more default settings to the system default
    mpfconfig.yaml file
* Virtual platform interface: Updated it so that it works when
    hardware DMDs are specified in the config files

## 0.10

Released: October 25, 2014

* Added enable_events, disable_events, and reset_events to devices.
* Removed the First Flips plug-in. (Since the thing above replaces it)
* Added support for network switches and drivers for FAST Pinball
    controllers.
* Added support for multiple USB connections to FAST Pinball
    controllers to separate main controller traffic from RGB LED
    traffic.
* Changed default debounce on and off times to 20ms for FAST Pinball
    controllers.
* Individual targets hit in target groups will now post events
* Changed the default show priority to 1 so it will restore lights
    that weren't set with a priority by default
* Driver: Added a power parameter to driver.pulse()
* Score Reel: Added resync events to individual reels
* Score Reel: Changed repeat_pulse_ms config setting to
    repeat_pulse_time.
* Score Reel: Changed hw_confirm_ms config setting to hw_confirm_time.
* Changed default pulse time for all coils to 10ms
* Coils: (Fast): Added separate debounce_on and debounce_off settings
* Info Lights: Forced game_over light to off when game starts
* LEDs: Added force parameter to the off() method

## 0.9

Released: October 7, 2014

* Added a "Logic Blocks" plug-in which lets game programmers build
    flowchart-like game logic with the config files. No Python
    programming required!
* Created a "First Flips" plug-in which you can use to get your
    machine flipping as fast as possible. (This was written as part of
    our Step-by-Step Tutorial for getting started with MPF.)
* Added Tilt and Slam Tilt support. (This is built via our Logic
    Blocks, so they're very advanced, supporting grouping multiple quick
    hits as a single hit, settling time (to make sure the plumb bob is
    not still swinging when the next ball is started, etc.).
* Added Extra Ball / Shoot Again support
* Created OSC interfaces for /audits
* MAJOR rewrite to the ball controller and ball device modules
* Created a non-instrumented optimized software loop which is as lean
    as possible if you're running your game on a slow computer. (I'm
    looking at you Raspberry Pi!) Note: other single board computers are
    fine, like the BeagleBone Black or the ODOID, but man the Pi is
    slow.
* Added the ability to pull "data" from MPF via the OSC interface, so
    we can put player scores, ball in player, etc. on an iPhone, iPad,
    or Android device.
* Added an OSC audit interface so you can view audit data via your
    mobile device.
* Created an "Info Lights" plug-in which turns on or off lights
    automatically based on things that happen in the game. (Which player
    is up, current ball, tilt, game over, etc.) This is typically used
    in EM games, but of course the plug-in can be used wherever you need
    it.
* Finished the code for our Big Shot EM-to-SS conversion. This is
    included as a sample game in MPF, so you can see our config files
    and
* Logic Blocks which can be helpful when creating your own game.
* Fixed up drop targets to support the new lit/unlit scheme
* Added support for default states to targets and target groups (stand
    ups, rollovers, drop targets, etc.), including events that are
    posted when they are hit while lit or unlit, and the ability to
    light or unlight them via events
* Added Start Button press parameters which are automatically sent to
    the game when the start button is pressed. This is for things like
    how long the button was held and what other buttons where active at
    the time. (Start \* Right Flipper, etc.)
* Added a "pre-load check) to plug-ins that allows them to test
    whether they're able to run before they load and only load if
    everything checks out. (This means that a plug-in will no longer
    crash if a required Python module is missing.)
* Added 'no_audit' tag support. (If you add 'no_audit' as a tag to a
    switch, then the Auditor will not include that switch in the audit
    logs.)
* Created Action Events for shutting down the machine and added
    shutdown tag support (so you can cleanly shut down the machine
    simply by posting and event or pressing a button which is tagged
    with "shutdown")
* Added performance data logging to the machine run loop (so it now
    tracks the percentage of time spent doing MPF tasks, hardware tasks,
    and idle).
* Added a reload() method to Shows which causes that show to reload
    itself from disk. This is nice for testing shows since you can
    reload them without having to restart the machine each time.
* Added support for null steps in shows (literally a step that
    performs no action). This makes it easier to get timing right for
    music shows.
* Added the ability to force a light or LED to move to a given state,
    regardless of its current priority or cache.
* Added a method to test whether a device is valid. This will be used
    for our config file validator
* Added option for restart on long start button press
* Added option to allow game start with loose balls
* Score reels maintain a valid status, allowing other modules to know
    whether the score reels are showing the right data or not.
* Score reels now post an event when they're resyncing, allowing other
    modules to act on it. (For example the score reel controller uses
    this to turn off the lights for a score reel while it's resyncing.)
* Added option to remove all handlers for an event regardless of what
    their registered \*\*kwargs are.
* Added mpf command line options for verbose to console and optimized
    loops. (Now we can support different logging levels to the console
    and log file, meaning you can configure it so you only see important
    things on the console but you can see everything in the log file.)
* Added light on/off action events
* Added action events and methods to award the extra ball
* Created ball device disable_auto_eject() and enable_auto_eject()
    methods. This is how we handle player-controlled ejects (like when a
    ball starts or they're launching a ball out of a cannon).
* Changed scoring from "shots" to "events"
* Changed the hardware rules for clearing a rule so it disables any
    drivers that were currently active from that rule
* Updated are_balls_gathered() so that if you pass it a tag which
    doesn't exist, it always returns True
* Added management of switch handlers to machine modes so they can be
    automatically removed
* Changed switch handlers so they process delays from new handlers
    that are added
* Removed "standup" target device type (it was redundant with
    "target")
* Moved auditor, scoring, and shots out of system and into plugins

## 0.8

Released: September 15, 2014

* Platform support for FAST Pinball hardware
* RGB LED support, including settings colors and fades
* Created target and target group device drivers for drop targets,
    standups, and rollovers (including events on complete, lit shot
    rotation, etc.)
* Created an OSC interface to view & control your pinball machine from
    OSC client software running on a phone or tablet
* Changed our "light controller" to a "show controller" and added
    support for things other than lights (like coils and events). So now
    a show can be a coordinated series of lights, RGB LEDs, coil
    firings, and events.
* Created an "event triggers" plugin which lets you configure series
    of switches that trigger events, including custom timings, decays,
    and resets. (We use this for our titlt functionality but it's useful
    in other ways too.)
* Created the auditor module
* Created an intelligent diverter device driver (with hardware switch
    trigger integration)
* Created GI device drivers
* Created a system-wide MPF 'defaults' configuration file
* Created templates for new machines, new scriptlets, and new plugins
* Modified the on screen window to become a "real" LCD display plugin.
* Renamed "hacklets" to "scriptlets"
* Created a scriptlet parent class to make them even easier to use
* Broke the hardware module into "platforms" and "devices"
* Major rewrite of how the machine controller loads system modules and
    devices
* Shows now auto load
* Added the ability to attach handlers to lights so you can receive
    notifications of light status changes
* Reworked the EM score reel update process to simplify and streamline
    it

## 0.7

Released: September 4, 2014

* Support for lights and light shows.
* An on-screen display of game metrics like score, player, and ball
    number.
* A "hacklet" extension architecture which lets you add python code to
    finish up the "last 10%" of your game that you can't control via the
    machine configuration files.
* A formal plug-in architecture which allows easy creation and
    modification of plug-ins that will survive core MPF framework
    updates.
* Cleaned up the machine flow and made that controllable via the
    config files
* Changed the -x command line option so it doesn't use fakepinproc,
    got rid of the p_roc methods that detected fakepinproc. (Now even
    with the P-ROC platform it will use our virtual platform interface
    when no physical hardware is present. This means you don't need
    pyprocgame to use fakepinproc.
* Changed the command line options to break out machine root from
    config files
* Moved command line options to their own python dictionary
* Changed time.clock() back to time.time() since clock was not real
    world which affected the light shows
* Created new events to capture start and stop of machine flow modes
* Added light support to P-ROC platform interface
* Reorganized the machine files into machine-specific subfolders
* Created an int_to_pwm() static method in Timing

## 0.6

Released: August 19, 2014

* Addition of a Shot Controller, allowing you to configure and group
    switches which become shots in the machine. (Read more about the
    concept of shots in our blog post from last week.)
* Addition of a Scoring Controller, allowing you to map score values
    to shots (and general scoring support for the machine).
* Addition of the Score Reel Controller, Score Reel devices, and Score
    Reel Group devices for mechanical score reels in EM-style machines.
    (Details here.)Switched entire framework timing over to real time
    system clock times (time.clock()) instead of ticks (for delays,
    tasks, switch waits, etc.)
* Changed ball controller that if it counts more balls than it thought
    it had, it will invoke ball_found()
* Changed the switch controller so it will ignore new switch events if
    they come in with the current status the switch already is
* The switch controller will ignore repeat switch events from the
    hardware if they are the same state that the switch was in before
* Added chime support for EM-style machines
* Changed game_start event to a queue
* Change game_start event name to game_starting (some of these entries
    might seem trivial, but I also use this list to track the changes I
    need to make to the documentation)
* Created a queue for adding new tasks so our set won't change while
    iterating

## 0.5

Released: August 5, 2014

* Created a single device parent class that's used for all devices.
* Rewrote and cleaned up devices. Now coils, switches, and lights are
    all devices, as are the more complex ones.
* Added "events" to the keyboard interface. This means you can use the
    keyboard to post MPF events (along with parameters).
* Separated out ball live confirmation and valid playfield
* Built a bunch of valid playfield methods
* Changed ball_add_live_request from direct calls to events so they'd
    be slotted in properly
* Broke valid playfield out into its own module
* Made the ball device "entrance" switch work
* Built a quick "coil test" mode
* Added kwargs to event handlers (meaning you can register a handler
    with kwargs)
* Figured out how to handle the "first time" counts of ball devices
* Added checks to attract mode to make sure all balls are home, and to
    the ball controller to prevent game start if all balls are not home
* Changed ejects to events. (So if you want to request that a device
    ejects a ball, you post an event rather than calling the device)
* Changed the balldevice_name_eject_request to be the event you use to
    call it, rather than the notification of the eject attempt.
* Created a get_status() method for ball devices
* Created a gather_balls() method and wrote the code that will send
    all the balls home before a game can be started.
* Updated stage_ball() code so it didn't ask for another ball if there
    was already an eject in progress
* Moved detection of how balls fall back in out of devices and into
    the events that watch for the entrance
* Create player and event based ejects. (This is a system to allow
    players or events to eject balls from ball devices. Useful for
    cannons like in STTNG.)
* Got stealth and auto eject out of the ball device code since they
    shouldn't care about that.
* Rewrote a lot of the ball device stuff.
* Added a manual eject capability for devices without eject coils
* Moved around some things between the ball controller and ball
    devices so that everything lives where it 'makes sense'
* Added method to check whether an event has any handlers registered
    for it.
* Ball devices now post events based on tags when balls enter them
* Ball devices can now eject their ball if no event is registered.
    This will prevent balls from getting "stuck" in unconfigured devices
    and will make prototyping on new machines faster.
* Changed event logging to show "friendly" names of handlers
* Converted flippers to use a config dictionary instead of variables
* Cleaned up the eject confirmation and valid playfield functionality
* Added a remove_switch_handler method to the switch controller

## 0.4

Released: July 25, 2014

* MAJOR rewrite of how the hardware platform modules interact with the
    framework's hardware module and how hardware is configured in
    general. It's way simpler and cleaner now. :)
* Created a parent class for Devices
* Cleaned up the way hardware objects use their parent class
* Fixed the ball controller so it doesn't get confused on the initial
    count after machine start up.
* Cleaned up switch processing and added a logical parameter so we
    only have to do all the conversion for NC or NO in one place
* Renamed the none interface to virtual. Rewrote it with the new
    platform interface way of working.
* Added support for holdPatter in coils
* Change add_live() to use tags instead of the plunger device
* Made it so many things, like ball search, autofires, etc. would not
    crash the machine if they weren't there.

## 0.3

Released: July 16, 2014

* Changed the way config files are loaded by making Config a normal
    section of any config file instead of using a special initial
    configuration file that did nothing but point to additional files.
    Details here.
* Created a virtualhardware platform for virtual / software only
    testing that does not require P-ROC or FAST drivers.

## 0.2

Released: July 11, 2014

* Added docstring documentation
* Added /sphinx folder and got the sphinx html docs included
* Created the first version of the documentation

## 0.1

Released: June 27, 2014

* Command line parameters to select real or fake (simulated)
    controller hardware.
* Command line parameters to select logging level
* Command line parameters to select the location of the initial config
    file
* Reads an initial config file which is a list of additional config
    files
* Processes those config files in order to build a config dictionary
* All platform-specific hardware code is isolated into its own module.
    Config files specify which platform is used. All game code is
    100%interchangeable between platforms.
* Game loop runs with configurable loop rate. System timer tick event
    is raised every tick.
* Periodic and one-time use timers can be setup
* Switches, Coils, Lamps, and LEDs are read in and configured from the
    config files
* Switch events are read from the hardware
* Driver commands can be sent to the hardware
* Autofire drivers are automatically configured from the config files.
    They can be enabled, disabled, and reconfigured as needed.
* Flippers are automatically configured based on config files. They
    can use EOS or not, and be based on two coils (main/hold) or one
    coil with pulse+pwm. Multiple coils can be connected to the same
    switch, and vice-versa.
* The computer keyboard can be used to simulate switch presses. Key
    map configuration information is stored in the config dictionary. It
    supports momentary, toggle (push on / push off), and inverted (key
    press = open) key modes. Also supports combo key mapping (Shift,
    Ctrl, etc.)
* A switch controller receives all notifications of debounced hardware
    switch events.
* Can specify timed switch modes that trigger certain methods. (i.e.
    do blah() when switch_1 is active for 500ms.)
* Event manager handles system events, including registering handlers,
    priorities, aborting events, and maintaining a queue.
