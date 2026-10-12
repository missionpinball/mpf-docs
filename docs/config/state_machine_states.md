---
title: "state_machine_states: Config Reference"
---

# state_machine_states: Config Reference

--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**NO** :no_entry_sign:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|

The `state_machine_states:` section of your config is where you
configure the states of your
[state machine](state_machines.md).

See
[state machines](../game_logic/logic_blocks/state_machines.md) for details.

## Optional settings

The following sections are optional in the `state_machine_states:`
section of your config. (If you don't include them, the default will be
used).

### events_when_started:

List of one (or more) events.

These events will be posted when the state machine enters this state. This
is the entry action for this state in your finite state machine.

### events_when_stopped:

List of one (or more) events.

These events will be posted when the state machine leaves this state. This
is the exit action for this state in your finite state machine.

### events_when_restored:

!!! info ""

    Configuration property available in MPF 0.81/0.58

List of one (or more) events.

These events will be posted when the state machine is restored to this state.
This happens when the mode containing your state machine is stopped and then started again.
For example, if a mode is active across balls for a player, or is stopped and restarted within a single ball.

### label:

Single value, type: `string`.

The full name/description of this state.

### show_when_active:

Single value, type: [show_config:](show_config.md).

A show which is played when the state machine is in this state. This is
kind of an entry action as you could use `events_when_started` and a
[show_player:](show_player.md) to achieve the same. It is
meant as a helper because it is common to play one show per step.

## Related How To guides

* [State Machine Logic Block](../game_logic/logic_blocks/state_machines.md)
