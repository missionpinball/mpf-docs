---
title: How to configure switches (Penny K Pinball PKONE)
---

# How to configure switches (Penny K Pinball PKONE)


Related Config File Sections:

* [pkone:](../../config/pkone.md)
* [switches:](../../config/switches.md)

To configure switches with Penny K Pinball PKONE hardware, you can
follow the guides and instructions in the
[Switches](../../mechs/switches/index.md) docs.

However there are a few things to know and some additional options you
get with Penny K Pinball PKONE hardware that is discussed here.

## number:

When you're using PKONE Extension boards, switches plug into individual
Extension boards. Then the Extension boards are connected together in a
chain.

![image](../images/pkone-extension.png)

The `number:` setting for each switch is its board's Address ID number
in the PKONE chain, then the dash, then the switch input number (1-35).

``` yaml
switches:
  my_switch:
    number: 0-0    # Extension board at address 0, switch 0
  some_other_switch:
    number: 2-24    # Extension board at address 2, switch 24
```

Notes:

* The PKONE Extension board Address ID switches can be set from 0 to
    7.
* Switches 31-35 are setup in the hardware to support optos and
    other normally closed (NC) switches. Do not list them as NC
    switches in your configuration as the hardware already inverts the
    values before sending them to MPF.

## What if it did not work?

Have a look at our
[PKONE troubleshooting guide](../../troubleshooting/index.md).
