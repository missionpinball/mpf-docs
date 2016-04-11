displays: (config setting)
==========================
Sets the names and resolutions of the logical displays in your machine.

.. include:: _machine_config_yes.rst
.. include:: _mode_config_no.rst

::

   displays:
     display1:
       height: 400
       width: 300
     display2:
       height: 800
       width: 600

In the MPF Media Controller, all display content is targeted towards one of the
display names from this list. Many machines will only have one display, however
some could have more. (On screen LCD and DMD, LCD and smaller playfield display,
etc.)

Note that the displays listed here are "logical"--they're not tied to any
physical display. Once you define your list of displays here, you configure
which display is the source for your on-screen window in the ``window:`` section
of the machine config, and you specify which of these logical displays is the
source for your DMD or RGB DMD in the ``dmd:`` or ``color_dmd:`` section of your
machine config.


Settings & options
------------------
<name>:
~~~~~~~
The sub-entries in the ``displays:`` section sepcify the name of each display,
each which contain additional settings. The example config section above
contains two displays, called *display1* and *display2*.

You can name your displays whatever you want. However certain pre-defined names
have special behavior:

* *window*: Will be used as the default logical display for an on-screen window
  in the event the window doesn't have a source display configured.
* *dmd*: Will be used as the default logical display for a physical DMD or RGB
  DMD in the event the DMD doesn't have a source display configured.

Another slighty more real-world example might look like this:

::

   displays:
     window:
       height: 768
       width: 1024
     dmd:
       height: 32
       width: 128
       default: true

Note that you do not set color settings (number of colors, etc) at the display
level. Color is handled at the physical display level or on screen widget level,
not at the display level.


default:
~~~~~~~~
Single value, type: boolean (Yes/No or True/False). Default: False

True/False value which specifies whether a display is the default display. If a
display is set to be the default, that's the display that receives slides and
widgets if the slides/widgets are posted without a target.

Note that only one display can be the default.


fps:
~~~~
Single value, type: integer. Default: 0

.. todo::
   Add description.


height:
~~~~~~~
Single value, type: integer. Default: 600

Height of the display, in pixels.


width:
~~~~~~
Single value, type: integer. Default: 800

Width of the display, in pixels.

