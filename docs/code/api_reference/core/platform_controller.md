# self.machine.platform_controller

``` python
class mpf.core.platform_controller.PlatformController(machine: MachineController)
```

Bases: `mpf.core.mpf_controller.MpfController`

Manages all platforms and rules.

## Accessing the platform_controller in code

There is only one instance of the platform_controller in MPF, and it’s accessible via `self.machine.platform_controller`.

## Methods & Attributes

The platform_controller has the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`clear_hw_rule(rule: mpf.core.platform_controller.HardwareRule)`

Clear all rules for switch and this driver.

Parameters:

* **rule** – Hardware rule to clean.

`set_delayed_pulse_on_hit_rule(enable_switch: mpf.core.platform_controller.SwitchRuleSettings, driver: mpf.core.platform_controller.DriverRuleSettings, delay_ms, pulse_setting: mpf.core.platform_controller.PulseRuleSettings = None) → mpf.core.platform_controller.HardwareRule`

Add delayed pulse on hit rule to driver. Always do the full pulse. Even when the switch is released. Pulse is delayed accurately by the hardware.

Parameters:

* **enable_switch** – Switch which triggers the rule.
* **driver** – `class DriverRuleSettings`
* **delay_ms** – Delay before the pulse in ms
* **pulse_setting** – `class PulseRuleSettings`

`set_pulse_on_hit_and_enable_and_release_and_disable_rule(enable_switch: mpf.core.platform_controller.SwitchRuleSettings, eos_switch: mpf.core.platform_controller.SwitchRuleSettings, driver: mpf.core.platform_controller.DriverRuleSettings, pulse_setting: Optional[mpf.core.platform_controller.PulseRuleSettings] = None, hold_settings: Optional[mpf.core.platform_controller.HoldRuleSettings] = None, eos_settings: Optional[mpf.core.platform_controller.RepulseRuleSettings] = None) → mpf.core.platform_controller.HardwareRule`

Add pulse on hit and enable and release and disable rule to driver. Pulse and then enable driver. Cancel pulse and enable when switch is released or a disable switch is hit.

Parameters:

* **enable_switch** – Switch to enable coil.
* **eos_switch** – Switch to switch from pulse to hold and to trigger repulses.
* **driver** – Driver to enable.
* **pulse_setting** – Pulse settings.
* **hold_settings** – Hold settings.
* **eos_settings** – How to repulse the coil when EOS opens.

`set_pulse_on_hit_and_enable_and_release_rule(enable_switch: mpf.core.platform_controller.SwitchRuleSettings, driver: mpf.core.platform_controller.DriverRuleSettings, pulse_setting: mpf.core.platform_controller.PulseRuleSettings = None, hold_settings: mpf.core.platform_controller.HoldRuleSettings = None) → mpf.core.platform_controller.HardwareRule`

Add pulse on hit and enable and release rule to driver. Pulse and enable a driver. Cancel pulse and enable if switch is released.

Parameters:

* **enable_switch** – Switch which triggers the rule.
* **driver** – Driver to trigger.
* **pulse_setting** – `class PulseRuleSettings`
* **hold_settings** – `class HoldRuleSettings`

`set_pulse_on_hit_and_release_and_disable_rule(enable_switch: mpf.core.platform_controller.SwitchRuleSettings, eos_switch: mpf.core.platform_controller.SwitchRuleSettings, driver: mpf.core.platform_controller.DriverRuleSettings, pulse_setting: Optional[mpf.core.platform_controller.PulseRuleSettings] = None, eos_settings: Optional[mpf.core.platform_controller.RepulseRuleSettings] = None) → mpf.core.platform_controller.HardwareRule`

Add pulse on hit and release and disable rule to driver. Pulse driver. Cancel pulse when switch is released or a disable switch is hit.

Parameters:

* **enable_switch** – Switch to enable coil.
* **eos_switch** – Switch to cancel pulse and trigger repulses.
* **driver** – Driver to enable.
* **pulse_setting** – Pulse settings.
* **eos_settings** – How to repulse the coil when EOS opens.

`set_pulse_on_hit_and_release_rule(enable_switch: mpf.core.platform_controller.SwitchRuleSettings, driver: mpf.core.platform_controller.DriverRuleSettings, pulse_setting: mpf.core.platform_controller.PulseRuleSettings = None) → mpf.core.platform_controller.HardwareRule`

Add pulse on hit and release rule to driver. Pulse a driver but cancel pulse when switch is released.

Parameters:

* **enable_switch** – Switch which triggers the rule.
* **driver** – `class DriverRuleSettings`
* **pulse_setting** – `class PulseRuleSettings`

`set_pulse_on_hit_rule(enable_switch: mpf.core.platform_controller.SwitchRuleSettings, driver: mpf.core.platform_controller.DriverRuleSettings, pulse_setting: mpf.core.platform_controller.PulseRuleSettings = None) → mpf.core.platform_controller.HardwareRule`

Add pulse on hit rule to driver.  Always do the full pulse. Even when the switch is released.

Parameters:

* **enable_switch** – Switch which triggers the rule.
* **driver** – `class DriverRuleSettings`
* **pulse_setting** – `class PulseRuleSettings`
