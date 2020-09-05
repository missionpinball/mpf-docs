Fine-tuning ball device timing
==============================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/ball_devices`                                                  |
+------------------------------------------------------------------------------+

The default timeouts in :doc:`ball_devices </config/ball_devices>` are very
conservative and usually too long.
You might have noticed delays after the eject of the second ball when starting
a multiball.
This is caused by the default ``eject_timeouts`` setting which will cause the
ball device to wait ``10s`` until the ball is confirmed to be on the playfield.
Only after that the next ball will be ejected because before that timeout the
ball may return back into the device (e.g. roll back in the plunger lane).

To minimize delays during ejects to the playfield you need to measure the
maximum time the ball may take to return after an eject.
Set ``eject_timeouts`` to that value but not lower.
If you set it lower the ball may become confirmed and then you end up with
two simultanious ball inside the plunger lane.
In case that time is still too long you might be able to use
``confirm_eject_switch`` (but that might require a hardware change).

Also, please note that this only applies to devices ejecting to a playfield.
If you are ejecting into another device (e.g. trough to plunger lane) the
timeout does not really matter because the ball will be confirmed once it
hits the target device.
