---
title: machine_reset_phase_3
---

# machine_reset_phase_3


--8<-- "event.md"

The third phase of resetting the machine.

These events are posted when MPF boots (after the init_phase events are
posted), and they're also posted subsequently when the machine is reset
(after exiting the service mode, for example).

This is a queue event. The machine reset phase 3 will not be complete
until the queue is cleared.

*This event does not have any keyword arguments*
