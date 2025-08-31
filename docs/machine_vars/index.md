---
title: Machine Variables
---

# Machine Variables

MPF uses the concept of *machine variables* to track dynamically-created
variables that apply on a machine-wide basis. Machine variables are
similar in concept to
[player variables](../game_logic/players.md), except machine variables are machine-wide instead of
per-player. Examples of things that are stored in machine variables
include:

* The number of credits on the machine (if you're using the credits
    mode and not set to free play)
* The scores of the last game played (which are typically shown in the
    attract mode display loop)
* The names and scores of the high scores (which are also shown in the
    attract mode display loop and in the "status" screen when a player
    holds a flipper button in during a game).

Machine variables can be set to `persist`, meaning they are saved to
disk and available to MPF the next time it boots up. (For example, if
you first turn on a pinball machine, it will still show the scores of
the last game played in the attract mode.) These machine variables are
stored in the `<your_machine_folder>/data/machine_vars.yaml` file.
Machine variables that are saved to disk can optionally be written with
an expiration time which means they're cleared out if MPF boots after
the time has passed. (For example, the number of credits on the machine
might only persist for a few hours.)

Like player variables, you can use machine variables in your config
files, particularly in text display widgets, to show things on your
display.

If you want to use a machine variable in a slide player you can access
it similarly to normal variables, you need to use the syntax
`(machine|my_var_name)` where `my_var_name` obviously has to be replaced
with your variable name. If you want to access the machine variable in a player, e.g. segment player you need to use this syntax
`{machine.my_var_name}`. In other words, when using the the first notation with the pipe symbol you access the value of the variable
as a string, in the latter case using the dot notation you access the value itself.

### Video about machine and [player variables](../player_vars/index.md):

<div class="video-wrapper">
<iframe width="560" height="315" src="https://www.youtube.com/embed/PUxEsNUGXPY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Related Configs

* [machine_vars: Config Reference](../config/machine_vars.md)
* [variable_player: Config Reference](../config/variable_player.md)

## Built-in Machine Variables

You can create your own machine variables in your configs. There are
also several machine variables that are automatically created. Here's a
list of the machine variables that are "built in" and available for
use in your configs, grouped by feature set:

#### MPF general info

* [mpf_extended_version](mpf_extended_version.md)
* [mpf_version](mpf_version.md)
* [python_version](python_version.md)
* [platform](platform.md)
* [platform_machine](platform_machine.md)
* [platform_release](platform_release.md)
* [platform_system](platform_system.md)
* [platform_version](platform_version.md)

#### Previous game scores

* [player(x)_score](playerx_score.md)

#### High scores

* [(high_score_category)(position)_label](high_score_categoryposition_label.md)
* [(high_score_category)(position)_name](high_score_categoryposition_name.md)
* [(high_score_category)(position)_value](high_score_categoryposition_value.md)
* [(high_score_category)(position)\_(variable_type)_(variable)](high_score_categoryposition_variabletype_variable.md)

#### Credit management (if not on free play)

* [credit_units](credit_units.md)
* [credits_denominator](credits_denominator.md)
* [credits_numerator](credits_numerator.md)
* [credits_string](credits_string.md)
* [credits_value](credits_value.md)
* [credits_whole_num](credits_whole_num.md)

#### MPF-MC version information (pre-MPF 0.80)

* [mc_extended_version](mc_extended_version.md)
* [mc_version](mc_version.md)

## Platform-specific machine variables

Some platforms will also add additional machine variables based on
how they are set up. Some examples:

* [fast_(x)_firmware](fast_x_firmware.md)
* [fast_(x)_model](fast_x_model.md)
* [lisy_api_version](lisy_api_version.md)
* [lisy_hardware](lisy_hardware.md)
* [lisy_version](lisy_version.md)
* [p_roc_hardware_version](p_roc_hardware_version.md)
* [p_roc_revision](p_roc_revision.md)
* [p_roc_version](p_roc_version.md)
* [pkone_firmware](pkone_firmware.md)
* [pkone_hardware](pkone_hardware.md)

## Related Events

* [machine_var_(var_name)](../events/machine_var_machine_var.md)
