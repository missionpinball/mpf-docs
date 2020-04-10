Tutorial step 3: Get flipping!
==============================

There's something exciting about seeing the first flips from your
own code, so in this step we're going to focus on getting your flippers working.

To do that, you have to add some entries to your config file to tell
MPF about some coils and switches, then you have to group them
together to tell MPF that they should act like flipper devices. So go ahead
and open that ``/config/config.yaml`` file that you created in the previous step.

1. Add your flipper switches
----------------------------

The ``switches:`` section of your machine config file is where you list
all the switches in your machine and map physical switch numbers to
more friendly switch names. (This is what makes it possible to interact
with switch names like "left_flipper" and "right_inlane" versus "switch 27"
or "switch 19".)

So on the line after the ``#config_version=5`` entry from the previous
tutorial step, write ``switches:`` (note
the colon). Then on the next line, type four spaces (these must be
spaces, not a tab), and write ``s_left_flipper:``. Then on the next
line, type eight spaces and add ``number:``. Repeat that again for
``s_right_flipper:``.

So now your ``config.yaml`` file should look like this:

.. code-block:: mpf-config

   #config_version=5

   switches:
     s_left_flipper:
       number:
       tags: left_flipper
     s_right_flipper:
       number:
       tags: right_flipper

In case you're wondering why we preface each switch name with "s\_",
that's a little trick we learned that makes things easier as you get
deeper into your configuration. We do this because most text editors
and IDEs have "autocomplete" functions where it will pop up a list to
autocomplete values as you type. So if you preface all your switches
with "s\_" (and your coils with "c\_", your lights with "l\_", etc.),
then as soon as you type "s\_" into your YAML file you should get a popup
list with all your switches which you can use to select the right one.
These saves lots of headaches later caused by not entering the name
exactly right somewhere. :)

If you use Sublime as your editor, it just
does this automatically. Other editors might require plugins. (For
example, you can add this functionality to Atom with a free package
called "autocomplete-plus".)

Notice that we added tags called ``left_flipper`` and ``right_flipper``.
These are optional, but recommended. The reason is that MPF includes
a :doc:`combo switch </game_logic/combo_switches/index>` feature which
posts events when player switches are held in combination. If you add
these tags to your flipper switches, an event called *flipper_cancel*
will be posted when the player hits both flipper buttons at the same time
which you can use to cancel shows and other things you want the player to
be able to skip.

When naming your switches (and most devices in MPF), your name can't start
with a number and it should only be a combination of letters, numbers, and
underscores.

Also, the names you enter here are the internal names that you'll use for these switches
in your game code and configuration file. When it comes time to create
"friendly" names for these switches which you'll expose via the
service menu, you can create plain-English labels with spaces and
capitalization everything. But that comes later.

In pre-0.50 versions, MPF was not case-sensitive and would internally convert most
things to lowercase before comparison. This proved to be problematic, so MPF is
now case-sensitive for all elements of your config files. Our configuration directives
use only lowercase letters, underscores, and numbers. While you are free to format
your tags as you wish, be aware that case-consistency is now required.

Speaking of formatting files, let's look at a few important things
to know about YAML files (which is the format of the file we're creating
here):

* You cannot use tabs to indent in YAML. (It is `literally not allowed <http://www.yaml.org/faq.html>`_.)
  Most text editors can be configured to automatically insert spaces when you push the tab key, or you can just
  hit the space bar a bunch of times.
* The exact number of spaces you use for the indents doesn't matter (most people use
  groups of two or four), but what is absolutely important is that all items at the same "level" must be indented
  with the same number of spaces. In other words ``s_left_flipper:`` and ``s_right_flipper:`` need to have the
  same number of spaces in front of them. In a practical sense this shouldn't be a problem, because again most
  text editors let you use the tab key to automatically insert space characters.
* You cannot have a space between the setting name and the colon. GOOD: ``switches:``. BAD: ``switches :``
* You must must have a space after the colon and the setting value. GOOD: ``balls: 3``. BAD: ``balls:3``
* Anything on a line following a hash sign ``#`` is ignored, so you can use this to add comments and notes to yourself.

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
switch is connected to. However, different controllers use different number formats.

The :doc:`/hardware/numbers` guide explains how hardware numbering works on each of the various hardware platforms MPF
supports, so check that out now and enter your real numbers, not the made-up
ones we use below.

.. code-block:: mpf-config

   switches:
     s_left_flipper:
       number: 0  # this can be blank if you don't have physical hw yet
     s_right_flipper:
       number: 1  # if you do have physical hw, most likely your number will be different

3. Add your flipper coils
-------------------------

Next you need to add entries for your flipper coils. These will be
added to a section called ``coils:``. If you're using dual-wound coils,
you'll actually have four coil entries here—-both the main and hold
coils for each flipper. If you're using single-wound coils, then
you'll only have one coil for each flipper (which we'll configure to
pulse-width modulation for the holds).

If you have no idea what we're talking about, read our
:doc:`/mechs/flippers/index` documentation
for an introduction to flipper concepts, dual-wound versus single-
wound, holding techniques, end-of-stroke switches, and a bunch of
other stuff that's important that you probably never thought about.

Here's an example of how you'd enter your coils for a machine with two
dual-wound coils. If you have single-wound coils, or you have more than
two flippers, refer to the :doc:`/mechs/flippers/index` documentation for
examples of how to configure them.

.. code-block:: mpf-config

   coils:
     c_flipper_left_main:
       number: 0  # again, these numbers will probably be different for you
     c_flipper_left_hold:
       number: 1  # check your platform-specific documentation for the actual numbers
       allow_enable: true
     c_flipper_right_main:
       number: 2
     c_flipper_right_hold:
       number: 3
       allow_enable: true

Again, note each coil name is indented four spaces, and each "number"
listed under them is indented eight spaces, there's no space before
the colons, and there is a space after the colons. Like the switch
numbers, the ``number:`` entry under each coil is the number that the
pinball hardware controller uses for this coil. The exact number will
depend on what type of controller hardware and driver boards you're using.

Also note that the two hold coils have ``allow_enable:`` entries added, with values of "true".
Anyway, the purpose of the ``allow_enable:`` setting is that as a safety precaution, MPF does not allow you to enable
(that is, to hold a coil in its "on" position) unless you specifically add ``allow_enable: true`` to that coil's config.
This will help to prevent some errant config from enabling a coil that you didn't mean to enable and burning it up or
starting a fire.

So in the case of your flippers, the "hold" coil of a flipper needs to have ``allow_enable: true`` since in order for it
to act as a flipper, that coil need to be allowed to be enabled (held on).

4. Add your flipper "devices"
-----------------------------

Okay, you have your coils and switches defined, but you can't
flip yet because you don't have any flippers defined. Now you might be
thinking, "Wait, but didn't I just configure the coils and switches?"
Yes, you did, but now you have to tell MPF that you want to create a
flipper device which links together one switch and one (or two) coils
to become a "flipper". MPF supports dozens of different types of
:doc:`/mechs/index`, some of which (like flippers), are created
by combining other devices.

You create your flipper devices by adding a ``flippers:`` section to
your config file, and then specifying the switch and coil(s) for each flipper.
Since the flippers belong to a playfield we also create this now.
Here's what you would create based on the switches and coils we've defined so far:

.. code-block:: mpf-config

    #! switches:
    #!   s_left_flipper:
    #!     number: 0
    #!   s_right_flipper:
    #!     number: 1
    #! coils:
    #!   c_flipper_left_main:
    #!     number: 0
    #!   c_flipper_left_hold:
    #!     number: 1
    #!     allow_enable: true
    #!   c_flipper_right_main:
    #!     number: 2
    #!   c_flipper_right_hold:
    #!     number: 3
    #!     allow_enable: true
    playfields:
      playfield:
        tags: default
        default_source_device: None  # use None in steps before 8

    flippers:
      left_flipper:
        main_coil: c_flipper_left_main
        hold_coil: c_flipper_left_hold
        activation_switch: s_left_flipper
      right_flipper:
        main_coil: c_flipper_right_main
        hold_coil: c_flipper_right_hold
        activation_switch: s_right_flipper

5. Try running MPF to make sure your config file is ok
------------------------------------------------------

At this point you should run your game to make sure it runs okay. Your
flippers aren't going to work yet, but mainly we want to make sure MPF
can read your config files and that there aren't any errors. Open a
command prompt, switch to your machine folder, and run MPF again (like
Step 2), also with the ``-b`` option.
Additionally, we will add the ``-t`` option to disable the text UI and show
the log on the console instead (you can also see it inside the ``logs`` folder
inside your machine):

.. code-block:: doscon

    $ mpf -t -b

The console output will look similar to Step 2 as well, and it won't
look like much is happening here. The main thing is to make sure that
MPF starts and runs without giving you any errors--meaning that everything
you setup in your config file is ok.

.. code-block:: doscon

   $ mpf -t -b
   INFO : root : Loading config.
   INFO : YamlMultifileConfigLoader : Machine config file #1: config.yaml
   INFO : ConfigProcessor : Loading config from cache: /tmp/7146c817793475fbeb8d22f907d7bbbc.mpf_cache
   INFO : ConfigProcessor : Loading config from cache: /tmp/49091ea856e626b51c4160f53a2ef744.mpf_cache
   INFO : ConfigProcessor : Loading config from cache: /tmp/4cc7d3d11df84bb81fda7943558aba56.mpf_cache
   INFO : Machine : Mission Pinball Framework Core Engine v0.54.0-dev.18
   INFO : Machine : Command line arguments: {'no_load_cache': False, 'create_config_cache': True, 'bcp': False, 'configfile': ['config.yaml'], 'force_assets_load': False, 'jsonlogging': False, 'logfile': 'logs/2020-04-01-21-45-55-mpf.log', 'pause': False, 'production': False, 'text_ui': False, 'loglevel': 15, 'consoleloglevel': 20, 'force_platform': None, 'syslog_address': None, 'mc_file_name': None, 'no_sound': False}
   INFO : Machine : MPF path: /pinball/src/mpf/mpf
   INFO : Machine : Machine path: /mpf-examples/tutorial/step_3
   INFO : Machine : Platform: linux
   INFO : Machine : Python executable location: /usr/bin/python3
   INFO : Machine : Python version: 3.6.9 (64-bit)
   INFO : Machine : Initialise MPF.
   INFO : EventManager : Event: ======'machine_var_credits_string'====== Args={'value': 'FREE PLAY', 'prev_value': None, 'change': True}
   INFO : EventManager : Event: ======'machine_var_mpf_version'====== Args={'value': 'MPF v0.54.0-dev.18', 'prev_value': None, 'change': True}
   INFO : EventManager : Event: ======'machine_var_mpf_extended_version'====== Args={'value': 'MPF v0.54.0-dev.18, Config version:5, Show version: 5, BCP version:1.1', 'prev_value': None, 'change': True}
   INFO : EventManager : Event: ======'machine_var_python_version'====== Args={'value': '3.6.9', 'prev_value': None, 'change': True}
   INFO : EventManager : Event: ======'machine_var_platform'====== Args={'value': 'Linux-4.15.0-72-generic-x86_64-with-Ubuntu-18.04-bionic', 'prev_value': None, 'change': True}
   INFO : EventManager : Event: ======'machine_var_platform_system'====== Args={'value': 'Linux', 'prev_value': None, 'change': True}
   INFO : EventManager : Event: ======'machine_var_platform_release'====== Args={'value': '4.15.0-72-generic', 'prev_value': None, 'change': True}
   INFO : EventManager : Event: ======'machine_var_platform_version'====== Args={'value': '#81-Ubuntu SMP Tue Nov 26 12:20:02 UTC 2019', 'prev_value': None, 'change': True}
   INFO : EventManager : Event: ======'machine_var_platform_machine'====== Args={'value': 'x86_64', 'prev_value': None, 'change': True}
   INFO : EventManager : Event: ======'init_phase_1'====== Args={}
   INFO : EventManager : Event: ======'init_phase_2'====== Args={}
   INFO : EventManager : Event: ======'init_phase_3'====== Args={}
   INFO : EventManager : Event: ======'init_phase_4'====== Args={}
   INFO : EventManager : Event: ======'machine_var_audits_switches_s_left_flipper'====== Args={'value': 0, 'prev_value': None, 'change': True}
   INFO : EventManager : Event: ======'machine_var_audits_switches_s_right_flipper'====== Args={'value': 0, 'prev_value': None, 'change': True}
   INFO : EventManager : Event: ======'init_phase_5'====== Args={}
   INFO : EventManager : Event: ======'init_done'====== Args={}
   INFO : EventManager : Event: ======'machine_reset_phase_1'====== Args={}
   INFO : EventManager : Event: ======'machine_reset_phase_2'====== Args={}
   INFO : EventManager : Event: ======'machine_reset_phase_3'====== Args={}
   INFO : EventManager : Event: ======'reset_complete'====== Args={}
   INFO : EventManager : Event: ======'mode_attract_will_start'====== Args={}
   INFO : EventManager : Event: ======'mode_attract_starting'====== Args={}
   INFO : Mode.attract : Started. Priority: 10
   INFO : EventManager : Event: ======'mode_attract_started'====== Args={}
   INFO : EventManager : Event: ======'collecting_balls_complete'====== Args={}
   INFO : Machine : Starting the main run loop.

At this point you can stop it by making sure your console window has
focus and then hitting ``CTRL+C``.

What if it didn't work?
~~~~~~~~~~~~~~~~~~~~~~~

If your game ran fine, then you can skip down to Step 6 below. If
something didn't work or you got an error, then there are a few things
to try depending on what your error was.

If the last line in your console output was something like this:

.. code-block:: python

  ValueError: Found a "switchs:" section in config file C:\your_machine\config\config, but that section is not valid in machine config files.

That means that it found a section in your config file that is not valid. Most likely this is due to a typo. For example,
the above example has "switchs" instead of "switches".

Or maybe the error is more like this:

.. code-block:: python

   AssertionError: Config validation error: Entry flippers:left_flipper:main_coil:c_fliper_left_main is not valid.

This is showing that the ``flippers:left_flipper:main_coil:c_fliper_left_main`` entry is not valid. Again this is a
typo--the coil name is spelled wrong (one "p" in flipper instead of two).

Or something like this:

.. code-block:: python

   AssertionError: Your config contains a value for the setting "flippers:left_flipper:holdcoil", but this is not a valid setting name.

Again pretty self-explanatory.  The setting ``flippers:left_flipper:holdcoil`` is not valid. (It should actually be
"hold_coil", not "holdcoil".)

So you can see that we've tried to be pretty helpful when it comes to typos and config file errors. The trick it just to
read through the output in the logs and to trace down what they're complaining about.

You might also get errors saying there's some kind of YAML problem. For example, if you remove the colon after the
``coils:`` section and re-run MPF, you get the following error:

.. code-block:: python

   ValueError: YAML error found in file /Users/brian/git/mpf-examples/tutorial/config/config.yaml. Line 16, Position 24

Line 16, Position 24. Pretty straightforward, except the missing colon is actually on line 15. This is because removing
the colon still produced valid YAML until it hit the next line. The point is that if you get a YAML error, look a few
lines above and below the line number from the error.

Again, recapping the rules of YAML:

+ Be sure to indent with spaces, not tabs.
+ Make sure that all the "child" elements are indented the same. So
  your ``s_left_flipper`` and ``s_right_flipper`` both need to be indented
  the same number of spaces, etc.
+ Make sure you *do not* have a space *before* each colon.
+ Make sure you *do* have a space *after* each colon.
+ Make sure you have the ``#config_version=5`` as the first line in your file.

If you struggle to spot the problem read our
:doc:`/troubleshooting/debugging_yaml_parse_errors` guide.

6. Enabling your flippers
-------------------------

Just running MPF with your game's config file isn't enough to get your
flippers working. By default, they are only turned on when a ball
starts, and they automatically turn off when a ball ends. But the
simple config file we just created doesn't have a start button or your ball trough or
plunger lane configured, so you can't actually start a game yet. So
in order to get your flippers working, we need to add a configuration
into each flipper's entry in your config file that tells MPF that we
just want to enable your flippers right away, without an actual game.
(This is just a temporary setting that we'll remove later.) To do
this, add the following entry to each of your flippers in your config
file:

.. code-block:: yaml

   enable_events: machine_reset_phase_3

We'll cover exactly what this means later on. (Basically it's telling
each of your flippers that they should enable themselves when MPF is booting up, rather than them waiting for a
ball to start.) So now the ``flippers:`` section of your config file should look like this: (If you have single-wound
coils, then you won't have the ``hold_coil:`` entries here.)

.. code-block:: mpf-config

   #! switches:
   #!   s_left_flipper:
   #!     number: 0
   #!   s_right_flipper:
   #!     number: 1
   #! coils:
   #!   c_flipper_left_main:
   #!     number: 0
   #!   c_flipper_left_hold:
   #!     number: 1
   #!     allow_enable: true
   #!   c_flipper_right_main:
   #!     number: 2
   #!   c_flipper_right_hold:
   #!     number: 3
   #!     allow_enable: true
   #! playfields:
   #!   playfield:
   #!     tags: default
   #!     default_source_device: None  # use None in steps before 8
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

At this point the rest of the steps on this page are for getting your
physical machine connected to your pinball controller. If you don't
have a physical machine yet then you can skip directly to :doc:`/tutorial/4_adjust_flipper_power`.

7. Configure MPF to use your physical pinball controller
--------------------------------------------------------

If you have a physical pinball machine (or at least a something on your
workbench) which is hooked up to a FAST, P-ROC, P3-ROC, OPP, or Stern SPIKE
controller, then you need to add the hardware information to your
config file so MPF knows which platform interface to use and how to
talk to your hardware. To configure MPF to use a hardware pinball
controller, you need to add a ``hardware:`` section to your config file,
and then you add settings for ``platform:`` and ``driverboards:``.

Remember earlier in this step, we provided links to the documentation for
each platform. Here they are again:

* :doc:`FAST Pinball </hardware/fast/index>`
* :doc:`Multimorphic P-ROC/P3-ROC </hardware/multimorphic/index>`
* :doc:`Open Pinball Project (OPP) </hardware/opp/index>`
* :doc:`Stern SPIKE </hardware/spike/index>`
* :doc:`LISY </hardware/lisy/index>`

You only need look at those docs for the specifics parts of the config that
vary depending on your hardware. The good news is that 99.9% of the MPF
config files are identical regardless of the hardware you're using.

Here are some various examples of different types of hardware configs. Please
understand that these are just some examples! Do not copy them for your own
use, rather, follow the instructions from the bullet list above.

FAST Pinball with FAST IO driver boards:

.. code-block:: mpf-config

   hardware:
     platform: fast
     driverboards: fast

   fast:
     ports: com4, com5

   switches:
     s_left_flipper:
       number: 00

P-ROC installed in an existing WPC machine:

.. code-block:: mpf-config

   hardware:
     platform: p_roc
     driverboards: wpc

   switches:
     s_left_flipper:
       number: SF2

P3-ROC with P-ROC driver & switch boards:

.. code-block:: mpf-config

   hardware:
     platform: p3_roc
     driverboards: pdb

   switches:
     s_left_flipper:
       number: 0-0

In case you are using :doc:`the Virtual Pinball (VPX) Platform </hardware/virtual/virtual_pinball_vpx>` the config file will look like:

.. code-block:: mpf-config

    hardware:
      platform: virtual_pinball

    switches:
      s_sling:
        number: 0
      s_flipper:
        number: 3

    coils:
      c_sling:
        number: 0
      c_flipper:
        number: 1
        allow_enable: true


See? They're all different.

7a. Understand the "virtual" hardware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you just added a ``platform:`` setting to your config file which specifies a physical hardware platform, now every
time you run MPF with that config, it will try to connect to the physical hardware. But what happens if you want to use
MPF without your physical pinball hardware attached? In that case, you can run MPF with either the ``-x`` or ``-X``
command line options. (Lowercase "x" is the "virtual" platform, and uppercase "X" is the "smart virtual" platform.)

We'll talk more about those later. The point is that if you have configured your machine for physical hardware and then
you want to run MPF without the physical hardware, you need to add either ``-x`` or ``-X`` to your ``mpf`` command when
you run it.

8. One last check before powering up
------------------------------------

Okay, now we're really close to flipping. Before you proceed take a
look at your config file to make sure everything looks good. It should
look something like this one, though of course that will depend on
what platform you're using, whether you have dual-wound or single-
wound flipper coils, and what type of driver boards you have (which
will affect your coil and switch numbers). But here's the general
idea. (This is the exact file we use with a FAST WPC controller plugged into an
existing *Demolition Man* machine.)

.. code-block:: mpf-config

   #config_version=5

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
       allow_enable: true
     c_flipper_right_main:
       number: FLRM
     c_flipper_right_hold:
       number: FLRH
       allow_enable: true

   playfields:
     playfield:
       tags: default
       default_source_device: None  # use None in steps before 8

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
order. We put the ``hardware:`` section at the top, but that's just our
personal taste. It really makes no difference.

9. Running your game and flipping!
----------------------------------

At this point you're ready to run your game, and you should be able to
flip your flippers! Run your game with the following command:

.. code-block:: doscon

    C:\your_machine\mpf -t -b

Watch the console log for the entry about the attract mode starting.
Once you see that then you should be able to hit your flipper buttons
and they should flip as expected! You might notice that your flippers
seem weak. That's okay. The default flipper power settings are weak
just to be safe. We'll show you how to adjust your flipper power
settings in the next step of this tutorial. You'll also notice that
switch events are posted to the console. ``State:1`` means the switch
flipped from inactive to active, and ``State:0`` means it flipped from
active to inactive.

::

    INFO : SwitchController : <<<<< switch: s_left_flipper, State:1 >>>>>
    INFO : SwitchController : <<<<< switch: s_left_flipper, State:0 >>>>>
    INFO : SwitchController : <<<<< switch: s_right_flipper, State:1 >>>>>
    INFO : SwitchController : <<<<< switch: s_right_flipper, State:0 >>>>>

Here's a companion video which shows running your game at this point
in the tutorial based on the config file above: (Note that this
companion video is showing *Judge Dredd*, and it's based on an older
version of MPF, but the basic concepts are the same.)

https://www.youtube.com/watch?v=SkxZxkHHmXw

What if it doesn't work?
------------------------

If your game doesn't flip while you're running this config, there are a
few things it could be: If the game software runs but you don't have
any flipping, check the following:

+ Make sure you're *not* using the ``-x`` or ``-X`` command line options, since
  those tells MPF to run in with the "virtual" hardware (e.g. software-only) mode meaning it won't talk to
  your actual physical hardware.
+ Verify that your switch and coil numbers are set properly. Remember
  the values of "0" and "1" and stuff that we used here are just for the
  sake of this tutorial. In real life your coil numbers are going to be
  something like ``A8`` or ``FLLH`` or ``C15`` or ``A1-B0-7``, and your switches
  will be something more like ``E5`` or ``0/4`` or ``SD12``. Again look the how
  to guides for your specific platform for details on how their numbers should
  be set.
+ Make sure you added ``enable_events: machine_reset_phase_3`` to each
  of your flipper configurations.
+ Make sure your coin door is closed! If you're running MPF on an
  existing Williams or Stern machine, remember that when the coin door
  is open, there's a switch that cuts off the power to the coils. (Ask
  us how we knew to add this to the list. :)
+ It's possible that your flippers are working, but their power level
  is so low that they're not actually moving. (In this case you might
  hear them click when you hit the flipper button.) In this case you can
  move on to the next step in the tutorial where we adjust the flipper
  power.

If MPF crashes or gives an error:

+ If you're using a P-ROC and you get a bunch of really fast messages
  about `Error opening P-ROC device` and `Failed, trying again...`, this
  is because (1) your pinball machine is not turned on, (2) your P-ROC is
  not connected to your computer (via USB), or (3) you have a problem
  with the P-ROC drivers. If you're running MPF in a virtual machine,
  make sure the USB connection is set to go to the VM.
+ If you're using FAST or OPP hardware and you get an error about a port
  configuration, or not being able to open a port, then make sure your
  port numbers are correct. If you were previously connecting to one of
  those ports via a terminal emulator, make sure you've disconnected from
  the port in that software before running MPF.

If a flipper gets stuck on:

+ Really this shouldn't happen. :) But it did on our machine just now
  and we really really confused. :) It turns out it was our flipper
  button which was stuck in the "on" position. The *Judge Dredd*
  machine we were using at the time had those aftermarket magnetic
  sensor buttons with the little magnets on the button flags, one of
  them came unglued and slipped out of alignment, making the switch
  stuck in the "on" position.

If you're still running into trouble, feel free to post to the mpf-users
Google group. We'll incorporate your issues into this tutorial to
make it easier for everyone in the future!

If you get YAML errors either copy the complete example below or read our
:doc:`/troubleshooting/debugging_yaml_parse_errors` guide.

Check out the complete config.yaml file so far
----------------------------------------------

If you want to see a complete ``config.yaml`` file up to this point, there's a "tutorial"
machine in the mpf-examples repo that you downloaded in Step 1. (This is the same
repo that contains the Demo Man game that you ran in Step 1.)

The complete machine config is in the ``mpf-examples/tutorial/step_3``
folder.

.. code-block:: doscon

   C:\mpf-examples\tutorial>mpf -t

