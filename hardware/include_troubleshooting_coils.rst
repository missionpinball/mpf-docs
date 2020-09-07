Coils Are Not Firing
--------------------

What to do if your coils are not working?

Check if Your Hardware is Working at all
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sounds stupid but this is a good start:
Is the hardware working at all?
Do you see switch hits in the logs?
If not, check our section ``Your hardware is not working at all``.

Check the Watchdog
^^^^^^^^^^^^^^^^^^

If switches (or other features of the platform) are working but coils are not
we have to dig deeper.
Most hardware platforms have some kind of watchdog.
Often there is some LED which indicates if the watchdog is received.
The MPF log might also contain clues (especially if you have enabled ``debug``
and run MPF with verbose flags ``-v -V``).
If the watchdog is not received by your platform it will not enable coils.

In most cases watchdog related problems indicate wiring problems.
Check if your boards are properly wired.

Test Your Coil Numbers using MPF Service CLI
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Hardware is connected and generally working, watchdog is good but still your
coils are not working?
Maybe something with the numbering is odd.
Lets tests that using the :doc:`MPF Service CLI </tools/service_cli/index>`.
Alternatively, you can also use
:doc:`service mode </game_logic/service_mode/index>` if you already configured.
Both ways work similarly.

1. Open two consoles
2. Start your game (e.g. using ``mpf both``)
3. Start the service cli from within your game folder using ``mpf service``.
4. Type ``list_coils`` and press ``ENTER`` to see a list of coils.
5. Type ``coil_pulse your_coil`` and press ``ENTER`` to pulse it.

Does it work? If not check the log and try verify the coil number.
If you do not specify ``default_pulse_ms`` MPF will use ``10ms`` which might
not be enough for some mechs.
Try to increase that gently (maybe ``20ms`` or ``30ms``).
