---
title: "CFE-Smart_Virtual_Platform-1: Switch used in virtual_platform_start_active_switches was not found in switches section"
---

# CFE-Smart_Virtual_Platform-1: Switch used in virtual_platform_start_active_switches was not found in switches section

Related Config File Sections:

* [switches:](../config/switches.md)
* [virtual_platform_start_active_switches:](../config/virtual_platform_start_active_switches.md)

This error occurs when you use a switch in
`virtual_platform_start_active_switches` which is not defined in your
`switches` section.

## Examples

This is how it should look:

``` mpf-config
switches:
  s_ball_switch1:
    number:
  s_ball_switch2:
    number:
  s_ball_switch3:
    number:
# Two switches should be active at start
virtual_platform_start_active_switches:
  - s_ball_switch1
  - s_ball_switch2
```

Alternatively, this could be a comma separated list:

``` mpf-config
switches:
  s_ball_switch1:
    number:
  s_ball_switch2:
    number:
  s_ball_switch3:
    number:
# Two switches should be active at start
virtual_platform_start_active_switches: s_ball_switch1, s_ball_switch2
```

## Common Pitfalls

### Using spaces instead of commas

In MPF versions before 0.54 you could also use spaces instead of commas.
Even though this syntax was never officially supported in lists it still
was supported code. This was also used in previous versions of the
documentation and the tutorial.

``` yaml
# INVALID SYNTAX
virtual_platform_start_active_switches: s_ball_switch1 s_ball_switch2  # note the space instead of a comma
```

To fix this turn it into one of the two syntaxes above. See
[How to add lists to config files](../config/instructions/lists.md) for details.

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

* [virtual_platform_start_active_switches:](../config/virtual_platform_start_active_switches.md)
* [How to add lists to config files](../config/instructions/lists.md)
