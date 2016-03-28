
The *keyboard:* section of the config files is used to configure
options for how you map computer keyboard keys to pinball machine
switches. This sectioncan be used in your machine-wide config files.
This section *cannot* be used in mode-specific config files. (An
overview of the Keyboard Interface which explains thisconcept is
`here`_.)


::

    
    keyboard:
        z:
            switch: flipperLwL
        slash:
            switch: flipperLwR
        s:
            switch: start
        1:
            switch: trough1
            toggle: True
            start_active: True
        2:
            switch: trough2
            toggle: True
            start_active: True
        shift-p:
            switch: lockPost
            invert: True
        q:
            event: machine_reset
        ctrl-shift-4:
            event: advance_reel_test
            params:
                reel_name: score_1p_10
                direction: 1




Key & key combination entries
-----------------------------

Once you create your *keyboard:* section, you create subsections for
each key or key combination you want to configure. For simple keys
(without modifiers), you can just enter the key. (In the sample file
above, this is `z`, `s`, `1`, `2`, `q`, and `4`.) These entries are
not case sensitive.



Using special keys
~~~~~~~~~~~~~~~~~~

For "special" keys, it's probably just easiest to enter the keys as
words. Here are some examples of words that map to keys:


+ comma
+ period
+ equals
+ minus
+ backquote
+ leftbracket
+ rightbracket
+ slash
+ backslash
+ asterisk
+ plus


You can see a complete list in the `Pygame documentation on key
symbols`_. Pretty much you can use anything that's after the "K_" in
the list. Note that you can't use the Escape key because that's
currently hard-coded to exit out of MPF when you hit it. (We'll change
that in the future so you can configure it.) Note that this keyboard
interface focuses on keys, not symbols. In other words the "plus" key
is if you have a full size keyboard with a number pad which has a
dedicated plus key. If you're using a laptop with the shared plus &
equals key, that is the equals key, or the equals key with a shift
modifier.



Adding SHIFT, CTRL, and ALT modifiers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Since there are probably more switches in your machine then there are
keys on your keyboard, you can also specify key combinations along
with the key entries. These are called "modifier keys," and MPF
supports four different ones:


+ shift
+ ctrl
+ alt
+ meta (Exact meaning depends on the platforms. It's the Command key
  on a Mac, and the CTRL or Windows key on Windows.)


You can add one (or more) modifier keys by adding the modifier name
with a dash (minus sign) before the key, like this:


::

    
    t:
        switch: foo
    shift-t:
        switch: tilt
    shift-ctrl-t:
        switch: slamTilt


Modifier key names are not case sensitive and can be added in any
order. (i.e. `shift-ctrl-t`is the same as `ctrl-shift-t`.) We use
modifier keys for lesser-used entries. The tilt is a good example,
like in the snippet above. We might use the `T`key during regular game
play for some switch, but if we want to hit the plumb bob tilt then
we'll hit `CTRL+T`, and if we want a slam tilt then we'll hit
`CTRL+SHIFT+T`.



Optionsfor each key & key combination
-------------------------------------

Once you enter the key or key combination, then you need to create a
subsection which defines what this key or key combination does when
it's hit. There are several options:



switch:
~~~~~~~

The switch name of the pinball machine switch you want this key (or
key combination) to control.



toggle:
~~~~~~~

If True, then the key acts like a "push on / push off" key, where you
just have to tap it once to hold the switch active. This is useful for
switches in ball devices, since you don't want to have to hold down
the keys on your keyboard forever whenever a ball is locked in a
device. Default is *False*. You might want to create multiple entries
for the same switch for different key combinations. For example:


::

    
        1:
            switch: trough1
            start_active: True
        shift-1:
            switch: trough1
            toggle: True


In the above code, you can momentarily "tap" the *trough1* switch by
hitting the *1* key, but if you want to lock that switch on, then you
can push *Shift+1*.



invert:
~~~~~~~

If True, then this key is inverted, meaning the associated switch is
active when you're not pushing the key down, and it's inactive when
you're holding the key.



event:
~~~~~~

You can specify an event name to be posted when this key is pressed.
This is useful for testing when you want to test some part of your
game code based on an event. For example, you could map a keyboard key
to *clockwise_orbit_hit* event instead of having to hit the
*left_orbit_enter* key quickly followed by the *right_orbit_enter*
key. Events entered here are transmitted posted by the MPF core engine
process.



mc_event:
~~~~~~~~~

This is similar to the *event:* entry, except an *mc_event* is posted
as events in the media controller process, rather than in the MPF
process.



params:
~~~~~~~

This section contains subsections which are a list of parameters that
are posted along with the *event* or *mc_event* specified above. Using
the following configuration file snippet as an example:


::

    
    keyboard:
        4:
            event: advance_reel_test
            params:
                reel_name: score_1p_10
                direction: 1


This keyboard entry will post the event *advance_reel_test*when the
*4* key is pressed, and it will pass the parameters
*reel_name=score_1p_10*and *direction=1*. This complete entry is the
equivalent of the following game code:
`self.machine.events.post('advance_reel_test', reel_name=score_1p_10,
direction=1)`

.. _here: https://missionpinball.com/docs/mpf-core-architecture/keyboard/
.. _Pygame documentation on key symbols: http://www.pygame.org/docs/ref/key.html


