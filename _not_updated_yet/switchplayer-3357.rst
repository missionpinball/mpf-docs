
You use the `switch_player:` section of your machine configuration
file to enter a "script" of switch events that will automatically be
played back to simulate your machine being used (for troubleshooting
and testing purposes). This sectioncan be used in your machine-wide
config files. This section *cannot* be used in mode-specific config
files. Here's an example from our *Demo Man* game. This script puts a
ball in the trough, hits start, moves the ball from the trough to the
plunger lane, hit's launch, moves the ball out of the plunger lane,
and hits a few playfield targets.


::

    
    switch_player:
        start_event: machine_reset_phase_3
        start_delay: 1s
        steps:
          - time: 100ms
            switch: s_trough_1
            action: activate
          - time: 600ms
            switch: s_start
            action: hit
          - time: 100ms
            switch: s_trough_1
            action: deactivate
          - time: 1s
            switch: s_shooter_lane
            action: activate
          - time: 1s
            switch: s_ball_launch
            action: hit
          - time: 100ms
            switch: s_shooter_lane
            action: deactivate
          - time: 1s
            switch: s_right_inlane
            action: hit


There are a few configuration settings:



start_event:
~~~~~~~~~~~~

This is the MPF event that will trigger this script to begin. If you
don't add this section, it will automatically begin when the
`machine_reset_phase_3` event is posted.



start_delay:
~~~~~~~~~~~~

This is an MPF time string entry which specifies how soon the script
kicks off after the start_event is posted.



steps:
~~~~~~

This is a series of steps, each with three settings:



time:
~~~~~

An MPF time string entry of how long to wait before performing the
action in this step.



switch:
~~~~~~~

The switch name (from the `Switches:` section of your config file) for
the switch whose state you're setting.



action:
~~~~~~~

What action you want to be applied to the switch. There are three
options:


+ activate - Sets the switch to active. This is the "logical" setting
  of the switch which *does* take into consideration a switch's "NC"
  setting. (So for example, an opto switch going active technically
  means the switch hardware opens, but since it's an NC switch, it's
  inverted. "Active" means the game thinks there's a ball there.
+ deactivate - Sets the switch to inactive. (i.e. no ball activating
  it.)
+ hit - Does a quick "hit" of the switch which activates and then
  immediately deactivates the switch, like when a ball rolls over a
  target or a player hit's the launch button.




Launching Switch Player scripts via the command line
----------------------------------------------------

Remember that in MPF you can have as many machine configuration files
as you want, and you can list additional config files in other config
files. This means if you have a game that you sometimes want to test
with an automatic script and other times you don't, you can create a
simple standalone config file for the switch test without having to
duplicate all your settings. For example, imagine you have your "main"
configuration file in `config.yaml`. You launch it like this:


::

    
    python mpf.py your_machine_folder


You don't need to specify any configuration folder option here because
MPF automatically looks for a file called `config.yaml`at
`your_machine_folder/config/config.yaml`. Now what if you wanted to
create an automatic switch script for this machine? In that case,
create a second configuration file called `autotest.yaml` and set it
up like this:


::

    
    config:
        - config.yaml
    
    switch_player:
        <...>


To run your game with this switch player script, use a command like
this:


::

    
    python mpf.py your_machine -c autotest


The `-c`option tells MPF that you want to use the configuration file
`your_machine/config/autotest.yaml` instead of
`your_machine/config/config.yaml`. If you look at that file from
above, notice that it contains the settings for your Switch Player, it
contains the link to the switch player plugin, and it contains a link
to the main `config.yaml` which it merges in when you run it. So this
is how you can have one main config file but then still have the
option to use or not use your automated switch playback scripts.



