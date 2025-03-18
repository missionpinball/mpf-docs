---
title: Switches
---

# Switches


Related Config File Sections:

* [switches:](../../config/switches.md)
* [switch_overwrites:](../../config/switch_overwrites.md)

MPF's *switch* device represents a switch in a pinball machine. This
device is used for switches, including cabinet buttons, rollovers,
targets, optos, trough switches, DIP switches, etc.

There are two switch types most commonly seen in pinball machines (read
those for details):

* [Mechanical switches](mechanical_switches.md)
* [Optical switches](optos.md)

And an additional two types used in a handful of machines (read those
for details):

* [Proximity switches](proximity_switches.md)
* [Reed switches](reed_switches.md)

Typical switch applications in pinball machines are:

* [Rollover/lane switches](rollover_switches.md)
* [Standup targets](../targets/stationary_targets.md)
* [Spinners](../spinners.md)
* [Flipper buttons](../flippers/index.md) and
    [Flipper end-of-stroke switches](../flippers/eos_switches.md)
* As part of a mech such as
    [Drop targets](../targets/drop_targets/index.md),
    [Popbumpers](../pop_bumpers/index.md) or
    [Ball Devices](../ball_devices/index.md)/[Troughs](../troughs/index.md)
* [Service and door switches](service_and_door_switches.md)

MPF supports all types of switches found in all generations of pinball
machines, including matrix switches, direct switches, Fliptronics
switches, switches connected to I/O boards, etc.

Switches only have two states](*active* and *inactive*. (We don't say
"open" or "closed" because sometimes switches are normally-closed
which mean they're actually active when they're open.) In MPF, you
configure your switches in the `switches:` section of your machine
configuration file, including options (like whether the switch is
"active" when it's in the open state or the closed state.)

You can also configure [debounce settings](debounce.md) for each switch, which controls how MPF responds to switch
events. Saying that a switch has to be "debounced" means that the
pinball controller makes sure the switch is actually in its current
state for a few milliseconds before it send the switch event to MPF.
This can be useful to filter out unwanted or phantom switch events which
might happen due to electrical interference or other little weird
things.

Most switches in pinball machines are debounced except for the ones that
you absolutely want to fire instantly, like flipper switches and the
switches attached to automatically fired coils like slingshots and pop
bumpers.

This is an example:

``` yaml
switches:
  my_switch:
    number)

*state*

Numeric value which represents the logic state of this switch. 0 is
    inactive, 1 is active.

*recycle_jitter_count*
