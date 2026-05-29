---
title: MPF Soft Power Down Sequence
---

# MPF Soft Power Down Sequence

The soft power down sequence is a process you can take advantage of to shut down your game process cleanly,
or even command the entire computer to shut down. The FAST Neuron processor supports a native integration
of this feature with its soft power button, but other controllers can take advantage of the system as well.


## Steps


Post the event: request_soft_shutdown
Boolean event is posted to allow blocking: machine_request_shutdown
Either handlers fail it out, and machine_abort_shutdown is posted
Or handlers do not block, so machine_will_shutdown is posted,
and then the subsystems are each gracefully exiting and the event loop is completed.
If a custom script is defined with machine:soft_shutdown_exit_command, then it will be executed asynchronously.


Neuron additional steps:
The Neuron can also use the request_soft_shutdown event, but it has a native hook to this already.
If in soft power mode, the watchdog WD: command will automatically detect when the soft power button is pressed,
it will then report the synthetic switch event fast_soft_power_switch_active
it will then report the synthetic switch event fast_soft_power_switch_inactive.

If the time between these occurrences is > fast:net:soft_power_hold_time then it will issue request_soft_shutdown, starting the standard loop.


For non-FAST Neuron systems, or FAST Neurons using standard power (not soft power), the controller will not be automatically shut down at the end.
