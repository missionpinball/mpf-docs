Tools
=====

There are several tools which have been created to help you build your game in MPF.

:doc:`MPF Monitor <monitor/index>`
----------------------------------

The MPF Monitor is a graphical utility you can use to interact with a running instance of MPF. See lights
change in action, click to control switches, and lay out everything on an image of your playfield.

:doc:`"Interactive" MC (or "iMC") <imc/index>`
----------------------------------------------

The interactive MC lets you create YAML configurations for slides and widgets in realtime and see them
on a display. This is great for fine tuning and tweaking your slides.

:doc:`Service Cli <service_cli/index>`
--------------------------------------

The MPF service cli is a fast way to debug or troubleshoot your machine during
development and operation.

:doc:`Lightshow Creator <showcreator/index>`
--------------------------------------------

A lightshow generator for MPF.

Machine Fuzzer
--------------

Fuzz your machine using afl to find crashes in MPF, your config or your code.
Currently not documented. Let us know if you want to use it.

Hardware Debugger
-----------------

The hardware debugger allows you to scan all your configured hardware platforms.
In some cases it also supports firmware updates and configuration settings.
See :doc:`mpf hardware </running/commands/hardware>` for details.


Future Tools
------------

* GUI config builder
* Music builder / looper / manager
* Show builder
* Slide / animation tool
* Auto machine documentation builder
* Device / asset explorer (Why did this sound stop? Why is this LED red? etc)


.. toctree::
   :titlesonly:
   :hidden:

   monitor/index
   imc/index
   service_cli/index
   showcreator/index
