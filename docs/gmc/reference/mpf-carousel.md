---
title: MPFCarousel
---

# MPFCarousel

The `MPFCarousel` node works in tandem with the MPF Carousel mode to support dynamic content switching based on rotation events (a timer, flipper presses, or anything else).

!!! note "Requires MPF 0.80"

    The MPF 0.80 events that drive the `MPFCarousel` are changed from those in MPF 0.57. If you have an existing MPF 0.5 carousel you may need to update your event handlers.

## Node Configuration

Add an `MPFCarousel` node to your slide and create child nodes for each carousel item you wish to render. You can use the eyeball icon in the *Scene* panel to preview what each carousel item will look like. Each child node needs to have a name that corresponds to one of the `selectable_items:` in your MPF config file.

![image](../images/carousel_children.png)

When the MPF Carousel mode selects an item to display, it will post event with the name of the carousel mode and the name of the selected item. The `MPFCarousel` node will then iterate through its child nodes and hide all children except one with the same name as the selected item.

### carousel_name:

Single value, type `String`. Default `None`.

This is the name of the carousel mode in MPF that will be triggering changes. The name is required so that GMC can correctly identify in case multiple carousels are active at once.