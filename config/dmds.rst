dmds:
=====

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``dmds:`` section of your config is where you configure the settings for physical DMDs (dot matrix
displays). You only need this section if you have a physical monochrome DMD connected to a 14-pin header on a hardware
controller. If you have an RGB DMD, configure that in the :doc:`rgb_dmds` section.

If you want to show a virtual DMD in an on-screen window, you configure that as a display widget with a dot filter.
That does not involve this ``dmds:`` section.

Note that there are no *height* and *width* settings here. The pixel size of your DMD is determined by the size of the
``source:`` display which drives the content for this DMD.

.. code-block:: mpf-config

    displays:
      dmd:
        width: 128
        height: 32
    dmds:
      my_dmd:  # name of this DMD which can be whatever you want
        brightness: .5
        fps: 25
        gamma: 2.5

Note that this section is called ``dmds:`` (plural). Just like
"switches" and "coils" and most everything else in MPF, this is a section that
contains all your DMDs. Now since this is a DMD, you probably only have one,
(though MPF can support as many as you want), but it's important to note that
you add a ``dmds:`` section to your config, then under that you
add an entry for a specific DMD (which can be whatever you want), and then
you enter one or more of the following settings:

(If you don't include any of the settings below, the default will be used).

.. config


Optional settings
-----------------

The following sections are optional in the ``dmds:`` section of your config. (If you don't include them, the default will be used).

brightness:
~~~~~~~~~~~
Single value, type: ``number`` (will be converted to floating point). Default: ``1.0``

A brightness multiplier for the DMD. Default is 1.0 which is full brightness, but if you want to dim the DMD, you can
set this to some value lower than 1.0. (e.g. a value of 0.9 will be 90% brightness, etc.)

fps:
~~~~
Single value, type: ``integer``. Default: ``30``

How many frames per second this DMD will be updated.
A value of 30 should be fine and smooth. Some people claim that higher values look better, but as far as we can tell,
that just makes your CPU work harder. But feel free to experiment.

gamma:
~~~~~~
Single value, type: ``number`` (will be converted to floating point). Default: ``1.0``

Sets the gamma of the DMD. See :doc:`instructions/gamma_correction` for details.

Note that the default setting of ``1.0`` means that no gamma correction is
used. Some physical DMDs do their own internal gamma correction, so this setting
is fine. Others require pre-corrected gamma, so you can set that value here.

You might try a value of 2.2 first and adjust up or down until it looks right.

.. important:: Gamma setting is important!

   We can't stress enough that setting the gamma for your DMD is important for
   making it look right. So click the link above and make the adjustment. It's
   a one-time thing.

luminosity:
~~~~~~~~~~~
List of one (or more) values, each is a type: ``number`` (will be converted to floating point). Default: ``.299, .587, .114``

A list of three values (from 0.0 to 1.0) that represent the percentage of red, green, and blue that will be used to
produce the monochrome colors from the source display. All three of these values should add up to 1.0.

only_send_changes:
~~~~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

Specifies whether every frame is sent to the DMD, or only changed frames.

platform:
~~~~~~~~~
Single value, type: ``string``. Defaults to empty.

Name of the platform this DMD is connected to. The default value of ``None`` means the
default hardware platform will be used. You only need to change this if you have
multiple different hardware platforms in use and this coil is not connected
to the default platform.

See the :doc:`/hardware/platform` guide for details.

shades:
~~~~~~~
Single value, type: ``integer`` (must be a power of 2). Default: ``16``

How many shades the physical DMD can show. Modern pinball controllers support 16 shades.

source_display:
~~~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``dmd``

The name of the display (from the ``displays:`` section of your machine config) that is the source for this physical
DMD. Whatever's on the source display will be displayed on the DMD. If you don't specify a source, MPF will
automatically use a source display called "dmd".

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

Not used.


Related How To guides
---------------------

* :doc:`/displays/display/dmd`
