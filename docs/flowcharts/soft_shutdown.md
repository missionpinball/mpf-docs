---
title: MPF Soft Power Down Sequence
---

# MPF Soft Power Down Sequence

The soft power down sequence is a process you can take advantage of to shut down your game process cleanly,
or even command the entire computer to shut down. The FAST Neuron processor supports a native integration
of this feature with its soft power button, but other controllers can take advantage of the system as well.


## Steps

Any MPF game can be configured with a soft power request system.
The default game logic listens for the event `request_soft_shutdown`, which you can post via an event player:

```yaml
event_player:
  my_trigger_event: request_soft_shutdown
```

The core MPF code in `machine.py` listens for this event, and will post the [boolean event](../events/overview/event_types.md#boolean-events) [*machine_request_shutdown*](../events/machine_request_shutdown.md).

If any handlers return False, the soft powerdown will abort, and the event *machine_abort_shutdown* is posted.

If there are no handlers, or all handlers return True, the powerdown will continue. The event *machine_will_shutdown* is posted and the machine subsystems will begin graceful exit procedures.

Finally, if the config option [machine:soft_shutdown_exit_command](../config/machine.md#soft_shutdown_exit_command) is defined, it will be executed asynchronously.


## FAST Neuron integration

Games using the FAST Neuron controller can also use the *request_soft_shutdown* event, but MPF also is able to listen to the built-in Soft Power switch provided by the platform.

These functions only operate when using the soft power mode, see the [FAST website](https://fastpinball.com/wiring/neuron/solid-state-relay/) for wiring details.

If in soft power mode, the watchdog `WD:` command will automatically detect when the soft power button is pressed or released.
While MPF is running, if the soft power switch is pressed, the synthetic switch event *fast_soft_power_switch_active* will be posted.
When the switch is released, the synthetic switch event *fast_soft_power_switch_inactive* is posted.

If the time between the button press and release is longer than the config value [fast:net:soft_power_hold_ms](../config/fast/fast_net.md#soft_power_hold_ms) then it will post *request_soft_shutdown*, starting the standard procedure described above.

For non-FAST Neuron systems, or FAST Neurons using standard power (not soft power), the controller will not automatically shut down at the end of the shutdown process.
