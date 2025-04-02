---
title: GMC Tilt Slides
---

# Tilt Slides in GMC

GMC provides a default slide for handling warnings and tilt, and the standard [tilt mode](../../game_logic/modes/tilt.md)
in the MPF configuration provides a set of automatic hooks to display the slide with different messages.

The previous guide, [Bonus Slides in GMC](bonus_mode.md), walks through creating your own slide
to override the default provided by MPF. Regarding the GMC slide files, Tilt slide customization works in just the same way.

## Configure Tilt Settings

If you don't have a tilt mode already, follow the general [tilt guide](../../game_logic/tilt/index.md).
The [configuration settings](../../config/tilt.md#optional-settings) have not been changed between MPF 0.57 and 0.80.

The default tilt mode includes three hooks for automatically displaying the slide `tilt.tscn`.
The slide expects a [token](../reference/slide_player.md#tokens) called `text`.
The first tilt warning sends the text "WARNING", the second sends "DANGER", and tilting out sends "TILT".

If you use a number larger than three for your [tilt:warnings_to_tilt setting](../../config/tilt.md#warnings_to_tilt),
these further warning events do not have default slides provided, nor slide_player hooks.

For example, if you change the setting to 4 and wanted to use the text "UH OH" for the third warning,
you could declare the `slide_player` extension in your overriding tilt mode file:

``` yaml
##! mode: modes/tilt/config/tilt.yaml
slide_player:
  tilt_warning_3: # event
    tilt: # slide
      expire: 1s
      tokens:
        text: UH OH
```

## Creating a custom Tilt Slide

There are two basic approaches to customizing the tilt slide.
If you only want the standard warning and tilt text (and any custom further warning texts per the previous section),
but want to add various display elements, you can provide a custom slide with an event variable for `text`.

The if you want further complexity or different behaviors around the slides, but still want to use the
default tilt mode, you can override the `slide_player` from the default tilt mode and use slides in
any way you want.

## Approach 1: Replace the default slide `tscn` file

To replace the default tilt slide, you need to create a new slide named `tilt.tscn` whereever you
create your GMC slides. The only event token provided by the default config is `text`, so
you can create a [MPFVariable](../reference/mpf-variable.md) with the `variable_type` of *"Event Arg"*
and `variable_name` of "text" to display this.

## Approach 2: Replace the default `slide_player`

If the first approach does not offer enough flexibility, you can build upon it by also extending the default tilt
mode's `slide_player`. First, make your custom slide or slides, we'll call them `tilt_warning.tscn` and `tilt_splash.tscn`.
Populate them with whatever display and dynamic elements you want -- you will need to provide any event variables yourself
later on.

In your custom tilt mode config (`/modes/tilt/config/tilt.yaml`) you need to overwrite the default slide_player.
This will replace ALL behaviors from the default tilt slide_player, so you will need to recreate any if there
are some you want to keep.

Every tilt infraction by a player will post a warning event, [tilt_warning_(number)](../../events/tilt_warning_number.md),
with appropriate number. The final infraction will instead post the event [tilt](../../events/tilt.md) and end the current ball.
You will want to create a `slide_player` hook for each warning and the final tilt event, using your custom slide names instead
of `tilt` as the slide name. Finally, you need to either include [expire](../reference/slide_player.md#expire) values or
custom hooks for when to hide the slides. MPF will automatically post the event [tilt_clear](../../events/tilt_clear.md)
when the machine has successfully cleared and collected all active balls to finish the ball end process, so this
is a good one to put your tilt slide removal on.

For instance, with our example custom slides `tilt_warning`, and `tilt_splash`, we might write:

``` yaml
##! mode: modes/tilt/config/tilt.yaml
slide_player:
  _overwrite: True # overwrite the default slide_player from tilt mode

  tilt_warning_1: # event name
    tilt_warning: # slide name
      expire: 1s
      tokens:
        warning_number: 1

  tilt_warning_2:
    tilt_warning:
      expire: 1s
      tokens:
        warning_number: 2

  tilt:
    tilt_splash:
      action: play

  tilt_clear:
    tilt_splash:
      action: remove

```
