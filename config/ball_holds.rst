ball_holds:
===========

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+

.. overview

The ``ball_holds:`` section of your config is used to list and configure
:doc:`ball holds </game_logic/ball_holds/index>`.

Note that ball holds are used to temporarily hold a ball while the game is doing something
else. (Starting a video mode, playing an intro show, etc.) If you want to hold and lock
a ball towards multiball, use the ``multiball_locks:`` section instead.

Ball holds do not affect the "balls in play" count, and they are not used
to hold balls from ball-to-ball or between players.

Here's an example

.. code-block:: mpf-config

   #! switches:
   #!   s_ball1:
   #!     number:
   #! coils:
   #!   c_eject:
   #!     number:
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

.. config


Required settings
-----------------

The following sections are required in the ``ball_holds:`` section of your config:

hold_devices:
~~~~~~~~~~~~~
List of one (or more) values, each is a type: string name of a :doc:`ball_devices <ball_devices>` device. Defaults to empty.

A list of one (or more) ball devices that will collect balls which
will count towards this hold.


Optional settings
-----------------

The following sections are optional in the ``ball_holds:`` section of your config. (If you don't include them, the default will be used).

balls_to_hold:
~~~~~~~~~~~~~~
Single value, type: ``integer``. Defaults to empty.

The number of balls this ball hold should hold. If you don't include it, then
the ball hold capacity will be automatically calculated based on the combined
capacity of all the ball devices that make up this ball hold.

If one of the associated hold devices receives a ball and this ball hold is
full, then the ball device will just release the ball again.

disable_events:
~~~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

Event(s) which disable this ball hold.

enable_events:
~~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

Event(s) which enable this ball hold.

priority:
~~~~~~~~~
Single value, type: ``integer``. Default: ``0``

Relative priority when claiming balls entering a device.
This can be used to give one :doc:`ball_hold <ball_holds>` or
:doc:`multiball_lock <multiball_locks>` preference when claiming balls.

release_all_events:
~~~~~~~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

Event(s) which cause this ball hold to release all balls.

release_one_events:
~~~~~~~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

Event(s) which cause this ball hold to release a single ball.

release_one_if_full_events:
~~~~~~~~~~~~~~~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

Event(s) which cause this ball hold to release a single ball only if the ball
hold contains the number of balls that matches its ``balls_to_hold:`` setting.

reset_events:
~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Default: ``machine_reset_phase_3, ball_starting, ball_will_end, service_mode_entered``

Event(s) which cause this ball hold to reset its held ball count.

source_playfield:
~~~~~~~~~~~~~~~~~
Single value, type: string name of a :doc:`ball_devices <ball_devices>` device. Default: ``playfield``

The name of the playfield that feeds balls to this hold. If you only
have one playfield (which is most games), you can leave this setting
out. Default is the playfield called *playfield*.

console_log:
~~~~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``basic``

Log level for the console log for this device.

debug:
~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

See the :doc:`documentation on the debug setting </config/instructions/debug>`
for details.

file_log:
~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``basic``

Log level for the file log for this device.

label:
~~~~~~
Single value, type: ``string``. Default: ``%``

A descriptive label.

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Defaults to empty.

Special / reserved tags for ball holds: *None*

See the :doc:`documentation on tags </config/instructions/tags>` for details.


Related How To guides
---------------------

* :doc:`/game_logic/ball_holds/index`
* :doc:`/game_design/game_modes/mystery_award`
* :doc:`/game_logic/ball_locks/index`
* :doc:`/mechs/scoops/index`
