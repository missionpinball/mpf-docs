dmd_frame (BCP command)
=======================

Parameters: data(*see note) Origin: Media controller **Response:**
None Used by the media controller to send a DMD frame to the pin
controller which the pin controller displays on the physical DMD. Note
that this command does not used named parameters, rather, the data is
sent after the command, like this: `dmd_frame?<raw byte string>` This
command is a special one in that it's sent with ASCII encoding instead
of UTF-8. The data is a raw byte string that is exactly 4096 bytes. (1
bytes per pixel, 128x32 DMD resolution = 4096 pixels.)The 4 lowbits of
each byte are the intensity (0-15), and the 4 highbits are ignored.
