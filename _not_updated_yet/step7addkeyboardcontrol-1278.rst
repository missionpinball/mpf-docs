
Once you get to this point, you should be able to run the MPF core
engine as well as the media controller, and you should have a pop-up
window which shows a virtual DMD. You should have your flippers
configured, and if you have a physical machine connected, you should
be able to flip. In this next step, we're going to add some keyboard
settings to your config which will let you map keyboard keys on your
computer to switches in your pinball machine.This lets you "play" your
game on your computer, which is useful for (1) cases where you don't
have a physical machine nearby, and (2) scenarios where your pinball
machine is all the way on the other side of the room and you don't
feel like getting up every time you start the machine. :)



(A) Create your key-to-switch mappings
--------------------------------------

The first step is to create your key-to-switch mappings in your config
file.You do this by adding a `keyboard:` section to your config file,
and then in there you add entries for each keyboard key and what type
of action in MPF you want to map them to. (Switches, in this case.)
Here's an example where we map the left flipper button to the `Z` key
and the right flipper button to the `/` key:


::

    
    keyboard:
        z:
            switch: s_left_flipper
        /:
            switch: s_right_flipper


Again make sure that you have proper YAML formatting. The "z" and "/"
entries should indented the same number of spaces, and the "switch"
words should be indented further. Also make sure you have a space to
the right of the colon after `switch:`. At first you might think it's
a bit tedious to have to write the word "switch" for each line. After
all, why can't you just enter them as `z: s_left_flipper`? This is
because the MPF keyboard interface can actually be used to control `a
lot more than just keys`_. The details of that are not important now,
so for now just make sure your `keyboard:` section looks like the
example above.



(B) Test your new keyboard interface!
-------------------------------------

At this point we're ready to test this out. Save your config file and
run your game again. (Seriously, we can't tell you how many times
things don't work only to realize we didn't save our config after
changing it!). So now run your game, starting both the media
controller and the MPF core. Again you can either do this by running
both commands manually (each one in a separate console window)


::

    
    python mc.py c:\pinball\your_machine



::

    
    python mpf.py c:\pinball\your_machine


Or if you're on Windows and you're using the batch file launcher, via:


::

    
    mpf c:\pinball\your_machine


Note that if you have a physical machine connected, *your physical
flippers will not flip with the keyboard keys*. (We'll cover why not
in Step (C) below.) In order for the keys to work, the catch is that
the graphical popupwindow (the one with the virtual DMD in it) has to
be the active window for it to receive the keys. (It has to have
"focus", in OS parlance.) Just like how your typing is only sent to
the current active window on your desktop, the media controller's
graphical window has to be active for your game to see your keystrokes
and convert them to switches. So make sure this window is active (you
can ALT+TAB to it—it's the Pygame logo which is ayellow cartoon
alligator holding a Nintendo controller in his mouth) or click on it.
Then try hitting the "Z" and "/" keys, and you should see them show up
in your console window which is running the MPF core engine as MPF
switch events, like this:


::

    
    INFO : SwitchController : <<<<< switch: s_left_flipper, State:1 >>>>>
    INFO : SwitchController : <<<<< switch: s_left_flipper, State:0 >>>>>
    INFO : SwitchController : <<<<< switch: s_right_flipper, State:1 >>>>>
    INFO : SwitchController : <<<<< switch: s_right_flipper, State:0 >>>>>


When you hit a key that you've configured on your keyboard, it's
actually received by the media controller which in turn converts it to
switch name and sends it to the MPF core engine via the TCP socket the
two processes use to communicate.If you launched the media
controllerwith the `-v -V` command line options (the uppercase *-V*
enables verbose logging to the console), you'll actually see the BCP
(that's "Backbox Control Protocol"—the protocol the media controller
and MPF core engine use to communicate) messages being sent. They'll
look something like this:


::

    
    DEBUG : BCP : Sending "switch?state=1&name=s_left_flipper"
    DEBUG : BCP : Sending "switch?state=0&name=s_left_flipper"


And if you enabled verbose logging of the MPF core engine, you'll also
see BCP messages showing it receiving the switch messages from the
media controller, like this:


::

    
    DEBUG : BCPClient.local_display : Received "switch?state=1&name=s_left_flipper"
    DEBUG : SwitchController : <<<<< switch: s_left_flipper, State:1 >>>>>
    DEBUG : BCPClient.local_display : Received "switch?state=0&name=s_left_flipper"
    DEBUG : SwitchController : <<<<< switch: s_left_flipper, State:0 >>>>>


Notice that there are actually state changeseach time you hit a key.
The "State: 1" meansthat switch has becomeactive (i.e. when you press
down the key), and the "State: 0" means that switch has just become
inactive (when you release the key). You can experiment with this by
holding down a key and seeing the log event for the associated switch
becoming active, and then when you release it you'll see that switch
becoming inactive. Go ahead and play around with this, and notice that
you can push and hold the two keys in different orders and
combinations, and MPF (thanks to Pygame) keeps it all straight.



(C)Why can't "flip" your physical machine with the keyboard?
------------------------------------------------------------

If you're working with a physical machine with this tutorial, you
might be surprised to see that your flippers don't fire when you hit
the *Z* or */* keys! Even more confounding is that you will still see
the flipper switch events in your console log, and if you reach over
and hit the physical buttons on your machine, the flippers will work.
So what gives?!? To understand why this happens you have to understand
how the MPF handles "quick response" switches which are used for
things like flippers, slingshots, and pop bumpers. As you can imagine,
those types of devices require near-instant response. When you hit a
flipper button, you want that flipper to fire *instantly*. So for
those types of devices, MPF actually writes a out a configure to the
physical pinball controller that tells it "Hey, if you see this
switch, fire this coil." (This happens with both P-ROC and FAST
controllers.) That keeps the entire cycle within the pinball
controller itself, and the pinball controller can respond by firing
that coil with sub-millisecond level response times. Compare that to
the alternative where the player would push a button on the pinball
machine, the pinball controller would receive it, then it would have
to be sent via USB to the host computer, then the host computer would
have to process it and figure out that a coil needed to be fired, then
it would have to send that coil firing command back across the USB bus
to the pinball controller, and then finally the pinball controller
could fire that coil. Even though computers are really fast, that
whole process would still take a few milliseconds which would be
horrible in a pinball scenario. To deal with this,the pinball
controllers allow rules to be written to their hardware where we can
set up which coils we'd like to be fired (and with whichsettings) when
switches change state. So part of what the thousands of lines of code
of MPF do behind the scenes is when you set up your flippers in the
`flippers:` section of your config file, it actually writes those
rules out to the hardware controller so the hardware controller can
handle them. These rules are dynamic and updated often. For example
they're deactivated when a game is not in progress, when it tilts, and
(optionally) between balls, and you can change them to do all sorts of
novelty things like inverted flippers, no hold flippers, weak
flippers, etc. By the way, even when you write hardware rules to your
pinball controller, the MPF software still receives notification when
those switches change state. After all, you might want to play a sound
effect or update a score even if the hardware controller fired the
actual coil, and in the case of flipper buttons you need to know when
they're activated forlane changes and to cancel video modes and stuff.
In this case you still have one physical switch in your machine and
one switch configured in your config files—it's just that if you have
a hardware rule configured for a switch then when that switch changes
state, the pinball controller fires the associated coil *in addition*
to sending the switch state change to MPF as usual. You might think
there's a potential issue around timing for this situation. After all,
if the hardware fires the coil instantly but it takes awhile for the
host computer to receive notification and play a sound, doesn't that
mean that the coil action and sound will be out of sync? In theory,
yes, but in practicality we're only talking about a few
milliseconds—much faster than any human can notice. (In fact if you
think about it, sound only travels at about 1 foot per millisecond, so
a typical player standing 4 feet away from the speakers in the backbox
is already hearing everything on a 4ms delay, and of course no human
can notice that, so in this case we're fine.)



What if it doesn't work?
------------------------

If you don't see your switch events in the console when you press your
keys, there are a few things you can try to troubleshoot:


+ Double-check to make sure you actually saved your updated config
  file. :)
+ Make sure no modifier keys (shift, control, etc.) are being pressed
  at the same time. Since there are way more switches in a pinball
  machine than keys on a keyboard, MPF lets you add modified keys to
  your `keyboard:` map. This means that MPF will see `Z`, `SHIFT+Z`,
  `CRTL+Z`, `SHIFT+CTRL+Z`, etc. all as different switches.
+ Remember that the media controller'spop-up window has to be in
  focus. Make sure it's the active window on your desktop and try
  hitting your keys again.
+ Remember that your physical flippers will not flip if you hit the
  keyboard keys for your flipper buttons.




Check out the complete config.yaml file so far
----------------------------------------------

If you want to see a complete `config.yaml` file up to this point,
it’s available in the MPF package at
`<your_mpf_root>/machine_files/tutorial/config/step7.yaml`. (You need
to rename this file to `config.yaml` to use it.) And remember if
you're using physical hardware, your coil and switch numbers will be
different than the ones in the sample file, since you'll need to
configure them based on your driver boards' actual inputs and outputs.

.. _a lot more than just keys: https://missionpinball.com/docs/configuration-file-reference/keyboard/


