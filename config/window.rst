window:
=======

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``window:`` section of your config is where you configure the properties
of the main on-screen window which is created by MPF-MC.

.. code-block:: mpf-config

    window:
      width: 800
      height: 600
      title: Mission Pinball Framework
      resizable: true
      borderless: true
      fullscreen: false
      exit_on_escape: true
      source_display: window
      effects:
        - type: dmd

.. note::
   If you do not add a ``window:`` section to your machine config, MPF will
   create a window at the default size of 800x600.

.. config


Optional settings
-----------------

The following sections are optional in the ``window:`` section of your config. (If you don't include them, the default will be used).

borderless:
~~~~~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

Controls whether the pop-up window has a border (the "frame") around it.

effects:
~~~~~~~~
Unknown type. See description below.

An optional list of effects to apply to the window contents. These effects perform image processing to the
source image and can be used to get an old school "DMD look" or "color DMD look" to your window
as well as other special effects.  For more information on effects, please review the
:doc:`effects </displays/widgets/display/effects>` documentation.

exit_on_escape:
~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``true``

Controls whether the MPF MC shuts down when the ``Esc`` key is pressed.

fullscreen:
~~~~~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

Controls whether the pop-up window should be a full screen window (if the
value is "true") or whether it should be a regular window.

height:
~~~~~~~
Single value, type: ``integer``. Default: ``600``

The initial height of the popup window, specified in pixels.

icon:
~~~~~
Single value, type: ``string``. Defaults to empty.

The icon for the window which will be shown in the title bar.

left:
~~~~~
Single value, type: ``integer``. Defaults to empty.

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
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

Controls whether the pop up window is used.

resizable:
~~~~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``true``

Specifies whether the pop-up window can be resized (by dragging an edge with
the mouse). If your window is full screen, then this setting will have no
effect.

show_cursor:
~~~~~~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``true``

Specifies whether the mouse cursor should be drawn when the pointer is moved
over the window. If you set this to False/No, then when you drag the pointer
over the window, the pointer will disappear.

source_display:
~~~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``window``

The name of the MPF display that will be used for the source content for
the pop-up window.

title:
~~~~~~
Single value, type: ``string``. Default: ``Mission Pinball Framework``

The text that's shown in the window title bar (assuming your window is
not full screen and not borderless).

top:
~~~~
Single value, type: ``integer``. Defaults to empty.

Used to position the pop up window in a fixed position when MPF MC starts.

See the setting ``left:`` for details.

width:
~~~~~~
Single value, type: ``integer``. Default: ``800``

The initial width of the popup window, specified in pixels.


Related How To guides
---------------------

* :doc:`/displays/display/lcd`
* :doc:`/displays/display/multiple_screens`
* :doc:`/displays/display/adding_dot_look_to_lcd`
