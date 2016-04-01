Core modules (mpf)
==================

The MPF core engine contains several core system components which live in the
``/mpf/core`` folder. Some of the components do OS-like things (the system
clock, timers, an event manager, task scheduling, etc.), while others are more
pinball-specific (a switch controller, platform drivers, effects controllers,
etc.).

There's really not too much you need to know about the core modules, but we
include descriptions of  them here for completness. We designed MPF to be
flexible and extensible, so  anything that is not absolutely 100% required for
every machine is considered a "plugin" and located in the ``/mpf/plugins``
folder. The rest of this documentation section details the OS-like core system
components. Then we have separate documentation sections which cover the
pinball- specific stuff as well as the plugins.

List of MPF core modules
------------------------

.. toctree::

   
