---
title: RE-P-Roc-1 - Known Firmware Bug in P/P3-Roc
---

# RE-P-Roc-1 - Known Firmware Bug in P/P3-Roc


Related Config File Sections:

* [p_roc:](../config/p_roc.md)

This error occurs when you try to use `pulse_power` on drivers on the
P3-Roc with firmware 2.14 or earlier and enable a rule with hold.

This can be solved by either removing `pulse_power` from the coil in
question or by upgrading the firmware. Firmware can be obtained from the
Multimorphic Member Area.

See [How to update the Firmware of the P-Roc or P3-Roc](../hardware/multimorphic/firmware_upgrade.md) for details about the upgrade process.

## Need more help troubleshooting?

Have a look at our [Troubleshooting](../troubleshooting/index.md) section. It might give you some hints for certain classes of
problems.

## What if this did not fix your problem?

Please tell us about your error in the [community forum](../community/index.md) and we might
be able to update this page afterwards. Or even better:
[You help us to update it afterwards](../about/help_docs.md).

## Is something missing here? Do you have a helpful hint for others experiencing this error?

Please
[create a Pull Request and add it](../about/help_docs.md). Alternatively, please tell us in the [community forum](../community/index.md).

## Related How To guides

* [How to configure Multimorphic (P-ROC & P3-ROC) hardware](../hardware/multimorphic/index.md)
* [Troubleshooting P-Roc/P3-Roc](../hardware/multimorphic/troubleshooting.md)
* [How to update the Firmware of the P-Roc or P3-Roc](../hardware/multimorphic/firmware_upgrade.md)
