
(This page is a work in progress) MPF 0.30 introduces
*#config_version=4*. Here are the changes:



New Sections:
-------------

coil_player gi_player flasher_player trigger_player led_player
widget_player



Renamed Sections:
-----------------

In all config_players, "tocks_per_sec" is removed, and a "speed"
option is added (since show steps are based on time instead of tocks)



Removed Sections:
-----------------

timing: hz



Changes:
--------

Power settings for coils in the coil_player have been change to values
from 0.0 to 1.0 instead of 0-100. light_player split to led_player and
light_player All players All "playable" configs are now available both
in shows and slides



