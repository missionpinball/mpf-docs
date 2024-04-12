---
title: GMC Slides
---

# GMC Slides

The **MPFSlide** base class is used for all slides that GMC will render based on MPF `slide_player:` configs. This page outlines how the slides work and some of what you can do with them.

## Slide Scenes: Files and Naming

Every slide you create will be a unique Godot scene file (`.tscn`) that uses the `MPFSlide` node as its root. GMC will automatically look for slide scenes in the project root's `/slides` folder (and subfolders) as well as every `/modes/<mode_name>/slides` folder (and subfolders).

You can name your slides scenes whatever you'd like, except spaces are not allowed. GMC will find all scene files in the various `slides` folders and map their filenames, so that MPF `slide_player:` commands can reference the slides by their filename.

For example, if you had a slide file `/slides/base.tscn` and another file `/modes/skillshot/slides/skillshot_overlay.tscn`, your MPF configs might look like this:

``` yaml

    slide_player:
        mode_base_started: base
        skillshot_hit:
            skillshot_overlay:
                action: remove
```

For this reason, it's important that every slide has a unique name, regardless of which folder its in.

!!! tip

    If you accidentally create a new scene and forget to set `MPFSlide` as the root node, it's okay. In the *Scene* panel, you can create a new node of `MPFSlide`, right-click it, and select *Make Scene Root* to make that the new root node of the scene.

## Slide Stacks

Each Display maintains a "stack" of slides that are currently part of the game. The stack is ordered by priority, with the highest-priority slides on top. Whenever a slide is added or removed, the stack is re-ranked.

By default, each slide is placed in the stack with the priority of the mode that added it. You can include a `priority:` config option in the slide player, which will **add** the custom priority to the mode's priority.

!!! note "Transparency Works!"

    Not every slide scene has to fill the entire screen or have an opaque background. GMC tracks and updates all slides in the stack, so you can add a partially-transparent "overlay" slide to the stack and the slide(s) below it will be visible and update while the overlay is active.

## Slide Context

Every slide is created with a "context", which refers to the parent that created the slide. Typically this will be the name of the mode that called `slide_player` to create the slide.

When a mode stops in MPF, an event is posted to clear that context from the running game. This means that any slides, widgets, sounds, and lights that were started by the mode will be automatically removed.

This context auto-removal is a convenient feature for cleaning up a mode, but sometimes you may want a slide to outlive the mode that created it. You can provide a `custom_context` in the `slide_player` configuration to define your own context name—possibly the name of another mode if you want it to auto-clear with that mode, or any other name you'd like. Note that if you give a custom context that's not a mode name, you will have to manually remove the slide when you are done with it.

## Slide Features

Once you've created a slide scene in Godot, the entire world of Godot features are available to you! You can add text, images, videos, and anything else. You can animate slide elements with an AnimationPlayer, create cool effects with a Particle generator, and stylize with custom Shaders.

You can read up all about Godot's features on the [Godot Documentation page](https://docs.godotengine.org/en/stable/getting_started/introduction/index.html) or check out some [Godot tutorials and guides](https://docs.godotengine.org/en/stable/community/tutorials.html) for inspiration!

## Slide Custom Methods

With all of the robust features available through Godot, how can you use MPF to control behavior of a slide after it's on screen? Through the use of **slide methods**, a new feature of MPF to trigger custom behavior on a slide.

To give a slide custom behavior, you need to create a custom script for the slide that extends the base `MPFSlide` with new functionality. Open your scene in the Editor and in the *Scene* panel select the root node. Click on the red-x page icon to detach the `MPFSlide` script from the node, and then click the button again (with a green-plus now) to create a new script. Godot will automatically fill in the name of the scene as the name of the script, so you can just click *Create* to make the script.

On the first line of the script, set the line to be `extends MPFSlide` so that this node still has all the necessary functionality of a Slide. You can then create a new function called whatever you like, and give it custom behavior.

In this example, we have a scene *multiball_base_slide.tscn* and a matching script *multiball_base_slide.gd*. We've created an `AnimationPlayer` node and given it an animation named "explode", and we'll make a method that plays this animation. Our script file looks like this:

``` gd
    ## multiball_base_slide.gd

    extends MPFSlide

    func explode():
        $AnimationPlayer.play("explode")
```

We can then trigger this method from MPF with the slide player's `action: method` configuration.

``` yaml

    slide_player:
        jackpot_counter_complete:
            multiball_base_slide:
                action: method
                method: explode
```

This config tells GMC to call the method named "explode" on the `multiball_base_slide` when the *jackpot_counter_complete* event occurs.

This is a simple example of playing an animation from an AnimationPlayer, but the possibilities are endless. Godot scripting is a powerful tool that can do anything you can dream of, and with the `action: method` config option you can fully customize slide behavior based on MPF events.
