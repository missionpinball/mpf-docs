---
title: "GMC Example: Slide with Score and Player"
---

# Tutorial: Slide with Score, Player, and Ball

In this GMC tutorial we'll create a base slide for our game that includes the player score, ball number, and player number (when a multiplayer game is active).

## Configure the Slide Player

In your MPF config for your base mode, set the following:

``` yaml

    slide_player:
        mode_base_started: base
```

This will trigger the slide with a file name *base.tscn* when the base mode starts.

## Create a Base Slide

In the */modes/base* folder of your project, create a *slides* folder and in that folder create a new scene (*Create New > Scene*). Set the Root Type to be `MPFSlide` and save the file as *base.tscn*

Open the slide in the editor and add a new Node of type `Sprite2D`. In the *Inspector* panel, under *Texture* choose *Quick Load* and select a nice background image. Drag the corners of the image node until it fills the dimensions of the slide.

## Add a Score
Add a new node of type `MPFVariable`, drag the corners until it fills the full width of the slide, and move it down to the middle. In the *Label > Text* field enter "1,000,000" so you can visualize what the text will look like.

Lower in the *Inspector* panel, expand *Theme Overrides > Font Sizes* and set the font size to be a large number, like 200px. Under *Colors* enable the *Font Outline Color* (the default black is fine), and under *Constants* set the *Outline Size* to 6. If you have a custom font you'd like to use, you can set that in the *Fonts* section.

You should now see "1,000,000" large in the middle of the slide. Go to the top of the *Inspector* panel and set the following values:

  * *Variable Type*: Current Player
  * *Variable Name*: score
  * *Comma Separate*: enabled
  * *Min Digits*: 2

You can now play the project, start MPF, and start a game. You'll see `00` appear at the beginning, and as you press keyboard inputs to score points, the score value will update automatically. Neat!