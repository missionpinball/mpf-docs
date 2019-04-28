Overwriting Tilt Slides
=======================

The :doc:`tilt mode <index>` comes with very basic slides.
You can overwrite them using the following config:

.. code-block:: mpf-config

   ##! mode: tilt
   # in your modes/config/tilt.yaml
   slides:
     _overwrite: true   # this is important to overwrite the existing slides
     tilt_warning_1:
       widgets:
       - type: text
         text: WARNING
       expire: 1s
     tilt_warning_2:
       widgets:
       - type: text
         text: WARNING
         y: top-2
         anchor_y: top
       - type: text
         text: WARNING
         y: top-18
         anchor_y: top
         expire: 1s
       expire: 2s
     tilt:
     - type: text
       text: TILT


By setting the ``_overwrite: true`` you will overwrite the complete ``slides:``
section of the built-in tilt mode.
The slides above are the default slides.

.. note::

   You can add a slide for the ``slam_tilt`` event.
   However, by default the ``tilt`` slide is also shown at the same time so
   you have to make sure that your slide has a higher priority than that
   slide.
