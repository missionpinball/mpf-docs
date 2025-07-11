---
title: "spi_bit_bang: Config Reference"
---

# spi_bit_bang: Config Reference

--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|

The `spi_bit_bang:` section of your config is where you configure the
[How to use SPI Bit Bang in MPF](../hardware/spi_bit_bang.md) platform.

## Required settings

The following sections are required in the `spi_bit_bang:` section of
your config:

### clock_pin:

Single value, type: `string` name of a
[digital_outputs:](digital_outputs.md)
device. Defaults to empty.

This output is used to clock the SPI chip.

### cs_pin:

Single value, type: `string` name of a
[digital_outputs:](digital_outputs.md)
device. Defaults to empty.

This output is used to chip select the SPI chip. It usually also
triggers the parallel read of the chip.

### miso_pin:

Single value, type: `string` name of a
[switches:](switches.md) device. Defaults to
empty.

This input is read serially to determine the state of your inputs.

## Optional settings

The following sections are optional in the `spi_bit_bang:` section of
your config. (If you don't include them, the default will be used).

### bit_time:

Single value, type: `time string (secs)`
([Instructions for entering time strings](instructions/time_strings.md)). Default: `50ms`

How long should the platform wait until reading the `miso_pin`.
Depending on your platform it might need a while to settle. Especially
if your platform is connected via USB. If your inputs are local (i.e. on
a RPi) this might be very short compared.

### clock_time:

Single value, type: `time string (ms)`
([Instructions for entering time strings](instructions/time_strings.md)). Default: `1ms`

How long should the clock pulse be? 1ms is the lower limit for most
platforms and more than long enough for any chip so this should be good.

### debug:

Single value, type: `boolean` (`true`/`false`). Default: `false`

Set to true to get more debug output.

### inputs:

Single value, type: `integer`. Default: `8`

How many inputs should the platform read? Reading less inputs will
result in faster updates.

## Related How To guides

* [How to use SPI Bit Bang in MPF](../hardware/spi_bit_bang.md)
* [Using the Stern Spike Trough](../mechs/troughs/spike_trough.md)
