Tutorial step 6: Add keyboard control
=====================================

Once you get to this point, you should be able to run the MPF game
engine as well as the media controller, and you should have a pop-up
window which shows some text. You should have your flippers
configured, and if you have a physical machine connected, you should
be able to flip.

In this step, we're going to add some keyboard
settings to your machine config which will let you map keyboard keys on your
computer to switches in your pinball machine. This lets you "play" your
game on your computer, which is useful for (1) cases where you don't
have a physical machine nearby, and (2) scenarios where your pinball
machine is all the way on the other side of the room and you don't
feel like getting up every time you start MPF.

1. Create your key-to-switch mappings
-------------------------------------

The first step is to create your key-to-switch mappings in your config
file. You do this by adding a ``keyboard:`` section,
and then in there you add entries for each keyboard key and what type
of action in MPF you want to map them to. (Switches, in this case.)

Here's an example where we map the left flipper button to the ``Z`` key
and the right flipper button to the ``?`` key:

.. code-block:: mpf-config

    keyboard:
      z:
        switch: s_left_flipper
      '?':
        switch: s_right_flipper

Note that the question mark is in quotes since it's a non-standard
character, and if you don't put it in quotes, it will confuse the
YAML parser.

Also it's weird that the key is the question mark, because if you push
that key normally it types a slash. (The question mark is the shift
option for that key.) So if you set a key mapping and it doesn't work,
try the other character on the key.)

Again make sure that you have proper YAML formatting. The ``z:`` and ``"?":``
entries should indented the same number of spaces, and the "switch"
words should be indented further. Also make sure you have a space to
the right of the colon after ``switch:``. At first you might think it's
a bit tedious to have to write the word "switch" for each line. After
all, why can't you just enter them as ``z: s_left_flipper``? This is
because the MPF keyboard interface can actually be used to control
:doc:`a lot more than just keys </hardware/virtual/keyboard>`.
The details of that
are not important now, so for now just make sure your ``keyboard:``
section looks like the example above.


2. Test your new keyboard interface
-----------------------------------

At this point we're ready to test this out. Pretty simple. Save your config file and
run your game again. (Seriously, we can't tell you how many times
things don't work only to realize we didn't save our config after
changing it!). So now run your game, starting both the media
controller and the MPF core. Again you can either do this by running
both commands manually in separate windows or by running ``mpf both -t``.

Note that if you have a physical machine connected, *your physical
flippers will not flip with the keyboard keys*.

Let's repeat this to be clear. If MPF is connected to physical hardware,
pushing flipper button keys on your keyboard will not actually operate
your physical switches. (We'll cover why not in Step 3 below.)

In order for the keys to work, the catch is that
the graphical popup window (the one with the attract mode slide in it) has to
be the active window for it to receive the keys. (It has to have
"focus", in OS parlance.) Just like how your typing is only sent to
the current active window on your desktop, the media controller's
graphical window has to be active for your game to see your keystrokes
and convert them to switches. So make sure this window is active (you
can ALT+TAB to it or click on it).

Then try hitting the "Z" and "/" keys, and you should see them show up
in your console window which is running the MPF game engine as MPF
switch events, like this:

::

    INFO : SwitchController : <<<<< switch: s_left_flipper, State:1 >>>>>
    INFO : SwitchController : <<<<< switch: s_left_flipper, State:0 >>>>>
    INFO : SwitchController : <<<<< switch: s_right_flipper, State:1 >>>>>
    INFO : SwitchController : <<<<< switch: s_right_flipper, State:0 >>>>>

When you hit a key that you've configured on your keyboard, it's
actually received by the media controller which in turn converts it to
switch name and sends it to the MPF game engine. (This is because the MC
controls the popup window, not MPF, and you need a window to track key states.)

Notice that there are actually state changes each time you hit and release a key.
The "State: 1" means that switch has become active (i.e. when you press
down the key), and the "State: 0" means that switch has just become
inactive (when you release the key). You can experiment with this by
holding down a key and seeing the log event for the associated switch
becoming active, and then when you release it you'll see that switch
becoming inactive. Go ahead and play around with this, and notice that
you can push and hold the two keys in different orders and
combinations.

3. Why can't you "flip" your physical machine with the keyboard?
----------------------------------------------------------------

If you're working with a physical machine with this tutorial, you
might be surprised to see that your flippers don't fire when you hit
the ``Z`` or ``/`` keys! Even more confounding is that you will still see
the flipper switch events in your console log, and if you reach over
and hit the physical buttons on your machine, the flippers will work.
So what gives?!?

This happens because MPF uses "hardware rules" to program quick-response
mechanisms (like flippers), meaning the flippers are activated by the
control system rather than MPF software.

Read the :doc:`/hardware/hw_rules` guide for details.

4. Install the MPF Monitor (optional)
-------------------------------------
While pressing keyboard switches is great and fast it would be a lot
of work to map all your switches to the keyboard (and remembering
which key does what). Therefore you can later use the
:doc:`MPF monitor </tools/monitor/running>` to lay them out visually
and trigger them with your mouse (you can start using it right now
if you want).

What if it doesn't work?
------------------------

If you don't see your switch events in the console when you press your
keys, there are a few things you can try to troubleshoot:

+ Double-check to make sure you actually saved your updated config
  file. :)
+ Make sure no modifier keys (shift, control, etc.) are being pressed
  at the same time. Since there are way more switches in a pinball
  machine than keys on a keyboard, MPF lets you add modified keys to
  your ``keyboard:`` map. This means that MPF will see ``Z``, ``SHIFT+Z``,
  ``CRTL+Z``, ``SHIFT+CTRL+Z``, etc. all as different switches.
+ Remember that the media controller's pop-up window has to be in
  focus. Make sure it's the active window on your desktop and try
  hitting your keys again.
+ Remember that your physical flippers will not flip if you hit the
  keyboard keys for your flipper buttons.
+ Check if numlock is enabled. This seems to be common issue on Windows 10.
  Disable numlock in this case.
+ Make sure you started ``mpf both -t`` and did not omit ``-t`` as this would
  hide the log and show the text ui instead.

Check out the complete config.yaml file so far
----------------------------------------------

If you want to see a complete ``config.yaml`` file up to this point, it's in the ``mpf-examples/tutorial/step_6``
folder.

You can run this file directly by switching to that folder and then running the following command:

::

   C:\mpf-examples\tutorial>mpf both -t

