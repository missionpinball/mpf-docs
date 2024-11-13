---
title: "segment_displays:"
---

# segment_displays:


--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|

The `segment_displays:` section of your config is where you define your
[segment displays](../mc/displays/alpha_numeric.md). This can be 7-segment or alphanumeric displays which are
typically used in older machines.

## Required settings

The following sections are required in the `segment_displays:` section
of your config:

### number:

Single value, type: `string`. Defaults to empty.

The number of the display. The meaning depends on the hardware platform.

* [Cobra serial segment display](../hardware/opp/cobrapin/cobrapin_serial_segment_displays.md): Not relevant, just use always `1`

## Optional settings

The following sections are optional in the `segment_displays:` section
of your config. (If you don't include them, the default will be used).

### default_color:

List of one (or more) values, each is a type: `color` (*color name*,
*hex*, or list of values *0*-*255*). Default: `white`

--8<-- "todo.md"

### default_transition_update_hz:

Single value, type: float_or_token. Default: `30`

The speed (steps per second) at which text transition effects will be
updated in the display.

### integrated_commas:

Single value, type: `boolean` (`true`/`false`). Default: `false`

Determines whether or not the physical segment display has integrated
commas in each character rather than taking up an entire character. When
set to `true`, commas are collapsed with the preceding character when
calculating text transition effects.

### integrated_dots:

Single value, type: `boolean` (`true`/`false`). Default: `false`

Determines whether or not the physical segment display has integrated
dots/periods in each character rather than taking up an entire
character. When set to `true`, dots/periods are collapsed with the
preceding character when calculating text transition effects.

### platform:

Single value, type: `string`. Defaults to empty.

This can be used to overwrite the platform which is defined in the
*hardware* section for segment_displays.

### platform_settings:

Single value, type: dict. Defaults to empty.

Platform specific settings. See your
[segment platform documentation](../hardware/segment_display_platforms.md).

### size:

Single value, type: `integer`. Default: `7`

The number of characters in the segment display. This value should be
set to match the number of characters in your physical hardware (or
virtual emulator). It is important to set this number correctly for the
text transition effects.

### update_method:

Single value, type: `String`. Default: `"stack"`

The method by which segment display text is updated via segment display player.

When set to "replace", this segment display will only track one text string at a time
and all updates must be explicitly sent to the display player. These text strings do
*not* create subscriptions or respond to variable changes.

When set to "stack", new text entries are added on top of previous ones (based on priority)
and when removed, the next-highest priority one is rendered. These text strings *will*
create subscriptions for variables within them, and automatically update the displayed
text when the variable value changes. This is a convenient way to
persist player variables (e.g. score) without having to continually push updates.

!!! warning "Can cause memory bloat"

    Using the "stack" method for updates will create a new event subscriber for each entry, so misusing the segment_display_player and sending manual updates will cause
    hundreds or thousands of subscribers to be created, which can cause lag and memory issues.

    In a future release of MPF **"replace" will become the default setting** because it is more aligned with how most people implement their segment_display_player.

    If you know what you're doing and want to use "stack", you should set it explicitly in your config to prevent errors when the default changes to "replace".

    If you are unsure or don't know which to use, use "replace".

### use_dots_for_commas:

Single value, type: `boolean` (`true`/`false`). Default: `false`

--8<-- "todo.md"

### console_log:

Single value, type: one of the following options: none, basic, full.
Default: `basic`

Log level for the console log for this device.

### debug:

Single value, type: `boolean` (`true`/`false`). Default: `false`

Set this to true to see additional debug output. This might impact the
performance of MPF.

### file_log:

Single value, type: one of the following options: none, basic, full.
Default: `basic`

Log level for the file log for this device.

### label:

Single value, type: `string`. Default: `%`

Name of this device in service mode.

### tags:

List of one (or more) values, each is a type: `string`. Defaults to
empty.

Not used.

## Related How To guides

* [Alpha-Numeric / Segment Displays](../mc/displays/alpha_numeric.md)
* [Segment Display Platforms in MPF](../hardware/segment_display_platforms.md)
