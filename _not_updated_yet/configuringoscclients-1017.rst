
We'll add full documentation for configuring OSC clients soon, but in
the meantime here's the down-and-dirty guide. You need to send an
emptyOSC messageto the address /sync to establish a connection with
the OSC host running as part of MPF. If you've set your machine type
to 'wpc', you can alternately send an empty message to /wpcsync. Using
wpcsync tells MPF to look for and to send WPC coil, switch, and lamp
numbers instead of their names.



Switches
~~~~~~~~

On your client, you can use /sw/switchname to control or display
switch states. MPF will send and OSC data value of 1.0 when a switch
is active, and 0 when it's inactive. On the flip-side, it will expect
to receive a value of 1.0 to activate a switch or 0.0 to deactivate a
switch.



Matrix Lights
~~~~~~~~~~~~~

On your client, you can use /light/lightname to control or display
switch states. MPF will send and OSC data value of 1.0 when a switch
is active, and 0 when it's inactive. On the flip-side, it will expect
to receive a value of 1.0 to activate a lightor 0.0 to deactivate it.



Coils
~~~~~

Send an OSC message to /coil/coilname to pulse that coil. Currently
this only supports pulse, and it's one-way. (i.e. the OSC client will
not display the current status of coils like it does with switches and
lights.



Events
~~~~~~

You can send an OSC message to /ev/eventname to cause MPF to post
whatever event you want.



RGB LEDs
~~~~~~~~

This feature is not yet implemented.



