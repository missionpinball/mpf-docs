LISY Protocol
=============

The LISY protocol is a generic serial protocol to control pinball machines.
It was developed for the :doc:`LISY platform <index>` but is also used in other
custom pinball platforms such as :doc:`APC </hardware/apc/index>`.


Theory of operations
--------------------

All communication is initiated from the host PC.
Commands are binary and generally have a fixed length.
They may contain a length byte to indicate how many entries are to
expect (i.e. three color values).
Strings are zero terminated in both command and response.

At startup MPF resets the hardware and queries the count of all peripherals
(i.e. switches, coils, lamps).
Afterwards, it will query the state of switches and configure coils/lamps.

During the runtime MPF periodically polls changed switches and sends a
watchdog every 500ms.
The platform is expected to disable all outputs after 1s without watchdog.

Protocol reference (v0.08)
--------------------------

.. csv-table:: General command format
   :header: "Byte", "Length", "Description"
   :widths: 10, 10, 30

   "0", "1", "Command Byte (see table below"
   "1 - n", "n - 1", "Payload (n-1 bytes)"

.. csv-table:: String format (in both payload and response)
   :header: "Byte", "Length", "Description"
   :widths: 10, 10, 30

   "0 to (n-1)", "n - 1", "String"
   "n", "n - 1", "Null byte"

Get Connected Hardware (0x00)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Get the name of the connected hardware.
Does not have any payload.

Example:

.. csv-table:: Command 0x00 - Get Connected Hardware
   :header: "Byte", "Length", "Example", "Comment"
   :widths: 10, 10, 10, 30

   "1", "1", "0", "Command 0 - Get Connected Hardware"

Returns a null terminated string.

Example: ``LISY80``.

MPF uses this string to identify the platform and might perform certain
quirks based on this info if necessary.

Get Firmware Version (0x01)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Get firmware version of the hardware board.
Does not have any payload.

Example:

.. csv-table:: Example Command 0x01 - Get Firmware Version
   :header: "Byte", "Length", "Example", "Comment"
   :widths: 10, 10, 10, 30

   "1", "1", "1", "Command 1 - Get Firmware Version"

Returns a null terminated string.

Example: ``4.01``.

MPF parses this string as semantic version.
It exposes the version as variable and in the logs.
This might be used to perform quirks around known bugs.

Get API Version (0x02)
^^^^^^^^^^^^^^^^^^^^^^

Get the API version.
Does not have any payload.

Example:

.. csv-table:: Example Command 0x02 - Get API Version
   :header: "Byte", "Length", "Example", "Comment"
   :widths: 10, 10, 10, 30

   "1", "1", "2", "Command 2 - Get API Version"

Returns a null terminated string.

Example: ``0.08``.

MPF parses this string as semantic version.
This is expected to be ``0.08`` for this version.
MPF might refuse old API versions at some point.

Get Lamp Count (0x03)
^^^^^^^^^^^^^^^^^^^^^

Get count of lamps connected to the hardware platform.
Does not have any payload.

Example:

.. csv-table:: Example Command 0x03 - Get Lamp Count
   :header: "Byte", "Length", "Example", "Comment"
   :widths: 10, 10, 10, 30

   "1", "1", "3", "Command 3 - Get Lamp Count"

Returns one byte:

.. csv-table:: Response to 0x03 - Get Lamp Count
   :header: "Byte", "Length", "Description"
   :widths: 10, 10, 30

   "0", "1", "Lamp count ``l`` (0 to 255). 0 if no lamps exist."

Example:

.. csv-table:: Example Response to 0x03 - Get Lamp Count
   :header: "Byte", "Length", "Example", "Comment"
   :widths: 10, 10, 10, 30

   "0", "1", "64", "Platform supports 64 lights with numbers 0 to 63."

MPF uses this number to refuse any lamps with a number larger or equal than
``l``.
Lamps in LISY are expected to be ``on/off`` type devices and do not support
fading or dimming.
Use this for older style lamps and GIs.

Get Solenoid Count (0x04)
^^^^^^^^^^^^^^^^^^^^^^^^^

Get count of solenoids connected to the hardware platform.
Does not have any payload.

Example:

.. csv-table:: Example Command 0x04 - Get Solenoid Count
   :header: "Byte", "Length", "Example", "Comment"
   :widths: 10, 10, 10, 30

   "1", "1", "4", "Command 4 - Get Solenoid Count"

Returns one byte:

.. csv-table:: Response to 0x04 - Get Solenoid Count
   :header: "Byte", "Length", "Description"
   :widths: 10, 10, 30

   "0", "1", "Solenoid count ``c`` (0 to 127). 0 if no solenoids exist."

Example:

.. csv-table:: Example Response to 0x04 - Get Solenoid Count
   :header: "Byte", "Length", "Example", "Comment"
   :widths: 10, 10, 10, 30

   "0", "1", "64", "Platform supports 64 solenoids with numbers 0 to 63."

MPF uses this number to refuse any solenoids with a number larger or equal than
``c``.

Get Sound Count (0x05)
^^^^^^^^^^^^^^^^^^^^^^

Get count of sounds available.
Does not have any payload.

Example:

.. csv-table:: Example Command 0x05 - Get Sound Count
   :header: "Byte", "Length", "Example", "Comment"
   :widths: 10, 10, 10, 30

   "1", "1", "5", "Command 5 - Get Sound Count"

Returns one byte:

.. csv-table:: Response to 0x05 - Get Sound Count
   :header: "Byte", "Length", "Description"
   :widths: 10, 10, 30

   "0", "1", "Sound count ``m`` (0 to 255). 0 if no sounds exist."

Example:

.. csv-table:: Example Response to 0x05 - Get Sound Count
   :header: "Byte", "Length", "Example", "Comment"
   :widths: 10, 10, 10, 30

   "0", "1", "128", "Platform supports 128 sounds with numbers 0 to 127."

MPF uses this number to refuse any sounds with a number larger or equal than
``m``.
This is used for older machines with a hardware soundcard.
In :doc:`LISY <index>` it can be used to play sounds from the ROM of the
original game.
Return ``0`` if you do not support sounds in your platform.

