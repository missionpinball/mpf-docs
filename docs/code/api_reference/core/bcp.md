# bcp API Reference

`self.machine.bcp`

``` python
class mpf.core.bcp.bcp.Bcp(machine: MachineController)
```

Bases: `mpf.core.mpf_controller.MpfController`

BCP Module.

## Accessing the bcp in code

There is only one instance of the bcp in MPF, and it's accessible via self.machine.bcp.

## Methods & Attributes

The bcp has the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`send(bcp_command, **kwargs)`

Emulate legacy send.

Parameters:

* **bcp_command** – Commmand to send

## Related Pages:

* [bcp: Config Reference](../../../config/bcp.md)
