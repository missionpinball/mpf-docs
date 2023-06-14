---
title: [diverter](../index.md)(name)_enabling
---

# [diverter](../index.md)(name)_enabling


--8<-- "event.md"

The diverter called (name) is enabling itself. Note that if this
diverter has `activation_switches:` configured, it will not physically
activate until one of those switches is hit. Otherwise this diverter
will activate immediately.

## Keyword arguments

(See the [Conditional Events](overview/conditional.md)
guide for details for how to create entries in your config file that
only respond to certain combinations of the arguments below.)

`auto`

:   Boolean which indicates whether this diverter enabled itself
    automatically for the purpose of routing balls to their proper
    location(s).

Event is posted by [diverters:](../config/diverters.md)
