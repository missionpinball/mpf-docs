
Controls the on-screen window that MPF creates, including properties
of the window itself as well as the initial set ofdisplay elements
you'd like to show up in that window. This sectioncan be used in your
machine-wide config files. This section *cannot* be used in mode-
specific config files.


::

    
    window:
        width: 800
        height: 600
        title: Mission Pinball Framework
        resizable: yes
        frame: yes
        fullscreen: no
        fps: auto
        quit_on_close: True
        elements:
        - type: VirtualDMD
          width: 512
          height: 128
          h_pos: center
          v_pos: center
          pixel_color: ff5500
          dark_color: 220000
          layer: 1
          pixel_spacing: 2
    
        - type: Text
          font: tall title
          text: JUDGE DREDD
          h_pos: right
          v_pos: bottom
          y: -10
          x: -20
          size: 60
          antialias: yes
          layer: 1
          color: ee9900
    
        - type: Shape
          shape: box
          width: 514
          height: 130
          layer: 2
          thickness: 2
          v_pos: center
          h_pos: center
          color: 00ff00
    
        - type: Movie
          movie: torches
          repeat: True
          layer: 0




width:
~~~~~~

Width of the window in pixels. Default is 800.



height:
~~~~~~~

Height of the window in pixels. Default is 600.



title:
~~~~~~

Text title of the window. Default is "Mission Pinball Framework".



resizable:
~~~~~~~~~~

True/False which controls whether this window is resizable.



frame:
~~~~~~

True/False which controls whether the window has a "frame" around it
(including the title bar, etc).



fullscreen:
~~~~~~~~~~~

True/False which enables full screen mode for the on screen window. If
True, the width and height settings are ignored.



fps:
~~~~

The number of frames per second that the on screen window updates
itself. (The "frame rate," or "refresh rate," in other words.) A value
of "auto" means that it refreshes at the same rate as the `Machine
Hz`_. On some systems (and depending on how many and what type of
display elements you have in your window), the system can get bogged
down trying to refresh the window too fast, so you can enter a lower
frame rate here. You should try out the "auto" setting though. Our
main test system in a Windows 7 virtual machine with a 640 x 160 on
screen virtual DMD, and we can run 60fps no problem even while we're
driving a physical pinball machine. And that's using a VM!



quit_on_close:
~~~~~~~~~~~~~~

Whether MPF should quit when the window is closed. Default is yes.
(Note this feature has not yet been implemented.)



elements:
~~~~~~~~~

A list of one or more display elements that will be shown as the
initial content in the window. See the sections on `Display Elements`_
for the specifics of the different types of elements that you can use,
and see their related entries in the `configuration file reference`_
for details of their settings.

.. _Display Elements: https://missionpinball.com/docs/displays/display-elements/
.. _Machine Hz: https://missionpinball.com/docs/system/timers-machine-tick-speed-hz/
.. _configuration file reference: https://missionpinball.com/docs/configuration-file-reference/


