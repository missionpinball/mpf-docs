mpf service (command-line utility)
==================================

Start the command line service mode. Run this command from your machine folder.
Service CLI will connect to MPF via BCP and put the machine into service mode.


Command line options
--------------------
``mpf service`` will spawn an interactive shell.

list_coils
~~~~~~~~~~

List all coils in the machine.

coil_pulse <name>
~~~~~~~~~~~~~~~~~

Pulse coil <name>.

enable_pulse <name>
~~~~~~~~~~~~~~~~~~~

Enable coil <name>. This only works if enable is allowed for this coil.

disable_pulse <name>
~~~~~~~~~~~~~~~~~~~~

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

