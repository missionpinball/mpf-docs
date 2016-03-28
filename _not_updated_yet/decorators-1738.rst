
Decorators are used to, well, "decorate" display objects in MPF.
They're essentially like display effects that are applied on topof
`display elements`_. For example, you might have a Text display
element which shows the text "PRESS START" on the display. If you want
that text to blink, then you can apply the "blink" decorator to it,
and boom! You now have blinking text. Decorators can be applied to any
display element (text, image, animation, shape), etc. You can chose to
decorate all the elements on a slide or just certain ones. You can
apply multiple decorators to the same element, and decorators continue
to function even when the slide is transitioning in or out. Different
types of decorators have different settings. The blink decorator, for
example, lets you specify the on time and off time (in seconds), as
well as how many times the element will blink. (Once, twice, forever,
etc.) So far we've only created one type of decorator (blink), but we
have plans to create more. (Fade, slide, rotate, expand, sparkle,
shimmer, color shift, invert, edge glow, etc.) It's very easy to
create and plug-in your own decorators too.(If you do then please
share them with us so we can include them in the MPF package!)

.. _display elements: https://missionpinball.com/docs/displays/display-elements/


