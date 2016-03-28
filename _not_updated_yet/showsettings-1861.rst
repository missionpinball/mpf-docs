
This page discusses all the settings and options you can use when
playing shows. (If you're looking for details about how to actually
create shows, look `here`_.) All of the settings and options discussed
here are available to you regardless of the technique you use to play
or stop the show, whether it's via the machine configuration file, via
the action event, or manually in code. (Details of the three of these
options are `here`_.)



Options for Playing shows
-------------------------

When you play a show, you can use the following options. All of them
are optional (i.e. the show player will use the default option if you
don't specifically set it to be something else).



tocks_per_sec
~~~~~~~~~~~~~

Integer of how fast your show runs. ("Playback speed,"in other words.)
Your show files specify action times in termsof 'tocks', like "make
this light red for 3 tocks, then off for4 tocks, then a different
light on for 6 tocks." When you play ashow, you specify how many tocks
per second you want it to play.Default is 30, but you might even want
tocks_per_sec of only 1or 2 if your show doesn't need to move than
fast. Note this doesnot affect fade rates. So you can have
tocks_per_sec of 1 butstill have lights fade on and off at whatever
rate you want.Also the term "tocks" was chosen so as not to confuse it
with"ticks" which is used by the machine run loop.



priority
~~~~~~~~

Integer value of the relative priority of this show. Ifthere's ever a
situation where multiple shows want to controlthe same item, the one
with the higher priority will win.("Higher" means a bigger number, so
a show with priority 2 willoverride a priority 1.) Default is 0. You
don't have to worry about this unless you have overlapping shows
playing at once.



repeat
~~~~~~

True/False as to whether the show repeats (i.e. 'loops') when it's
done playing. Default is False.



num_repeats
~~~~~~~~~~~

Integer of how many times you want this show to repeatbefore stopping.
A value of 0 means that it repeatsindefinitely. Note this only works
if you also have `repeat=True`. Default is 0 which means if you set
repeat=True then this show will play indefinitely (until you stop it).



blend
~~~~~

True/Falsewhich controls whether this show "blends" its lights with
lowerpriority shows and scripts. For example, if this show turns
alight off, but a lower priority show has that light set to blue, if
you have blend=True thenthe light will "show through" as blue while
it's off here.If you don't want that behavior, set blend to be False.
Then offhere will be off for sure (unless there's a higher priority
showor command that turns the light on). Default is False.



hold
~~~~

True/Falsewhich controls whether the lights or LEDs remain intheir
final show state when the show ends.



start_location
~~~~~~~~~~~~~~

Integer of which position in the show file the showshould start in.
Usually this is 0 but you can specify a start point of whatever you
want to start partway through a show. This is also used for restarting
shows that you paused. The default is "None" which means the show will
start playing wherever it last ended (or at the beginning if it hasn't
been played yet). Use a value of 0 if you want to force the show to
start playing at the beginning.



callback
~~~~~~~~

A callback function that is invoked when the show isstopped. This
setting is not available via shows that you play via the `ShowPlayer:`
config file settings, but you can use this for shows you play with
action events and manually via code.



Options for Stopping Shows
--------------------------

The options available when you stop shows are pretty simple:



reset
~~~~~

True/False which controls whether the show is reset back to the
beginning when it stops. If False, you can play the show again and it
will pick up where it left off (unless you override it by specifyinga
`start_location` when you play it). Default is True.



hold
~~~~

True/False which controls whether the lights (matrix lights and LEDs)
in this show stay on or not when the show ends. If True, any lights
that this show turned on in the last step will stay on. If False, when
the show ends, it will release control of the lights and they can be
reset to whatever other state they should be via other shows or
sections of the game.

.. _here: https://missionpinball.com/docs/shows/playing-shows/
.. _here: https://missionpinball.com/docs/shows/creating-shows/


