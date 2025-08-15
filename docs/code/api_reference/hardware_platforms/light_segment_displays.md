# light_segment_displays API Reference

Config Reference:

* [light_segment_displays:](../../../config/light_segment_displays.md)

`self.machine.hardware_platforms['light_segment_displays']`

``` python
class mpf.platforms.light_segment_displays.LightSegmentDisplaysPlatform(machine)
```

Bases: `mpf.core.platform.SegmentDisplayPlatform`

Platform which drives segment displays on lights of another platform.

## Accessing the light_segment_displays platform via code

Hardware platforms are stored in the `self.machine.hardware_platforms` dictionary, so the light_segment_displays platform is available via `self.machine.hardware_platforms['light_segment_displays']`.

## Methods & Attributes

The light_segment_displays platform has the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`configure_segment_display(number: str, platform_settings) → mpf.platforms.light_segment_displays.LightSegmentDisplay`

Configure light segment display.
