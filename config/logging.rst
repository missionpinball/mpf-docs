logging:
========

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

In the logging section you can configure which how verbose parts of MPFs should
log.

.. code-block:: mpf-config

   logging:
     console:
       asset_manager: none
       ball_controller: none
       ball_search: basic
       bcp: basic
       bcp_client: basic
       bcp_interface: basic
       bcp_server: basic
       clock: none
       config_players: none       # todo
       data_manager: none       # todo subclasses
       delay_manager: none
       device_manager: none
       event_manager: none
       file_manager: none       # todo
       logic_blocks: none
       machine_controller: basic
       mode_controller: basic
       placeholder_manager: none
       platforms: none       # todo
       players: basic       # todo
       plugins: none       # todo
       score_reel_controller: none
       scriptlets: none       # todo
       service_controller: basic
       settings_controller: none
       show_controller: none
       switch_controller: basic
       timers: none
     file:
       asset_manager: basic
       ball_controller: basic
       ball_search: basic
       bcp: basic
       bcp_client: basic
       bcp_interface: basic
       bcp_server: basic
       clock: none
       config_players: basic
       data_manager: basic
       delay_manager: none
       device_manager: basic
       event_manager: basic
       file_manager: basic
       logic_blocks: basic
       machine_controller: basic
       mode_controller: basic
       placeholder_manager: basic
       platforms: basic
       players: full
       plugins: basic
       score_reel_controller: basic
       scriptlets: basic
       service_controller: basic
       settings_controller: basic
       show_controller: basic
       switch_controller: full
       timers: none


.. config


Related How To guides
---------------------

.. todo:: :doc:`/about/help_us_to_write_it`
