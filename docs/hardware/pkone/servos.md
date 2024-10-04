---
title: How to configure servos (Penny K Pinball PKONE)
---

# How to configure servos (Penny K Pinball PKONE)


Related Config File Sections:

* [servos:](../../config/servos.md)

You can drive up to four servos from any PKONE Extension board.

Overview video about [servos](../../mechs/servos/index.md):

<div class="video-wrapper">
<iframe width="560" height="315" src="https://www.youtube.com/embed/wA6KEODwQ5w" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## number:

When you're using PKONE Extension boards, coils plug into individual
Extension boards. Then the Extension boards are connected together in a
chain to the controller.

![image](/docs/hardware/images/pkone-extension.png)

The `number:` setting for each servo is its board's Address ID number
in the PKONE chain, then the dash, then the servo output number (11-14).

``` mpf-config
servos:
  servo_1:
    number: 0-11    # Extension board with Address ID 0, servo 11 (the first one)
  some_other_servo:
    number: 2-14    # Extension board with Address ID 2, servo 14
```

Notes:

* The PKONE Extension board Address ID switches can be set from 0 to
    7.
* Servos are numbered from 11 to 14 on the PKONE Extension board and
    not from 1 to 4.

All the servo config options are explained in-depth in the
[servos: section](../../config/servos.md) of the
config file reference.

## What if it did not work?

Have a look at our
[PKONE troubleshooting guide](../../troubleshooting/index.md).
