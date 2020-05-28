mpf game (command-line utility)
===============================

Starts the MPF game engine (the main MPF process).

Command line options
--------------------
There are several command-line options you can use when running MPF. Note that
single commands that take no options can be combined, so ``mpf game -vVa`` is the
same as ``mpf game -v -V -a``.

-a (lowercase)
~~~~~~~~~~~~~~

Forces MPF to reload the config from the actual YAML config files, rather than
from cache.

MPF contains a caching mechanism that caches YAML config files, and
if the original files haven't changed since the last time MPF was run, it loads
them from cache instead. Cached files are stored in your machine's temp folder
which varies depending on your system.

-A (uppercase)
~~~~~~~~~~~~~~

Do not cache the config files.

-b
~~

Disables MPF's BCP interface, meaning MPF will not try to connect to a media
controller via BCP. This is used if for some reason you just want to run MPF
without MPF MC. Without this option, MPF will not start because it will just
sit there trying to connect to the media controller.

-c (lowercase)
~~~~~~~~~~~~~~

Specifies the name of the config file (or files) to load. Default ``config.yaml``
is used if this option is omitted. You do not have to specify the .yaml extension.

Examples:

Run MPF and load the config file ``config/config.yaml``:

.. code-block:: shell

   $ mpf game

Run MPF and load the config file ``config/nodisplay.yaml``:

.. code-block:: shell

   $ mpf game -c nodisplay

You can also chain multiple config files together by specifying a comma-separated
list (no spaces). For example, to load ``config/config.yaml`` first, and then
once that's loaded, merge in changes from ``config/fast.yaml``, run:

.. code-block:: shell

   $ mpf game -c config,fast

To load a machine folder from some other location, such as ``/home/brian/pinball/demo_man/config/config.yaml``:

.. code-block:: shell

   $ mpf game -c /home/brian/pinball/demo_man/config/config.yaml

-C (uppercase)
~~~~~~~~~~~~~~

Specify the name of the MPF default config file which is loaded before your before
your machine config. (MPF includes a file ``mpfconfig.yaml`` which is inside the
MPF package which sets up default things like which modules are loaded, paths used,
etc. If for some reason you want to override this file, you can do so with the `-C` option.

-h
~~

Displays the command line help and exits. (Pretty much what's on this page.)

-f
~~


Forces MPF to load all assets at start (rather than the default behavior where
some assets can be loaded only when modes start or based on other events).
This is useful during development to ensure that all assets are valid and
loadable.

-t
~~

Disable Text UI.
This can be helpful while debugging and is also recommended when running the
machine in production.


-l (lowercase "L")
~~~~~~~~~~~~~~~~~~

Specifies the name and path of the log file.

The default stores the log file in the ``/logs`` folder in your machine folder,
with a file name of ``<year>-<month>-<day>-<hour>-<min>-<sec>-mpf-<hostname>.log``.

Note that log files are standard log file formats that can be read and parsed
with log file utilities. (The "Console" app is built-in to OS X, for example.)

--syslog_address
~~~~~~~~~~~~~~~~

Log to the specified syslog address. This can be a domain socket such as ``/dev/log`` on
Linux or ``/var/run/syslog`` on Mac. Alternatively, you an specify ``host:port`` for remote
logging over UDP.

-v (lowercase)
~~~~~~~~~~~~~~

Enables verbose logging to the log file. Warning: Your log files will be huge, perhaps
1MB per minute of game time. Definitely only use this when you're
troubleshooting.

-V (uppercase)
~~~~~~~~~~~~~~

Enables verbose logging to the console output.

Note that due to the way the command prompt console
works on Windows, enabling verbose logging on Windows will
significantly affect MPF (in a bad way). Windows computers can run MPF
no problem, but because of their weird console slowness we recommend
that you do not use the `-V` command line option from a Windows
computer.

-x (lowercase)
~~~~~~~~~~~~~~

Ignores all ``platform:`` settings in your config files and forces MPF to run
using the :doc:`virtual platform </hardware/virtual/smart_virtual>` interface.
This is nice for testing when you don't have your physical hardware attached.

-X (uppercase)
~~~~~~~~~~~~~~

Like `-x`, except it forces the
:doc:`smart virtual platform </hardware/virtual/smart_virtual>`.

--vpx
~~~~~

Like `-x`, except it forces the
:doc:`Virtual Pinball (VPX) platform </hardware/virtual/virtual_pinball_vpx>`.
