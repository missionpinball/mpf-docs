rgb_dmds:
=========

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

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

(If you don't include any of the settings below, the default will be used).

hardware_brightness:
~~~~~~~~~~~~~~~~~~~~
Single numeric value, Default: ``0.5``

A brightness multiplier for the DMD. Default is 0.5 which is 50% brightness,
(because LED RGB DMDs are crazy bright!), but you can adjust this higher or
lower as needed.

Note that brightness is closely related to gamma (see below). You'll probably
want to adjust both of them together.

.. include:: template_setting.rst

gamma:
~~~~~~
Single numeric value, Default: ``2.2``

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

fps:
~~~~
Single value, type: ``integer``. Default: ``30``

How many frames per second this DMD will be updated. Note that some RGB DMDs
cannot handle the full 30fps, so you might have to dial this back to around
25 or so or else the DMD won't be able to keep up and will get behind.

only_send_changes:
~~~~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

Specifies whether every frame is sent to the DMD, or only changed frames.

source_display:
~~~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``dmd``

The name of the display (from the ``displays:`` section of your machine config) that is the source for this physical
DMD. Whatever's on the source display will be displayed on the DMD. If you don't specify a source, MPF will
automatically use a source display called "dmd".

platform:
~~~~~~~~~

Single value, type: ``string``. Default: ``None``

Name of the platform this DMD is connected to. The default value of ``None`` means the
default hardware platform will be used. You only need to change this if you have
multiple different hardware platforms in use and this coil is not connected
to the default platform.

See the :doc:`/hardware/platform` guide for details.

