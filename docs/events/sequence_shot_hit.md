---
title: (sequence_shot_name)_hit
---

# (sequence_shot_name)\_hit


--8<-- "event.md"

The sequence_shot called (sequence_shot_name) was just completed.

## Keyword arguments

(See the [Conditional Events](overview/conditional.md)
guide for details for how to create entries in your config file that
only respond to certain combinations of the arguments below.)

#### `elapsed`:
*added in MPF 0.56.1*

How much time has elapsed since the sequence shot started. (e.g. how long did this sequence shot take to complete?)

You can use the elapsed parameter to troubleshoot sequence_shot timeouts or for estimating ball speed. The elapsed time posted in the sequence shot hit event can be easily used to trigger other things like a speed calculation.

Event is posted by [sequence_shots:](../config/sequence_shots.md)
