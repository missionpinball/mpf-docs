ball_locks:
===========

*Config file section*

.. include:: _machine_config_yes.rst
.. include:: _mode_config_yes.rst

.. overview

The ``ball_locks:`` section of your config lets you setup logical
ball locks which can be used to physically or virtually lock balls.
This section can be used in your machine-wide config files. This
section can be used in mode-specific config files. Here’s an example:

::

    ball_locks:
        bunker:
            balls_to_lock: 3
            lock_devices: bd_bunker

Required settings
-----------------

The following sections are required in the ``ball_locks:`` section of your config:

<name>:
~~~~~~~

The logical name of this ball lock device.

balls_to_lock:
~~~~~~~~~~~~~~
Single value, type: ``integer``. 

The number of balls this ball lock should hold. If one of the
associated lock devices receives a ball and this logical ball lock is
full, then the ball device will just release the ball again.

lock_devices:
~~~~~~~~~~~~~
List of one (or more) values, each is a type: string name of a ``ball_devices:`` device. 

A list of one (or more) ball devices that will collect balls which
will count towards this lock.

Optional settings
-----------------

The following sections are optional in the ``ball_locks:`` section of your config. (If you don't include them, the default will be used).

debug:
~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

See the :doc:`documentation on the debug setting </config/instructions/debug>`
for details.

disable_events:
~~~~~~~~~~~~~~~
List of one or more events (with optional delay timings), in the
:doc:`device control events </config/instructions/device_control_events>` format.
Default: ``None`` (Note that if you add an entry here, it will replace the default. So if you
also want the default value(s) to apply, add them too.)

Event(s) which disable this ball lock.

enable_events:
~~~~~~~~~~~~~~
List of one or more events (with optional delay timings), in the
:doc:`device control events </config/instructions/device_control_events>` format.
Default: ``None`` (Note that if you add an entry here, it will replace the default. So if you
also want the default value(s) to apply, add them too.)

Event(s) which enable this ball lock.

label:
~~~~~~
Single value, type: ``string``. Default: ``%``

.. todo::
   Add description.

release_on_events:
~~~~~~~~~~~~~~~~~~~
List of one or more events (with optional delay timings), in the
:doc:`device control events </config/instructions/device_control_events>` format.
Default: ``None`` (Note that if you add an entry here, it will replace the default. So if you
also want the default value(s) to apply, add them too.)

Event(s) which cause this ball lock to release a single ball.

request_new_balls_to_pf:
~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``True``

Boolean which controls whether this logical ball lock will
automatically add another ball into play after it locks a ball.

reset_events:
~~~~~~~~~~~~~
List of one or more events (with optional delay timings), in the
:doc:`device control events </config/instructions/device_control_events>` format.
Default: ``None`` (Note that if you add an entry here, it will replace the default. So if you
also want the default value(s) to apply, add them too.)

Event(s) which cause this ball lock to reset its locked ball count.

.. todo:: more detail needed

source_playfield:
~~~~~~~~~~~~~~~~~
Single value, type: string name of a ``ball_devices:`` device. Default: ``playfield``

The name of the playfield that feeds balls to this lock. If you only
have one playfield (which is most games), you can leave this setting
out. Default is the playfield called *playfield*.

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

Special / reserved tags for ball locks: *None*

See the :doc:`documentation on tags </config/instructions/tags>` for details.
