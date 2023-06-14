---
title: How to configure alpha-numeric displays (P-ROC)
---

# How to configure alpha-numeric displays (P-ROC)


Related Config File Sections:

* [segment_displays:](../../config/segment_displays.md)
* [p_roc:](../../config/p_roc.md)

The P-ROC includes support four alpha-numeric displays (0-3). You can
configure them in MPF:

``` mpf-config
segment_displays:
  display1:
    number: 0
  display2:
    number: 1
  display3:
    number: 2
  display4:
    number: 3
```

Note that the [Alpha-Numeric / Segment Displays](../../mc/displays/alpha_numeric.md) guide has more details on using alpha numeric and segment
displays.

Video about segment displays:

<div class="video-wrapper">
<iframe width="560" height="315" src="https://www.youtube.com/embed/Jyf3jxGXnTw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## What if it did not work?

Have a look at our
[troubleshooting guide for the P/P3-Roc](../../troubleshooting/index.md).
