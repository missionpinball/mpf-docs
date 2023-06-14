---
title: Troubleshooting Fadecandy
---

# Troubleshooting Fadecandy


If you got problems with your hardware platform we first recommend to
read our
[troubleshooting guide](../../troubleshooting/index.md). Here are some hardware platform specific steps:

## Enable Debugging

If you got problems with your platform try to enable `debug` first. As
described in the
[general debugging section](../../troubleshooting/general_debugging.md) of our
[troubleshooting guide](../../troubleshooting/index.md) this is done by adding `debug: true` to your `fadecandy`
config section:

``` mpf-config
fadecandy:
  debug: true
```

This will add a lot more debugging and might slow down MPF a bit. We
recommend to disable/remove it after finishing debugging.

## Flickering Lights after a few Restarts

At some point fadecandy might exhibit erratic behavior or flickering
lights after a few restarts of MPF. This usually can be fixed by power
cycling the fadecandy (i.e. unplug it from USB and plug it in again). We
created a [bug report in the fadecandy
repository](https://github.com/scanlime/fadecandy/issues/112) for this
case. We suspect a race which triggers some data corruption in the
fadecandy firmware. If you are an embedded engineer or know anybody who
could help to fix this issue please let us know. Nevertheless, we have
never seen this outside of debugging sessions where we restart MPF
frequently so it manageable once you know what it is.

--8<-- "troubleshooting.md"
