How to run the "MC Demo" example
================================

The :doc:`MPF Examples <mpf-examples> GitHub repository includes a machine
configuration called "MC Demo" which is a demo of many different features of
the MPF media controller. Here are a few random screen shots of it:

.. image:: images/mc_demo.jpg

You can run it and use the arrow keys on your computer to step through
different slides, and then you can look at the source config file to see how
it all works.

It's designed to both show you what's possible and to show you how to do
different things with the MC.

1. Download the MPF examples bundle
-----------------------------------

Instructions :doc:`here <mpf-examples>`.

2. Run it
---------

Open a command prompt or terminal window, and change to the "mc_demo" folder
in the "mpf-examples" package you downloaded. Then run:

::

   mpf mc

Note that the MC Demo is an MC configuration only—it does not require or use
the MPF game engine, so that's why you can run ``mpf mc`` and not ``mpf`` or
``mpf both``. (You can run ``mpf both`` and that's fine too.)

When you run the demo, use the left and right arrow keys to step through the
different slides.

3. Check out the config (with notes!)
-------------------------------------

You can browse the complete config in the ``mc_demo/config/config.yaml`` file.
Or check it out online `here <https://github.com/missionpinball/mpf-examples/blob/dev/mc_demo/config/config.yaml>`_.
