bcp:
====

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``bcp:`` section of your config file controls how the MPF
core engine communicates with the standalone media controller.

There's a default ``bcp:`` section in the default ``mpfconfig.yaml`` system-wide defaults
section that should be fine to get started, and then you can override
it if needed for a specific situation:

.. code-block:: mpf-config

   bcp:
       connections:
           local_display:
               host: localhost
               port: 5050
               type: mpf.core.bcp.bcp_socket_client.BCPClientSocket
               required: True
               exit_on_close: True

       servers:
           url_style:
               ip: 127.0.0.1
               port: 5051
               type: mpf.core.bcp.bcp_socket_client.BCPClientSocket

       debug: false

connections:
------------

The `connections:` section is where you can specify the connections
the MPF core engine will make to standalone media controllers. MPF
supports connecting to multiple media controllers simultaneously which
is why you can add multiple entries here.

The ``connections:`` section contains the following nested sub-settings

Optional settings
~~~~~~~~~~~~~~~~~

The following sections are optional in the ``connections:`` section of your config. (If you don't include them, the default will be used).

host:
^^^^^
Single value, type: ``string``. Default: ``None``

The host to connect to for this connection.

port:
^^^^^
Single value, type: ``integer``. Default: ``5050``

The port to connect to for this connection.

type:
~~~~~
Single value, type: ``string``. Default: ``None``

The class to implement the transport.
Use ``mpf.core.bcp.bcp_socket_client.BCPClientSocket`` to use the standard
MPF BCP protocol.

More implementations are possible here. For instance, a highly efficient
implemententation for production or an encrypted socket for communication
over the Internet.

required:
---------
Single value, type: ``boolean``. Default: ``True``

Whatever this connection is required for MPF to run.
Set this to false if you want MPF not to wait for this connection on start.

exit_on_close:
--------------
Single value, type: ``boolean``. Default: ``True``

Whatever MPF should exit if this connection disconnects.
This is usually true for the media manager because we want MPF to exit once it
is closed.

servers:
--------
The `servers:` section is where you can specify bcp server instances
which can be connected from other processes.
For instance, this is used for the :doc:`service cli </running/commands/service>`.
MPF supports connecting to multiple servers simultaneously which
is why you can add multiple entries here.

The ``servers:`` section contains the following nested sub-settings

ip:
~~~
Single value, type: ``string``. Default: ``None``

The IP to bind the server on.
Starting in MPF 0.33, you can use ``ip: None`` and MPF will listen for incoming
connections on all network interfaces.

port:
~~~~~
Single value, type: ``int``. Default: ``5050``

The port to bind the server on.

type:
~~~~~
Single value, type: ``string``. Default: ``None``

The class to implement the transport.
Use ``mpf.core.bcp.bcp_socket_client.BCPClientSocket`` to use the standard
MPF BCP protocol.


debug:
~~~~~~
Single value, type: ``boolean``. Default: ``False``

Set this to true to see more debug messages in the log.
