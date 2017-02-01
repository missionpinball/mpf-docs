keyboard:
=========

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

The ``keyboard:`` section of your config is used to configure
options for how you map computer keyboard keys to pinball machine
switches and events. This is useful for testing your game from your
computer when you're not around your physical machine.

Note that you can also use the :doc:`MPF Monitor </monitor/index>` for this, and since the
Monitor was released, most people use that instead of the ``keyboard:`` section of
a config. However the ``keyboard:`` section is still nice for down-and-dirty testing
and for posting events.

Here's an example of it in action:

.. code-block:: yaml

    keyboard:
        z:
            switch: left_flipper
        slash:
            switch: right_flipper
        s:
            switch: start
        1:
            switch: trough1
            toggle: True
        2:
            switch: trough2
            toggle: True
        shift+p:
            switch: lock_post
            invert: True
        q:
            event: machine_reset
        ctrl+shift+4:
            event: advance_reel_test
            params:
                reel_name: score_1p_10
                direction: 1

You can also read more about the ``keyboard:`` section in the :doc:`/tutorial/6_keyboard`
documentation.

Key & key combination entries
-----------------------------

Once you create your ``keyboard:`` section, you create subsections for
each key or key combination you want to configure. For simple keys
(without modifiers), you can just enter the key. (In the sample file
above, this is ``z``, ``s``, ``1``, ``2``, ``q``, and ``4``.)

These entries are not case sensitive.

Using special keys
~~~~~~~~~~~~~~~~~~

For "special" keys, it's probably just easiest to enter the keys as
words. Here are some examples of words that map to keys:

* equals
* minus
* dash
* leftbracket
* rightbracket
* backslash
* apostrophe
* semicolon
* colon
* comma
* period
* slash
* question

Note that you can't use the Escape key because that's currently hard-coded
to exit out of MPF when you hit it.

Note that this keyboard interface focuses on keys, not symbols. In other words
the "plus" key is if you have a full size keyboard with a number pad which has a
dedicated plus key. If you're using a laptop with the shared plus &
equals key, that is the equals key, or the equals key with a shift
modifier.

Adding SHIFT, CTRL, and ALT modifiers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Since there are probably more switches in your machine then there are
keys on your keyboard, you can also specify key combinations along
with the key entries. These are called "modifier keys," and MPF
supports them in combination with regular keys, like this:

.. code-block:: yaml

    t:
        switch: foo
    shift-t:
        switch: tilt
    shift+ctrl+t:
        switch: slam_tilt

You an add ``debug: true`` in the ``keyboard:`` section to get a printout
on the console of the current key and/or modifiers that are pushed down
which is helpful in figuring out exactly what the modifier keys are called
on your system.

Use it like this:

.. code-block:: yaml

   keyboard:
      debug: yes

This will print out results live as you hit keys and combinations which will
look something like this:

::

   KEYS: d
   KEYS: s
   KEYS: shift
   KEYS: shift+s
   KEYS: f
   KEYS: super
   KEYS: meta+c
   KEYS: shift
   KEYS: shift+d
   KEYS: lctrl
   KEYS: ctrl+f
   KEYS: escape

Options for each key & key combination
--------------------------------------

Once you enter the key and/or key combination, then you need to create a
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

.. code-block:: yaml

        1:
            switch: trough1
        shift+1:
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

.. code-block:: yaml

    keyboard:
        4:
            event: advance_reel_test
            params:
                reel_name: score_1p_10
                direction: 1

This keyboard entry will post the event *advance_reel_test* when the
*4* key is pressed, and it will pass the parameters
*reel_name=score_1p_10* and *direction=1*.
