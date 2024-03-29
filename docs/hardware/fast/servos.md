---
title: How to configure servos (FAST Pinball)
---

# How to configure servos (FAST Pinball)

!!! note "FAST Pinball servos are mostly different now"

    This documentation describes how to use servos connected to
    a special daughter board on FAST I/O boards. This is not the
    current way FAST does things, and this documentation is here
    for historical purposes for people who might be doing things
    this way.

    Modern FAST servos use the
    EXP bus via expansion boards. See the
    [documentation](https://fastpinball.com/docs) on the FAST
    website for details.

Related Config File Sections:

* [servos:](../../config/servos.md)

You can drive servos from any FAST IO board by adding the FAST Servo
Controller daughter board to it. You then configure and use the servos
like normal. The only real "FAST-specific" thing is the number.

Overview video about [servos](../../mechs/servos/index.md):

<div class="video-wrapper">
<iframe width="560" height="315" src="https://www.youtube.com/embed/wA6KEODwQ5w" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## number:

The number of the servo requires a bit of math. Each FAST IO board
"reserves" six slots for daughter board accessories (regardless of
whether there's a daughter board there are not). So the numbers go like
this:

* First board in the chain (Board 0), numbers 0, 1, 2, 3, 4, 5
* Second board in the chain (Board 1), numbers 6, 7, 8, 9, 10, 11
* Third board in the chain (Board 2), numbers 12, 13, 14, 15, 16, 17
* Fourth board in the chain (Board 3), numbers 18, 19, 20, 21, 22, 23
* etc.

So to figure out the number for your servo, first figure out which board
it's plugged into, then look at which connection on that board it uses,
then figure out the number based on the list above.

By default, standalone numbers like this have to be entered in hex
format, so once you find your number, enter it as the hex equivalent:

  Regular   Hex
  --------- -----
  0         0
  1         1
  2         2
  3         3
  4         4
  5         5
  6         6
  7         7
  8         8
  9         9
  10        a
  11        b
  12        c
  13        d
  14        e
  15        f
  16        10
  17        11
  18        12
  19        13
  20        14
  21        15
  22        16
  23        17

If you don't want to mess with all this hex stuff, you can set the
config number format to "int" via the `fast: config_number_format:`
setting. See the [fast:](../../config/fast.md) section of
the config file reference for details.

## What if it did not work?

Have a look at our
[FAST troubleshooting guide](../../troubleshooting/index.md).
