---
title: carousel_items_empty
---

# carousel_items_empty


--8<-- "event.md"

A carousel determined that it has
no selectable_items that are valid for display. This can be because
the `mode_settings` for the carousel mode still needs to be set,
or because all of the `selectable_items` were dynamically evaluated
and removed from the valid option set. Use the `carousel` keyword
argument to filter on the correct carousel if have any config player
behaviors that need to happen in response.

## Keyword arguments

(See the [Conditional Events](overview/conditional.md)
guide for details for how to create entries in your config file that
only respond to certain combinations of the arguments below.)

#### `carousel`:

The name of the carousel that had an item selected.
