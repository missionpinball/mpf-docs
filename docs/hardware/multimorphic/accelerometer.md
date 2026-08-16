---
title: How to configure the accelerometer (P3-ROC)
---

# How to configure the accelerometer (P3-ROC)

THe P3-ROC includes an accelerometer which you can use with MPF to
detect g-force changes (to use as a tilt) as well as 3-axis leveling (to
use to determine whether the machine is level).

To use the accelerometer on the P3-ROC, add it to your machine-wide
config file like this:

``` yaml
accelerometers:
  p3_roc_accelerometer:
    number: 1
```

The name (which is "p3_roc_accelerometer" in the example above)
doesn't really matter.

Other than that, use it like you would any accelerometer in MPF, by
following the docs and guides in the
[Accelerometers](../../mechs/accelerometers.md) section of
the documentation.

## What if it did not work?

Have a look at our [troubleshooting guide for the P/P3-Roc](../../troubleshooting/index.md).

## Related Pages:

* [accelerometers: Config Reference](../../config/accelerometers.md)
* [accelerometers API Reference](../../code/api_reference/devices/accelerometers.md)
* [Accelerometers](../../mechs/accelerometers.md)
