---
title: carousel_item_highlighted
---

# carousel_item_highlighted


--8<-- "event.md"

An item was highlighted in a carousel. This event is posted
when the carousel initially displays and highlights its initial item
and also when moving the carousel to the next or previous item.

## Keyword arguments

(See the [Conditional Events](overview/conditional.md)
guide for details for how to create entries in your config file that
only respond to certain combinations of the arguments below.)

#### `carousel`:

The name of the carousel that had an item selected.

#### `direction`:

The direction that the highlight change was performed in. Can be any of:

"forwards", "backwards", or `None`. Note that `None` is the Python keyword, not the string "None".

#### `item`:

The string name of the newly-highlighted item.
