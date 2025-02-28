---
title: Drop Targets
---

# Drop Targets


Related Config File Sections:

* [drop_targets:](../../../config/drop_targets.md)
* [drop_target_banks:](../../../config/drop_target_banks.md)

Mission Pinball Framework's (MPF) *drop target* device represents a
switch in a pinball machine. This device is used for drop target banks
with a coil for resetting. If the reset coil resets more than just this
one drop target configure all targets as a
[drop target bank](drop_target_bank.md) and
put the coil there. Additionally, there may be a knockdown coil which
allows the software to knock the target down.

![image](../../images/drop_target_front.jpg)

![image](../../images/drop_target_side.jpg)

![image](../../images/drop_target_back.jpg)

This is an example:

``` mpf-config
switches:
  s_drop_target:
    number:
coils:
  c_reset_drop_target:
    number:
  c_knock_down_coil:
    number:
drop_targets:
  d_drop_target:
    switch: s_drop_target
    reset_coil: c_reset_drop_target
```
