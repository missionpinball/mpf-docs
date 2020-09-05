osc:
====

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``osc:`` section of your config is where you configure the
:doc:`osc platform </hardware/osc/index>`.

.. config


Optional settings
-----------------

The following sections are optional in the ``osc:`` section of your config. (If you don't include them, the default will be used).

events_to_send:
~~~~~~~~~~~~~~~
List of one (or more) events. The device will add handlers for those events. Defaults to empty.

You can list all events which you want to be forwarded to your OSC remote.
This is an example:

.. code-block:: mpf-config

   hardware:
     platform: osc

   osc:
     remote_ip: 127.0.0.1
     remote_port: 8000

     events_to_send:
       - player_score
       - some_non_osc_switch_active
       - some_non_osc_switch_inactive

listen_ip:
~~~~~~~~~~
Single value, type: ``string``. Default: ``127.0.0.1``

The IP MPF should use to listen for incoming UDP OSC connections.
You can also set this to ``0.0.0.0`` if you want MPF to listen on all
interfaces instead of just on loopback (local connections only).

listen_port:
~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``9000``

The port MPF shoud use to listen for incoming UDP OSC connections.

remote_ip:
~~~~~~~~~~
Single value, type: ``string``. Default: ``127.0.0.1``

The IP address of your remote OSC server.
MPF will send all messages to this IP.

remote_port:
~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``8000``

The port of your remote OSC server.


Related How To guides
---------------------

* :doc:`/hardware/osc/index`
