---
title: "show_player:"
---

# show_player:


--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**YES** :white_check_mark:|

!!! note

    This section can also be used in a show file in the `shows:` section of
    a step.

The `show_player:` section of your config is where you start, stop,
pause, (etc.) shows.

Here is an example:

``` yaml
show_player:
  some_event: your_show_name
  some_other_event: another_show
```

In the example above, when the event *some_event* is posted, the show
called `your_show_name` will be played (started). When the event
*some_other_event* is posted, the show called `another_show` will be
played.

See [Show player](../config_players/show_player.md) for
details.

## Optional settings

The following sections are optional in the `show_player:` section of
your config. (If you don't include them, the default will be used).

### action:

Single value, type: one of the following options: play, stop, pause,
resume, advance, step_back, update, queue. Default: `play`

#### `play`:

Starts playing the show. This is the default action which will
happen if you don't include an `action:` setting.

#### `stop`:

Stops the show. Removes and "undoes" anything the show did, and
posts the show stop events.

#### `pause`:

Pauses the show by holding it at the current step. Posts the show pause events.

#### `resume`:

Resumes a previously paused show.

#### `advance`:

Manually advances a show to the next step. Posts the show advance events.

#### `step_back`

Manually moves the show back to the previous step. Posts the show
step_back events.

#### `update`:

Not yet implemented. In the future it will be used to change a
setting of a running show, like changing the playback speed.

### block_queue:

Single value, type: `boolean` (`true`/`false`). Default: `false`

You can use `block_queue: yes` if you want the show to block a queue
event until the show is done. Note that you can only use this if the
event that starts the show is a
[queue event](../events/overview/event_types.md).

For example, the mode stopping events are queue events. So take a look
at the following config:

``` yaml
show_player:
  mode_my_mode_stopping:
    show_1:
      block_queue: true
```

In the example above, when the mode called *my_mode* posts its stopping
event, show_1 will start playing. However because this show is set to
block the queue event, the mode stopping event will not finish until the
show finishes. In other words, the mode will not fully stop, and the
*mode_my_mode_stopped* event will not be posted until the show ends.

If you didn't use the block_queue setting, then the show would start
and then stop right away since the mode would end and be over (and shows
started in modes are stopped when those modes end).

If you used this setting, make sure that you don't have `loops: -1`, or
a `duration: -1` as the final step of the show, since those will mean
the show will never end, and then the queue event will never be
unblocked, and your machine will hang.

### events_when_advanced:

List of one (or more) events. Those will be posted by the device.
Defaults to empty.

Event(s) that will be posted when this show has been manually advanced
to the next step.

### events_when_completed:

List of one (or more) events. Those will be posted by the device.
Defaults to empty.

Event(s) that will be posted when this show has completed, meaning it
ran through to the last step and ended naturally.

Note that if a show loops, these events are *not* posted when the loop
happens. (You can use the *events_when_looped* for that.) However if a
show is set to loop a specific number of times and then ends, these
events will be posted at the end.

Note that if you want an event to post whenever the show stops, even if
it didn't make it all the way to the end, you can use
*events_when_stopped*.

### events_when_looped:

List of one (or more) events. Those will be posted by the device.
Defaults to empty.

Event(s) that will be posted when this show has looped (meaning it
reached the end and is jumping back to the first step).

### events_when_paused:

List of one (or more) events. Those will be posted by the device.
Defaults to empty.

Event(s) that will be posted when this show has been paused.

### events_when_played:

List of one (or more) events. Those will be posted by the device.
Defaults to empty.

Event(s) that will be posted when this show is played (started).

### events_when_resumed:

List of one (or more) events. Those will be posted by the device.
Defaults to empty.

Event(s) that will be posted when this show is resumed from a pause.

### events_when_stepped_back:

List of one (or more) events. Those will be posted by the device.
Defaults to empty.

Event(s) that will be posted when this show has been manually stepped
back to the previous step.

### events_when_stopped:

List of one (or more) events. Those will be posted by the device.
Defaults to empty.

Event(s) that will be posted when this show has been stopped. Note that
these events are posted anytime the show has been stopped, regardless of
whether it made it to the end and stopped on its own, or whether it was
stopped randomly where it was.

### events_when_updated:

List of one (or more) events. Those will be posted by the device.
Defaults to empty.

Event(s) that will be posted when this show has been updated. Note that
the show "update" function has not been implemented yet, so this
setting is more of a placeholder at the moment.

* [show_config:](show_config.md)

### key:

Single value, type: `string`. Defaults to empty.

Used to set a unique identifier you can set when playing a show which
can then be used later to identify a show you want to perform an action
on.

### loops:

Single value, type: `int_or_token`. Default: `-1`

Controls the looping / repeating of the show. The default if you don't
include this setting is `loops: -1` means that the show will repeat
indefinitely until it's stopped.

If you just want a show to play once and then stop, use `loops: 0`.

Since this setting is the number of times it loops, the value will be
one less than the number of times the show will play. (e.g. `loops: 1`
means the show will loop once which means it will play through twice.)

Note that if a show only has one step, *loops* will be set to 0,
regardless of the actual loops setting.

### manual_advance:

Single value, type: `boolean` (`true`/`false`). Default: `false`

If you set this to yes/true, then the show will not auto-advance based
on time. Instead you will have to manually advance the show step-by-step
with additional show_player entries with `action: advance` entries.

This can be useful if you want to have some kind of slow progress based
on a series of events instead of a show that auto plays.

For example:

``` yaml
show_player:
  some_event:
    show_1:
      manual_advance: true
  some_advance_event:
    show_1:
      action: advance
```

In the example above, the event *some_event* will start show_1, but that
show will stay on its first step since it's set to manually advance.
Then each time the event *some_advance_event* is posted, show_1 will
advance to its next step.

### priority:

Single value, type: `int_or_token`. Default: `0`

Adjusts the priority of the show that's played.

By default, shows play at the priority of the mode where the show_player
entry is. So this setting merely adjusts the show's priority up or
down. For example, if you have a mode running at priority 300, and a
show in a show_player with the setting `priority: 10`, then that show
will run at priority 310. Priorities can also be negative.

The show's priority affects the priority of everything it does. Sounds,
slides, LEDs, etc.

### show:

Single value, type: `string`. Defaults to empty.

--8<-- "todo.md"

### show_queue:

Is this still a thing? Need to confirm, June 2023

--8<-- "todo.md"

### show_tokens:

One or more sub-entries. Each in the format of `string` : template_str

Allows you to specify show token values that will be used to replace the
show tokens in the show when it's played.

Read what show tokens are [here](../shows/tokens.md).

For example:

``` yaml
show_player:
  some_event:
    show1:
      show_tokens:
        led: right_inlane
```

In the example above, the show called "show1" will be played, but the
show token called "led" in the show will be replaced at runtime with
the value "right_inlane".

To learn more about show tokens and how to use dynamic values take a look at the [Tokens](../shows/tokens.md) reference page.

### speed:

Single value, type: template_float_or_token. Default: `1`

Controls the playback speed of the show. The default value of 1 means
the show plays back at 1x speed. (In other words, it plays at the actual
speed each step is configured for. In this case you don't actually need
to include the setting.)

If you want to play the show at 2x the speed, use `speed: 2`. If you
want to play it at half speed, use `speed: .5`. Etc.

You can use dynamic placeholders here also, as of MPF 0.56.1. This allows a show to be played using a variable speed.

### start_running:

Single value, type: `boolean` or `template` (`true/false`;
[Instructions for entering templates](instructions/dynamic_values.md)). Default: `True`

Whether the show starts running immediately when it is played.

By default, calling `play` on a show begins at the starting step and
advances through the steps according to the show config. If
`start_running` is false, the show will play the starting step and
immediately pause. You can begin playing the show by calling show_player
with `action: resume`.

### start_step:

Single value, type: `integer` or `template`
([Instructions for entering templates](instructions/dynamic_values.md)). Default: `1`

Which step the show starts on when it's played.

Note that you can use a
[dynamic value](instructions/dynamic_values.md) for this setting.

### sync_ms:

Single value, type: `int_or_token`. Defaults to empty.

Sets the sync_ms value of this show which will delay the start to a
certain millisecond multiple to ensure that multiple shows started at
different times all play in sync with each other.

See the [Synchronizing multiple shows](../shows/sync_ms.md) documentation for
details.

## Related How To guides

* [Shows](../shows/index.md)
* [Tutorial step 16: Create an attract mode display show](../tutorial/16_attract_mode_show.md)
* [Show player](../config_players/show_player.md)
