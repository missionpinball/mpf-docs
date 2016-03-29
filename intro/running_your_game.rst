How to start MPF and run your game
==================================

.. note:: This page is a reference for how to start MPF and all the
   various command-line options. If you're brand-new to MPF and running
   it for the first time, we recommend that you follow our :doc:`step-by-step
   getting started tutorial </tutorial/index>`. The first few steps will walk you through
   downloading and installing MPF and getting our sample *Demo Man*
   machine up and running.)

MPF is a console-based application which you
run from the command line. There are actually two separate processes
that you need to run for MPF: The core MPF game engine and the
separate media controller . The game engine talks to the pinball
hardware and runs the game logic, and the media controller drives the
LCD/DMD and audio. The game engine and media controller talk to each
other via an open protocol called *BCP* (for "Backbox Control
Protocol") via a TCP socket. At this point you might be wondering why
the game engine and media controller are two separate processes? Two
reasons:

+ Having two processes means that each one can run on a separate core
  in a multi-core host computer. This makes efficient use of hardware
  since the trend is to have multiple cores. If the game engine and
  media controller were combined, then your quad-core Raspberry Pi 2
  would have all the MPF stuff running on one core while the other three
  cores were wasted doing nothing.
+ Having two processes means can replace the built-in Python-based
  media controller with something else if you want different features.
  For example, there is a group of people building an open source Unity
  3D-based media controller which can be used for very advanced 3D
  display graphics.

.. note:: Prior to MPF 0.30, we recommended that you put your machine's folder
   in the ``/machine_files`` folder inside the MPF package. That is changed now,
   since starting in MPF 0.30, MPF is properly installed into a system location.
   Now you can put your machine folder(s) wherever you want.

To run an MPF game, you have to start both the media controller and
the MPF game engine. You can do both of these via the command line.
However, by default, each component "takes over" the terminal window
while it's running, so you actually need to open two terminal windows
and run the MPF core engine in one and the media controller in the
other. If you don't want to do this we also have a batch file which
you can use instead which automatically pops up the two separate
windows and runs both pieces. (More on that in the next section.)
Anyway, to run MPF, first start the media controller.

Open a command window and change into the root of your machine folder. Then run:

::

    mpf mc <enter>

Then in a second terminal window, start the MPF game engine:

::

    mpf <enter)

.. note:: Prior to MPF 0.30, you launched MPF by actually running ``python``
   from the command prompt. Starting in MPF 0.30, when you install MPF, the
   command ``mpf`` is registered in a system path, so now you switch to your
   machine folder and start the game by running MPF directly.

Understanding MPF commands
--------------------------

When you install MPF, the command "mpf" is registered with your system. You can
open a terminal window or command prompt and run "mpf", by itself, from anywhere.

There are several sub-commands you can specify when you run MPF. You specify a
sub-command by running `mpf <command>`. (Some mpf commands take additional
options).

Here are a list of valid MPF commands:

* ``mpf core`` (Starts the core MPF game engine)
* ``mpf md`` (Stars the MPF Media Controller)
* ``mpf both`` (Starts both the core game engine and the media controller)
* ``mpf migrate`` (Runs the migration tool to migrate your config and show files
  to the current version of MPF.)

Note that if you just run ``mpf`` by itself, that's the same thing as running
``mpf core``.

There are several command line parameters and options you can add to
both the MPF engine and the media controller. The order of these
options is not important. <your machine folder> : The only required
command line parameter is to pass the folder location of your
machine's folder. The idea is that you can have one copy of MPF which
can be used to drive multiple machines, so you use this command line
parameterto specify which machine you're running. This command line
parameter does not have any dashes or letters that precede it. The
machine folder is the folder that contains your machine's *config*,
*modes*, etc. folders. You can pass a full path to your machine file.
For example, if MPF is in the *C:\pinball\mpf* folder, and your
machine folder is *c:\pinball\your_machine*, you would switch to the
*c:\pinball\mpf* folder and run MPF like this:


::


    python mpf.py c:\pinball\your_machine


Or if you're using the batch file to launch the MPF core engine and
media controller at the same time:


::


    mpf c:\pinball\your_machine


`-c` : Specifies the name (and optionally the path) of the initial
configuration file MPF will load. If you don't specify this option, it
will automatically look for *config/config.yaml* in your machine path
folder. (So it looks for a file called *config.yaml* in a folder
called *config*.) Note that you can also specify a comma-separate list
of multiple files, and MPF will load them in order, meaning that
settings in the latter files overwrite settings in the earlier files.
This is great if you want to test different configurations. For
example, you might have your default *config.yaml* with all your
settings, including the media controller to run in full screen mode,
but you might also create a second config file called
*small_window.yaml* which sets your display to run in a small window
which is nice when you're troubleshooting. So then you could run your
machine in full screen mode via:


::


    mpf c:\pinball\your_machine


And then you could run the small windowed version via:


::


    mpf c:\pinball\your_machine -c config,small_window


`-X` : (Uppercase "X") Forces MPF to use the smart virtual platform
interface, regardless of what your *hardware: platform:* is set to.
Note that the smart virtual platform is the default which is used if
you do not specify a platform in your machine config file. `-x` :
(Lowercase "x") Forces MPF to use the virtual platform interface,
regardless of what your *hardware: platform:* is set to. `-b` : Sets
MPF to not connect to the Media Controller via BCP. This is nice if
you're just running the MPF core engine without a media controller so
you don't get all those timeout messages about it not being able to
connect to a BCP server. `-v` : (Lowercase "v") Enables verbose
logging to the log file. Warning: Your log files will be huge, perhaps
1MB per minute of game time. Definitely only use this when you're
troubleshooting. `-V` : (Uppercase "V") Enables verbose logging to the
console output. Note that on due to the way the command prompt console
works on Windows, enabling verbose logging on Windows will
significantly affect MPF (in a bad way). Windows computers can run MPF
no problem, but because of their weird console slowness we recommend
that you do notuse the `-V`command line option from a Windows
computer. `-C` : Sets the location of the default system-wide
configuration file. This file has the same format (and can contain the
same information) as any machine configuration file, but it's read in
first. This parameter is optional. If you do not specify it, MPF will
automatically loadan MPF configuration file from
`/mpf/mpf/mpfconfig.yaml`, and the media controllerwill automatically
loadan system-wideconfiguration file from
`/mpf/media_controller/mcconfig.yaml`. `-l` : Specifies the name of
the log file that will be generated. (This log file contains the same
content as the console window output.) By default it creates a file in
the `mpf/logs`folder with a filename that's based on the computer host
name plus a time and date stamp. For example, 2014-06-26-13-39-39
-mpf-computername.log represents June 06, 2014 at 1:39:39pm. A
separate log file will be created by the MPF game engine and the media
controller. Their formats are the same with the example of "mpf" in
the game engine log file and "mc" in the media controller log file.
`-h` : Displays the command-line option help message. (Basically it
just describes everything here.) `--version:` Prints the version of
MPF, the config file version required, and the version of BCP this
build of MPF is using. Then it quits. So you use it like this: *python
mpf.py --version.*
