Plugin player
=============

The *plugin player* isn't a regular config player, rather, it's a stub that developers can use to add their own types
of config players.

For example, MPF-MC uses the plugin player to add three additional config players: *slide player*, *widget player*, and
*sound player*. Since sounds and display are handled by MPF-MC, the MPF core doesn't know anything about sounds or
displays, so this is how MPF-MC is able to add its features to MPF shows and config files.