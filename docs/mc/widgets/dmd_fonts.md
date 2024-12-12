---
title: How to use DMD fonts
---

# How to use DMD fonts


MPF includes three built-in fonts which are pre-configured as widget
styles which look good on DMDs. These fonts are included in the MPF-MC
package. They can be used with any widget that uses fonts, including the
Text and Text Input widgets.

If you don't use one of these fonts on your DMD and just show some
text, here's what the results look like:

``` mpf-mc-config
slides:
  my_slide:
    - type: text
      text: MISSION
#! slide_player:
#!   show_slide_event: my_slide
##! test
#! post show_slide_event
#! advance_time_and_run .1
#! assert_slide_on_top my_slide
#! assert_text_on_top_slide MISSION
```

![image](../images/dmd_default.png)

Sure, it works, but it doesn't look good because the default font is a
regular font that's made for a high-res display.

Instead you can use these three styles. (Of course you can use your own
fonts too, but sometimes it's hard to find ones that look good on a
low-res DMD.)

## style: big

[big](#) is 10 pixels tall.

``` mpf-mc-config
slides:
  my_slide:
    - type: text
      style: big
      text: MISSION
#! slide_player:
#!   show_slide_event: my_slide
##! test
#! post show_slide_event
#! advance_time_and_run .1
#! assert_slide_on_top my_slide
#! assert_text_on_top_slide MISSION
```

![image](../images/dmd_big.png)

## style: med

[medium](#) is 7 pixels tall.

``` mpf-mc-config
slides:
  my_slide:
    - type: text
      style: medium
      text: MISSION
#! slide_player:
#!   show_slide_event: my_slide
##! test
#! post show_slide_event
#! advance_time_and_run .1
#! assert_slide_on_top my_slide
#! assert_text_on_top_slide MISSION
```

![image](../images/dmd_med.png)

## style: small

[small](#) is 5 pixels tall.

Notice that this font has a color set and we're using it with a Color
DMD. All three of these fonts (like any font) can be used on a mono or
color DMD.

``` mpf-mc-config
slides:
  my_slide:
    - type: text
      style: small
      text: MISSION
      color: 00ffcc
#! slide_player:
#!   show_slide_event: my_slide
##! test
#! post show_slide_event
#! advance_time_and_run .1
#! assert_slide_on_top my_slide
#! assert_text_on_top_slide MISSION
```

![image](../images/dmd_small.png)
