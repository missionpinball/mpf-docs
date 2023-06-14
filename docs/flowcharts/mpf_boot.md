---
title: MPF Boot Up / Start Up Sequence
---

# MPF Boot Up / Start Up Sequence


The first phase of operation of MPF is the start up sequence which is
basically everything that takes from from the time you run `mpf` until
the time your machine is up and running in attract mode. We're not
going to list every single detail here---to see that just look at a log
file generated in verbose mode---but this should give you a pretty high
level gist:

1.  Loads the configuration from file:
    `<your MPF project root>/mpf/mpfconfig.yaml`

2.  Loads the machine config file you specified in the command line.
    Note that this config file may load other config files.

3.  Sets the default hardware platform. (FAST, P-ROC, OPP, SPIKE,
    virtual, etc.)

4.  Loads the system modules. The exact order is specified in
    `mpfconfig.yaml`. Currently it's:

    1.  config_processor
    2.  timing
    3.  event manager
    4.  mode controller
    5.  Device manager

        1.  Device modules are loaded
        2.  Machine-wide devices are created

    6.  switch controller
    7.  ball controller
    8.  light controller
    9.  bcp
    10. logic blocks
    11. variable player/scoring
    12. shot profile manager

5.  System events are registered (for things like shutdown, quit, etc.)

6.  Posts the event *init_phase_1* .

    1.  The event player is initialized

7.  Posts the event *init_phase_2* .

    1.  The ball controller configures eject targets
    2.  The playfield configures eject targets
    3.  Score reels configure their switches
    4.  BCP sets up connections
    5.  The switch controller sets up switch events
    6.  The device manager registers all the control_events for
        machine-wide devices

8.  Plugins are loaded

9.  Posts the event *init_phase_3* .

    1.  The ball lock devices initialize
    2.  Diverters register for switches
    3.  The shot profile manager registers shot profiles

10. Scriptlets are loaded

11. Posts the event *init_phase_4* .

    1.  Drop targets update their states from their switches
    2.  The auditor initializes
    3.  OSC starts
    4.  The asset managers start loading machine-wide assets
    5.  The mode controller processes and loads all the modes

12. Posts the event *init_phase_5* .

    1.  The light controller processes machine-wide light scripts and
        light player entries

13. The machine controller's `reset()` method is called.

14. Reset posts the event *machine_reset_phase_1*.

    1.  Ball devices initialize their switches
    2.  BCP sends the reset command to any attached media controllers

15. Reset posts the event *machine_reset_phase_2*.

    1.  The ball controller updates its count of known balls
    2.  Ball devices configure their eject targets

16. Reset posts the event *machine_reset_phase_3*.

    1.  Ball locks are reset
    2.  Drop targets are reset
    3.  Drop target banks are reset
    4.  GI is enabled
    5.  Multiball devices are reset
    6.  The attract mode starts as its a registered handler for
        *machine_reset_phase_3* .
