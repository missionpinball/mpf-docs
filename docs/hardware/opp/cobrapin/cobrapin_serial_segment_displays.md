---
title: CobraPin Serial Segment Displays
---

# NeoSeg (CobraPin) Serial Segment Displays


Video about CobraPin serial segment displays. The video shows a prototype
7-digit 16-segment version versus the production 8-digit 14-segment
version. Hence use the video only for general information. For configuration information follow the information below.

<div class="video-wrapper">
<iframe width="560" height="315" src="https://www.youtube.com/embed/iMeX1qC4EA0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Add Segment Display Platform

NeoSeg displays consist of a string of serial LED controllers connected
to segment display LEDs. Each LED channel is connected to a segment. You
must add light_segment_displays as the segment_displays platform so MPF
knows to send segment display commands to the light controller:

``` mpf-config
hardware:
  segment_displays: light_segment_displays
```

## Create the NeoSeg Light Groups

For each neo segment you would like to use you have to use light group, in other words there is a 1:1 mapping between a light group and the piece of hardware you hold in your hands.

The creation of the mpf lights for a NeoSeg display is handled by
creating a light_group using `neoseg_displays`. This is much easier
than defining each light for each of the 120 segments in an 8-digit
display.

``` mpf-config
neoseg_displays:
  neoSeg_0:
    start_channel: 0-0-0
    size: 8digit
    light_template:
      type: w
      subtype: led
      color_correction_profile: NeoSeg_orange
```

Here we have created a neoseg_display light_group named "neoSeg_0."
The group starts at light channel 0-0-0, which is the first light
channel on Board 0 on CobraPin, for example. It is an 8-digit display.

Note that we are dealing with light *channel* numbers, not light
numbers. If you have all RGB LEDs, the channel number is 3 times your
light number. An 8-digit NeoSeg display occupies 120 channels while the
2-digit display occupies 30 channels. So if we added another NeoSeg
display after neoSeg_0, its start_channel would be 0-0-0 plus 120...so
0-0-120.

We had to add a light template so that we could identify it as a single
channel LED.

Also, the use of a color_correction_profile enables you to change the
brightness of a NeoSeg display. This is especially handy when using
NeoSeg displays of different colors since each color has a different
default brightness. Use the whitepoint setting to vary the brightness:

``` mpf-config
light_settings:
  color_correction_profiles:
    NeoSeg_orange:
      whitepoint: [.9, .9, .9]
```

## Create Segment Displays

Once you have the light groups defined, you can arrange them into
displays. The light group is a `neoseg_displays` object and the logical display a `segment_displays` object. You can combine multiple light groups into one logical display.  In other cases you might have a 1:1 mapping between light groups and segment displays. In the latter case it might seem to overcomplicate things but this concept gives you the flexibility you might need. These are the displays that can be targeted by a segment_display_player.

``` mpf-config
segment_displays:
  neoSegTop:
    number: 1
    size: 16
    integrated_dots: true
    use_dots_for_commas: true
    default_transition_update_hz: 30
    platform_settings:
      light_groups:
        - neoSeg_0
        - neoSeg_1
      type: 14segment
```

Here we create a 16-digit display called "neoSegTop" built from 2
8-digit displays -- "neoSeg_0" and "neoSeg_1". The
"integrated_dots" and "use_dots_for_commas" settings are required to
use the comma segments built into NeoSeg displays. NeoSeg displays have
a type of "14segment."

Be sure to change "size" to the total number of digits that you intend
to use in the display. In some cases, the opening in your backglass may
only be wide enough for 7 digits for example. In that case, change the
size to 7 and the 8th digit will remain unused.

## Complete Example Config for Hardware Definition

Below you find a complete example config file how to define your hardware. With this you can use a `segment_display_player` to diplay a certain text upon a given event.

``` mpf-config
#config_version=5

hardware:
  platform: opp
  driverboards: gen2
  segment_displays: light_segment_displays

#create light group for each NeoSeg display
neoseg_displays:
  neoSeg_0:
    start_channel: 0-0-0
    size: 8digit
    light_template:
      type: w
      subtype: led
      color_correction_profile: NeoSeg_orange
  neoSeg_1:
    start_channel: 0-0-120
    size: 8digit
    light_template:
      type: w
      subtype: led
      color_correction_profile: NeoSeg_white

  neoSeg_7:
    start_channel: 0-0-660
    size: 2digit
    light_template:
      type: w
      subtype: led
      color_correction_profile: NeoSeg_blue
  neoSeg_8:
    start_channel: 0-0-690
    size: 2digit
    light_template:
      type: w
      subtype: led
      color_correction_profile: NeoSeg_red

#use light groups to arrange into a segment display
segment_displays:
  neoSegTop:
    number: 1
    size: 16
    integrated_dots: true
    use_dots_for_commas: true
    default_transition_update_hz: 30
    platform_settings:
      light_groups:
        - neoSeg_0
        - neoSeg_1
      type: 14segment

  neoSegBot:
    number: 1
    size: 4
    integrated_dots: true
    use_dots_for_commas: true
    default_transition_update_hz: 30
    platform_settings:
      light_groups:
        - neoSeg_8
        - neoSeg_7
      type: 14segment

#use color_correction_profile whitepoint to adjust the brightness of each
#NeoSeg display
light_settings:
  color_correction_profiles:
    NeoSeg_red:
      whitepoint: [.8, .8, .8]
    NeoSeg_white:
      whitepoint: [.55, .55, .55]
    NeoSeg_blue:
      whitepoint: [.5, .5, .5]
    NeoSeg_orange:
      whitepoint: [.9, .9, .9]
    NeoSeg_yellow:
      whitepoint: [1, 1, 1]
    NeoSeg_green:
      whitepoint: [.5, .5, .5]
```
## Complete Example Config for Show Definition

Below you find a complete example config file to display scored points. It is not using all possible hardware options like the example above, but it includes the display of a show on the LED segments. To keep this example simple the `neoseg_displays` object is mapped 1:1 to a `segment_displays` object.

``` mpf-config
#config_version=5

hardware:
  platform: opp
  driverboards: gen2
  segment_displays: light_segment_displays

#create light group for each NeoSeg display
neoseg_displays:
  neoSeg_0:
    start_channel: 0-0-0
    size: 8digit
    light_template:
      type: w
      subtype: led
      
segment_displays:
  neoSegTop:
    number: 1
    size: 16
    integrated_dots: true
    use_dots_for_commas: true
    default_transition_update_hz: 30
    platform_settings:
      light_groups:
        - neoSeg_0
      type: 14segment
      
show_player:
  player_score{player_num==1}: #of course for more than 1 player you need to have multiple entries
    p1_score:
      show_tokens:
        txt: "{(players[0].score):d}"
        
shows:
  p1_score:
  - duration: -1
    segment_displays:
      neoSegTop:
        text: (txt)

```
To learn more about show tokens and how to use dynamic values take a look [here](../../../shows/tokens.md).
