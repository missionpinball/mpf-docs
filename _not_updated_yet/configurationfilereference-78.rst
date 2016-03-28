
As we mentioned in the introduction, MPF uses the YAML configuration
files to configure itself for just about everything your machine does.
This section of the documentation is the configuration file reference
which has all the detailed options about how all these files work.
There are two types of config files: *machine config files* and *mode
config files*.


+ Machine config files are stored in the
  *<your_machine_folder>/config* folder. Anything specified there
  applies to your enter machine and are active for the entire duration
  of MPF running.
+ Mode config files are stored in the
  *<your_machine_folder>/modes/<mode_name>/config* folder. They are
  activated when the mode starts and deactivated when the mode ends.


Not all settings are usable in the mode config files. Refer to the
details in each entry for details. Before we jump in, take a look at a
made-up example of the types of things you might find in your config
files.


::

    
    hardware:
        platform: p_roc
        driverboards: wpc
    
    switches:
        flipperLwR_EOS:
             number: SF1
        flipperLwR:
            number: SF6
    
    coils:
        flipperLwRMain: 
            number: FLRM
        flipperLwRHold: 
            number: FLRH
    
    flippers:
        LowerRight:
            main_coil: flipperLwRMain
            hold_coil: flipperLwRHold
            activation_switch: flipperLwR
            eos_switch: flipperLwR_EOS
            label: Right Main Flipper


Remember you can have as many configuration files as you want (for
both the machine and mode specific config files. MPF will read them
all in and merge them into a single master list. So whether you have
all these sections in a single huge file called *my_game.yaml* or
whether you break them into *coils.yaml*, *flippers.yaml*, and
*switches.yaml* is up to you.



