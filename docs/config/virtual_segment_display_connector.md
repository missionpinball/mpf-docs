---
title: "virtual_segment_display_connector: Config Reference"
---

# virtual_segment_display_connector: Config Reference

--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|

The `virtual_segment_display_connector:` section of your config is where
you configure the connector that establishes the link between segment
displays and the virtual segment display emulator widgets in the MPF-MC.

``` yaml
virtual_segment_display_connector:
  segment_displays: display1
```

## Optional settings

The following sections are optional in the
`virtual_segment_display_connector:` section of your config. (If you
don't include them, the default will be used).

### bcp_connection:

Single value, type: `string`. Default: `local_display`

The name of the BCP connection the MPF-MC is connected to. Normally this
does not need to be modified as the default value should be correct.

### debug:

Single value, type: `boolean` (`true`/`false`). Default: `false`

### segment_displays:

List of one (or more) values, each is a type: string name of a
[segment_displays:](segment_displays.md)
device. Defaults to empty.

A list of one or more segment display names which is used to specify
which segment displays should be activated in the connector to send the
appropriate information to the MPF-MC.

## Related How To guides

* [How to setup and use the virtual segment display emulator](../mc/widgets/segment_display_emulator/how_to.md)
