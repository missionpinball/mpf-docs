How to run MPF and the MPF-MC on different computers
====================================================

Since the BCP protocol uses a standard TCP socket connection, you can actually run MPF and the
MPF-MC on different computers. (We're not sure what the use case for this is exactly, but it's definitely possible.)

To do it, just install MPF on one computer and MPF-MC on another.

Then on the machine running MPF, configure the ``host:`` setting as the name or IP address of the machine running the
MPF-MC, and on the MPF-MC computer, set the ``servers:`` section to listen on the IP address you want to use. (See
the :doc:`bcp section of the config file reference </config/bcp>` for details.

Remember to set the firewall on the computer running MPF-MC to accept incoming connections on the port that BCP is
listening on.

.. warning::

   The BCP protocol has no security, so it's fine if both the computers are inside your pinball machine or on your
   home network, but it's not designed to be run across a public network.
