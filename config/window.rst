window:
=======

*Config file section*

* Valid in machine config files: **YES**
* Valid in mode config files: **NO**

.. overview

The ``window:`` section of your config is where you configure the properties
of the on-screen window which is created by MPF-MC.

::
    window:
        width: 800
        height: 600
        title: Mission Pinball Framework
        resizable: yes
        borderless: yes
        fullscreen: no
        exit_on_escape: True
        source_display: window


Optional settings
-----------------

The following sections are optional in the ``window:`` section of your config. (If you don't include them, the default will be used).

borderless:
~~~~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``0``

Controls whether the pop-up window has a border (the "frame") around it.

exit_on_escape:
~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``true``

Controls whether the MPF MC shuts down when the ``Esc`` key is pressed.

fullscreen:
~~~~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``0``

Controls whether the pop-up window should be a full screen window (if the
value is "true") or whether it should be a regular window.

height:
~~~~~~~
Single value, type: ``integer``. Default: ``600``

The initial height of the popup window, specified in pixels.

icon:
~~~~~
Single value, type: ``string``. Default: ``None``

The icon for the window which will be shown in the title bar.

left:
~~~~~
Single value, type: ``integer``. Default: ``None``

Used to position a non-fullscreen window in a precise location on the screen.
(This is useful if you're using an LCD display in your machine and your
backbox has a smaller opening than the size of the screen. In that case you
need to make sure the pop-up window always shows up in the proper location.)

The ``left:`` value specifies how many pixels the left edge of the window will
be offset from the left edge of the screen. (See the ``top:`` setting to
control the vertical placement.)

maxfps:
~~~~~~~
Single value, type: ``integer``. Default: ``60``

Sets the maximum frames-per-second that the window is updated. Setting a lower
value can potential save CPU / GPU usage.

minimum_height:
~~~~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``0``

If you have a resizable window, this specifies the minimum height the window
can be resized to.

minimum_width:
~~~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``0``

If you have a resizable window, this specifies the minimum width the window
can be resized to.

no_window:
~~~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

Controls whether the pop up window is used.

resizable:
~~~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``1``

Specifies whether the pop-up window can be resized (by dragging an edge with
the mouse). If your window is full screen, then this setting will have no
effect.

show_cursor:
~~~~~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``1``

Specifies whether the mouse cursor should be drawn when the pointer is moved
over the window. If you set this to False/No, then when you drag the pointer
over the window, the pointer will disappear.

source_display:
~~~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``default``

The name of the MPF display that will be used for the source content for
the pop-up window.

title:
~~~~~~
Single value, type: ``string``. Default: ``Mission Pinball Framework v0.30.0``

The text that's shown in the window title bar (assuming your window is
not full screen and not borderless).

top:
~~~~
Single value, type: ``integer``. Default: ``None``

Used to position the pop up window in a fixed position when MPF MC starts.

See the setting ``left:`` for details.

width:
~~~~~~
Single value, type: ``integer``. Default: ``800``

The initial width of the popup window, specified in pixels.


