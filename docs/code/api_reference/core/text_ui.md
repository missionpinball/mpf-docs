
# self.machine.text_ui

`class mpf.core.text_ui.TextUi(machine: MachineController)`

Bases: mpf.core.mpf_controller.MpfController

Handles the text-based UI.

## Accessing the text_ui in code

There is only one instance of the `text_ui` in MPF, and it’s accessible via `self.machine.text_ui`.

## Methods & Attributes

The text_ui has the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`stop(**kwargs)`

Stop the Text UI and restore the original console screen.

