Service Command Line
====================

The MPF service cli is a fast way to debug or troubleshoot your machine during
development and operation.

1. Start your game (e.g. using ``mpf both``)
2. Start the service cli from within your game folder using ``mpf service``.

Your game will go into service mode and you can run diagnostics commands.
Once you are done the game will continue and exit service mode.
You can use tab to complete commands and arguments.

Commands
--------

list_coils
~~~~~~~~~~

List all coils in the machine.

coil_pulse <name>
~~~~~~~~~~~~~~~~~

Pulse coil <name>.

coil_enable <name>
~~~~~~~~~~~~~~~~~~

Enable coil <name>. This only works if enable is allowed for this coil.

coil_disable <name>
~~~~~~~~~~~~~~~~~~~

Disable coil <name>.

list_switches
~~~~~~~~~~~~~

List all switches in the machine.

monitor_switches
~~~~~~~~~~~~~~~~

Watch for switch changes. Prints any changes until you press Ctrl+c.

list_lights
~~~~~~~~~~~

List all lights in the machine.

light_color <name> <color>
~~~~~~~~~~~~~~~~~~~~~~~~~~

Turn light <name> into color <color>.

light_off <name>
~~~~~~~~~~~~~~~~

Turn light <name> off.

exit/quit
~~~~~~~~~

Exit service cli. Game will reset and start.


See :doc:`mpf service command line reference </running/commands/service>`.
