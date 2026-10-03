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
  -> PKONE EX2 USB connection - Port: com3 at 115200 baud (firmware v3.0, hardware rev 20)

- EX2 boards:
  -> Address ID: 0 (firmware v3.0, hardware rev 20)

- Switch boards:
  -> Address ID: 1 (firmware v3.0, hardware rev 20)

- Lightshow boards:
  -> Address ID: 2 (MIX firmware v3.0, hardware rev 20)
```

See [mpf hardware (command-line utility)](../../running/commands/hardware.md) for
details.

## Enable Debugging

If you got problems with your platform try to enable `debug` first. As
described in the
[general debugging section](../../troubleshooting/general_debugging.md) of our
[troubleshooting guide](../../troubleshooting/index.md) this is done by adding `debug: true` to your `pkone` config
section:

``` yaml
pkone:
  debug: true
```

This will add a lot more debugging and might slow down MPF a bit. We
recommend to disable/remove it after finishing debugging.

## Startup and watchdog errors

MPF places a deadline on controller reset, board discovery, mixed LED
configuration and initial switch snapshots. Check the first reported failure
rather than repeatedly reconnecting:

* A timeout usually means the wrong serial port, a missing board reply, a bad
  CAN cable or incorrect termination.
* An address mismatch usually means duplicate DIP-switch addresses.
* A malformed switch snapshot indicates incompatible firmware or corrupted
  serial/CAN traffic.
* A hardware-watchdog timeout stops MPF because the boards have disabled their
  outputs. Correct the connection and restart MPF before testing again.
