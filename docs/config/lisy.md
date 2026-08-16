---
title: "lisy: Config Reference"
---

# lisy: Config Reference

--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|

The `lisy:` section of your config is where your lisy platform. See
[How to use MPF with the LISY platform](../hardware/lisy/index.md) for details.

## Optional settings

The following sections are optional in the `lisy:` section of your
config. (If you don't include them, the default will be used).

### baud:

Single value, type: `integer`. Defaults to empty.

Baudrate when connecting to LISY using a serial port.

### connection:

Single value, type: one of the following options: network, serial.
Default: `network`

Whatever to use a network or serial connection.

### console_log:

Single value, type: one of the following options: none, basic, full.
Default: `none`

Log level for the console log for this platform.

### debug:

Single value, type: `boolean` (`true`/`false`). Default: `false`

See the
[documentation on the debug setting](instructions/debug.md) for details.

### disable_dtr:

Single value, type: `boolean` (`true`/`false`). Default: `true`

If set to `True` MPF will try to prevent your operating system from
toggling the DTR line of your serial. This is needed for
[APC](../hardware/apc/index.md) and some other
controllers which would reset when this happens. If in doubt check the
documentation of your controller.

### display_flash_duty:

Single value, type: `number` (will be converted to floating point).
Default: `0.5`

--8<-- "todo.md"

### display_flash_frequency:

Single value, type: `number` (will be converted to floating point).
Default: `1.0`

How fast should the displays flash? Defaults to once per second or 1Hz.

### file_log:

Single value, type: one of the following options: none, basic, full.
Default: `basic`

Log level for the file log for this platform.

### max_led_batch_size:

Single value, type: `integer`. Default: `12`

How many LEDs can be batched on your controller? This might differ on
different controllers. If in doubt check the documentation of your
controller.

### network_host:

Single value, type: `string`. Defaults to empty.

Host to connect when connecting to LISY via network.

### network_port:

Single value, type: `integer`. Defaults to empty.

Port to connect when connecting to LISY via network.

### poll_hz:

Single value, type: `integer`. Default: `100`

How fast should MPF poll LISY for switch changes? Defaults to 1000Hz

### port:

Single value, type: `string`. Defaults to empty.

Serial port when connecting to LISY using serial.

### send_length_after_command:

Single value, type: `boolean` (`true`/`false`). Default: `false`

Some controllers require an additional length byte after the command.

## Related How To guides

* [How to use MPF with the LISY platform](../hardware/lisy/index.md)
* [Arduino Pinball Controller](../hardware/apc/index.md)
