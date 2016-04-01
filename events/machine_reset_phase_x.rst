machine_reset_phase_(number) (MPF event)
========================================

This is a series of events posted as the machine is resetting.

* machine_reset_phase_1
* machine_reset_phase_2
* machine_reset_phase_3

These events are posted when MPF boots (after the init_phase events are posted),
and they're also posted subsequently when the machine is reset (after existing
the service mode, for example).

Keyword arguments: None
