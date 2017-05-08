How to change the TCP ports MPF uses
====================================

.. note:: The functionality for changing the BCP port in the MPF-MC was added
   in MPF-MC v0.32.10.

Various MPF components talk to each other via a TCP socket protocol called
BCP (which we invented). By default, MPF and MPF-MC each
listen for incoming BCP connections on the following two TCP ports:

* ``5050`` MPF-MC
* ``5051`` MPF

When MPF-MC starts up, it starts listening on port 5050. If the MPF game engine
doesn't connect, MPF-MC will sit there and wait for it. No problem.

When the MPF game engine starts, it attempts to connect to the MC on port 5050.
If it can't make a connection, it will try again, and keep trying until a
connection is made. (Note that you can control the behavior of this in the
config files.)

The MPF game engine also listens for incoming BCP connections on 5051. This is
not used by MPF-MC, but is used by other things that need to connect to MPF,
such as the MPF Monitor.

If you have a port conflict (because something else on your system is using
port 5050 or 5051), then you can change the MPF and MPF-MC ports to whatever
you want. Just add the following two sections to your machine-wide config
file. Note that you have to change it in two places, the "bcp" section which
is what the MPF game engine reads to know what port the MC is listening on,
and the "mpf-mc" section which is what the MC reads to know what port it should
listen on.

Valid port numbers are anything between 1024 and 65535.

::

   # config_version=4

bcp:
  connections:
     local_display:
        port: 1234

mpf-mc:
  bcp_port: 1234
