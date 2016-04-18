external_show_frame (BCP command)
=================================

Parameters: name, led_data, light_data, flasher_data, gi_data Origin:
Mediacontroller **Response:** None Sends updated device values(LED
colors, light intensities, flasher pulse times, GI brightness) for an
externally-controlled`hardwareshow`_ that is currently running. All of
the data parameters are optional, but at least one must be included in
each external_show_frame command.
Parameter Description name The name of the external show (must be
currently running). led_data Aconcatenated list of hex RGB color
values that correspond to the list of LED names in the *leds*
parameter when the external show was started (ex:
led_data=0000009999990000FF). light_data Aconcatenated list of hex
brightness values (00 to FF) that correspond to the list of light
names in the *lights* parameter when the external show was started
(ex: light_data=0099FF). flasher_data A concatenated list of values (o
= off, 1 = flash) that correspond to the list of flasher names that in
the *flashers* parameter when the external show was started (ex:
0010011). gi_data A concatenated list of hex brightness values (00 to
FF) that correspond to the list of GI names in the *gis* parameter
when the external show was started (ex: 0099FF).
