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
and the right flipper button to the ``/`` key:

::

    keyboard:
        z:
            switch: s_left_flipper
        /:
            switch: s_right_flipper

Again make sure that you have proper YAML formatting. The "z" and "/"
entries should indented the same number of spaces, and the "switch"
words should be indented further. Also make sure you have a space to
the right of the colon after ``switch:``. At first you might think it's
a bit tedious to have to write the word "switch" for each line. After
all, why can't you just enter them as ``z: s_left_flipper``? This is
because the MPF keyboard interface can actually be used to control
`a lot more than just keys </config/keyboard>`_. The details of that
are not important now, so for now just make sure your ``keyboard:``
section looks like the example above.

2. Test your new keyboard interface
-----------------------------------

At this point we're ready to test this out. Pretty simple. Save your config file and
run your game again. (Seriously, we can't tell you how many times
things don't work only to realize we didn't save our config after
changing it!). So now run your game, starting both the media
controller and the MPF core. Again you can either do this by running
both commands manually in separate windows or by running ``mpf both``.

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

To understand why this happens you have to understand
how the MPF handles "quick response" switches which are used for
things like flippers, slingshots, and pop bumpers. As you can imagine,
those types of devices require near-instant response. When you hit a
flipper button, you want that flipper to fire *instantly*.

So for these types of devices, MPF actually writes a out a configuration rule to the
physical pinball controller that tells it "Hey, if you see this
switch, fire this coil." (This happens on all platforms, including FAST, P-ROC, and
OPP.) That keeps the entire switch read / coil fire cycle within the pinball
controller itself, and the pinball controller can respond by firing
that coil with sub-millisecond level response times.

Compare that to
the alternative where the player would push a button on the pinball
machine, the pinball controller would receive it, then it would have
to be sent via USB to the host computer, then the host computer would
have to process it and figure out that a coil needed to be fired, then
it would have to send that coil firing command back across the USB bus
to the pinball controller, and then finally the pinball controller
could fire that coil. Even though computers are really fast, that
whole process would still take a few milliseconds which would be
horrible in a pinball scenario.

To deal with this,the pinball
controllers allow rules to be written to their hardware where we can
set up which coils we'd like to be fired (and with which settings) when
switches change state. So part of what the thousands of lines of code
of MPF do behind the scenes is when you set up your flippers in the
``flippers:`` section of your config file, it actually writes those
rules out to the hardware controller so the hardware controller can
handle them. These rules are dynamic and updated often.

For example
they're deactivated when a game is not in progress, when it tilts, and
(optionally) between balls, and you can change them to do all sorts of
novelty things like inverted flippers, no hold flippers, weak
flippers, etc.

By the way, even when you write hardware rules to your
pinball controller, the MPF software still receives notification when
those switches change state. After all, you might want to play a sound
effect or update a score even if the hardware controller fired the
actual coil, and in the case of flipper buttons you need to know when
they're activated for lane changes and to cancel video modes and stuff.

In this case you still have one physical switch in your machine and
one switch configured in your config files—-it's just that if you have
a hardware rule configured for a switch then when that switch changes
state, the pinball controller fires the associated coil *in addition*
to sending the switch state change to MPF as usual.

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

Check out the complete config.yaml file so far
----------------------------------------------

If you want to see a complete ``config.yaml`` file up to this point, it's in the ``mpf-examples/tutorial``
folder with the name ``step6.yaml``.

You can run this file directly by switching to that folder and then running the following command:

::

   C:\mpf-examples\tutorial>mpf both -c step6

