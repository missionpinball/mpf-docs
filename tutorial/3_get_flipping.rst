Tutorial step 3: Get flipping!
==============================

There's something exciting about seeing the first flips of your own
pinball machine (whether it's a machine you built from scratch or an
existing machine you're writing custom code for), so in this step we're
going to focus on getting your flippers working.

To do that, you have to add some entries to your config file to tell
MPF about some coils and switches, then you have to group them
together to MPF that they should act like flipper devices. So go ahead
and open the ``config.yaml`` file in the ``/your_machine/config`` folder
that you created in the previous step.


1. Add your flipper switches
----------------------------

The ``switches:`` section of your machine config file is where you list
all the switches in your machine and map physical switch numbers to
more friendly switch names. (This is what makes it possible to interact
with switch names like "left_flipper" and "right_inlane" versus "switch 27"
and "switch 19".)

So on the line after the ``#config_version=4`` entry from the previous
tutorial step, write ``switches:`` (note
the colon). Then on the next line, type four spaces (these must be
spaces, not a tab), and write ``s_left_flipper:``. Then on the next
line, type eight spaces and add ``number:``. Repeat that again for
``s_right_flipper:``.

So now your ``config.yaml`` file should look like this:

::

    #config_version=4

    switches:
        s_left_flipper:
            number:
        s_right_flipper:
            number:

In case you're wondering why we preface each switch name with ``s_``,
that's a little trick we learned that makes things easier as you get
deeper into your configuration. We do this because most text editors
and IDEs have "autocomplete" functions where it will pop up a list to
autocomplete values as you type. So if you preface all your switches
with ``s_`` (and your coils with ``c_``, your lights with ``l_``, etc.),
then as soon as you type "s_" into your YAML file you should get a popup
list with all your switches which you can use to select the right one.
These saves lots of headaches later caused by not entering the name
exactly right somewhere. :)

If you use Sublime as your editor, it just
does this automatically. Other editors might require plugins. (For
example, you can add this functionality to Atom with a free package
called "autocomplete-plus".)

Also, note that most things in MPF config files are case-insensitive.
So what happens internally is MPF converts everything to
lowercase. (Well, not everything. Certain things like labels and text
strings and stuff will be in whatever case you enter them as. But in
general stuff is case insensitive.)

The reason we mention this is
because you can *not* have two things configured with the same name
that only vary based on case sensitivity. For example, the switch
names ``s_lane_trEk`` and ``s_lane_treK`` are not allowed since they'd
both be converted internally to ``s_lane_trek``.

Speaking of formatting files, let's look at a few important things
to know about YAML files (which is the format of the file we're creating
here):

* You you cannot use tabs to indent in YAML . (It is `literally not allowed <http://www.yaml.org/faq.html>`_.)
  Most text editors can be configured to automatically insert spaces when you push the tab key, or you can just
  hit the space bar a bunch of times.
* The exact number of spaces you use for the indents doesn't matter (most people use
  groups of two or four), but what is absolutely important is that all items at the same "level" must be indented
  with the same number of spaces. In other words ``s_left_flipper:`` and ``s_right_flipper:`` need to have the
  same number of spaces in front of them. In a practical sense this shouldn't be a problem, because again most
  text editors let you use the tab key to automatically insert space characters.
* You cannot have a space between the setting name and the colon. GOOD: ``switches:``. BAD: ``switches :``
* Must must have a space after the colon and the setting value. GOOD: ``balls: 3``. BAD: ``balls:3``

This all might seem kind of annoying, but that's just the way it is with YAML files. When we started building
MPF, we weighed the pros and cons of lots of different config file formats (XML, INI, JSON, TOML, text, Python,
etc.), and YAML was the best trade-off in terms of having the features we needed while being the easiest to use.

By the way, at some point we'll create GUI tools you can use to build your configs instead of having to hand-edit
YAML files, but that's probably a few years away, so in the meantime, get used to YAML. :)

2. Enter the hardware numbers for your switches
-----------------------------------------------

The ``config.yaml`` file you have so far is completely valid. However, you'll notice that the ``number:`` setting
for each switch is blank. If you are not using MPF with a physical pinball machine yet, you can keep these
numbers blank. But if you want to control a real pinball machine, you need to enter values for each switch's
``number:`` setting.

The exact number you enter for each switch is dictated by which switch input on your pinball controller each
switch is connected to. Also, different types of pinball controllers use different number formats. (For example,
the P3-ROC with SW-16 switch boards uses a combination of board number and switch number. FAST Pinball controllers
with FAST I/O boards use sequential switch numbers. Controllers retrofitted into WPC machines use the letter "S" or "D"
(for matrix switches or direct switches) followed by the switch number from the table in the machine's operator's
manual.

.. todo:: link to hw-specific docs

::

    switches:
        s_left_flipper:
            number: 0
        s_right_flipper:
            number: 1

Make sure (now and forever) that you've formatted the YAML file
properly, like this:

NOTE: This is as far as I have for the docs. Everything below here is still
for MPF 0.21 that I have not converted yet. So stop here. :)


(C) Add your flipper coils
--------------------------

Next you need to add entries for your flipper coils. These will be
added to a section called `coils:`.If you're using dual-wound coils,
you'll actually have four coil entries here—both the main and hold
coils for each flipper. If you're using single-wound coils, then
you'll only have one coil for each flipper (which we'll configure to
pulse-width modulation for the holds). If you have no idea what we're
talking about, read the `Flippers section of the MPF documentation`_
for an introduction to flipper concepts, dual-wound versus single-
wound, holding techniques, end-of-stroke switches, and a bunch of
other stuff that's important that you probably never thought about. If
you have dual-wound coils, your `coils:` section of the documentation
should look like this:


::


    coils:
        c_flipper_left_main:
            number: 0
        c_flipper_left_hold:
            number: 1
        c_flipper_right_main:
            number: 2
        c_flipper_right_hold:
            number: 3


Again, note each coil name is indented four spaces, and each "number"
listed under them is indented eight spaces, there's no space before
the colons, and there is a space after the colons. Like the switch
numbers, the `number:` entry under each coilis the number that the
pinball hardware controller uses for this coil. The exact number will
depend on P-ROC or FAST and whether you're using their driver boards
and standard Williams boards. (Refer to the ` `coils:` section of our
configuration file reference`_ for more details about coil numbers for
your specific hardware.) Also, again, if you're only using virtual
hardware at this point, you can enter whatever you want for your
numbers. (It's okay if some of your flipper coil numbers are the same
as your switch numbers, since MPF keeps track of coil numbers and
switch numbers separately.)



(D) Add your flipper "devices"
------------------------------

Okay, so now you have your coils and switches defined, but you can't
flip yet because you don't have any flippers defined. Now you might be
thinking, "Wait, but didn't I just configure the coils and switches?"
Yes, you did, but now you have to tell MPF that you want to create a
flipper device which links together one switch and one (or two) coils
to become a "flipper". MPF supports dozens of different types of
`devices`_, which, broadly-speaking, and be broken down into two
classes:


+ There are low level rawhardware devices which you actually connect
  to your pinball controller. These are coils, switches, matrix lights,
  RGB LEDs, flashers, motors, and servos.
+ There are higher-level logical devices which are familiar pinball
  devices, like flippers, pop bumpers, troughs, drop targets, shots,
  etc.All these higher-level devices are logical groupings of the lower
  level devices: a flipper is *this* switch plus *that* coil, a drop
  target is *this* switch and *that* knockdown coil and *this* reset
  coil, etc.


So getting back to the flippers, you create your logical flipper
devices by adding a `flippers:` section to your config file, and then
specifying the switch and coil(s) for each flipper. Here's what you
would create based on the switches and coils we've defined so far:


::


    flippers:
        left_flipper:
            main_coil: c_flipper_left_main
            hold_coil: c_flipper_left_hold
            activation_switch: s_left_flipper
        right_flipper:
            main_coil: c_flipper_right_main
            hold_coil: c_flipper_right_hold
            activation_switch: s_right_flipper




What if your flippers coils only have one winding?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The example in the tutorial above uses dual-wound flipper coils where
MPF literally sees each flipper coil as two separate coils (with two
separate names and two separate drivers). When you push the flipper
button, MPF energizes both coils initially, but cuts the power to the
main coil after a few milliseconds so only the lower power hold coil
remains active. This prevents the flipper coil from burning up. As an
alternative, some flippers just use normal (single winding) coils and
then the hardware controller controls the flow of electricity through
it to prevent it from burning up. In that case the hardware will send
an initial constant pulse for a few milliseconds to give the flipper
its strong initial pulse, and then it will flip the current on & off
really fast (really fast, like hundreds of times per second) to keep
the flipper in the 'up' position without overheating it. If you have
single-wound flipper coils (or if you have traditional dual-wound
coils but you don't want to waste two drivers per flipper and you just
want to use a single winding), make sure you've read `our
documentation on flipper devices`_ for all the details about how that
works. If you'd like to use single-wound flipper coils, you need to do
two things in your config file:


+ First, you can remove the `hold_coil:` entries from your two
  flippers since you don't have hold coils.
+ Second, you need to add a `hold_power:` entry to each of your two
  coils in the `coils:` section of your config file. This is how you
  tell MPF what timing it should use to quickly pulse the current to
  that coil when its being held on.


Here's an example of what the `coils:` and `flippers:` sections of
yourconfig file would look like if you're using single wound coils .
(The `switches:` section would be the same in both cases):


::


    coils:  #P-ROC / P3-ROC only
        c_flipper_left_main:
            number: 0
            pulse_ms: 20
            hold_power: 2
        c_flipper_right_main:
            number: 2
            pulse_ms: 20
            hold_power: 2



::


    flippers:
        left_flipper:
            main_coil: c_flipper_left_main
            activation_switch: s_left_flipper
        right_flipper:
            main_coil: c_flipper_right_main
            activation_switch: s_right_flipper


Note that we used a values of 2 for the *hold_power*. The *hold_power*
setting is a whole number from 0-8 which represent a percentage of
power that's applied when that coil is held on. (0 = 0%, 4=50%,
8=100%, etc.) At this point we have no idea if `hold_power: 2` is the
correct setting or not. We can fine-tune that later. (And again,
*hold_power* is only used with single-wound coils. Dual-wound coils
fire both windows at full power all the time.)



(E) Try running MPF to make sure your config file is ok
-------------------------------------------------------

At this point you should run your game to make sure it runs okay. Your
flippers aren't going to work yet, but mainly we want to make sure MPF
can read your config files and that there aren't any errors. Open a
command prompt, switch to your MPF projectfolder, and run this:


::


    python mpf.py your_machine -v -b


Notice that we have the familiar *-v* option to write a verbose log
file, but we also have a new *-b* option. The *-b* option (which means
"no BCP") tells MPF that it should not try to connect to a media
controller to run a display. We're adding that option for now because
we haven't configured a media controller yet as that's something we'll
get to in a few more steps. When you run this, you'll see some things
loading and a message that your attract mode has started. If you see
this, then congrats! Your config file is okay and your game is
running. It will kind of look like it's hung, but it's not—it's
actually running.


::


    C:\pinball\mpf>python mpf.py c:\pinball\your_machine -v -b
    INFO : Machine : Mission Pinball Framework v0.21.0
    INFO : Machine : Machine config file #1: C:\pinball\your_machine\config\step4
    INFO : Machine : Loading system modules...
    INFO : DeviceManager : Loading devices...
    INFO : Machine : Loading plugins...
    INFO : SwitchController : Dumping current active switches
    INFO : Mode.attract : Mode Starting. Priority: 10
    INFO : Mode Controller : +=========== ACTIVE MODES ============+
    INFO : Mode Controller : | attract : 10                        |
    INFO : Mode Controller : +-------------------------------------+


At this point you can stop it by making sure your console window has
focus and then hitting `CTRL+C`. When you stop it, you'll see a few
more lines appear on the console which have information about the
"target" and "actual" game loop rates. By default MPF is configured to
run at 30 loops (or "ticks") per second, and hopefully you should see
your actual loop rate somewhere in that neighborhood, like this:


::


    INFO : Machine : Target MPF loop rate: 30 Hz
    INFO : Machine : Actual MPF loop rate: 30.0 Hz
    INFO : Machine : Hardware loop rate: 63.98 Hz
    INFO : root : MPF run loop ended.




Potential errors and how to fix them
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If your game ran fine, then you can skip down to Section(F) below. If
something didn't work then there are a few things to try depending on
what your error was. If the last line in your console output is *
AssertionError: Device 'x' does not have a valid config *, that means
that device entry in your config file isn't right. Probably this is
caused by incorrect indentation errors. If the last line in your
console output is * AssertionError: Device 'x' has an empty config *,
that means the device entry in your config file doesn't have any sub-
sections under it (like you're missing the *number:* setting, for
example). If the last line in your console output is * CRITICAL: YAML
File Interface: Error found in config file 'x'. Line x, Position x *,
that means you have a formatting problem with your YAML file. The line
and position numbers will get you close to finding where the problem
is, but they're never exactly right because most formatting errors in
YAML files actually affect how the YAML processor sees the file, so
it's reporting what it saw based on your error. The big "gotchas" with
YAML files are:


+ Be sure to indent with spaces, not tabs
+ Make sure that all the "child" elements are indented the same. So
  your `s_left_flipper` and `s_right_flipper` both need to be indented
  the same number of spaces, etc.
+ Make sure you *do not* have aspace *before* each colon.
+ Make sure you *do* have a space *after* each colon.
+ Make sure you have the `#config_version=3` as the first line in your
  file.




(F)Enabling your flippers
-------------------------

Just running MPF with your game's config fileisn't enough to get your
flippers working. By default, they are only turned on when a ball
starts, and they automatically turn off when a ball ends. But the
basic config file doesn't have a start button or your ball trough or
plunger lange configured, so you can't actually start a game yet. So
in order to get your flippers working, we need to add a configuration
into each flipper's entry in your config file that tells MPF that we
just want to enable your flippers right away, without an actual game.
(This is just a temporary setting that we'll remove later.) To do
this, add the following entry to each of your flippers in your config
file:


::


    enable_events: machine_reset_phase_3


We'll cover exactly what this means later on. (Basically it's telling
each of your flippers that they should enable themselves once the
initial initialization phase is done, rather then them waiting for a
ball to start.) So now the `flippers`: section of your config file
should look like this:


::


    flippers:
        left_flipper:
            main_coil: c_flipper_left_main
            hold_coil: c_flipper_left_hold
            activation_switch: s_left_flipper
            enable_events: machine_reset_phase_3
        right_flipper:
            main_coil: c_flipper_right_main
            hold_coil: c_flipper_right_hold
            activation_switch: s_right_flipper
            enable_events: machine_reset_phase_3


Atthis point the rest of the steps on this page are for getting your
physical machine connected to your pinball controller. If you don't
have a physical machine yet then you can skip directly to `Step 6: Add
a display`_.



(G) Configure MPF to use your FAST, P-ROC, or P3-ROC Controller
---------------------------------------------------------------

Ifyou have a physical pinball machine (or at least a something on your
workbench) which is hooked up to a FAST, P-ROC, or a P3-ROC Pinball
controller, then you need to add the hardwareinformation to your
config file so MPF knows which platform interface to use and how to
talk to your hardware. To configure MPF to use a hardware pinball
controller, you need to add a `hardware:` section to your config file,
and then you add settings for `platform:` and `driverboards:`. Some
hardware platforms requireadditional settings for ports and stuff too.
Let's look at the specifics depending on your hardware platform.



If you're using a P-ROC:
~~~~~~~~~~~~~~~~~~~~~~~~

If you're using MPF with a P-ROC,simply add the entry ` platform:
p_roc ` in your ` hardware: ` section. (This is for a P-ROC only.
Instructions for the P3-ROC are in the next section.) For the driver
boards, you have the option to use either the P-ROC driver boards
(like the PD-16), or existing WPC or Stern driver boards (like if
you're plugging your P-ROC into an existing machine). For this
tutorial you can use use either. If you want to use P-ROC driver
boards, you add an entry ` driverboards: pdb `. If you want to use WPC
driver boards with an existing machine, you add the entry `
driverboards: wpc `. And if you want to use MPF on a Stern S.A.M.
machine, you add the entry ` driverboards: sternSAM `. So the
`hardware:` section you add to your config file will look like this:


::


    hardware:
        platform: p_roc
        driverboards: pdb


Or like this:


::


    hardware:
        platform: p_roc
        driverboards: wpc


Or like this:


::


    hardware:
        platform: p_roc
        driverboards: sternSAM




If you're using a P3-ROC:
~~~~~~~~~~~~~~~~~~~~~~~~~

For the P3-ROC, everything is the same as the P-ROC above, except you
use `p3_roc` for your platform. (And of course you'duse `pdb` for the
driver boards since the P3-ROC doesn't support other types.)



If you're using a FAST Pinball controller:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To use MPF with a FAST Pinball controller, you add an entry `
platform: fast ` to the ` hardware: ` section of your config file.
FAST Pinball controllers also have the option of either working with
either WPC or FAST driver boards, so you need to add the configuration
entry ` driverboards: fast ` or ` driverboards: wpc `, depending on
what you have. When using a FAST Controller, the `hardware:` section
of your config file will either look like this:


::


    hardware:
        platform: fast
        driverboards: fast


Or like this:


::


    hardware:
        platform: fast
        driverboards: wpc


FAST Controllers also require that MPF is configured for the serial
port and baud rate. This is done via a section in the config file
called `fast:` which will look like this:


::


    fast:
        ports: com3, com4, com5


If you're using a FAST controller, the above section will be 100%
accurate for you except for the names of the ports. You'll have to
change those to the actual port names that the FAST controller uses on
your system. If you don't know the name of the ports, read the
`ports:`section of `our configuration file reference for FAST`_ for
instructions on how to figure out which port it's using. (Basically
just plug in your FAST controller and look for the four COM ports that
pop up, and then add the first three for a FAST Core or WPC
controller, and the middle two for a FAST Core controller.) If you're
using a FAST controller, you'll end up adding both `hardware:` and
`fast:` sections to your config file, like this:


::


    hardware:
        platform: fast
        driverboards: wpc
    fast:
        ports: COM3, COM4, COM5




(H) Make sure you have your hardware drivers installed
------------------------------------------------------

Just like any peripheral you plug into a computer, you need install
drivers and the interface software before your computer can talk to a
hardware pinball controller. You should have gotten the drivers
installed when you originally setup MPF, but if you started with no
hardware and you're adding it now, go back to the `installation
documentation`_ and read the section for your platform to get the
drivers installed.



(I) One last check before powering up
-------------------------------------

Okay, now we're really close to flipping. Before you proceed take a
look at your config file to make sure everything looks good. It should
look something like this one, though of course that will depend on
what platform you're using, whether you have dual-wound or single-
wound flipper coils, and what type of driver boards you have (which
will affect your coil and switch numbers). But here's the general
idea. (This is the exact file we use with a P-ROC plugged into an
existing *Demolition Man* machine.)


::


    #config_version=3

    hardware:
        platform: fast
        driverboards: wpc

    switches:
        s_left_flipper:
            number: SF4
        s_right_flipper:
            number: SF6

    coils:
        c_flipper_left_main:
            number: FLLM
        c_flipper_left_hold:
            number: FLLH
        c_flipper_right_main:
            number: FLRM
        c_flipper_right_hold:
            number: FLRH

    flippers:
        left_flipper:
            main_coil: c_flipper_left_main
            hold_coil: c_flipper_left_hold
            activation_switch: s_left_flipper
            enable_events: machine_reset_phase_3
        right_flipper:
            main_coil: c_flipper_right_main
            hold_coil: c_flipper_right_hold
            activation_switch: s_right_flipper
            enable_events: machine_reset_phase_3


Note that the individual sections of the config file can be in any
order. Weput the `hardware:` section atthe top, but that's just our
personal taste. It really makes no difference.



(J) Running your game and flipping!
-----------------------------------

At this point you're ready to run your game, and you should be able to
flip your flippers! Run your game with the following command:


::


    python mpf.py your_machine -v -b


Watch the console log for the following entry:


::


    INFO : Mode Controller : +=========== ACTIVE MODES ============+
    INFO : Mode Controller : | attract : 10                        |
    INFO : Mode Controller : +-------------------------------------+


Once you see that then you should be able to hit your flipper buttons
and they should flip as expected! You might notice that your flippers
seem weak. That's okay. The default flipper power settings are weak
just to be safe. We'll show you how to adjust your flipper power
settings in the next step of this tutorial. You'll also notice that
switch events are posted to the console. `State:1` means the switch
flipped from inactive to active, and `State:0` means it flipped from
active to inactive.


::


    INFO : SwitchController : <<<<< switch: s_left_flipper, State:1 >>>>>
    INFO : SwitchController : <<<<< switch: s_left_flipper, State:0 >>>>>
    INFO : SwitchController : <<<<< switch: s_right_flipper, State:1 >>>>>
    INFO : SwitchController : <<<<< switch: s_right_flipper, State:0 >>>>>


Here's a companion video which shows running your game at this point
in the tutorial based on the config file above: (Note that this
companion video is showing *Judge Dredd*, but we're using *Demolition
Man* as our sample machine in this tutorial. That's okay since
everything is basically the same. The only difference is the actual
outputs that are configured for the switch and coil connections.)
https://www.youtube.com/watch?v=SkxZxkHHmXw



What if it doesn't work?
------------------------

If your game doesn't flip while you're running this code, there are a
few things it could be: If the game software runs but you don't have
any flipping, check the following:


+ Make sure you're *not* using the `-x` command line option, since
  that tells MPF to run in software-only mode meaning it won't talk to
  your actual physical hardware.
+ Verify that your switch and coil numbers are set properly. Remember
  the values of "0" and "1" and stuff that we used here are just for the
  sake of this tutorial. In real life your coil numbers are going to be
  something like "A8" or "FLLH" or "C15" or "A1-B0-7", and your switches
  will be something more like "E5" or "0/4" or "SD12". Again look at our
  configuration file reference for both `coils`_ and `switches`_ for
  explanations of all the different options for the `number:` setting
  depending on what type of hardware, driver boards, and connections you
  have in your physical machine.
+ Make sure you added `enable_events: machine_reset_phase_3` to each
  of your flipper configurations.
+ Make sure you don't have a typo in your config file. (For example,
  `flipper:` instead of `flippers:`, etc.) Search throughthe log file
  (in verbose mode) for your flipper names to make sure they're being
  created and activated.
+ Make sure your coin door is closed! If you're running MPF on an
  existing Williams or Stern machine, remember that when the coin door
  is open, there's a switch that cuts off the power to the coils. (Ask
  us how we knew to add this to the list. :)
+ It's possible that your flippers are working, but their power level
  is so low that they're not actually moving. (In this case you might
  hear them click when you hit the flipper button.) In this case you can
  move on to the next step in the tutorial where we adjust the flipper
  power.


If the game software crashes or gives an error:


+ If you're using a P-ROC and you get a bunch of really fast messages
  about `Error opening P-ROC device` and `Failed, trying again...`, this
  is because (1)your pinball machine is not turned on, (2) your P-ROC is
  not connected to your computer (via USB), or (3) you have a problem
  with the P-ROC drivers. If you're running MPF in a virtual machine,
  make sure the USB connection is set to go to the VM.
+ If you're using a P-ROC and you get an error `ImportError: No module
  named pinproc`, that means you either (1) don't have the P-ROC drivers
  installed, or (2) you have multiple instances of Python on your
  computer and you installed the drivers into one and you're running MPF
  from the other. `Post to the forum`_ and we can help sort it out.
+ If you get an with the name of something not being valid from your
  config file, that probably means that you mistyped something. For
  example if you mistype one of your switch or coil names in your
  `flippers:` section, then there will be an error when the game tries
  to enable the flippers since one of those names doesn't point back to
  a real switch or coil in your machine.


If a flipper gets stuck on :


+ Really this shouldn't happen. :) But it did on our machine just now
  and we really really confused. :) It turns out it was our flipper
  button which was stuck in the "on" position. (The *Judge Dredd*
  machine we were using at the time had those aftermarket magnetic
  sensor buttons with the little magnets on the button flags, and one of
  them came unglued and slipped out of alignment, making the switch
  stuck in the "on" position.)


If you're still running into trouble, feel free to post to our `MPF
users forum`_. We'll incorporate your issues into this tutorial to
make it easier for everyone in the future!


.. _MPF users forum: https://missionpinball.com/forum/f/mpf-users/
.. _Atom: https://atom.io/
.. _JetBrains: https://www.jetbrains.com/
.. _our configuration file reference for FAST: https://missionpinball.com/docs/configuration-file-reference/fast/
.. _Step 6: Add a display: https://missionpinball.com/docs/tutorial/add-a-display/
.. _installation documentation: https://missionpinball.com/docs/installing-mpf/
.. _Post to the forum: /forum
.. _PyCharm: https://www.jetbrains.com/pycharm/


