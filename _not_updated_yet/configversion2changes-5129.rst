
In MPF 0.19, we have incremented the version number of the YAML
configuration files that MPF uses. (We use the version number to make
sure that the YAML files you've created are compatible with the latest
version of MPF. More details `here`_.) In order to use MPF 0.19 and
newer, you will have to update your YAML files to version 2. We know
this is a pain, but with the complete rewrite of the "target" code
(standups, rollovers, drop targets, etc.) in 0.19, none of the
existing target configurationwill work. While we were at it, we
decided to implement several other changes we had been wanting to do
for awhile. (Mostly find-and-replace name changes.) To make this
update as easy as possible, we created a `config file migration tool`_
that scans your existing YAML files and auto-updates them as much as
possible and then highlights the areas you'll have to change manually.
There's one catch: if you haven't already added '#config_version=1' to
your config files, do it now or they will be skipped (this includes
your mode config files).



Target / Rollover / Standup / Drop Target config sections
---------------------------------------------------------

(Note: this page is not done yet... so that's why it seems like random
notes.) targets, targetgroups, rollovers, rollovergroups, droptargets,
droptarget groups:throw out everything you once knew switch events are
new double_zeros is out, min_digits: 2 is how you'd do that now tps in
light scripts -> tocks_per_sec movies -> videos holdpatter
machine_flow_attract_start/machine_flow_attract_stop are now just
called attract_start and attract_stop.



Other "find and replace"-type changes:
--------------------------------------

Over the past year of creating MPF, we've had a lot of variation of
several config file sections. So we're redoing everything now to be
consistent, and as such, the following sections have changed in config
file version 2. You can do a simple find+replace across your YAML
files for these changes.
Old New assetdefaults asset_defaults autofire coils autofire_coils
balldevices ball_devices ballsearch ball_search droptargets
drop_targets droptargetbanks drop_target_banks languagestrings
language_strings lightplayer light_player lightscripts light_scripts
logicblocks logic_blocks ledsettings led_settings machineflow
machine_flow matrixlights matrix_lights mediacontroller
media_controller openpixelcontrol open_pixel_control score reels
score_reels score reel groups score_reel_groups showplayer show_player
slideplayer slide_player soundplayer sound_player soundsystem
sound_system switchplayer switch_player targetgroups target_groups
virtual platform start active switches
virtual_platform_start_active_switches
.. _config file migration tool: https://missionpinball.com/docs/tools/config-file-migrator/
.. _here: https://missionpinball.com/docs/configuration-file-reference/config_version/


