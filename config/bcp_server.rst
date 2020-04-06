bcp_server:
===========

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **NO**  |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``servers:`` setting in your ``bcp:`` section of your config is where
you configure listeners for incoming BCP connections.

.. config


Required settings
-----------------

The following sections are required in the ``bcp_server:`` section of your config:

type:
~~~~~
Single value, type: ``string``.

The class to implement the transport.
Use ``mpf.core.bcp.bcp_socket_client.BCPClientSocket`` to use the standard
MPF BCP protocol.


Optional settings
-----------------

The following sections are optional in the ``bcp_server:`` section of your config. (If you don't include them, the default will be used).

ip:
~~~
Single value, type: ``string``.

The IP to bind the server on.
Starting in MPF 0.33, you can use ``ip: None`` and MPF will listen for incoming
connections on all network interfaces.

port:
~~~~~
Single value, type: ``integer``. Default: ``5050``

The port to listen for incoming connections.


Related How To guides
---------------------

* :doc:`/displays/mc/unity_bcp_server`
* :doc:`/displays/mc/creating_your_own`
