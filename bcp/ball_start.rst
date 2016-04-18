ball_start (BCP command)
========================

Parameters: player_num, ball Origin: Pin controller **Response:** None
Indicates that a ball has started. It passes the player number ("1",
"2", etc.) and the ball number as parameters. This command will be
sent every time a ball starts, even if the same player is shooting
again after an extra ball.
