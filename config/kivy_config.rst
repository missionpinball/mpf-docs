kivy_config:
============

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``kivy_config:`` section of your config is where you configure kivy.

You can directly configure kivy here. Usually you don't need this but in some
cases it allows some additional tweaking (e.g. for embedded workloads).
All options are documented in
`the kivy config documentation <https://kivy.org/docs/api-kivy.config.html#available-configuration-tokens>`_.

This is an example:

.. code-block:: mpf-config

   kivy_config:
     kivy:
       desktop: 1
       exit_on_escape: true
     graphics:
       borderless: false
       fbo: hardware  # hardware, software, force-hardware
       fullscreen: false
       multisamples: 2
       position: auto  # auto, custom
       show_cursor: true
       resizable: true

.. config


Related How To guides
---------------------

* :doc:`/displays/display/multiple_screens`
