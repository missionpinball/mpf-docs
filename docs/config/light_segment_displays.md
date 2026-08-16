---
title: "light_segment_displays: Config Reference"
---

# light_segment_displays: Config Reference

--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|

The `platform_settings:` of your `segment_displays` section is where you
map segment displays to lights when using the
[light segment displays platform](../hardware/light_segment_displays.md).

## Optional settings

The following sections are optional in the `light_segment_displays:`
section of your config. (If you don't include them, the default will be
used).

### display_flash_duty:

Single value, type: `number` (will be converted to floating point).
Default: `0.5`

For 7segment your segments are: a, b, c, d, e, f, g and dp (see:
[7-Segment Displays in
Wikipedia](https://en.wikipedia.org/wiki/Seven-segment_display_character_representations)
for details) For BCD your segments are: x0, x1, x2, x3 and dp (see:
[Binary Coded Decimal in
Wikipedia](https://en.wikipedia.org/wiki/Binary-coded_decimal) for
details) For 14segment your segments are: l, m, n, k, j, h, g2, g1, f,
e, d, c, b, a and dp (see: [14 Segment Displays in
Wikipedia](https://en.wikipedia.org/wiki/Fourteen-segment_display) for
details) For 16segment your segments are: u, t, s, r, p, n, m, k, h, g,
f, e, d, c, b, a and dp (see: [16 Segment Displays in
Wikipedia](https://en.wikipedia.org/wiki/Sixteen-segment_display) for
details)

dp is an optional decimal point per display.

### display_flash_frequency:

Single value, type: `number` (will be converted to floating point).
Default: `1.0`

How fast should the displays flash? Defaults to once per second or 1Hz.

## Related How To guides

* [How to Connect Segment Displays as Lights to MPF](../hardware/light_segment_displays.md)
* [Alpha-Numeric / Segment Displays](../mc/displays/alpha_numeric.md)
* [Segment Display Platforms in MPF](../hardware/segment_display_platforms.md)
