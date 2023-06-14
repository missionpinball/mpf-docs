---
title: CFE-ConfigValidator-13: Cannot convert value to boolean
---

# CFE-ConfigValidator-13: Cannot convert value to boolean


This error occurs when MPF expects a boolean value (i.e. `true` or
`false`) for a config setting but got a value of a different type.

## Examples

For instance, the `debug` setting for a
[switch](../config/switches.md) is a boolean:

``` mpf-config
switches:
  s_flipper_left:
    number: 1
    debug: true   # we want all the details about this switch in the logs
```

You can see which settings are boolean in the
[config reference](../config/index.md) of your
device.

## Common Pitfalls

### Widget Animations Repeat

In MPF versions before 0.53 `repeat` in widgets has been an integer
which has been converted to boolean internally. A lot of examples (and
the tutorial) contained `repeat: -1`. You need to change this to
`repeat: false` to fix this error.

### Using Quotes

If you use `debug: "false"` (with quotes around `false`) MPF will not
recognize `false` as a boolean but as a string. Remove the quotes to fix
this.

## Need more help troubleshooting?

Have a look at our [Troubleshooting](../troubleshooting/index.md) section. It might give you some hints for certain classes of
problems.

## What if this did not fix your problem?

Please tell us about your error in the [MPF Users Google
Group](https://groups.google.com/forum/#!forum/mpf-users) and we might
be able to update this page afterwards. Or even better:
[You help us to update it afterwards](../about/help_docs.md).

## Is something missing here? Do you have a helpful hint for others experiencing this error?

Please
[create a Pull Request and add it](../about/help_docs.md). Alternatively, please tell us in the [MPF Users Google
Group](https://groups.google.com/forum/#!forum/mpf-users).

## Related How To guides

* [config reference](../config/index.md)
