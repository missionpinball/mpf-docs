
You can use the `light_scripts:` section of your machine config files
to create "scripts" which control how lights or LEDs behave. Then you
can use the `light_player:` section to apply those scripts to specific
lights or LEDs. This sectioncan be used in your machine-wide config
files. ` `_ This section *cannot* be used in mode-specific config
files. Light scripts are very similar in concept to light shows. The
difference is that when you create a light show file, you include the
specific lights in the show itself. With light scripts, you create a
generic script you can apply to any light (or lights) later on. For
example, you might create a show file that says "turn on
*light_shoot_again*, then *light_bonus_2x*, then turn them both off."
Every time you run that show, it applies to the lights
*light_shoot_again* and *light_bonus_2x*. A script, on the other hand,
might say "turn the LED red, then yellow, then off". There's no light
or LED name specified in the script, and instead you can later apply
that script to any light you want. So in the `light_scripts:`section
of your config file, you actually create a listing of all the
different scripts you want to use later in your game. You don't
actually apply them at this point. You just create them. For example:


::

    
    light_scripts:
        flash:
            - tocks: 1
              color: ff
            - tocks: 1
              color: 0
        on:
            - tocks: 1
              color: ff
    
        rainbow_cycle:
            - tocks: 1
              color: ff0000
            - tocks: 1
              color: ff5500
            - tocks: 1
              color: ffff00
            - tocks: 1
              color: 00ff00
            - tocks: 1
              color: 0000ff
            - tocks: 1
              color: ff0099


You'll notice that the script format is similar to the `show format`_
except that the script doesn't contain any light names. The
`light_scripts:`section above has three scripts in it: *flash*, *on*,
and *rainbow_cycle*. Scripts that you will apply to `Matrix
Lights`_only use `00` (off) or `ff` (on), while scripts which you'll
apply to `RGB LEDs`_ have six-character hex color codes. Notice that
each step of the script starts with a dash (and the space between the
dash and the work "tocks" is important). The "tocks" represents the
relative timing of one step versus the next. (Tocks have nothing to do
with real-world time, since when you run a script you can specify how
many tocks per second it runs at.) Once you create your scripts, you
can apply them to certain lights based on MPF events with the
`light_player:`section of your config. (The `light_player:`section can
exist in your machine-wide config file or a mode-specific config
file.)

.. _RGB LEDs: https://missionpinball.com/docs/mechs/rgb-led/
.. _Matrix Lights: https://missionpinball.com/docs/mechs/matrix-light/
.. _show format: https://missionpinball.com/docs/shows/creating-shows/


