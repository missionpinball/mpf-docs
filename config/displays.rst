displays:
=========

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``displays:`` section of your config is where you configure the logical displays in your machine. A display is used
to show slides, and can be an on-screen window or a DMD.

You can have more than one display. For example, if you want to have a DMD and also display an on-screen window, you'll
actually have two ``displays:``, the DMD is one and the on-screen window is the other.

Here's an example ``displays:`` section from *Demo Man* with two displays:

.. code-block:: mpf-config

   displays:
     window:
       height: 200
       width: 600
     dmd:
       width: 128
       height: 32
       default: true
       round_anchor_x: left

In the example above, one of the displays is called *window* and the other is called *dmd*. Note that the names here are
completely arbitrary. Just naming a display "window" does not make it show up in the window, and naming a display "dmd"
doesn't make it show up in the DMD. (When you configure your window in the ``window:`` section of your config, you
specify the name of the display you want to be the *source* for the window content. Same for the DMD.)

The names of the displays are used as "targets" for your slides. So when you show a slide, you specify which display
you want it to show on. If you don't specify a target, it will choose the default. If you only have one display, you
never have to worry about this because that display will always be the default. If you have more than one, you can add
the ``default: true`` to a display here to tell MPF which display is your default which is used when you play slides
without specifying a target.

.. note::

   Starting in MPF v0.33, If you do not put a ``displays:`` section in your
   machine config, MPF will automatically create a single display called
   "default" with a size of 800x600. (This matches the default window size.)

Each display in your ``displays:`` section can have the following settings:

.. config


Optional settings
-----------------

The following sections are optional in the ``displays:`` section of your config. (If you don't include them, the default will be used).

default:
~~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

Specifies that this display is the default, meaning it's the display that's used if you show a slide without specifying
a target for that slide. If you only have one display, it will be the default automatically.

height:
~~~~~~~
Single value, type: ``integer``. Default: ``600``

The height if the display, in pixels. Note that if you're showing this display on the screen, you can scale the screen
window which will scale the display. So the height here can be thought of as the "native" height of the display.

round_anchor_x:
~~~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``center``

Indicates that this display should not render widgets on fractional horizontal pixels,
e.g. anchoring an 11px-wide widget at -5.5 pixels. When specified with ``left`` or ``right``, this
display will round the pixel position to the nearest whole pixel in that direction.

This setting can also be configured on an individual widget to override the display's configuration.

round_anchor_y:
~~~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``middle``

Indicates that this display should not render widgets on fractional vertical pixels,
e.g. anchoring an 11px-high widget at -5.5 pixels. When specified with ``bottom`` or ``top``, this
display will round the pixel position to the nearest whole pixel in that direction.

This setting can also be configured on an individual widget to override the display's configuration.

width:
~~~~~~
Single value, type: ``integer``. Default: ``800``

The width of the display, in pixels.

console_log:
~~~~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``basic``

Log level for the console log for this device.

debug:
~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

Set this to true to see additional debug output. This might impact the performance of MPF.

file_log:
~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``basic``

Log level for the file log for this device.

label:
~~~~~~
Single value, type: ``string``. Default: ``%``

Name of this device in service mode.

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Defaults to empty.

Unused.


Related How To guides
---------------------

* :doc:`/displays/index`
