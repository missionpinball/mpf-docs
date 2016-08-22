MPF core modules
================

.. toctree::
   :titlesonly:
   :hidden:

   asset
   asset_loader
   asset_manager
   asset_pool
   ball_controller
   ball_search
   bcp
   bcp_client
   data_manager
   clock
   color_correction_profile
   config_player
   config_processor
   config_validator
   data_manager
   delay_manager
   delay_manager_registry
   device
   device_manager
   events
   file_interface
   file_manager
   logic_block_manager
   machine_controller
   mode
   mode_controller
   platform
   player
   rgb_color
   score_controller
   scriptlet
   shot_profile_manager
   show_controller
   switch_controller

The MPF core engine contains several core system components which live in the
``/mpf/core`` folder. Some of the components do OS-like things (the system
clock, timers, an event manager, task scheduling, etc.), while others are more
pinball-specific (a switch controller, platform drivers, effects controllers,
etc.).

There's really not too much you need to know about the core modules, but we
include descriptions of them here for completeness. We designed MPF to be
flexible and extensible, so anything that is not absolutely 100% required for
every machine is considered a "plugin" and located in the ``/mpf/plugins``
folder. The rest of this documentation section details the OS-like core system
components. Then we have separate documentation sections which cover the
pinball-specific stuff as well as the plugins.
