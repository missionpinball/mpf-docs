---
title: Drop Target Bank
---

# Drop Target Bank


Related Config File Sections:

* [drop_targets:](../../../config/drop_targets.md)
* [drop_target_banks:](../../../config/drop_target_banks.md)

In MPF, you can combine multiple drop targets into drop target banks.
The main reasons for doing this are to combine reset coils (since one
coil typically resets an entire bank) and to get additional events
posted when the entire bank is up, down or in a mixed state.

![image](/docs/mechs/images/drop_target_bank.jpg)

This is an example:

``` mpf-config
#! switches:
#!   s_drop_front:
#!     number:
#!   s_drop_middle:
#!     number:
#!   s_drop_back:
#!     number:
#! coils:
#!   c_drop_reset:
#!     number:
drop_targets:
  front:
    switch: s_drop_front
  middle:
    switch: s_drop_middle
  back:
    switch: s_drop_back
drop_target_banks:
  vuk_bank:
    drop_targets: front, middle, back
    reset_coils: c_drop_reset
    reset_on_complete: 1s
```

## Monitorable Properties

For
[dynamic values](../../../config/instructions/dynamic_values.md) and
[conditional events](../../../events/overview/conditional.md), the prefix for drop target banks is
`device.drop_target_banks.(name)`.

*complete*

:   Boolean (true/false) which shows whether every target in this bank
    is complete (down).

*down*

:   Number of drop targets in the bank that are in the down state.

*up*

:   Number of drop targets in the bank that are in the up state.

## Related How To guides

* [Welcome to The Mission Pinball Framework!](../../../index.md)
* [/events/drop_target_bank_drop_target_bank_mixed](fixing_drop_target_reset_issues.md)

## Related Events

* [drop_target_bank_(name)_down](../../../events/drop_target_bank_drop_target_bank_down.md)
* [drop_target_bank_(name)_up](../../../events/drop_target_bank_drop_target_bank_up.md)
* [drop_target_bank_(name)_mixed](../../../events/drop_target_bank_drop_target_bank_mixed.md)
