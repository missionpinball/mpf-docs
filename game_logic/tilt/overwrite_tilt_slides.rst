Overwriting Tilt Slides
=======================

The :doc:`tilt mode <index>` comes with very basic slides.
You can overwrite them using the following config:

.. code-block:: mpf-mc-config

   #! switches:
   #!   s_tilt:
   #!     number:
   #!     tags: tilt_warning
   ##! mode: tilt
   # in your modes/config/tilt.yaml
   slides:
     _overwrite: true   # this is important to overwrite the existing slides
     tilt_warning_1:
       widgets:
         - type: text
           text: "STOP IT"
       expire: 1s
     tilt_warning_2:
       widgets:
         - type: text
           text: WARNING
           y: top-2
           anchor_y: top
         - type: text
           text: "SERIOUSLY STOP IT"
           y: top-18
           anchor_y: top
           expire: 1s
       expire: 2s
     tilt:
       - type: text
         text: TILT
   ##! test
   #! start_game
   #! post slam_tilt
   #! advance_time_and_run .1
   #! assert_mode_running tilt
   #! hit_and_release_switch s_tilt
   #! advance_time_and_run .1
   #! assert_text_on_top_slide "STOP IT"
   #! advance_time_and_run 2
   #! assert_text_not_on_top_slide "STOP IT"
   #! hit_and_release_switch s_tilt
   #! advance_time_and_run .1
   #! assert_text_on_top_slide "SERIOUSLY STOP IT"

By setting the ``_overwrite: true`` you will overwrite the complete ``slides:``
section of the built-in tilt mode.
The slides above are the default slides.

.. note::

   You can add a slide for the ``slam_tilt`` event.
   However, by default the ``tilt`` slide is also shown at the same time so
   you have to make sure that your slide has a higher priority than that
   slide.
