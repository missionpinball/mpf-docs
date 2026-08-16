---
title: "CFE-DeviceManager-3: Device does not have a valid config. Expected a dictionary."
---

# CFE-DeviceManager-3: Device does not have a valid config. Expected a dictionary.

This error occurs when MPF expects a dictionary in a config of a device
but found something else.

## Examples

For instance, the settings of a
[switch](../config/switches.md) are a
dictionary (switches -> s_flipper_left).

``` yaml
switches:
  s_flipper_left:
    number: 1
    label: My Left Flipper
```

## Common Pitfalls

### Forgetting the Device Name

This error usually occurs when you omit the device name. For example if
you omit `s_flipper_left` this would look like this:

``` yaml
# BROKEN CONFIG
switches:
  number: 1
  label: My Left Flipper
```

Here MPF would see two switches with the names `number` and `label`.
Each of them has an invalid config (just a single value but not a
dictionary).

### YAML Formatting Issues

See [CFE-ConfigValidator-12: Item is not a dict](CFE-ConfigValidator-12.md) for more
general common pitfalls.

## Need more help troubleshooting?

Have a look at our [CFE-ConfigValidator-12](../troubleshooting/index.md) section. It might give you some hints for certain classes of
problems.

## What if this did not fix your problem?

Please tell us about your error in the [community forum](../community/index.md) and we might
be able to update this page afterwards. Or even better:
[You help us to update it afterwards](../about/help_docs.md).

## Is something missing here? Do you have a helpful hint for others experiencing this error?

Please
[create a Pull Request and add it](../about/help_docs.md). Alternatively, please tell us in the [community forum](../community/index.md).

## Related How To guides

* [CFE-ConfigValidator-12: Item is not a dict](CFE-ConfigValidator-12.md)
* [config reference](../config/index.md)
