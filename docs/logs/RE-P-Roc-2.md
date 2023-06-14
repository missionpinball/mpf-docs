---
title: RE-P-Roc-2 - Communication with P/P3-Roc broke down
---

# RE-P-Roc-2 - Communication with P/P3-Roc broke down


Related Config File Sections:

* [p_roc:](../config/p_roc.md)

In your log you will probably find a line such as:

``` doscon
OSError: Error in WriteData: wrote 0 of 8 bytes
```

This error occurs when `pinproc` (the library MPF uses to talk to the
P/P3-Roc) reports an error while talking to the P/P3-Roc via USB. This
is most likely a bad cable or a power supply issue. See
[Troubleshooting P-Roc/P3-Roc](../hardware/multimorphic/troubleshooting.md)
for potential causes and solutions.

## Need more help troubleshooting?

Have a look at our [Troubleshooting](../troubleshooting/index.md) section. It might give you some hints for certain classes of
problems.

## What if this did not fix your problem?

Please tell us about your error in the [MPF Users Google
Group](https://groups.google.com/forum/#!forum/mpf-users) and we might
be able to update this page afterwards. Or even better:
[You help us to update it afterwards](../about/help_docs.md).

## Is something missing here? Do you have a helpful hint for others experiencing this error?

Please
[create a Pull Request and add it](../about/help_docs.md). Alternatively, please tell us in the [MPF Users Google
Group](https://groups.google.com/forum/#!forum/mpf-users).

## Related How To guides

* [Troubleshooting P-Roc/P3-Roc](../hardware/multimorphic/troubleshooting.md)
* [Wiring and Connectors in Pinball Machines](../hardware/voltages_and_power/wiring_and_connectors.md)
* [Voltages and Power](../hardware/voltages_and_power/voltages_and_power.md)
