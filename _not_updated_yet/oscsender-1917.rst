
`osc_sender.py` is a command line tool which sends OSC commands to an
OSC server, such as the Mission Pinball Framework with the OSC plug-
in. (It will also work with pyprocgame with the `OSC mode Brian
created`_ for it.) It’s located in the MPF download package at
`/tools/osc_sender.py`. This tool was originally created in response
to a request on the `PinballControllers.com forum`_for someone who
wanted to send switch events to his pinball machine via a web page,
but really the sky’s the limit with this thing since you could script
it or tie it into whatever you want. You can read a list of the
various OSC addresses MPF uses in the documentation section about
`configuring OSC clients`_. To use it, pass two parameters. First is
the OSC address (the thing with slashes, *not* the host IP address),
and then the data, like this:


::

    
    python osc_sender.py /sw/start 1


By default this utility will also send a second OSC message with “0”
as the data to the same address after the first one is sent. Otherwise
you’d have to use it twice to activate the switch and then deactivate
the switch. If you want to not do this (like if you want to set a
switch and then keep it set), then add a `-t` command line option to
enable “toggle” mode. Also this will pull the local IP address via
Python, but that might not be the IP address you want to use (like if
you’re using it on a network or if there is more than one IP and it’s
grabbing the wrong one). In that case use the `-s` command line option
to specify an IP address (like `-s 10.0.1.14`). This utility will use
the default port of 8000 as the target port on the OSC server it’s
looking for. Use the command line option `-p` to specify a different
port. This OSC Sender is generic and not pinball specific at all. It
just sends your OSC address and data to whatever OSC server you want,
then exits. Run it as often as you want.

.. _PinballControllers.com forum: http://www.pinballcontrollers.com/forum/index.php?topic=1394
.. _OSC mode Brian created: https://missionpinball.com/blog/2013/11/controlling-pyprocgame-via-an-iphone-or-ipad-with-osc/
.. _configuring OSC clients: https://missionpinball.com/docs/plugins/osc-module/configuring-osc-clients/


