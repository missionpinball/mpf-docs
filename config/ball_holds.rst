ball_holds:
===========

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+

The ``ball_holds:`` section of your config is used to list and configure
:doc:`ball holds </game_logic/ball_holds/index>`.

Note that ball holds are used to temporarily hold a ball while the game is doing something
else. (Starting a video mode, playing an intro show, etc.) If you want to hold and lock
a ball towards multiball, use the ``ball_locks:`` section instead.

Ball holds do not affect the "balls in play" count, and they are not used
to hold balls from ball-to-ball or between players.

Here's an example

.. code-block:: mpf-config

   #! switches:
   #!    s_ball1:
   #!       number:
   #! coils:
   #!    c_eject:
   #!       number:

   ball_devices:
      bd_bunker:
         eject_coil: c_eject
         ball_switches: s_ball1

   ball_holds:
      bunker:
         balls_to_hold: 1
         hold_devices: bd_bunker

Each sub-entry under the ``ball_holds:`` section is the name of the logical ball
hold ("bunker") in the example above. Then each named ball hold has the
following settings:

Required settings
-----------------

The following sections are required in the ``ball_holds:`` section of your config:

hold_devices:
~~~~~~~~~~~~~
List of one (or more) values, each is a type: string name of a ``ball_devices:`` device.

A list of one (or more) ball devices that will collect balls which
will count towards this hold.

Optional settings
-----------------

The following sections are optional in the ``ball_holds:`` section of your config. (If you don't include them, the default will be used).

balls_to_hold:
~~~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``None``

The number of balls this ball hold should hold. If you don't include it, then
the ball hold capacity will be automatically calculated based on the combined
capacity of all the ball devices that make up this ball hold.

If one of the associated hold devices receives a ball and this ball hold is
full, then the ball device will just release the ball again.

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

Event(s) which disable this ball hold.

enable_events:
~~~~~~~~~~~~~~
List of one or more events (with optional delay timings), in the
:doc:`device control events </config/instructions/device_control_events>` format.

Default: ``None`` (Note that if you add an entry here, it will replace the default. So if you
also want the default value(s) to apply, add them too.)

Event(s) which enable this ball hold.

label:
~~~~~~
Single value, type: ``string``. Default: ``%``

A descriptive label.

release_one_if_full_events:
~~~~~~~~~~~~~~~~~~~~~~~~~~~

List of one or more events (with optional delay timings), in the
:doc:`device control events </config/instructions/device_control_events>` format.

Default: ``None`` (Note that if you add an entry here, it will replace the default. So if you
also want the default value(s) to apply, add them too.)

Event(s) which cause this ball hold to release a single ball only if the ball
hold contains the number of balls that matches its ``balls_to_hold:`` setting.

release_one_events:
~~~~~~~~~~~~~~~~~~~
List of one or more events (with optional delay timings), in the
:doc:`device control events </config/instructions/device_control_events>` format.

Default: ``None`` (Note that if you add an entry here, it will replace the default. So if you
also want the default value(s) to apply, add them too.)

Event(s) which cause this ball hold to release a single ball.

reset_events:
~~~~~~~~~~~~~

List of one or more events (with optional delay timings), in the
:doc:`device control events </config/instructions/device_control_events>` format.

Default: ``machine_reset_phase_3, ball_starting, ball_will_end, service_mode_entered`` (Note that if you add an entry here, it will replace the default. So if you
also want the default value(s) to apply, add them too.)

Event(s) which cause this ball hold to reset its held ball count.

.. todo:: more detail needed

source_playfield:
~~~~~~~~~~~~~~~~~
Single value, type: string name of a ``ball_devices:`` device. Default: ``playfield``

The name of the playfield that feeds balls to this hold. If you only
have one playfield (which is most games), you can leave this setting
out. Default is the playfield called *playfield*.

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

Special / reserved tags for ball holds: *None*

See the :doc:`documentation on tags </config/instructions/tags>` for details.
