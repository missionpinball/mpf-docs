---
title: State Machine Logic Block
---

# State Machine Logic Block


Related Config File Sections:

* [integrating_logic_blocks_and_shows](../../config/state_machines.md)
* [integrating_logic_blocks_and_shows](../../config/state_machine_states.md)
* [integrating_logic_blocks_and_shows](../../config/state_machine_transitions.md)

  Related How To Guides

* [Integrating Logic_Blocks and Shows](integrating_logic_blocks_and_shows.md)

"State machines" are a type of
[Logic Block](index.md) where you can trigger state transitions based on the current
state and an event.

Technically, this is a [finite state
machine](https://en.wikipedia.org/wiki/Finite-state_machine) as known
from CS class.

Video about state machines:

<div class="video-wrapper">
<iframe width="560" height="315" src="https://www.youtube.com/embed/qakxTF1H57E" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

This is an example:

``` mpf-config
##! mode: my_mode
state_machines:
  my_state:
    states:
      start:
        label: Start state
      step1:
        label:
        show_when_active:
          show: on
          show_tokens: None
        events_when_started: step1_start
        events_when_stopped: step1_stop
      step2:
        label:
    transitions:
      - source: start
        target: step1
        events: state_machine_proceed
      - source: step1
        target: step2
        events: state_machine_proceed2
        events_when_transitioning: going_to_step2
      - source: step2
        target: start
        events: state_machine_proceed3
      - source: step1, step2
        target: start
        events: state_machine_reset
##! test
#! start_game
#! start_mode my_mode
#! mock_event going_to_step2
#! assert_str_condition start device.state_machines.my_state.state
#! post state_machine_proceed
#! assert_str_condition step1 device.state_machines.my_state.state
#! assert_event_not_called going_to_step2
#! post state_machine_proceed2
#! assert_str_condition step2 device.state_machines.my_state.state
#! assert_event_called going_to_step2
```

## Storing the State in a Player Variable

If you want to store the state of your state machine in a player
variable your can use a
[variable_player](../../config/variable_player.md). You can then use it on slides or in places where conditions
do not work (yet).

``` mpf-config
##! mode: my_mode
state_machines:
  my_state:
    states:
      start:
        label: Start state
      step1:
        label:
        show_when_active:
          show: on
          show_tokens: None
        events_when_started: step1_start
        events_when_stopped: step1_stop
      step2:
        label:
    transitions:
      - source: start
        target: step1
        events: state_machine_proceed
      - source: step1
        target: step2
        events: state_machine_proceed2
        events_when_transitioning: going_to_step2
      - source: step2
        target: start
        events: state_machine_proceed3
      - source: step1, step2
        target: start
        events: state_machine_reset

variable_player:
  "{device.state_machines.my_state.state}":
    my_player_var:
      action: set
      string: "{value}"

##! test
#! start_game
#! start_mode my_mode
#! advance_time_and_run .1
#! mock_event going_to_step2
#! assert_str_condition start device.state_machines.my_state.state
#! assert_player_variable start my_player_var
#! post state_machine_proceed
#! advance_time_and_run .1
#! assert_str_condition step1 device.state_machines.my_state.state
#! assert_player_variable step1 my_player_var
#! assert_event_not_called going_to_step2
#! post state_machine_proceed2
#! advance_time_and_run .1
#! assert_str_condition step2 device.state_machines.my_state.state
#! assert_event_called going_to_step2
#! assert_player_variable step2 my_player_var
```

## Monitorable Properties

For
[dynamic values](../../config/instructions/dynamic_values.md) and
[conditional events](../../events/overview/conditional.md), the prefix for state machines is
`device.state_machines.<name>`.

*state*

:   The state of this state machine as string. This will be one of your
    entries in your states section.
