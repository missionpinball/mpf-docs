Using multiple screens
======================

This section covers using multiple displays and screens.

Distinction between displays, windows and screens
-------------------------------------------------

The MPF media controller knows windows and displays.
A ``window`` is the window where MPF-MC pops up on your desktop using kivy.
Internally, MPF can have multiple ``displays`` which are internal viewports
and can be targeted by slides.
A ``display`` can either be displayed on a ``window`` or on one or more DMDs.
Additionally, a ``display`` can also show one or more other ``displays`` using
:doc:`display widgets </displays/widgets/display/index>`.
MPF does not know about screens which are phyiscal monitors connected to your
machine.
However, the kivy window can span multiple screens.

Using multiple screens on your PC
---------------------------------

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
       window_state: visible # visible, hidden, maximized, minimized
       fbo: hardware # hardware, software, force-hardware
       fullscreen: false
       left: 0
       top: 0
       width: 3840   # width of display1 + display2
       height: 1080  # common height (or the maximum of both)
       maxfps: 30
       multisamples: 2
       position: custom # auto, custom
       show_cursor: true
       resizable: false
       rotation: 0
     displays:
       display1:
         width: 1920
         height: 1080
       display2:
         width: 1920
         height: 1080
       combined_display:
         width: 3840
         height: 1080
     slides:
       base_slide:
         - type: display
           source_display: display1
           width: 1920
           height: 1080
           x: left
           anchor_x: left
         - type: display
           source_display: display2
           width: 1920
           height: 1080
           x: right
           anchor_x: right
     slide_player:
       mc_ready:
         base_slide:
           target: combined_display

Use ``width`` and ``height`` to set the size of the window.
``left`` and ``top`` are used to position the window.

We created one window which spans both screens.
Then we define a display ``combined_display`` which will be displayed on
startup by the slide ``base_slide`` spanning both screens.
``base_slide`` contains two widgets which show the displays ``display1``
and ``display2``.
You can now target any slides to those two displays.
See :doc:`/displays/widgets/display/index` for details.

Using multiple displays
-----------------------

You can easily use two DMDs and one LCD (or two LCDs with the solution above).
To implement that you need to define multiple displays.
One diplay per DMD and one for your LCD.
If you want to show your DMDs on the LCD (i.e. during development) you can also
define a fourth display and create a slide which contains three
:doc:`display widgets </displays/widgets/display/index>` to show the other
three displays.
