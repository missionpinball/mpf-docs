mpf mc (command-line utility)
=============================

Starts the MPF Media Controller.

Command line options
--------------------
There are several command-line options you can use when running the MPF MC.
Note that single commands that take no options can be combined, so
``mpf mc -vVb`` is the
same as ``mpf mc -v -V -b``.

-c (lowercase)
~~~~~~~~~~~~~~

Specifies the name of the config file (or files) to load. Default ``config.yaml``
is used if this option is omitted. You do not have to specify the .yaml extension.

Examples:

Run MPF MC and load the config file ``config/config.yaml``:

::

   $ mpf mc

Run MPF and load the config file ``config/nodisplay.yaml``:

::

   $ mpf mc -c nodisplay

You can also chain multiple config files together by specifying a comma-separated
list (no spaces). For example, to load ``config/config.yaml`` first, and then
once that's loaded, merge in changes from ``config/fast.yaml``, run:

::

   $ mpf mc -c config,fast

To load a machine folder from some other location, such as ``/home/brian/pinball/demo_man/config/config.yaml``:

::

   $ mpf mc -c /home/brian/pinball/demo_man/config/config.yaml

-C (uppercase)
~~~~~~~~~~~~~~

Specify the name of the MPF MC default config file which is loaded before your before
your machine config. (MPF MC includes a file ``mcconfig.yaml`` which is inside the
MPF MC package which sets up default things like which modules are loaded, paths used,
etc. If for some reason you want to override this file, you can do so with the `-C` option.

Note that the ``-C`` option is used by both ``mpf game`` and ``mpf mc``, but
these two packages use different default files. So if you want to override the
default, you'll have to make one file that works for both or else launch the
MPF game engine and MPF MC separately (e.g. not using ``mpf both``.

-h
~~

Displays the command line help and exits. (Pretty much what's on this page.)

-f
~~


Forces MPF to load all assets at start (rather than the default behavior where
some assets can be loaded only when modes start or based on other events).
This is useful during development to ensure that all assets are valid and
loadable.

-l (lowercase "L")
~~~~~~~~~~~~~~~~~~

Specifies the name and path of the log file.

The default stores the log file in the ``/logs`` folder in your machine folder,
with a file name of ``<year>-<month>-<day>-<hour>-<min>-<sec>-mpf-<hostname>.log``.

Note that log files are standard log file formats that can be read and parsed
with log file utilities. (The "Console" app is built-in to OS X, for example.)

-L (uppercase)
~~~~~~~~~~~~~~

Specifies the name and path of the log file.

Note this is the same as ``-l`` (lowercase L), but it's included so if you use
:doc:`mpf both <both>` with manually specified log files that you can use ``-l``
for the MPF log and ``-L`` for the MC log.

-v (lowercase)
~~~~~~~~~~~~~~

Enables verbose logging to the log file. Warning: Your log files will be huge, perhaps
1MB per minute of game time. Definitely only use this when you're
troubleshooting.

-V (uppercase)
~~~~~~~~~~~~~~

Enables verbose logging to the console output.

Note that on due to the way the command prompt console
works on Windows, enabling verbose logging on Windows will
significantly affect MPF (in a bad way). Windows computers can run MPF
no problem, but because of their weird console slowness we recommend
that you do not use the `-V` command line option from a Windows
computer.

-x (lowercase)
~~~~~~~~~~~~~~

Ignores all ``platform:`` settings in your config files and forces MPF to run
using the *virtual* platform interface. This is nice for testing when you don't
have your physical hardware attached.

-X (uppercase)
~~~~~~~~~~~~~~

Like `-x`, except it forces the *smart virtual* platform.

Unused Options
--------------

Note that command line options ``-a -A -x -X`` are valid but ignored by the
MPF MC. This is because these options are used with the MPF game engine, but
if you start the MPF game engine and MPF MC at the same time via ``mpf both``,
all options will be sent to both the game engine and the MC, so the MC ignores
these options which it doesn't use.
