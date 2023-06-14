---
title: Wizard Modes
---

# Wizard Modes


Unlockable game modes that take over the playfield are typically
referred to as "wizard" modes and are often considered milestones for
a player's progress. Here we will outline some common approaches to
tracking, starting, and completing wizard modes in MPF.

## Achievements to Qualify Wizard Modes

The simplest way to track a player qualifying, attempting, and
completing wizard modes is through
[achievements](../config/achievements.md), a
special type of player variable that progress through a series of
pre-defined states.

One common approach for wizard modes is to have a counter that tracks
shots to qualify the mode. In this example, hitting three shots will
enable and immediately start the wizard mode:

``` mpf-config
##! mode: wizard_qualify
# mode: wizard_qualify
mode:
  start_events: mode_base_started
achievements:
  winterhascome:
    enable_events: logicblock_winteriscoming_count_complete
    start_events: achievement_winterhascome_state_enabled
counters:
  winteriscoming_count:
    starting_count: 0
    count_complete_value: 3
    count_events: winteriscoming_shot_hit
##! mode: winterhascome
# mode: winterhascome
mode:
  start_events: achievement_winterhascome_state_started
##! test
#! start_game
#! post mode_base_started
#! post winteriscoming_shot_hit
#! post winteriscoming_shot_hit
#! assert_mode_not_running winterhascome
#! post winteriscoming_shot_hit
#! assert_mode_running winterhascome
```

The different achievement states allow you to fine-tune when and how
modes can be qualified. Achievements can be *enabled/disabled*,
*selected*, *started/stopped*, and *completed*, and have some rules to
help control the flow:

* *disabled* achievements must be enabled before any other state
    changes will work
* *enabled* achievements can be disabled, selected, or started
* *selected* achievements can be disabled, started, or completed
* *started* achievements can be stopped or completed
* *completed* achievements cannot change state anymore

By combining these state flows with your qualifying shots, mode
selections, and end-of-ball events, there is a lot of flexibility for
using achievements to track wizard modes. For example, a one-time-only
wizard mode could distinguish between an *enabled* achievement (i.e. it
hasn't been played) and a *stopped* achievement (i.e. it has been
played), while a wizard mode awarding a bonus for accomplishing some
goal could distinguish between a *stopped* achievement and a *completed*
achievement.

Of course, there's no requirement that achievements be used to start
and stop wizard modes. Achievements are a convenience for tracking
progress, your own game design may have other approaches.

## Starting and Stopping Wizard Modes

Most wizard modes will be started and stopped like any other game mode,
using the mode [start_events](#) and [stop_events](#).
There will usually be a close relationship between the start/stop events
and the achievement state events, as in these typical examples:

    # Use a counter to enable an achievement
    achievements:
      captainschair:
        enable_events: completed_missions_count_hit{value==6}

    # Enable an achievement to start a mode [direct event]
    mode:
      start_events: achievement_captainschair_state_enabled

    # Enable an achievement to start a mode [indirect event]
    event_player:
      achievement_captainschair_state_enabled: start_mode_captainschair

    # Start an achievement when its wizard mode starts
    achievements:
      captainschair:
        start_events: mode_captainschair_started

    # Complete an objective to complete an achievement [direct event]
    achievements:
      captainschair:
        complete_events: logicblock_captainshots_counter_complete

    # Complete an objective to complete an achievement [indirect event]
    achievements:
      captainschair:
        complete_events: captainschair_complete
    event_player:
      logicblock_captainshots_counter_complete: captainschair_complete

    # Stop an achievement when a mode stops
    achievements:
      captainschair:
        stop_events: mode_captainschair_will_stop

For wizard modes that stop other game modes, disable qualifier shots or
ball locks, and/or have other "takeover" behaviors, consider using
[Mode Layering](mode_layering.md) to handle
the transitions in and out of wizard modes.

## After a Wizard Mode

Most wizard modes are only played once and have a "completion" goal
for the player to accomplish. Mid-game wizard modes (also called
"mini-wizard" modes) will usually end if the goal is completed, while
end-of-game wizard modes play until the ball drains. Similarly,
end-of-game wizard modes typically restart immediately on the players
next ball while mid-game wizard modes usually do not. Multiball wizard
modes usually remain active until only one ball is left in play.

Achievement states are an excellent way to track how a wizard mode ended
and whether it impacts future game behavior. If you're using the
*achievement_(name)_started* event to start your wizard mode the
`restart_after_stop_possible:` setting determines whether a "stopped"
achievement can be started and the `restart_on_next_ball_when_started:`
setting will post the *achievement_(name)_started* event when its
parent mode starts. If the wizard mode has a "completion" goal, the
achievement's "completed" state can be used to track whether a player
accomplished it.
