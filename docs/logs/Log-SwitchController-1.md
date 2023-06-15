---
title: Log-SwitchController-1: Received duplicate switch state for
  switch
---

Related Config File Sections:

* [switches:](../config/switches.md)

MPF expects to get only state changes from platforms. That is part of
the platform interface contract. This warning indicates that the
contract is violated (i.e. because MPF got a switch close but the switch
has been closed before). This might indicate bugs in the platform
firmware, our platform interface or the communication in between.

MPF handles this gracefully so there is no need to worry. It will just
ignore the second hit and carry on.

There are conditions where you will see this. Our smart virtual platform
will sometimes trigger this. Those are kind of bugs. Usually harmless
but we will fix them if you report them.

Additionally, you can trigger those warnings if you use more than source
of switch states at once for the same switch. That could be any two of a
hardware platform, MPF monitor or keyboard mappings.

Lastly, the P-Roc is known for sending switches twice when using
debounced switches. This has to do with its internal state machine and
is usually harmless.

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
