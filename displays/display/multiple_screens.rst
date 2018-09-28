Using multiple screens
======================

Some machines use more than one screen.
Unfortunately, kivy (the graphics framework we use) does only support one
screen and cannot easily be started two times.
This is mostly caused by OpenGL which is rarely used to render multiple
windows.
The simplest solution to this problem is to extend the MC window to span both
(or more) screens.
This can be achieved using the following config:

.. code-block:: mpf-config

   kivy_config:
    kivy:
      desktop: 1
      exit_on_escape: true
      pause_on_minimize: 0
      log_dir:
      window_icon:

    graphics:
      borderless: true
      window_state: visible  # visible, hidden, maximized, minimized
      fbo: hardware  # hardware, software, force-hardware
      fullscreen: false
      left: 0
      top: 0
      width: 3840
      height: 1080
      maxfps: 30
      multisamples: 2
      position: custom  # auto, custom
      show_cursor: true
      resizable: false
      rotation: 0

Use ``width`` and ``height`` to set the size of the window.
``left`` and ``top`` are used to position the window.

Then put a slide containing two ``display`` widgets on your display.
See :doc:`/displays/widgets/display/index` for details.
