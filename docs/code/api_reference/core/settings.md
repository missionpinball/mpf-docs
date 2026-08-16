---
title: API Reference - settings
---

# settings API Reference

`self.machine.settings`

``` python
class mpf.core.settings_controller.SettingsController(machine)
```

Bases: `mpf.core.mpf_controller.MpfController`

Manages operator controllable settings.

## Accessing the settings in code

There is only one instance of the settings in MPF, and it's accessible via `self.machine.settings`.

## Methods & Attributes

The settings has the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`add_setting(setting: mpf.core.settings_controller.SettingEntry)`

Add a setting.

`get_setting_machine_var(setting_name)`

Return machine var name.

`get_setting_value(setting_name)`

Return the current value of a setting.

`get_setting_value_label(setting_name)`

Return label for value.

`get_settings() → List[mpf.core.settings_controller.SettingEntry]`

Return all available settings.

`set_setting_value(setting_name, value)`

Set the value of a setting.

## Config Reference:

* [settings: Config Reference](../../../config/settings.md)
