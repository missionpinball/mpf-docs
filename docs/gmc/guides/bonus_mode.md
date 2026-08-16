---
title: GMC Bonus Slides
---

# Bonus Slides in GMC

With MPF 0.80 the bonus configuration is consolidated and simplified, providing a single *bonus_entry* event for all bonus-related information. This allows for the creation of dynamic slide contents hooked into a single event.

!!! note  "GMC Includes a Bonus Slide"

    This guide is actually a walkthrough for creating the *bonus.tscn* slide that is included in GMC as the default bonus slide. If you are happy with that slide, you don't need this guide!

    The reason for this guide is to explain *how* that slide works, so you can build your own custom bonus slide or just get a better understanding of conditional children, event-driven variables, and slide updates.

## Configure Bonus Settings

If you don't have a bonus mode already, in your MPF project create the file */modes/bonus/config/bonus.yaml* and update your machine config to include `bonus` as a mode.

MPF includes default bonus code with lots of functionality baked in, so all you need to configure in your *bonus.yaml* is what bonuses you want and MPF will fold your config into the default bonus config.

For instructions on configuring your bonus entries, see the [bonus mode_settings reference](../reference/bonus.md)

Next you need to set up your slide player to (1) play the bonus slide when bonus starts, (2) display some initial text before the entry calculations are shown, and (3) update the text with each entry.

``` yaml
# bonus.yaml

slide_player:
    mode_bonus_started: bonus
    bonus_start:
        bonus:
            action: update
            tokens:
                entry: initial
    bonus_entry:
        bonus:
            action: update
```

## Creating a Bonus Slide

In the Godot Editor, create a new slide scene named *bonus.tscn* that uses `MPFSlide` as the root node.

Give it a nice `ColorRect` background color, or a `Sprite2D` background image if you prefer.

### Conditional Children

There are five things that the Bonus Slide will show: initial text, each bonus entry, the subtotal, the multiplier, and the total. So we will create a [Conditional Children Node](../reference/mpf-conditional-children.md) with five children, one for each case.

In the *Scene* panel click the plus icon to create a new node and select `MPFConditionalChildren`. In the *Inspector* panel for this node, set the following:

  *  **Variable Type:** Event Arg
  *  **Variable Name:** entry

#### Initial Text

Right-click on the `MPFConditionalChildren` node in the *Scene* panel and *Add Child Node...*, select `Node2D`, and create the child. Double-click the new Node2D to rename it "*initial*".

Right-click on the "*initial*" node and add a new child node of type `MPFVariable` with the following settings:

  *  **Variable Type:** Current Player
  *  **Variable Name:** ball
  *  **Template String:** "End of Ball %s"
  *  **Label > Text:** "End of Ball 1"

Then set the position, font, size, color, et cetera, to your liking. This is what will appear when the bonus mode first starts, before the bonus calculations start appearing.

To keep things organized, click on the eyeball icon next to the "*initial*" node in the *Scene* panel to hide this for now.

#### Bonus Entries

Right-click again on the `MPFConditionalChildren` node, then *Add Child Node...*, `Node2D`, and create it. Rename this node to "*\_\_default\_\_*" (that's "default" with **two underscores** before and after).

!!! note

    *\_\_default\_\_* is a special name for `MPFConditionalChildren` which will appear as a fallback if none of the other child nodes match the condition. With this fallback, we can have as many bonus entries as we want with whatever names we want and they'll all use this child node.

Create two `MPFVariable` child nodes inside the *\_\_default\_\_* node. Name the first one "*text*" and set it up like so:

  *  **Variable Type:** Event Arg
  *  **Variable Name:** text
  *  **Initialize Empty:** Enabled
  *  **Label > Text:** "Bonus Entry Text"

Name the second one "*score*" and set it up as well:

  *  **Variable Type:** Event Arg
  *  **Variable Name:** score
  *  **Comma Separate:** Enabled
  *  **Initialize Empty:** Enabled
  *  **Label > Text:** "1,000,000"

Now set the position, font, size, color, et cetera how you want. When you're done, click the eyeball icon to hide the *\_\_default\_\_* node.

#### Subtotal Text

Right-click on the *\_\_default\_\_* node and select *Duplicate*, then rename the duplicate to "*subtotal*".

For these next children, we'll want to hard-code the title text but keep the same styling as the dynamic event-driven text from the bonus entries. In the *Scene* panel, select the "*text*" node child of "*subtitle*". In the *Inspector* panel, click on the hammer/screwdriver icon for the tools menu and choose *Copy Properties*.

Now delete the "*text*" node and create a new child node of type `Label`. Select this node and in the tools menu, choose *Paste Properties*. And then under *Label > Text* enter your subtotal title text, like "Bonus Subtotal" or "Base Bonus" or whatever you'd like.

#### Total Text

The setup for the bonus total is nearly identical to the subtotal, so right-click on the "*subtotal*" node and *Duplicate*, then rename the duplicate "*total*". Change the *Label > Text* of the text node to be "Total Bonus" or "Bonus Total" or such.

(As before, it's probably helpful to use the eyeball icon to hide the "*subtotal*" slide while working on the "*total*" slide, and so on.)

#### Multiplier Text

The setup for the multiplier text is *almost* the same as subtotal and total, so start by duplicating one of those and renaming the duplicate "*multiplier*". Once again, change the *Label > Text* of the text node to be whatever you want ("Multiplier" or "Bonus Multiplier" etc.).

The difference between the multiplier and the rest is we want to include an "X" after (or before?) the multiplier value. Select the "*score*" node under the "*multiplier*" node and go to the *Inspector* panel.

It's unlikely that somebody will get a 1000X bonus multiplier, but might as well uncheck *Comma Separate*.

Under *Template String*, enter `%sX` if you want an X immediately after the multiplier (e.g. "3X"), or `%s X` to have a space ("3 X"), or `x%s` for a lowercase prefix ("x3"). Or anything else you'd like!

## Under the Hood

And that's it! Your bonus slide is ready to go.

For those who want to know more, here's a rundown of how this all will play out when the bonus mode runs.

  1.  When the bonus mode starts, the `slide_player` will play the `bonus` slide (aka *bonus.tscn*). The file you just saved in your project will supersede the default GMC bonus slide, so your scene will appear.

  1.  The *mode_bonus_started* event does not include an argument named "entry", so none of the named conditional children match. The default child ("*\_\_default\_\_*") is selected, but since both variables have `Initialize Empty`, nothing appears on screen.

  1.  The first event the bonus mode posts is *bonus_start*, which triggers the slide player to call `update` on the `bonus` slide and passes the token `entry: initial`

  1.  This event triggers the slide to update and the conditional children node re-evaluates. It sees the `entry: initial` argument and since it has a child node named "initial", that child is made visible.

  1.  The MPF bonus mode begins iterating through the entries in the `mode_settings:` config, and for each one it posts a *bonus_entry* event that includes `entry`, `text`, and `score` arguments.

  1.  These events trigger the `slide_player:` to call `update` on the `bonus` slide again, passing the original event's arguments as part of the update.

  1.  The bonus slide continues to update on each event. Since none of the `entry` values match explicit child names, the "*\_\_default\_\_*" child is shown and its variables render the `text` and `score` values accordingly.

  1.  When the bonus entries are completed, MPF posts the subtotal, multiplier, and total versions of the *bonus_entry* event. (Note that if the multiplier is one, the subtotal and multiplier events will be skipped.)

  1.  The bonus slide updates on these events as well, but identifies child nodes named "*subtotal*", "*multiplier*", and "*total*" and shows the correct child for each event.