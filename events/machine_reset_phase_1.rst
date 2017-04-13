machine_reset_phase_1
=====================

*MPF Event*

The first phase of resetting the machine.

These events are posted when MPF boots (after the init_phase events are
posted), and they're also posted subsequently when the machine is reset
(after existing the service mode, for example).

This is a queue event. The machine reset phase 1 will not be complete
until the queue is cleared.

*This event does not have any keyword arguments*
