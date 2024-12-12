---
title: How to configure Simple LEDs (Penny K Pinball)
---

# How to configure Simple LEDs (Penny K Pinball)


Related Config File Sections:

* [lights:](../../config/lights.md)

Up to 45 Simple LED lights are supported on Penny K Pinball PKONE
Lightshow boards. Simple LED lights are single channel monochromatic
LEDs most frequently used under colored inserts in the playfield or
behind colored artwork behind a backglass.

## number:

When you're using PKONE Lightshow boards, simple LEDs plug into
individual Lightshow boards. Then the Lightshow boards are connected
together in a chain with other add-on boards (such as PKONE Extension
boards) to the controller.

![image](/docs/hardware/images/pkone-lightshow.png)

The `number:` setting for each simple LED is its board's Address ID
number in the PKONE chain, then the dash, then the simple LED output
number.

``` mpf-config
lights:
  special_light:
    number: 0-1    # Lightshow board with Address ID 0, simple LED 1
    subtype: simple
  some_other_light:
    number: 2-10    # Lightshow board with Address ID 2, simple LED 10
    subtype: simple
```

Notes:

* The PKONE Lightshow board Address ID switches can be set from 0 to
    3.

## subtype:

Single value, type: `string`. Defaults to empty.

This value is used to distinguish between simple LEDs and WS281X RGB
LEDs in the PKONE hardware system. This value must be set to `simple`
when setting up simple LEDs (WS281X RGB LEDs use `led` as the `subtype:`
value).

## What if it did not work?

Have a look at our
[PKONE troubleshooting guide](../../troubleshooting/index.md).
