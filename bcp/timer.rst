timer (BCP command)
===================

Parameters: name, action, ticks Origin: Pin controller **Response:**
Varies This command allows the pin controller to notify the media
controller about timer action that needs to be communicated to the
player. There are many timers in MPF (configured via the ` `Timers:`
section`_ of a config file). You can enable a timer to send its
details to the media controller by adding a `bcp: yes` setting to a
timer's settings.