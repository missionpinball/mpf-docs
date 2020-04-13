rgb_dmds:
=========

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``rgb_dmds:`` section of your machine config is where you configure
the settings for physical RGB DMDs (dot matrix displays). You only need this
section if you have a RGB DMD connected via USB. If you have a mono DMD,
configure that in the :doc:`dmds` section.

If you want to show a virtual RGB DMD in an on-screen window, you configure that
as a display widget with a dot filter. You don't need to use this ``rgb_dmds:`` section
to do that.

Note there are no *height* and *width* settings here. The pixel size of
your DMD is determined by the size of the ``source:`` display which drives the
content for this DMD.

Here's an example:

.. code-block:: mpf-config

   displays:
     dmd:
       width: 128
       height: 32
   rgb_dmds:
     smartmatrix:  # name of this DMD which can be whatever you want
       hardware_brightness: .5
       fps: 25
       gamma: 2.5

Note that this section is called ``rgb_dmds:`` (plural). Just like
"switches" and "coils" and most everything else in MPF, this is a section that
contains all your DMDs. Now since this is a DMD, you probably only have one,
(though MPF can support as many as you want), but it's important to note that
you add a ``rgb_dmds:`` section to your config, then under that you
add an entry for a specific DMD (which can be whatever you want), and then
you enter one or more of the following settings:

.. config


Optional settings
-----------------

The following sections are optional in the ``rgb_dmds:`` section of your config. (If you don't include them, the default will be used).

brightness:
~~~~~~~~~~~
Single value, type: ``number`` (will be converted to floating point). Default: ``1.0``

Brightness value multiplied in software (as an OpenGL shader in MC).
Using ``hardware_brightness`` is preferred if your hardware supports it.

channel_order:
~~~~~~~~~~~~~~
Single value, type: ``string`` (case-insensitive). Default: ``rgb``

Channel order of your rgb dmd.
Change this if colors are swapped on your hardware.
Any order (such as ``rgb``, ``grb``, ``brg`` and so) will work.

fps:
~~~~
Single value, type: ``integer``. Default: ``30``

How many frames per second this DMD will be updated. Note that some RGB DMDs
cannot handle the full 30fps, so you might have to dial this back to around
25 or so or else the DMD won't be able to keep up and will get behind.

gamma:
~~~~~~
Single value, type: ``number`` (will be converted to floating point). Default: ``2.2``

Sets the gamma of the DMD. See :doc:`instructions/gamma_correction` for details.

Note that the default setting of ``2.2`` will probably be ok, though if your
RGB DMD does its own internal gamma correction, you'll want to set the gamma
to ``1.0`` (which is effectively disabling it).

Note that gamma is closely related to brightness (below). You'll probably
want to adjust both of them together.

.. important:: Gamma setting is important!

   We can't stress enough that setting the gamma for your DMD is important for
   making it look right. So click the link above and make the adjustment. It's
   a one-time thing.

hardware_brightness:
~~~~~~~~~~~~~~~~~~~~
Single value, type: ``number`` or ``template`` (will be converted to floating point; :doc:`Instructions for entering templates </config/instructions/dynamic_values>`). Default: ``1.0``

A brightness multiplier for the DMD (because RGB DMDs are crazy bright).
Note that brightness is closely related to gamma (see above). You'll probably
want to adjust both of them together.

.. include:: template_setting.rst

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

Not used currently.


Related How To guides
---------------------

* :doc:`/hardware/dmd_platforms`
* :doc:`/displays/display/rgb_dmd`
