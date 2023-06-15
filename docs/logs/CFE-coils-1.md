---
title: CFE-coils-1: Driver must have a number
---

# CFE-coils-1: Driver must have a number


Related Config File Sections:

* [coils:](../config/coils.md)

This error occurs when MPF loads a coil which is has an empty number or
misses a number entry. Unfortunately, hardware needs a switch number to
address your coil and it cannot continue without a number.

## Examples

### Physical Coils

This is how a coil should look:

``` mpf-config
coils:
  your_coil:
    number: 1
```

The actual number depends on your hardware platform. See the
[How to configure "number:" settings](../hardware/numbers.md) guide for details.

### Virtual Coils

Sometimes you did not wire up a coil but you know that you will need it
later. This is a problem for your physical hardware controller but you
can tell MPF to use the `virtual` hardware platform for one particular
coil:

``` mpf-config
coils:
  your_virtual_coil:
    number:
    platform: virtual
```

In this case the number can be empty.

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

* [Coils (Solenoids)](../mechs/coils/index.md)
