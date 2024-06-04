---
title: MPFLogger
---

# MPFLogger

The `MPFLogger` is a special GMC node that provides access to logging functionality for GMC nodes within a scene.

To get logging from GMC nodes (a.k.a. nodes with class names that start with `MPF`), add an `MPFLogger` node to your scene and attach the nodes you wish to enable logging for.

## Node Configuration

An `MPFLogger` node can be added anywhere in a scene. Only GMC nodes that are attached via the `loggers` list will output logs at the selected level.

### enabled:

Single value, type `bool`. Default `true`.

If true, this logger will log events for the attached GMC nodes. If false, logging will be suppressed (i.e. only default warning/error logs will be output).

### log_level:

Single value. Default `INFO`.

The logging level of the GMC nodes to output.

### loggers:

Array of values, type `Node`.

A collection of GMC nodes to enable logging for at the selected `log_level`.

Click on *Array[Node]* to expand the list and then click *+ Add Element* to add a node to the logger. GMC nodes (those that start with `MPF`) support logging through `MPFLogger`, other node types will be ignored.

!!! note "Name Your Nodes"

    Loggers will output their logs with the name of the node prepended. If you have not renamed the nodes in the Scene tree from their default names, it may be difficult to ascertain which node is logging which lines.