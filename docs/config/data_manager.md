---
title: "data_manager: Config Reference"
---

# data_manager: Config Reference

--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|

The *data_manager:* section of the machine configuration file lets you
control how the data manager saves data.


``` yaml
data_manager:
    use_fsync: True
```

## Optional settings

The following sections are optional in the `data_manager:` section of your
config. (If you don't include them, the default will be used).

### use_fsync:

Single value, type: `boolean` (`true`/`false`). Default: `None`

Controls whether the data manager uses fsync when saving files.
By default this is used with audits.yaml, earnings.yaml, high_scores.yaml, and machine_vars.yaml.

The default is `None`, which allows MPF to select a behavior based on the platform it detects.
For Windows, this is `False`, as fsync does not work in certain cases and will cause excess logging.
For Mac and Linux, this is `True`, and it MPF use fsync.
