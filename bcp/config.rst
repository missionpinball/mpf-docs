config (BCP command)
====================

**Parameters:** variable1=value1&variable2=value2&etc=etc **Origin:**
Pin controller or media controller **Response:** None Config is
effectively the same as “set”, with the additional expectation that
the value will be stored to disk so as to be available at next start
or reset. A game may use any set of config variables it wants, but
here are someexamples of what they could be:
**Name** **Description** **credits** Set the number of credits in the
system. This would be a decimal number such as 1 or 1.3, or it might
be “free_play” **custom_message** Set the custom system message.
Newline values must be percent-encoded. **language** This allows the
pin controller to request a specific flavor of the presentation.
**grand_champ** Set info about the grand champion. Value format would
be initials,score. Initials may not contain commas. **high_score_N**
Set info about the one of the high scores. Value format would be
initials,score. Initials may not contain commas. **rating** This
allows the pin controller to specify a “movie rating” for the machine.
An example would be controlling “pg” versus “r” ratings for games such
as Sopranos, which can include risqué language, sounds, images, etc.
**volume_master** Set the masteraudio volume. volume_sfx Set the
volume of the sfx track.
