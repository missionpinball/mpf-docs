---
title: service_trigger
---

# service_trigger


*MPF-GMC Event*

This event is posted by a the built-in GMC Service slide.

## Keyword arguments

(See the [Conditional Events](overview/conditional.md)
guide for details for how to create entries in your config file that
only respond to certain combinations of the arguments below.)

### `action`:

This parameter is always included. The other parameters will depend on which action is selected. Options are:

* service_exit
* setting
* switch_test
* coil_test
* light_test

### Action-specific parameters:

#### service_exit:

This action does not include any other parameters.

#### setting:

This action includes two additional parameters:

`variable`: The name of the setting being changed.

`value`: The new value being selected for the setting.

#### switch_test, coil_test, and light_test:

These three actions all share the same additional parameter:

`sort`: a boolean value
