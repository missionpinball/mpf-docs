---
title: MPFSlide
---

# MPFSlide

`MPFSlide` is a Godot Node class provided by the MPF-GMC extension. All scenes that will be used as slides must derive from the `MPFSlide` class.

## Node Configuration

There are currently no options for configuring `MPFSlide` instances. Create any scene with any content and Godot features you like!

## Parameters

Slide instances created by `slide_player` have initial values that can be overridden with parameters in the slide player configuration.

### context:

Single value, type: `String`. Default: the calling mode's name

When a mode is stopped in MPF, a _clear_ event is broadcast to signal the end of the mode and to remove all slides, widgets, sounds, lights, and shows started by that mode. The value to track this is called "context", and by default each slide has a context of the name of the mode that created it.

If you do not wish for your slide to be removed when the calling mode ends, you can specify a different context value.

### key:

Single value, type: `String`. Default: the slide's file name

Once a slide is instantiated, it can be referenced by its `key` for actions like `update` and `remove`. By default, the slide's file name is used as its key.

In situations you may want multiple instances of a slide, you can specify a key manually. This key will then be used to reference the slide for any future actions.

### priority:

Single value, type: 'integer'. Default: `0`

This value will be added to the calling mode's priority to determine the overall stack priority of the slide. When a slide is added or removed from the stack, the stack is sorted with the highest priority slide on top.

## Methods

`MPFSlide` does not have any public methods exposed, but custom methods can be added to scene scripts that extend `MPFSlide`. These methods can be triggered from MPF `slide_player` with the `action: method` option. See the [slide_player: reference](slide_player.md) for more details.