
The `machine:` section of the configuration files holds settings that
relate to the physical pinball machine itself. This sectioncan be used
in your machine-wide config files. This section *cannot* be used in
mode-specific config files. For now this includes:


::

    
    machine:
        balls_installed: 6
        min_balls: 3
        glass_off_mode: true


Details about these options:



balls_installed:
~~~~~~~~~~~~~~~~

This is the number of balls that should be installed in the machine.
The operator will get warnings if the number is something else.



min_balls:
~~~~~~~~~~

It's super annoying if you walk up to a pinball machine on location
and can't start a game because it's missing a ball. So this setting
lets you specify the minimum number of balls that need to be installed
in order for a game to start. Note that it's up to you to make sure
your game code can handle fewer balls than you might be expecting.



glass_off_mode:
~~~~~~~~~~~~~~~

This setting controls what happens when a playfield switch is hit when
a game is not in progress. In a "final" machine on location, if a
playfield switch is hit, MPF will think there's a live ball on the
playfield. This is great functionality to have, but it's super
annoying when you're testing your machine. The problem is that if you
hit a switch during attract mode, MPF will think there's a ball on the
playfield and you won't be able to start a game until that ball
drains. But if you have the glass off and you hit a switch with your
finger, you essentially "break" MPF since there was never a ball there
(meaning it will never drain), and that's annoying. So enabling
*glass_off_mode* means that if a switch is hit with no ball in play,
MPF will not think there's a ball on the playfield and you can still
start a game. The default setting is *True*, and you can set this to
*False* once you finish your machine.



