---
title: "CFE-ConfigValidator-9: Required setting is missing from section in your config"
---

# CFE-ConfigValidator-9: Required setting is missing from section in your config

This error occurs when MPF does not find a required setting in one of
your config sections.

## Examples

For instance, every switch has to have a number in MPF:

``` mpf-config
switches:
  s_ball_switch1:
    number: 1
```

You can see which settings are required in the
[config reference](../config/index.md) of your
device. For this instance, check the
[switch config reference](../config/switches.md) and you will find that only `number` is a required setting.

## Common Pitfalls

### Omitting one of the required settings

If you omit on of the required settings you will see this error. To this
this browse to the [config reference](../config/index.md) of your device and add all the required settings.
Alternatively, you could use your
[IDE with the MPF language server](../tools/language_server/index.md) to auto-complete all required settings.

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
