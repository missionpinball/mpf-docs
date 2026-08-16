---
title: "fast:exp: Config Reference"
---

# fast:exp: Config Reference

--8<-- "deeper_config_section.md"

| Valid in | |
|-----|:----:|
|[machine](../instructions/machine_config.md) config files|**YES** :white_check_mark:|
|[mode](../instructions/mode_config.md) config files|**NO** :no_entry_sign:|

Within the [`fast:exp:`](fast_exp.md) (or `fast_int:`) section of your [fast:](../fast.md) config, you configure each of your EXP boards, as well as your Neuron EXP interface.

### model:

The product number of the IO board. E.G. `FP-EXP-0081`
Supported models in MPF as of 0.57.4 are:

* `FP-EXP-2000` - the Neuron LED ports
* `FP-EXP-1313` - single shaker interface
* `FP-EXP-0051` - DC motors, 4 LED headers
* `FP-EXP-0061` - Stepper board, 4 LED headers
* `FP-EXP-0071` - Servo board, 4 LED headers
* `FP-EXP-0081` - 2x4 LED headers
* `FP-EXP-0091` - 4 LED headers, custom breakouts

### address:

Single value, string, default: special

If you do not provide a value, the default address for the board model will be used.
If you are using only a single board of each model number, it should not be necessary to specify the address.
If you are using multiple boards with the same model, you must disambiguate them by modifying the solder jumpers.
The guide for this is in the [FAST website documentation](https://fastpinball.com/programming/exp/#expansion-board-addresses), but the general algorithm is that Jumper 0 being closed will increment the address by 1,
and Jumper 1 will increment the address by 2, so both will increment by 3, allowing up to four boards of the same model to be used in one system.

The FAST website has the full chart, but these are the default address values for each supported EXP board:

* `FP-EXP-2000` - `48`
* `FP-EXP-1313` - `30`
* `FP-EXP-0051` - `D0`
* `FP-EXP-0061` - `90`
* `FP-EXP-0071` - `B4`
* `FP-EXP-0081` - `84`
* `FP-EXP-0091` - `88`

### breakouts:

Single value, type: `dict`. Defaults to empty.

Specification of the remote breakout boards.

### led_ports:

Single value, type: `list`. Defaults to empty.

!!! note "This feature is not yet available and will require multiple upgrade steps"

    `led_ports` configuration is only supported on FAST EXP firmware 0.48, and as such
    requires upgrading to MPF version `0.58.0.dev1` or `0.81.0.dev1` via git or manual install.
    To prepare for this support, you should upgrade to `0.57.5` or `0.80.0` and upgrade all EXP
    firmware to 0.48, which is mandatory on 0.58 and 0.81 even if not using any custom header definitions.

Specification of the LED port configurations. Ports on most EXP boards go from 1-4, with the 0081 having a second set at numbers 5-8.
Each group of four ports may have up to 128 lights split in any way between the four ports. Each port may also be defined as one of four types.
The default assumption is that each port is 32 lights, WS2182 type (RGB LEDs only).

#### Changing port led counts:

To change the distribution of RGB lights, you must define some ports which will claim less than the standard 32 lights in order to also assign more than 32 to others.

``` yaml
fast:
  exp:
    boards:
      neuron:
        model: FP-EXP-2000
        led_ports:
          - port: 2
            count: 10
          - port: 4
            count: 54
          # ports 1 and 3 do not have to be defined as
          # they will default to 32 and we will have exactly 128 claimed
lights:
  last_on_chain_two:
    number: neuron-2-10
  last_on_chain_four:
    number: neuron-2-54
```

#### Changing port led types:

To change to RGBW SK6812 units, you can define the port to have just a type override:

``` yaml
fast:
  exp:
    boards:
      neuron:
        model: FP-EXP-2000
        led_ports:
          - port: 1
            type: sk6812
lights:
  my_sk6218_unit:
    number: neuron-1-1
    type: rgb
    # the rgbw type should not be used with SK6218s
    # on FAST hardware, use rgb or grb as appropriate
```

The SK6812 type is organized such that every four addresses is split up as channels 0, 1, and 2 as R G and B, and special channel W (inaccessible through normal channel lookups) as the last channel, which is set based on the floor value between the three other components.
For example, the color 'FFBBAA' would result in a white component value of 'AA' automatically.
There are no current plans for a workaround for different behavior or way to disable this with four-channel support.

#### Mixing WS2182 and SK6812, RGB and RGBW on a single chain:

The protocols for WS2182 and SK6812 light data are different and accidentally compatible, so it is possible to
set up a mostly-working string of lights with both kinds of unit mixed in. Due to GRBW and GRB channel orderings and four-vs-three channel-per-package management, you may end up having to hand define every channel on every light in a mixed string.

To specify which numbers on a mixed chain have four-channel SK6812 units, use the additional option `rgbw_numbers`

``` yaml
fast:
  exp:
    boards:
      neuron:
        model: FP-EXP-2000
        led_ports:
          - port: 1
            type: mixed
            count: 64
            rgbw_numbers: [1, 3, 64]
          - port: 2
            count: 0 # relocated all 32 to port 1
lights:
  my_first_sk6218_unit:
    number: neuron-1-1
    type: rgb # the rgbw type should not be used with SK6218s on FAST hardware, use rgb or grb as appropriate
  my_first_ws2182_unit:
    number: neuron-1-2
    type: rgb # a true rgb unit
  my_second_sk6218_unit:
    number: neuron-1-3
  my_second_ws2182_unit:
    number: neuron-1-4

  my_last_sk6812_unit:
    number: neuron-1-64
```

The white channel of the SK6812 units on a mixed port will behave with the same floor function as the sk6812 type port configuration.

### led_fade_time:

Single value, type: `time string (ms)`
[Instructions for entering time strings](../instructions/time_strings.md). Defaults to empty.

Specify the fade default for LEDs on this board. Note that values above the limit of 8191 (ms) will raise an error.

### led_hz:

Single value, type: `float`, default: `30`

Specify the refresh rate of the LEDs for this board. Note that values above the limit of 31.25 will be set to the limit.

### ignore_led_errors:

Single value, type: `boolean`, default: `false`

If false, LED hex communication decode errors will be raised as errors when encountered from this board.
If you encounter instability due to these errors, set this to true to silently ignore them.

## Using `exp_int:` - Raspberry Pi only

If using a Raspberry Pi connected directly to the Neuron controller, the LED headers on the Neuron will not be available on the normal EXP interface.
In order to access these Neuron LED headers, you must define a parallel structure to the existing `exp:` configuration, and move the Neuron EXP board definition over to it.

Example:

``` yaml
fast:
  exp_int:
    boards:
      neuron:
        model: FP-EXP-2000
```

## FAST Docs:

For more information, see the [FAST EXP Interface MPF Config page](https://fastpinball.com/mpf/config/exp/).
