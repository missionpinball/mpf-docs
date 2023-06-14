---
title: "step_stick_stepper_settings:"
---

# step_stick_stepper_settings:


--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**NO** :no_entry_sign:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|

The `step_stick_stepper_settings:` section of your config is where you
configure the
[Stepstick hardware platform](../hardware/stepstick.md).

## Optional settings

The following sections are optional in the
`step_stick_stepper_settings:` section of your config. (If you don't
include them, the default will be used).

### high_time:

Single value, type: `time string (secs)`
([Instructions for entering time strings](instructions/time_strings.md)) . Default: `20ms`

How long should the digital output be held to high during a step pulse?
This time depends on the latency/jitter of your output and the speed
your stepper can be moved. Usually the jitter of your output is the
limiting factor.

### low_time:

Single value, type: `time string (secs)`
([Instructions for entering time strings](instructions/time_strings.md)) . Default: `20ms`

How long should the digital output be held to low after a step pulse?
This time depends on the latency/jitter of your output and the speed
your stepper can be moved. Usually the jitter of your output is the
limiting factor.
