---
title: Troubleshooting OPP
---

# Troubleshooting OPP


If you got problems with your hardware platform we first recommend to
read our
[troubleshooting guide](../../troubleshooting/index.md). Here are some hardware platform specific steps:

## Run Hardware Scan

Using `mpf hardware scan` you can find out if your OPP boards are
talking properly to MPF using USB:

``` console
$ mpf hardware scan

Connected CPUs:
 - Port: com1 at 115200 baud
 -> Board: 0x20 Firmware: 0x10100
 -> Board: 0x21 Firmware: 0x10100

Incand cards:
 - CPU: com1 Board: 0x20 Card: 0 Numbers: [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]

Input cards:
 - CPU: com1 Board: 0x20 Card: 0 Numbers: [0, 1, 2, 3, 8, 9, 10, 11, 12, 13, 14, 15]
 - CPU: com1 Board: 0x21 Card: 1 Numbers: [0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]

Solenoid cards:
 - CPU: com1 Board: 0x20 Card: 0 Numbers: [0, 1, 2, 3]
 - CPU: com1 Board: 0x21 Card: 1 Numbers: [12, 13, 14, 15]

LEDs:
 - CPU: com1 Board: 0x21 Card: 1
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
opp:
  debug: true
```

This will add a lot more debugging and might slow down MPF a bit. We
recommend to disable/remove it after finishing debugging.

## Reducing the polling rate

If you encounter issues with the polling rate (in other words: Your OPP
processor boards can't answer MPF's polls fast enough) you may want to
change it. This can be done by simply adding the `poll_hz:` line to the
`opp:` section:

``` yaml
opp:
  ports: COM7
  poll_hz: 50    # defaults to 100
```

!!! note

    You only want to do this if you encounter issues. This will increase the
    time between two switches beeing read. If you set this too log you could
    miss hits if multiple hits happened between two polls.

## Coils Are Not Firing

What to do if your coils are not working?

--8<-- "troubleshooting_coils.md"

--8<-- "troubleshooting_lights.md"

--8<-- "troubleshooting.md"
