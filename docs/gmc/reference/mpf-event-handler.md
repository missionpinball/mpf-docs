---
title: MPFEventHandler
summary: A GMC Node for handling MPF events directly in Godot
---

# MPFEventHandler

`MPFEventHandler` is a Godot Node class provided by GMC that creates BCP event subscriptions to trigger behavior based on arbitrary MPF events.

## Node Configuration

An `MPFEventHandler` can be placed anywhere in your scene, but must be either the direct parent or direct child of the nodes that will handle the event callback.

### event_name:

Single value, type `String`

The name of the MPF event that this handler will subscribe to. If no BCP trigger is established for this event, one will be created on instantiation and removed when the node is destroyed.

### handler_direction:

Single value, one of `Parent` or `Children`. Default `Parent`

Controls whether the `MPFEventHandler` triggers behavior on its parent node or on its children nodes.

If set to `Parent`, the `call_method` callable will be invoked on the direct parent of the `MPFEventHandler` node. If the parent does not have a callable by the specified name, a warning will be logged.

If set to `Children`, the `call_method` callable will be invoked on every direct child of the `MPFEventHandler` node. If a child does not have a callable by the specified name, it will be logged.

### call_method:

Single value, type `String`

The name of a Callable (function) on the parent or child nodes that will be called when the event triggers. The event arguments will be passed to the callable as a dictionary.