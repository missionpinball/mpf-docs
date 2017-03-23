player_variable (BCP command)
=============================

**Parameters:**name, value, prev_value, change, player_num **Origin:**
Pin controller **Response:** None This is a generic "catch all" which
sends player-specific variables to the media controller any time they
change. Since the pin controller will most likely track hundreds of
variables per player (with many being internal things that the media
controller doesn't care about), it's recommended that the
pin controller has a way to filter which player variables are sent to
the media controller. Also note the parameter *player_num* indicates
which player this variable is for (starting with 1 for the first
player). While it's usually the case that the *player_variable*
command will be sent for the player whose turn it is, that's not
always the case. (For example, when a second player is added during
the first player's ball, the second player's default variables will be
initialized at 0 and a *player_variable* event for player 2 will be
sent even though player 1 is up.
