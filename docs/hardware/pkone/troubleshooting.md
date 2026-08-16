---
title: Troubleshooting Penny K Pinball PKONE Hardware
---

# Troubleshooting Penny K Pinball PKONE Hardware


If you got problems with your hardware platform we first recommend to
read our
[troubleshooting guide](../../troubleshooting/index.md). Here are some hardware platform specific steps:

## Run Hardware Scan

Using `mpf hardware scan` you can find out if your PKONE boards are
talking properly to MPF using USB:

``` shell
$ mpf hardware scan

## Penny K Pinball Hardware

- Connected Controllers:
  -> PKONE Nano - Port: com3 at 115200 baud (firmware v1.1, hardware rev 2)

- Extension boards:
  -> Address ID: 0 (firmware v1.1, hardware rev 2)
  -> Address ID: 1 (firmware v1.1, hardware rev 2)

- Lightshow boards:
  -> Address ID: 2 (RGB firmware v1.0, hardware rev 1)
  -> Address ID: 3 (RGBW firmware v1.0, hardware rev 1)
```

See [mpf hardware (command-line utility)](../../running/commands/hardware.md) for
details.

## Enable Debugging

If you got problems with your platform try to enable `debug` first. As
described in the
[general debugging section](../../troubleshooting/general_debugging.md) of our
[troubleshooting guide](../../troubleshooting/index.md) this is done by adding `debug: true` to your `opp` config
section:

``` yaml
pkone:
  debug: true
```

This will add a lot more debugging and might slow down MPF a bit. We
recommend to disable/remove it after finishing debugging.
