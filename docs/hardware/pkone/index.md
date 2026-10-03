---
title: How to configure MPF for Penny K Pinball PKONE hardware
---

# How to configure MPF for Penny K Pinball PKONE hardware

--8<-- "hardware_platform.md"

Here's a list of all the How To guides which explain how to use MPF
with Penny K Pinball PKONE hardware. These guides include the numbering
format (how you map specific entries in your config files to board and
connector locations) as well as overall settings that affect how your
PKONE hardware performs. (Watch dogs, update speeds, etc.).

For additional information, please visit the [Penny K Pinball
website](https://pennykpinball.com).

Current PKONE firmware supports these boards:

* **EX2**: 30 switch inputs, five opto inputs, ten coil outputs and four
  servo outputs.
* **Switch**: 40 switch inputs. Its two physical output connectors are
  disabled in the current firmware and must not be configured as MPF coils.
* **Lightshow**: 40 simple-light outputs and eight addressable-light groups
  with up to 64 pixels per group. Firmware 3.0 can configure each group as
  RGB or RGBW.

Each board on one CAN chain must have a unique Address ID. MPF hardware
numbers use that Address ID; the permanent board serial number is for
inventory and does not replace the DIP-switch address in an MPF config.

* [Connecting PKONE to your Computer](connecting.md)
* [Installing hardware drivers & configuring COM ports](config.md)
* [Switches](switches.md)
* [Coils/Drivers/Magnets/Motors](drivers.md)
* [RGB/RGBW LEDs](leds.md)
* [Simple LEDs/Lights](lights.md)
* [Servos](servos.md)
* [Troubleshooting](../../troubleshooting/index.md)
