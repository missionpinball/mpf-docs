---
title: MPFDisplay
---

# MPFDisplay

`MPFDisplay` is a Godot Node class provided by the MPF-GMC extension. Each unique display (monitor screen) should have its own display, though it is also possible to subdivide a single monitor into multiple displays.

## Node Configuration

All `MPFDisplay` instances must be first-level child nodes of the main `MPFWindow` root. The name of the `MPFDisplay` node is the name that can be used in MPF configs as the `target:` value when targeting a slide or widget to a specific display.

## Parameters

The Godot Editor *Inspector* panel provides the following parameters for the `MPFDisplay` node:

### is_default:

Single value, type: `bool`. Default: `false`

When the MPF `slide_player` is called to play a slide without an explicit `target:`, the default display will be targeted.

The `is_default` checkbox sets its `MPFDisplay` node to be the default display for the window. Only one display can be set to default, otherwise an error will be thrown. If no display is set to default, the first child `MPFDisplay` node of the `MPFWindow` node will be the default.

### initial_slide:

Single value, type: `Scene`. Default: *addons/mpf-gmc/slides/startup.tscn*

When GMC first boots, each `MPFDisplay` will render an initial slide while awaiting the connection to MPF. This slide can be customized with logos, images, and informational text.

Each `MPFDisplay` can have its own initial slide, or they can use the same. GMC includes a simple default slide to start with, but you can link any slide from your project to be the initial slide for the display.

## Methods

`MPFDisplay` does not have any public methods exposed.