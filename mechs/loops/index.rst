Loops / Orbits / Ramps
======================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/sequence_shots`                                                |
+------------------------------------------------------------------------------+
| :doc:`/config/sound_player`                                                  |
+------------------------------------------------------------------------------+

Ramps, loops or orbits usually contain two switches.
One at the entry and one to signal success.
To detect only shots where both switches were hit in order you can use
:doc:`sequence_shots </config/sequence_shots>`.

.. code-block:: mpf-config

   switches:
     s_ramp_entry:
       number: 1
     s_ramp_success:
       number: 2

   sequence_shots:
        ramp:
            switch_sequence: s_ramp_entry, s_ramp_success
            sequence_timeout: 3s

Additionally, most machines usually play a sound once the entry is hit to
signal the player that he hit the ramp and another sound on success to
indicate that the ball made it. You can use :doc:`/config/sound_player` to
achieve that. In this example you would use the events
``s_ramp_entry_active`` and ``ramp_hit`` to play the sounds:


.. code-block:: mpf-config

   sound_player:
     s_ramp_entry_active: indicate_ramp
     s_ramp_success: indicate_ramp_success
