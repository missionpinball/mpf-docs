---
title: "slide_player:"
---

# slide_player:

!!! caution "MPF 0.80 & GMC"

    This config reference is for the upcoming MPF 0.80 release and the GMC media controller. For generating slides in MPF 0.57, see the [current slide_player reference](../../config/slide_player.md).

--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|
|[shows](../shows/index.md) & show files|**YES** :white_check_mark:|

The `slide_player:` section of your config is where you configure slides
to be shown (or removed) based on events being posted.

This is an example:

``` mpf-mc-config
#! slides:
#!   slide1: []
#!   slide2: []
#!   slide3: []
slide_player:
  event1: slide1
  event2: slide2
  event3: slide3
```

See [Slide player](../config_players/slide_player.md) for
details.

## Optional settings

The following sections are optional in the `slide_player:` section of
your config. (If you don't include them, the default will be used).

### action:

Single value, type: one of the following options: play, remove. Default:
`play`

#### `play`

Makes the slide active. Note that the actual slide shown on a
display will be whichever active slide has the highest priority, so
depending on what other slides are active, this action might not
technically show the slide.

#### `method`

Calls a custom method on the slide scene using the `method:` parameter. This is used to trigger custom slide behavior in GMC. To pass additional parameters to the method, use `tokens:`.

On the receiving slide, the method will be called with two parameters: `settings`, the config here in slide player (including `tokens`), and `kwargs`, the arguments from the event that triggered this slide player.

#### `queue`

Queues the slide for playback at the end of the slide queue. Queued slides will be played sequentially, and the default is to queue the slide last.

#### `queue_first`

Queues the slide for playback at the beginning of the slide queue. This slide will be played before any already-queued slides, but after a currently-playing queued slide is finished.

#### `queue_immediate`

Queues the slide for playback immediately. If an existing queued slide is playing, it will be removed immediately and this slide will play. The rest of the queued slides will follow after this slide is finished.

#### `remove`

:   Removes the slide from the list of active slides. If this slide is
    the highest priority slide that's currently showing, then the
    next-highest priority slide will be shown in its place.

    If a `transition_out:` setting is used, then that transition will be
    used here.

For example, to remove *slide1* when the event *remove_slide_1* is
posted:

``` mpf-mc-config
#! slides:
#!   slide1: []
slide_player:
  remove_slide_1:           # event name
    slide1:                 # slide name
      action: remove
```

You can also specify a transition for the removal, like this:

``` mpf-mc-config
#! slides:
#!   slide1: []
slide_player:
  remove_slide_1:           # event name
    slide1:                 # slide name
      action: remove
      transition: fade
```

### expire:

Single value, type: `time string (secs)`
([Instructions for entering time strings](instructions/time_strings.md)). Defaults to empty.

Specifies that this slide should automatically be removed after the time
has passed. When it's removed, whichever slide is the next-highest
priority will be shown.

The expiration timer starts when the slide becomes active in the stack, so if the slide you're displaying here doesn't end up being shown because it's not the
highest-priority slide, the timer is still running in the background,
and the slide will still be removed when the timer expires.

When queueing a slide with the `action: queue` config, it's important to include an expiration time or else the queue will never advance.


``` mpf-mc-config
slides:
  base:
    widgets:
      - type: text
        text: BASE SLIDE
        color: ff0000
        font_size: 100
  expire_slide:
    widgets:
      - type: text
        text: EXPIRE 5s
        color: purple
        y: 66%
    expire: 5s
    transition_out:
      type: wipe
      duration: 5s
slide_player:
  mc_reset_complete.1: expire_slide
  mc_reset_complete.2: base
```

### max_queue_time:

Single value, type `item`. Defaults to empty.

If this slide is queued with `action: queue`, the `max_queue_time` is the longest duration the slide will be allowed in the queue. If the slide is not played from the queue before this time expires, it will be discarded.

### method:

Single value, type `string`. Defaults to empty.

The name of the slide method to call when `action: method` is used. Additional parameters can be provided in the `tokens:` config.

### priority:

Single value, type: int_or_token. Defaults to empty.

An adjustment to the priority of the slide that will be shown.

In MPF, all slides have a priority. Only one slide is show on a display
at a time, and the slide with the highest priority is automatically
shown. If that slide is removed, the next-highest priority slide is
shown.

If you have a `slide_player:` section in a mode-based config file, then
slides shown will automatically have the priority of the mode.
(`slide_player:` sections from your machine-wide config file use
priority `0`.) However you can adjust the priority of a slide (up or
down) by adding a `priority:` setting with a positive or negative value.

If a slide is being shown as part of a show, the slide will have the
priority set to whatever the priority of the show is (which itself is
also the priority of the mode unless you adjust it)

### target:

Single value, type: `string`. Defaults to empty.

Specifies the display target this slide will be shown on. If you do not
specify a target, then the slide will be shown on the default display.

In MPF, display targets are the names of the displays themselves.
However there is also a *slide_frame* widget (literally a widget which
you add to a slide which holds other slides, kind of line
picture-in-picture). When you add a slide_frame to a slide, you give it
a name, and that name is added to the list of valid targets.

So really the `target:` here is either the name of a display, or the
name of a slide_frame where you want this slide to be displayed.

!!! note

    This will be renamed to `display:` in the future, because that's more clear than `target`.

### tokens:

One or more sub-entries. Each in the format of `string` : `string`

Tokens can be passed to the slide with additional information that might affect the slide's content or behavior. Token values are parsed by the GMC slide when calculating variable values, and can be passed to custom methods on the slide.

