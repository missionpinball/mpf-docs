---
title: Customizing MPF Monitor
---

# Customizing MPF Monitor

MPF Monitor is configured with reasonable defaults for most MPF game projects.
As your project grows, you may want to customize various aspects of Monitor,
or use it in a variety of ways.

## Command line options

The most basic customizations are using alternative playfield images, yaml data sources,
and other command line changes.

### Change logfile

A custom logfile destination can be passed using `-l logfile.dest`
If not passed, the default will be `logs/TIMESTAMP-monitor-hostname.log`

### Change playfield image

Monitor supports several image formats. By default `<game folder>/monitor/playfield.jpg` is used, but
passing `-i imagename.etc` will find a file with that name in the `monitor/` folder, and use it instead.
PNG, JPG, BMP, GIF are supported, though GIF will only show the first frame, no animation.

### Connect to alternative/remote MPF server

Monitor will attempt to connect to MPF at localhost:5051 by default. To change this,
pass `-ip <address>` for alternative ip selection, and `-port <port>`to change the port.

## Display options

Monitor saves its own display layout configuration in `monitor/settings.ini`.
You should not need to alter this file directly, unless a window is lost far offscreen.
The best practice for multi-developer MPF projects is to not add this file to version control,
so that each computer can manage Monitor window placement separately.

## YAML Options

For the most part you should not need to edit the `monitor.yaml` directly, but there are a couple
hidden options that you can change if you do. Note: NEVER edit this file while MPF Monitor is running,
as you may lose your work when Monitor makes any changes.

### device_alpha

Usage:
`device_alpha: 200`

Device alpha is an option used to manage transparency of your devices on the playfield image.
The default is 220 -- use a lower number to increase transparency of every device. Valid range is 0-255.

### device_outline

Usage:
`device_outline: 4`

Device outline is an option used to set the pixel thickness of device borders on the playfield image.
The default is 3 -- you may want to tweak this value in case of very high resolution display or when
many devices are crowding each other in your playfield window.

### device_size

Usage:
`device_size: 0.02`

Device size is used to set the default size of devices when added the the playfield, or any device that does
not otherwise have a size specified.

## Custom Device Shapes

If you have a special use case, it may be worth defining a custom shape for your device.

Select the "custom" option in the shape dropdown, and exit Monitor. With Monitor closed, find that device in
`monitor.yaml` and set `custom_shape_points:` as an array of `[x, y]` vertex arrays. For example, a complete device
with a custom shape might look like:

```yaml
light:
  l_ball_release_warning:
    custom_shape_points:
    - - -0.47 # x1
      - 0.47  # y1
    - - 0.5   # x2
      - -0.5  # y2
    - - 0.5   # x3
      - 0     # y3
    shape: CUSTOM
    size: 0.08
    x: 0.76
    y: 0.71
```

It is recommended to keep all coordinates within the unit diameter circle at (0,0) to fit within Monitor's device painting and click handling expectations.
In other words limit points to the range of `[-.5,-.5]` to `[.5,.5]` or even less at the extremes. To make a large path, use `size:` instead.
