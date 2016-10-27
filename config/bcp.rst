bcp:
====

*Config file section*

* Valid in machine config files: **YES**
* Valid in mode config files: **NO**

.. overview

The ``bcp:`` section of your config file controls how the MPF
core engine communicates with the standalone media controller.

There's a default ``bcp:`` section in the default ``mpfconfig.yaml`` system-wide defaults
section that should be fine to get started, and then you can override
it if needed for a specific situation:

::

   bcp:
       connections:
           local_display:
               host: localhost
               port: 5050
               connection_attempts: 5
               require_connection: no

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

.. todo::
   Add description.

port:
^^^^^
Single value, type: ``integer``. Default: ``5050``

.. todo::
   Add description.

event_map:
----------

This section contains a list of MPF events that get mapped to BCP
commands. You shouldn't have to change this. This is what MPF uses
internally to map MPF events to the BCP command specification.


+ `<event_name>:` The name of the MPF event you're creating a mapping
  for.
+ `command:` The name of the BCP command that will be sent when the
  MPF event is posted.
+ `params:` A list of parameters that will be passed via BCP along
  with this BCP command.


player_variables:
-----------------

The `player_variables:` section lets you specify which MPF player
variables will be broadcast via BCP to the media controller. (MPF will
send these any time there's a change.) You can either list out the
individual names of the players variables you want to send, like this:


::


        player_variables:
            ball
            extra_balls


Or you can use the entry `__all__` (that's two underscores, the
letters "all", then two more underscores) to send every change of
every player variable to the media controller. Here's an example:


::


        player_variables:
            __all__