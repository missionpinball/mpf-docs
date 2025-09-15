---
title: Spanning Multiple Monitors
glightbox: true
---

# Spanning Multiple Monitors

GMC supports running multiple `MPFDisplay` parents across multiple monitors, with a little extra setup in Godot. This guide will help you setup your project to span across multiple screens so you can direct slides to a specific screen.

!!! caution "Work in Progress"

    Every operating system is different and we don't have the resources to test every scenerio on every system. If you are working with multiple screens, your help and feedback will be greatly appreciated to aid us in ironing out kinks and ensuring that this guide works for all cases!

!!! note "Click to expand guide images"

    The images in this guide can be expanded to full size by clicking on them.

## Set your Project Settings

Open the Project Settings menu and go to *Display > Window*, and in the upper right corner toggle on *Advanced Settings* to see additional configuration options.

  * **Viewport Width / Height**: Set these to be the maximum bounding box to contain all of your displays.
  * **Initial Position Type**: Absolute
  * **Resizable**: Off
  * **Borderless**: On
  * **Window Width / Height Override**: The same as the viewport width and height
  * **Embed Subwindows**: Off

In the example images, we will configure the project for two 1600x900 displays, so 3200x900 overall.

![image](../images/additional_display_project_display_settings.png){ width="300" }

## Create a custom Window scene

GMC uses a scene with an `MPFWindow` root node as the entry point for all displays and slides. There is a default *window.tscn* included in GMC that works for single-screen projects, but for a multi-screen project you'll need to create your own.

In your project root */slides* folder create a new scene with `MPFWindow` as the root node and save the scene (probably as *window.tscn* but you may choose something else).

The `MPFWindow` node will automatically size itself to the Viewport Width / Height defined in your Project Settings.

!!! note "Duplicating the built-in window"

    Instead of hand-creating the initial `MPFWindow` and main `MPFDisplay` node,
    you can find the built-in `window.tscn` file at `res://addons/mpf-gmc/slides/window.tscn`
    and right-click it to "Duplicate" the file, giving the duplicate a new name.

    Make sure you move the new file into your own project's "slides" folder,
    it should *NOT* be kept within the `addons/mpf-gmc/` area of your project,
    as that is the location for the GMC default assets.

Right-click on your new scene in the *FileSystem* window and select **Set as Main Scene**. This can be confirmed in the project settings.

In the example images, we use the name "window_override", stored in our `<gmc project root>/slides/overrides/`.

![image](../images/additional_display_project_main_scene.png){ width="300" }

## Create Main Display

The first display will be run on the main screen, and doesn't require extra setup. In your scene tree add a new node of type `MPFDisplay` and give it a name (this name will be how it's targeted in MPF `slide_player` ex: 'primary').

In the *Inspector* panel set `is_default` to true and select an initial slide. For most use cases, the default GMC initial slide will work (*/addons/mpf-gmc/slides/startup.tscn*). Expand the *Layout > Transform* section and set the size to be the dimensions of the main monitor.

In the example image, we are setting up the first of two displays, "a_display" and "b_display".

![image](../images/additional_display_mpfwindow_and_mpfdisplay.png){ width="300" }

## Create a Window Container

The second display will run on a separate monitor, so Godot must be configured to generate a new application window on that monitor.

Under your main Window root node, create a new node of type `Window` (just the default Godot `Window`, not the custom GMC `MPFWindow`).

In the *Inspector* panel, set the following:

  *  **Initial Position**: Absolute
  *  **Position**: The coordinates from the top-left of the main monitor
  *  **Size**: The dimensions of the screen

Under the *Flags* dropdown, set the following:

  * **Transient**: On
  * **Unresizable**: On
  * **Borderless**: On

![image](../images/additional_display_window_node.png){ width="300" }

Now create a new `MPFDisplay` child node of this `Window`. Set the same Initial Slide as the other, and under *Layout > Transform > Size* set the dimensions of the second monitor. Give this node a name that you will reference in MPF to target it (ex: 'mini-display').

![image](../images/additional_display_mpfdisplay_node.png){ width="300" }

In the Editor scene view, you should now see two copies of the MPF logo, one for each display.

You may need to change the layout positions of either of the display nodes a few times to get everything placed properly,
and if you are programming and testing on one computer, you may need to make layout and sizing changes when you switch to the
computer and display hardware actually mounted in your machine.

## Configure Slides in MPF

In your MPF config files, you can now target a specific display using the name of the `MPFDisplay` nodes. Whichever node is tagged as default does not need a target, but you can provide one for clarity. If your main display node is named "primary" and your other node is named "mini-display" then you could setup your attract mode like this:

``` yaml
slide_player:
    mode_attract_started:
        attract_main_slide:
            target: primary
        attract_mini_slide:
            target: mini-display
```
