mode_start (BCP command)
========================

Parameters: name, priority Origin: Pin controller **Response:** None A
game mode has just started. The mode is passed via the name parameter,
and the mode's priority is passed as an integer via the priority. For
example: `mode_start?name=base&priority=100`.