How to animate display widgets
==============================

One of the features of MPF is that you can animate display widgets. Animating a widget means that you can change a
widget's properties over time. You can pretty much change any numeric property, includine size, position, opacity, etc.

When animating widgets, you specify multiple properties to change at the same time, or a sequence of changes one after
the other (or both). You can also specify the duration of each step, the "easing" formula that affects the curve
(acceleration/decceleration) of the change, and whether the animation is a one-time thing or a repeating loop.

You can also configure animations to start playing as soon as the widget is created, or tie steps (or series of steps)
to MPF events, meaning a widget might be static, then the event "move_widget" is posted and it moves, then the event
"remove_widget" is posted and it's animated away.

This How To guide will show you how to do all of that.

1. Understanding animations in MPF
----------------------------------

MPF animations are properties of widgets. For example, here's a basic widget with no animations:

::

   slides:
      slide_1:
         widgets:
            - type: text
              text: MY TEXT
              color: red

To add animations to a widget, you simply add an ``animations:`` setting to that widget, and then under there you add
specific animation steps and settings. For example:

::

   slides:
      slide_1:
         widgets:
            - type: text
              text: MY TEXT
              color: red
              animations:
                entrance:                  # animation trigger event
                  - property: opacity      # name of the widget property we're animating
                    value: 1               # target value of that property for this step
                    duration: .5s          # duration for this step (how long it takes to get there)
                  - priority: opacity      # second step in the animation (starts with a hyphen)
                    value: 0
                    duration: .5s
                    repeat: true           # added to the final step, tells this animation to repeat (loop)

In the example above, an ``animations:`` setting has been added to the widget. Then under there, you add
the name of the event you want to use to trigger this animation to start. In this case a special event
called ``entrance:`` was used, which is a fake event name that makes this animation start immediately once
the widget is created.

Next, notice that under the event, there are two steps (each beginning with a hyphen and a space).

There are several settings you can specify in each step. (See the config file reference for animations for
details)

In this example, there are three settings for the first step:

::

                  - property: opacity
                    value: 1
                    duration: .5s

The **property** setting is the name of the widget's property that you want to animate. This can be almost any
numerical property of the widget, including ``x:``, ``y:``, ``opacity``, etc. (Different widget types have
different types of animatable properties. For example, on text widgets you can animate the ``font_size:``, on
various shape widgets you can animate the ``height:`` and ``width:``, etc.

Pretty much the only thing you can't animate at this point is rotation (since MPF doesn't currently
support widget rotation. That's a future feature we'll have to add).

2. Animating multiple properties at once
----------------------------------------

The example animation above includes two steps (one to set the opacity to 1 and the next to set it to 0).
By default steps are sequential, meaning that one step completes before the next one starts. However you can
add a ``timing: with_previous`` to an animation step which will make it so that step runs at the same time
as the step before it. This means you can animate multiple properties at once.

For example, to make the text grow and shrink while also fading on and off:

   slides:
      slide_1:
         widgets:
            - type: text
              text: MY TEXT
              color: red
              animations:
                entrance:                  # animation trigger event
                  - property: opacity      # name of the widget property we're animating
                    value: 1               # target value of that property for this step
                    duration: .5s          # duration
                  - priority: opacity
                    value: 0
                    duration: .5s
                    repeat: true



The example above is a widget that's part of a slide, but you can add animations to widgets anywhere a widget is defined
(in the slide properites, in a show step, as part of a :doc:`named widget <reusable_widgets>`, etc.)