Media Controllers
=================

One of the most important things to understand about the architecture
of MPF is that the core MPF game engine is completely separate from
the process that controls graphics and audio. We call the thing that
handles graphics and audio a "media controller." The game engine and
media controller talk to each other via something called "BCP"
which is a protocol we created for this purpose which stands for
"Backbox Control Protocol". (More details on BCP are available at the
`MPF developer site <http://developer.missionpinball.org>`_.)

Here's a diagram that shows what each piece does:

.. image:: images/mpf_game_engine_mc.png

Why are the MPF game engine and media controller two separate processes?
Two reasons:

First, having two processes means that each one can run on a separate core
in a multi-core host computer. This makes efficient use of hardware
since the trend is to have multiple cores. If the game engine and
media controller were combined, then your quad-core Raspberry Pi 3
would have all the MPF stuff running on one core while the other three
cores were wasted doing nothing.

Second, having two processes means you can replace MPF's default
media controller with something else if you want different features.
For example, there is a group of people building an open source
:doc:`Unity 3D-based media controller <unity_bcp_server>` which can be
used for very advanced 3D display graphics.

.. toctree::
   :maxdepth: 1

   mpfmc
   unity_bcp_server
   mpf_and_mc_different_machines
   multiple_mcs
   creating_your_own
   display_light_player
