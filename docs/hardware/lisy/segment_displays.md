---
title: Configuring Segment Displays in LISY
---

# Configuring Segment Displays in LISY


Related Config File Sections:

* [segment_displays:](../../config/segment_displays.md)
* [segment_display_player:](../../config/segment_display_player.md)

MPF can control all segment displays on your machine with LISY.
Configure them like this:

``` yaml
segment_displays:
  info_display:
    number: 0
  player1_display:
    number: 1
  player2_display:
    number: 2
  player3_display:
    number: 3
  player4_display:
    number: 4
```

Note that the [Alpha-Numeric / Segment Displays](../../mc/displays/alpha_numeric.md) guide has more details on using alpha numeric and segment
displays.

Video about segment displays:

<div class="video-wrapper">
<iframe width="560" height="315" src="https://www.youtube.com/embed/Jyf3jxGXnTw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## What if it did not work?

Have a look at our
[LISY troubleshooting guide](../../troubleshooting/index.md).
