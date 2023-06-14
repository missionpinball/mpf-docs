---
title: show_config:
---

# show_config:


--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**NO** :no_entry_sign:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|

The `show_config:` section of your config is where you configure a show
to play within a device.

See [show_player:](show_player.md) for more
details about the settings.

## Required settings

The following sections are required in the `show_config:` section of
your config:

### show:

Single value, type: `string`.

The show to play.

## Optional settings

The following sections are optional in the `show_config:` section of
your config. (If you don't include them, the default will be used).

### loops:

Single value, type: `integer`. Default: `-1`

How often should the show loop? `-1` means forever.

### manual_advance:

Single value, type: `boolean` (Yes/No or True/False).

Whatever, the show should advance manually only.

### priority:

Single value, type: `integer`. Default: `0`

Priority for this show. This is usually added to the mode priority if
the device is defined within a mode.

### show_tokens:

One or more sub-entries, each in the format of `string` : `string` Dict
of show tokens to pass to the show.

### speed:

Single value, type: `number` (will be converted to floating point).
Default: `1`

Speed multiplier for this show.

### start_step:

Single value, type: `integer`. Default: `1`

First step to play.

### sync_ms:

Single value, type: `integer`.

See the [Synchronizing multiple shows](../shows/sync_ms.md) documentation for
details.
