Configuring Sound in LISY
=========================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/hardware_sound_systems`                                        |
+------------------------------------------------------------------------------+
| :doc:`/config/hardware_sound_player`                                         |
+------------------------------------------------------------------------------+

With LISY your can use the sound card of your original game including all the
sounds of your game.

.. note::

   You can alternatively use the :doc:`built-in MPF sound system </sound/index>`
   which supports more modern audio features. In that case you need to connect
   the sound card of your PC to the audio amp of your machine (not covered here).

You can configure the external LISY
:doc:`hardware sound interface </config/hardware_sound_systems>` like this:

.. code-block:: mpf-config

   hardware_sound_systems:
     default:
       label: LISY

Built-in sounds
---------------

Any built-in sounds can be played using their number in the original game:

.. code-block:: mpf-config

   #! hardware_sound_systems:
   #!   default:
   #!     label: LISY
   hardware_sound_player:
     some_event_to_play_sound2:
       2:
         action: play
     some_event_to_stop_any_playing_sound: stop

Whatever those sounds loop or do not depends on the sound and the game.
In this case the event ``some_event_to_play_sound2`` will play the sound number
2. The event ``some_event_to_stop_any_playing_sound`` will stop any sound.

Additional sounds
-----------------

You can play additional sounds by placing mp3 files on the SD-card.
Soundfiles need to be placed in the mpf config directory on the SD card of
the LISY system in the subdirectory ``hardwaresounds``.
For LISY1 this is ``/boot/mpfcfg/LISY1/xxx`` and for LISY80 this is
``/boot/mpfcfg/LISY80/xxx`` (where ``xxx`` is the game number set via S2
according to the appendix in the
`LISY user manual <http://www.lisy80.com/english/documentation-lisy/>`_).

.. code-block:: mpf-config

   #! hardware_sound_systems:
   #!   default:
   #!     label: LISY
   hardware_sound_player:
     play_file:
       "some_file": play_file
     play_file_loop:
       "some_file":
         action: play_file
         platform_options:
           loop: true
           no_cache: false

Text-to-speech
--------------

LISY can also do text-to-speech:

.. code-block:: mpf-config

   #! hardware_sound_systems:
   #!   default:
   #!     label: LISY
   hardware_sound_player:
     event_to_play_text:
       text:
         action: text_to_speech
         value: "Hello MPF"
         platform_options:
           loop: false
           no_cache: true

Changing volume
---------------

Similarly, you can change volume:

.. code-block:: mpf-config

   #! hardware_sound_systems:
   #!   default:
   #!     label: LISY
   hardware_sound_player:
     event_to_set_volume_to_05:
       set_volume:
         action: set_volume
         value: 0.5
     increase_volume:
       increase_volume:
         action: increase_volume
         value: 0.1
     decrease_volume:
       decrease_volume:
         action: decrease_volume
         value: 0.1

Sounds in a show
----------------

You can also use any of the actions above in a show instead of in a standalone
:doc:`/config_players/hardware_sound_player`:


.. code-block:: mpf-config

   #! hardware_sound_systems:
   #!   default:
   #!     label: LISY
   ##! show: test
   - hardware_sounds:
       text:
         action: text_to_speech
         value: "Hello MPF"
         platform_options:
           loop: false
           no_cache: true
     duration: 2s


What if it did not work?
------------------------

Have a look at our :doc:`LISY troubleshooting guide <troubleshooting>`.
