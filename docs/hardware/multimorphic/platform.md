---
title: How to configure MPF for the P-ROC/P3-ROC platform
---

# How to configure MPF for the P-ROC/P3-ROC platform


Related Config File Sections:

* [hardware:](../../config/hardware.md)
* [p_roc:](../../config/p_roc.md)

Once you have your
[P-ROC/P3-ROC drivers installed](hardware_drivers.md), you need to configure your machine to use the P-ROC or
P3-ROC.

## 1. Set your platform

In your machine-wide config file, set the platform.

For the P-ROC:

``` yaml
hardware:
  platform: p_roc
```

For the P3-ROC:

``` yaml
hardware:
  platform: p3_roc
```

## 2. Set your driver boards:

Next, configure the driver boards setting which tells MPF which type of
driver boards you're using. If you're using the P-ROC driver boards
(like the PD-16 or PD-8x8), then you set it like this:

For the P-ROC:

``` yaml
hardware:
  platform: p_roc

p_roc:
  driverboards: pdb
```

For the P3-ROC:

``` yaml
hardware:
  platform: p3_roc

p_roc:
  driverboards: pdb
```

Note that if you're using a P-ROC with an existing machine, then your
driver boards will be either wpc, stern, etc. See the documentation on
[configuring MPF for use in existing machines](../../machines/index.md) for details.

## 3. Configure your watch dog timeout

The P-ROC has the ability to use a `watch dog` timer. This is enabled by default with a timeout of 1
second. If you would like to disable this, or you'd like to change the
timeout, you can do so in either the `p_roc:` or `p3_roc:` section of
your machine-wide config.

For the P-ROC or P3-Roc:

``` yaml
p_roc:
  use_watchdog: true
  watchdog_time: 1s
```

## What if it did not work?

Have a look at our
[troubleshooting guide for the P/P3-Roc](../../troubleshooting/index.md).
