---
title: Segment Display Transitions
---

# Segment Display Transitions


When MPF switches the current text on a segment display with another
text entry, a transition effect can be set that controls what text
transition between the new and existing text looks like. You can use
these transitions with the
[Segment Display player](../config_players/segment_display_player.md)
and within shows. You can set transitions as a property of the new text
entry that comes in, or as a property of the outgoing transition when
the current text entry is removed (incoming transitions always take
precedence over outgoing transitions).

Here's a list of all the types of segment display text transitions that
MPF supports.

## none

Setting a transition type of `none` means that no transition will be
used, and the incoming text instantly replaces the current text.

## push

The push transition means that the incoming text "pushes" the outgoing
text out of the way. (e.g. the outgoing text moves out while the
incoming text moves in)

Options for the push transition:

* direction: `left` or `right` (defaults to `right`).
* text: An optional text string that is inserted between the old and
    new text during the transition. Defaults to empty.
* text_colors: The color for each character in the optional transition
    `text` string (if the platform supports it). If a single color is
    supplied, all characters in the transition `text` string will be set
    to that color. See [Specifying Colors in Config Files](../config/instructions/colors.md) for more information on specifying colors in config
    files.

## cover

The cover transition means that the incoming text moves in on top of to
cover the current text. The outgoing text is not animated.

Options for the cover transition:

* direction: `left` or `right` (defaults to `right`).
* text: An optional text string that is inserted between the old and
    new text during the transition. Defaults to empty.
* text_colors: The color for each character in the optional transition
    `text` string (if the platform supports it). If a single color is
    supplied, all characters in the transition `text` string will be set
    to that color. See [Specifying Colors in Config Files](../config/instructions/colors.md) for more information on specifying colors in config
    files.

## uncover

The uncover transition means that the current text is moved out to
uncover the new incoming text.

Options for the uncover transition:

* direction: `left` or `right` (defaults to `right`).
* text: An optional text string that is inserted between the old and
    new text during the transition. Defaults to empty.
* text_colors: The color for each character in the optional transition
    `text` string (if the platform supports it). If a single color is
    supplied, all characters in the transition `text` string will be set
    to that color. See [Specifying Colors in Config Files](../config/instructions/colors.md) for more information on specifying colors in config
    files.

## wipe

The wipe transition means that the display text is wiped/switched from
the current text to the incoming text.

Options for the wipe transition:

* direction: `left` or `right` (defaults to `right`).
* text: An optional text string that is inserted between the old and
    new text during the transition. Defaults to empty.
* text_colors: The color for each character in the optional transition
    `text` string (if the platform supports it). If a single color is
    supplied, all characters in the transition `text` string will be set
    to that color. See [Specifying Colors in Config Files](../config/instructions/colors.md) for more information on specifying colors in config
    files.

## split

The split transition means that the text is split and either moved in or
out to reveal the other text value.

Options for the split transition:

* mode: `push` or `wipe` (defaults to `push`).
* direction: `in` or `out` (defaults to `out`).

## Configuring Transitions

Transitions are specified as an additional property of a
`segment_display_player:` config or the `segment_displays:` section of a
show config. For example:

``` mpf-config
#! segment_displays:
#!   display1:
#!     number: 1
segment_display_player:
  jackpot_completed:
    display1:
      text: JACKPOT
      priority: 1000
      expire: 2s
      transition:
        type: push
        direction: right
        text: " *** "
      transition_out:
        type: push
        direction: right
        text: " *** "
```

When the event "jackpot_completed" occurs, MPF will update the text in
the segment display called "display1" using the push transition. After
2 seconds, the "JACKPOT" text will expire and be removed, pushing the
text out to the right, restoring the previous text.

!!! note

    If the current text has a `transition_out:` setting, and the new text
    has a `transition:` setting, then the new text's transition setting
    will take precedence.
