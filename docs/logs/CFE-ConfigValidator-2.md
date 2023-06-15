---
title: CFE-ConfigValidator-2: Your config contains a value for the
  setting, but this is not a valid setting name
---

This error occurs when MPF does not know a setting you specified in a
device.

## Examples

For instance, a [switch](../config/switches.md) knows certain settings:

``` mpf-config
switches:
  s_flipper_left:
    number: 1
    label: My Left Flipper Switch Example
    tags: some_custom_tag
```

You can see which settings are allowed in the
[config reference](../config/index.md) of your
device.

## Common Pitfalls

### Typos

The most common source for this kind of error are typos. Check the name
of your referenced device with the setting. Casing matters here (i.e.
upper/lower case). Using an
[IDE with the MPF language server](../tools/language_server/index.md) can help here.

### Mixing Devices

Maybe you accidentially copied config attributes from a different type
of devices? Double check if you refered to the documentation of the
correct device. If you find incorrect documentation please tell us in
the forum.

### Incorrect Indent

With nested configs (i.e. slide_player or widget_player) you might have
used an option which should be indented one level further or one level
less. This can sometimes be a bit tricky. Using an
[IDE with the MPF language server](../tools/language_server/index.md) can help here.

### Running Config from a different MPF Version

Sometimes MPF config specifications change. Check if your MPF version
fits the config. If in doubt check the
[config reference](../config/index.md) for
your device.

## Need more help troubleshooting?

Have a look at our [Troubleshooting](../troubleshooting/index.md) section. It might give you some hints for certain classes of
problems.

## What if this did not fix your problem?

Please tell us about your error in the [community forum](../community/index.md) and we might
be able to update this page afterwards. Or even better:
[You help us to update it afterwards](../about/help_docs.md).

## Is something missing here? Do you have a helpful hint for others experiencing this error?

Please
[create a Pull Request and add it](../about/help_docs.md). Alternatively, please tell us in the [community forum](../community/index.md).

## Related How To guides

* [config reference](../config/index.md)
