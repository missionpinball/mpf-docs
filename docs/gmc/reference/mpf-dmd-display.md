---
title: MPFDMDDisplay
---

# MPFDMDDisplay

`MPFDMDDisplay` is a Godot Node class that extends the base `MPFDisplay` class and is special for hardware DMDs. The class includes special logic for rendering the display, transposing the pixel data, and sending the data back to MPF for delivery to the hardware DMD.

The DMD rendering flow does not use frames-per-second, but instead leverages the Godot engine's rendering system (`RenderingService.has_changed()`) to trigger display updates. This minimizes serial traffic by only sending new frame data when the frame changes.


## Node Configuration

Just like `MPFDisplay`, all `MPFDMDDisplay` instances must be first-level child nodes of the main `MPFWindow` root. The name of the `MPFDMDDisplay` node is the name of the DMD defined in the MPF config, and can be used in MPF configs as the `target:` value when targeting a slide or widget to a specific display.

When creating your Window scene, instead of adding an `MPFDisplay` node add a `MPFDMDDisplay` node instead. Or if you already have an `MPFDisplay` node, right-click the node and *Change Type...* to select MPFDMDDisplay.

## Parameters

![image](images/properties-mpf-display.png)

The Godot Editor *Inspector* panel provides the following parameters for the `MPFDMDDisplay` node (in addition to all `MPFDisplay` node parameters):


### pixel_order:

Single value. Default: `RGB`

The order of pixel data (Red, Green, Blue) sent to MPF. If your hardware DMD uses pixels that are RBG or GRB, you will need to set the appropriate value here to get the correct colors.

### resolution:

Single value, type: `Vector2i`.

This is the physical resolution of the hardware DMD. Regardless of the size of the display node, the rendered image will be scaled to this specified resolution for the pixel data sent to MPF.

If enabled, this display will render an empty screen if all slides are removed. If disabled (default), this display will persist the current slide even after its removal has been requested, until a new slide is triggered.

This is useful for situations where the game is shifting from one mode to another, and the running mode stops before the new mode starts. The ending mode's *clear* event will trigger the slide to be removed some fraction of a second before the starting mode's *mode_(name)_started* event triggers the new slide to be shown.

That scenario would result in a brief flash of a blank display, which is not desirable for most users. By disabling `allow_empty`, the outgoing slide will remain in the display until the next one replaces it.


### use_gpu:

Single value. Default: `NEVER`

**Not Yet Implemented**

## Methods

`MPFDMDDisplay` does not have any public methods exposed.
