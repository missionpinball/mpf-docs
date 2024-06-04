---
title: Random Slide Children
---

# Random Slide Children

In this tutorial we'll be using the `MPFChildPool` node to create a group of children for a slide, one of which will be chosen at random to display each time the slide is shown.

In this example we'll use a random video, but this same workflow can be used for random images, widgets, and entire scenes.

## Create an `MPFChildPool`

Open a scene with an `MPFSlide` root node and add a new child node of `MPFChildPool`. Under this child create three `MPFVideoPlayer` nodes and assign a different video to each one. (Or if you don't have three videos, create three `Sprite2D` nodes and assign a different image to each one).

## The Child Nodes

Using the eyeball icon next to each child, make each visible one at a time and position the children how you'd like each to appear on the slide.

Note that each child node can be the parent of any number of other nodes, so you can include text, images, other widgets, and anything you want as sub-children of the main child. The important thing is that each direct child of the `MPFChildPool` is what will be randomly selected from.

For the video example, set the `end_behavior` of each to `Remove Slide`, and make sure `Autoplay` is disabled and `Expand` is enabled.

## Configure Pool Behavior

Select the `MPFChildPool` node and in the *Inspector* panel, set the `playback_method` to `Random Force All`. This will ensure each child is picked once before any repeats.

If you are using the `MPFVideoPlayer`, set the `child_method` value to "play", which will call play on the child video when it's chosen.

## Play the Slide

Set up your MPF configs to play the slide, and start the game! Each time the slide plays, one of the child nodes from the `MPFChildPool` will be displayed. If you're using the video example, the video will play automatically and then the slide will disappear. The next time the slide is shown, a different video will play!