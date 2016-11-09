Glossary of MPF terms
=====================

Here's a list of terms you might come across in MPF. Note that this is not an exhaustive list of everything, rather,
these are terms we use in MPF that might not be obvious.

.. glossary::

   display
      A logical target which holds slides. Displays are abstract--purely
      logical. You use the machine config to map logical displays to the
      physical on-screen window or a DMD.

   machine folder
      The folder which holds your machine config files.

   player variable
      A named value that is stored on a per-player basis, such as the current
      ball number or score.

   watch dog
      A feature of a hardware control system that ensures you don't blow
      anything up if MPF crashes. Essentially it's a timer which runs on the
      hardware (typically set to a short amount of time, like 1 second) that
      has to be "pinged" by MPF constantly to reset the timer. If the timer
      runs out before its pinged, then the hardware system will shut off all
      power to its devices. In normal operation, MPF pings the watchdog
      constantly, but if MPF crashes or shuts down ungracefully, then the
      watchdog pings stop, the hardware timer expires, and the hardware
      controller shuts off all the power to the connected devices.

   widget
      A thing that is put on a display. There are different types of widgets,
      such as text, images, videos, shapes, etc.
