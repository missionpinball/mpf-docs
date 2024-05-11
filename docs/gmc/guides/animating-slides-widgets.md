---
title: Animating Slides and Widgets
---

# Animating Slides and Widgets

Godot offers a robust animation system that you can use for any purpose on your slides and widgets. This document covers the built-in animation support for *created*, *active*, and *removed* cases. For implementing arbitrary animations from custom events, see the [Slides Custom Methods](../slides.md#slide-custom-methods) documentation.

## Understanding Slide/Widget Lifecycle

Slides and widgets have a lifecycle of four possible states:

  *  **CREATED** when the slide or widget is instantiated and added to the display
  *  **ACTIVE** when the slide is placed at the top of the stack
  *  **INACTIVE** when the previously-active slide is removed from the top of the stack
  *  **REMOVED** when the slide or widget is removed from the display

GMC offers a convenient mechanism for triggering animations for these state changes, ideal for animating slides and widgets on to and off of the screen.

## Attach an AnimationPlayer Node

To use the built-in animations, you will need to add an `AnimationPlayer` Node to your scene. Then select the root node of your scene in the Godot Editor *Scene* panel (an `MPFSlide` or `MPFWidget` node) and in the *Inspector* panel, find the *Animation Player* property. Click on the *Assign...* button and select your AnimationPlayer node, or drag the AnimationPlayer node from the *Scene* panel onto the *Assign...* button.

## Create Animations

!!! note "See the Godot Docs"

    The Godot AnimationPlayer is a powerful and robust tool with dozens of features
    and options. It's highly recommended to review the [Introduction to Godot Animation Features](https://docs.godotengine.org/en/stable/tutorials/animation/introduction.html) guide before proceeding.

When you select the `AnimationPlayer` node in the *Scene* panel, the *Animation* panel will appear at the bottom of the editor. Click on the *Animation* button to create a new animation. You can name the animation "created", "active", "inactive", or "removed" depending on which lifecycle state you want to animate.

You can then create keyframes in the animation. For example, to have a slide fade-in when it's created, make an animation named "created".

The slide is currently 100% opaque which is what we want the *end* of the animation to be, so in the *Animation* panel drag the time slider to the end of the animation (by default, 1 second long).

In the *Scene* panel select the root node. In the *Inspector* panel find the *Visibility > Modulate* property, which should be a white box. Click on the key icon to create a keyframe of the Modulate property, defining that at this point of the animation (the end) the Modulate property should be 100% opaque.

Now drag the animation time slider to the beginning of the animation. Click on the white box of the Modulate property and find the `A` slider (for alpha channel, aka opacity). Slide the `A` value down to zero and click away from the color panel to dismiss it. Now click on the key icon again to create another keyframe in the animation, defining that at this point of the animation (the beginning) the Modulate property should be 0% opaque.

And that's it! When the slide is created, GMC will look at the `AnimationPlayer` attached to the root node and see an animation named "created", and therefore play the animation.

## When Animations Will and Will Not Play

There are some nuances to the lifecycle animations that need to be clarified to help avoid confusion and unexpected behavior.

### Created vs Active
When a slide is created, it will always have a `CREATED` state, but it will only get an `ACTIVE` state if it is the highest-priority slide on the stack. If a slide is simultaneously created and put on top of the stack, the `ACTIVE` animation will take precedence over the `CREATED` animation (if both are defined).

### Removal and Priority
An active slide may be removed and a new or underlying slide will become active, and both may have respective animations for those states.

#### If the new active slide has a *higher priority* than the old one:

  * The newly-active slide's `CREATED` or `ACTIVE` animation will play and the old slide will wait until the animation finishes before being removed. This allows a new slide to transition in overtop of the previous slide.

  * The outgoing `REMOVED` animation **will not play**. Because the new slide is on top of the old slide, there is no need to play the removal animation.

#### If the incoming active slide has a *lower priority* than the old one:

  * The newly-active slide's `CREATED` or `ACTIVE`animation **will not play**. Because the new slide is below the old slide, it must be present for when the old slide is removed.