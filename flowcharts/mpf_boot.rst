MPF Boot Up / Start Up Sequence
===============================

The first phase of operation of MPF is the start up sequence which is
basically everything that takes from from the time you run
``mpf`` until the time your machine is up and running in attract mode.
We're not going to list every single detail here—to see that just look
at a log file generated in verbose mode—but this should give you a
pretty high level gist:

#. Loads the configuration from file: ``<your MPF project
   root>/mpf/mpfconfig.yaml``
#. Loads the machine config file you specified in the command line.
   Note that this config file may load other config files.
#. Sets the default hardware platform. (FAST, P-ROC, OPP, SPIKE, virtual, etc.)
#. Loads the system modules. The exact order is specified in
   ``mpfconfig.yaml``. Currently it's:

    #. config_processor
    #. timing
    #. event manager
    #. mode controller
    #. Device manager

        #. Device modules are loaded
        #. Machine-wide devices are created

    #. switch controller
    #. ball controller
    #. light controller
    #. bcp
    #. logic blocks
    #. scoring
    #. shot profile manager

#. System events are registered (for things like shutdown, quit, etc.)
#. Posts the event *init_phase_1* .

    #. The event player is initialized

#. Posts the event *init_phase_2* .

    #. The ball controller configures eject targets
    #. The playfield configures eject targets
    #. Score reels configure their switches
    #. BCP sets up connections
    #. The switch controller sets up switch events
    #. The device manager registers all the control_events for machine-
       wide devices

#. Plugins are loaded
#. Posts the event *init_phase_3* .

    #. The ball lock devices initialize
    #. Diverters register for switches
    #. The shot profile manager registers shot profiles

#. Scriptlets are loaded
#. Posts the event *init_phase_4* .

    #. Drop targets update their states from their switches
    #. The auditor initializes
    #. OSC starts
    #. The asset managers start loading machine-wide assets
    #. The mode controller processes and loads all the modes

#. Posts the event *init_phase_5* .

    #. The light controller processes machine-wide light scripts and light
       player entries

#. The machine controller's ``reset()`` method is called.
#. Reset posts the event *machine_reset_phase_1*.

    #. Ball devices initialize their switches
    #. BCP sends the reset command to any attached media controllers

#. Reset posts the event *machine_reset_phase_2*.

    #. The ball controller updates its count of known balls
    #. Ball devices configure their eject targets

#. Reset posts the event *machine_reset_phase_3*.

    #. Ball locks are reset
    #. Drop targets are reset
    #. Drop target banks are reset
    #. GI is enabled
    #. Multiball devices are reset
    #. The attract mode starts as its a registered handler for
       *machine_reset_phase_3* .
