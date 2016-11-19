physical_dmds:
==============

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. versionchanged:: 0.31

.. overview

The ``physical_dmds:`` section of your config is where you configure the settings for a physical DMD (dot matrix
display). You only need this section if you have a physical monochrome DMD connected to a 14-pin header on a hardware
controller. If you have an RGB DMD, configure that in the ``physical_rgb_dmds:`` section.

If you want to show a virtual DMD in an on-screen window, you configure that as a DMD widget, not here.

Note that there are no *height* and *width* settings here. The pixel size of your DMD is determined by the size of the
``source:`` display which drives the content for this DMD.

Optional settings
-----------------

The following sections are optional in the ``physical_dmds:`` section of your config. (If you don't include them, the default will be used).

brightness:
~~~~~~~~~~~
Single value, type: ``number`` (will be converted to floating point). Default: ``0.5``

A brightness multiplier for the DMD. Default is 1.0 which is full brightness, but if you want to dim the DMD, you can
set this to some value lower than 1.0. (e.g. a value of 0.9 will be 90% brightness, etc.)

fps:
~~~~
Single value, type: ``integer``. Default: ``30``

How many frames per second this DMD will be updated. The default of 0 means it will run at the same rate as the MPF Hz.
A value of 30 should be fine and smooth. Some people claim that higher values look better, but as far as we can tell,
that just makes your CPU work harder. But feel free to experiment.

luminosity:
~~~~~~~~~~~
List of one (or more) values, each is a type: ``number`` (will be converted to floating point). Default: ``.299, .587, .114``

A list of three values (from 0.0 to 1.0) that represent the percentage of red, green, and blue that will be used to
produce the monochrome colors from the source display. All three of these values should add up to 1.0.

only_send_changes:
~~~~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

Specifies whether every frame is sent to the DMD, or only changed frames.

shades:
~~~~~~~
Single value, type: ``integer`` (must be a power of 2. Default: ``16``

How many shades the physical DMD can show. Modern pinball controllers support 16 shades.

source_display:
~~~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``dmd``

The name of the display (from the ``displays:`` section of your machine config) that is the source for this physical
DMD. Whatever's on the source display will be displayed on the DMD. If you don't specify a source, MPF will
automatically use a source display called "dmd".

platform:
~~~~~~~~~

.. versionadded:: 0.31

Single value, type: ``string``. Default: ``None``

Name of the platform this DMD is connected to. The default value of ``None`` means the
default hardware platform will be used. You only need to change this if you have
multiple different hardware platforms in use and this coil is not connected
to the default platform.

See the :doc:`/hardware/platform` guide for details.
