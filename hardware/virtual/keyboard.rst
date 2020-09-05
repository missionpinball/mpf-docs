Connecting Your Computer Keyboard to MPF Switches
=================================================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/keyboard`                                                      |
+------------------------------------------------------------------------------+
| :doc:`/config/switches`                                                      |
+------------------------------------------------------------------------------+

The MPF media controller includes a keyboard interface which allows you
to interact with your running machine via a computer keyboard.
In most cases you'd use this to simulate pinball switch events via keys on
your keyboard, but you can also post MPF events via keyboard presses.
You can map single key presses or combinations of keys, and you can
use the keyboard module with or without a physical pinball machine
connected to your computer.

To use the keyboard interface, you add a `keyboard:` section to your machine
configuration file and then create a list which maps keyboard keys to pinball
machine switch names or MPF events. Then when you press a key on the
keyboard, the switch controller receives that event and sends it to
the game.
The keyboard module tracks both key-down and key-up events,
so you can hold down a key to represent a ball sitting on a switch.
You can also set several options for each key, including:

* Specify that a key is a "toggle" key, meaning the switch stays in
  the state even after you let go of the key. (In other words, tap the
  key once to activate the switch. Tap it again to deactivate it.) This
  is helpful for things like your trough or ball locks where you want to
  simulate a ball sitting on a switch but you don't want to play a crazy
  game of keyboard Twister where you're trying to hold down all these
  keys at once.
* Specify that a key is inverted, so pressing (or holding) the
  keyboard key deactivates the switch, and releasing it activates the
  switch. (Note this is *not* needed to compensate for normally-closed
  switches, as the switch controller handles that automatically. This is
  just is you want to invert the computer's keyboard action.)
* Specify combo keys, so you can set up one switch action for the
  ``S``key, a different one for ``CTRL+S``, another one for ``SHIFT+S``, etc.

Note that you can also use the :doc:`MPF Monitor </tools/monitor/index>` for this.
However, often it is faster to use the keyboard to change switch states.
You can also use the MPF monitor and your keyboard in tandem.
Most people use keyboard mappings to change balls in troughs for example.

Additionally, the ``keyboard:`` section is nice for posting ad-hoc and debug
events.
For instance, it can be very useful to be able to start modes using the
keyboards when you are testing them if it is nontrivial to start them.

Here's an example of it in action:

.. code-block:: mpf-mc-config

    keyboard:
      z:
        switch: left_flipper
      slash:
        switch: right_flipper
      s:
        switch: start
      1:
        switch: trough1
        toggle: true
      2:
        switch: trough2
        toggle: true
      shift+p:
        switch: lock_post
        invert: true
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
^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Since there are probably more switches in your machine then there are
keys on your keyboard, you can also specify key combinations along
with the key entries. These are called "modifier keys," and MPF
supports them in combination with regular keys, like this:

.. code-block:: mpf-mc-config

  #! keyboard:
    t:
      switch: foo
    shift-t:
      switch: tilt
    shift+ctrl+t:
      switch: slam_tilt

Starting in MPF 0.33, you an add ``debug: true`` in the ``keyboard:`` section to get a printout
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


What if it did not work?
------------------------
Make sure debug: true is set under keyboard as described above.

Look at your log files to see what your key strokes are.

It is possible that numlock key is on by default (especially with a laptop that does not have dedicated numlock key and running Windows).

You might see something like this:

.. code-block:: console

   Keyboard : Processing key stroke for key s-numlock
   Keyboard : Processing key stroke for key s-numlock

If that is the case you may have to edit your computer's registry or run powershell to turn off numlock.
