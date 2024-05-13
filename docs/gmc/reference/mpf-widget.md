---
title: MPFWidget
---

# MPFWidget

`MPFWidget` is a Godot Node class provided by the MPF-GMC extension. All scenes that will be used as widgets must derive from the `MPFWidget` class (i.e. have an `MPFWidget` node as the scene's root node).

Widgets are like mini-slides that can be added to and removed from an existing slide using the MPF `widget_player:` config block. Widgets are reusable, customizable, and great for popups, hints, and notifications.


## Node Configuration

### animation_player:

An instance of an `AnimationPlayer` node that one or more animations named "created", "active", and/or "removed". If an `AnimationPlayer` node is attached and contains any of those animation names, the respective animation will play on the widget when the widget changes to that state.

## Parameters

Widget instances created by `widget_player` have initial values that can be overridden with parameters in the slide player configuration.

### context:

Single value, type: `String`. Default: the calling mode's name

When a mode is stopped in MPF, a _clear_ event is broadcast to signal the end of the mode and to remove all slides, widgets, sounds, lights, and shows started by that mode. The value to track this is called "context", and by default each widget has a context of the name of the mode that created it.

If you do not wish for your widget to be removed when the calling mode ends, you can specify a different context value.

Note that if a widget is added to a slide and that slide is removed, the widget will be removed as well, regardless of the widget's context.

### key:

Single value, type: `String`. Default: the widget's file name

Once a widget is instantiated, it can be referenced by its `key` for actions like `update` and `remove`. By default, the widget's file name is used as its key.

In situations you may want multiple instances of a widget, you can specify a key manually. This key will then be used to reference the widget for any future actions. This allows you to use the same widget multiple times on a slide and choose exactly which one you want to update or remove.

### priority:

Single value, type: 'integer'. Default: `0`

This value will be added to the calling mode's priority to determine the overall stack priority of the widget. When a widget is added or removed from the slide, the slide's widgets are sorted with the highest priority widget on top.

## Methods

`MPFWidget` does not have any public methods exposed, but custom methods can be added to scene scripts that extend `MPFWidget`. These methods can be triggered from MPF `widget_player` with the `action: method` option. These options are the same as for slides, so see the [slide_player: reference](slide_player.md) for more details.

When a custom function is called, two parameters are passed in: *settings*, the configuration settings from the widget player config, and *kwargs*, the arguments from the event that triggered the widget player. If you declared any `tokens:` in your config for the widget player, those will be available as `settings.tokens`.

``` code

    func my_custom_method(settings, kwargs):
        # Function does stuff here
```


!!! note "Godot requires parameters for this function"

    You don't have to _use_ the settings and kwargs parameters, but you _do_ need to include them in your method.

    Godot has a pattern for parameters that are required by a function but not used by it: prefix the parameter name with a single underscore. This tells Godot that you know there is a required parameter but you're not going to use it; otherwise, Godot will give you a warning that the parameter is not used.

    `func my_custom_method(_settings, _kwargs):`

### settings

Single value, type `Dictionary`.

The *settings* parameter passed to the custom method is the configuration used in the `widget_player:` config file. It includes settings like `priority`, `action`, and the `tokens:` dictionary if you made one.

### kwargs

Single value, type `Dictionary`.

The *kwargs* parameter passed to the custom method is the list of event arguments from the event that triggered the `widget_player` to be called in the first place.

For example, the *player_score* event includes arguments for `value`, `prev_value`, `change`, and `player_num`. If your widget player is triggered by the *player_score* event, like so:

``` yaml

    widget_player:
        player_score:
            score_widget:
                action: method
                method: my_method
```

Then in the `func my_method(settings, kwargs):` method of *score_widget.gd* you would have access to `kwargs.value`, `kwargs.prev_value`, `kwargs.change`, and `kwargs.player_num`.

If you're curious what event arguments are available for a given event, look at the MPF log files. Each event is logged with all its arguments, so you can quickly see what's available.
