How to configure mono/traditional DMD (FAST Pinball)
====================================================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/dmds`                                                          |
+------------------------------------------------------------------------------+

The FAST WPC and Core controllers can drive traditional single-color
pinball DMDs via the 14-pin DMD connector cable that's been in most
pinball machines for the past 25 years, like this:

.. image::  /hardware/images/display_mono_dmd.jpg

It makes no difference as to whether you're using an LED or an original
plasma gas DMD. (Also it doesn't matter what color it is.)

1. Verify your port settings
----------------------------

In order to use a DMD with a FAST Pinball controller, you need to have the
port that's connected to the DMD processor on the FAST board listed in the
``ports:`` section in the ``fast:`` section of your machine-wide config.

See the :doc:`config` guide for details.

2. Add a physical DMD device entry
----------------------------------

Once you have your hardware and port set, you need to create the actual device
entry for the DMD.

You do this in the ``dmds:`` section of the machine config. This
section is like the other common sections (switches, coils, etc.) where you
enter the name(s) of your device(s), and then under each one, you enter its
settings.

(And yes, in case you're wondering, it's possible to have more than one
physical DMD.)

To do this, create a section in your machine-wide config called
``dmds:``, and then pick a name for the DMD, like this:

.. code-block:: mpf-config

    dmds:
      my_dmd:
        shades: 16

You need to have at least one setting for this to be a valid YAML file, so we
usually just pick the ``shades`` and add that with a value of ``16`` (which
means the DMD runs will convert the display content to 16 mono shades when it
displays it).

The "shades" option is how many brightness shades you want. 1990s WPC machines
supported 4 shades, and modern Stern DMD machines support 16. The FAST Pinball
controllers support 16 shades (even on older 1990s plasma DMDs). Most
modern games will probably be 16 shades, but you can do 4 (or even 2) if you
want an old school look.

There are lots more options for the physical_dmd: section than just the
"shades" option listed here. Check the :doc:`/config/dmds` for a list
of all the options.

Note that one option you do NOT have for physical DMDs is the color. That's
because the color of the DMD is determined by the DMD itself. You don't actually
send it color values, rather, you just send it brightness levels, and the DMD
shows those brightness levels with whatever color the DMD is.

3. Set a source display
-----------------------

Now that you have everything configured, the last step is to make sure the DMD
knows what content to show. In MPF, you do this by mapping a physical DMD to
an :doc:`MPF display </displays/display/index>`.

By default, the DMD will look for a display (in your :doc:`/config/displays`
section called "dmd". However you can override this and configure the DMD to
use whatever logical display you want by setting a ``source_display:``
setting. (Just make sure that the width and height of your source display match
the physical pixel dimensions of the DMD or else it will be weird.)

A final config you can test
---------------------------

At this point you're all set, and whatever slides and widgets are shown on the
DMD's source display in MPF-MC should be shown on the physical DMD.

That said, all these options can be kind of confusing, so we created a quick
example config you can use to make sure you have yours set right. (You can
actually just save this config to ``config.yaml`` in a blank machine folder
and run it to see it in action which will verify that you've got everything
working properly.)

To run this sample config, you can run ``mpf both``.

When you run it, do not use the ``-x`` or ``-X`` options, because either of
those will tell MPF to not use physical hardware which means it won't try to
connect to the Teensy.

Note that the :doc:`/displays/display/dmd` guide has more details
on the window and slide settings used in this machine config.

.. code-block:: mpf-mc-config

   hardware:
     platform: fast
   fast:
     ports: com3, com4, com5  # be sure to change this to your actual ports
     driverboards: fast
   displays:
     window:  # on screen window
       width: 600
       height: 200
     dmd:  # source display for the DMD
       width: 128
       height: 32
       default: true
   window:
     width: 600
     height: 200
     title: Mission Pinball Framework
     source_display: window
   dmds:
     my_dmd:
       brightness: 1.0
   slides:
     window_slide_1:  # slide we'll show in the on-screen window
       - type: display
         effects:
           - type: dmd
             dot_color: ff5500
         width: 512
         height: 128
       - type: text
         text: MISSION PINBALL FRAMEWORK
         anchor_y: top
         y: top-3
         font_size: 30
       - type: rectangle
         width: 514
         height: 130
         color: 444444
     dmd_slide_1:  # slide we'll show on the physical DMD
       - type: text
         text: IT WORKS!
         font_size: 25
   slide_player:
     init_done:
       window_slide_1:
         target: window
       dmd_slide_1:
         target: dmd
   ##! test
   #! assert_text_on_top_slide "MISSION PINBALL FRAMEWORK" window
   #! assert_text_on_top_slide "IT WORKS!" dmd

What if it did not work?
------------------------

Have a look at our :doc:`FAST troubleshooting guide <troubleshooting>`.
