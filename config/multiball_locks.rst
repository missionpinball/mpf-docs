multiball_locks:
================

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **NO**  |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+

.. overview

The ``multiball_locks:`` section of your config is used to configure ball locks
which will lock balls for multiball. Note that if you only want to hold a ball
temporarily (like to play a show for an award) and then release it, use the
:doc:`/config/ball_holds` section instead.

Multiball lock devices are smart. They work with physical ball devices but
track the number of balls locked virtually which is not necessarily the same
as the number of balls that are physically contained in a ball device.

When a ball is locked, it will add a new ball into play from the ball device
which is set in ``default_source_device`` of your playfield unless the device
that just locked it is full,
in which case it will eject a ball from the full device. The events that
control the ball ejections are queue events, so you can interrupt the delivery
of a new ball with the :doc:`/config/queue_relay_player` (for example, to have
a mode selection screen before returning to play).

Whenever a new ball is locked, the event *multiball_lock_<name>_locked_ball*
is posted with an argument "total_balls_locked". When the lock is full, it
will post *multiball_lock_<name>_full*, which you can use as a start event
for a related :doc:`/config/multiballs` to start multiball. (And since the
multiball lock tracks the "virtual" ball lock count on a per-player basis,
this will still work even if another player previously emptied out the lock.
(In that case, the multiball will add any additional balls it needs from the
trough.)

Here's an example:

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
   ##! mode: mode1
   multiball_locks:
     bunker:
       balls_to_lock: 3
       lock_devices: bd_bunker

Each sub-entry under the ``multiball_locks:`` section is the name of the multiball
lock ("bunker") in the example above. Then each named ball lock has the
following settings:

.. config


Required settings
-----------------

The following sections are required in the ``multiball_locks:`` section of your config:

balls_to_lock:
~~~~~~~~~~~~~~
Single value, type: ``integer``. Defaults to empty.

The number of balls this ball lock should hold. If one of the
associated lock devices receives a ball and this logical ball lock is
full, then the ball device will just release the ball again.

lock_devices:
~~~~~~~~~~~~~
List of one (or more) values, each is a type: string name of a :doc:`ball_devices <ball_devices>` device. Defaults to empty.

A list of one (or more) ball devices that will collect balls which
will count towards this lock.


Optional settings
-----------------

The following sections are optional in the ``multiball_locks:`` section of your config. (If you don't include them, the default will be used).

balls_to_replace:
~~~~~~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``-1``

By default a multiball lock will immediately replace every ball it locks with a
new ball from the default device (i.e. the trough). With this setting you can
instruct the lock to replace only up to a certain number of locked balls. A
value of 0 means the lock will never replace balls, and -1 means it will always
replace balls (default).

This setting is useful for machines that physically lock multiple balls in a lock
and replace them from the trough. When a full lock starts a multiball, for example,
you may not want the game to add another ball from the trough. Usually this setting
will be used in tandem with replace-balls-in-play from :doc:`/config/multiballs`.

Caution: an improperly configured setting can lead the player to a state where
no balls are active on the playfield and the game becomes stuck. See
:doc:`/game_logic/multiballs/multiball_with_traditional_ball_lock` for instructions
and examples.

disable_events:
~~~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

Default: ``None`` (Note that if you add an entry here, it will replace the default. So if you
also want the default value(s) to apply, add them too.)

Event(s) which disable this ball lock, meaning that balls that enter one of the
lock devices don't count towards the lock. If you want to set up a ball lock that
requires the player to "re-light" the lock after locking a ball, you can set this
ball lock's "ball_locked" event as a disable event for this lock and then set some
other shot that re-enables the lock as an enable event.

enable_events:
~~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

Default: ``None`` (Note that if you add an entry here, it will replace the default. So if you
also want the default value(s) to apply, add them too.)

Event(s) which enable this ball lock. If this multiball lock is disabled, then a ball
entering one of its ball devices does not count towards the lock. You can use this
in situations where a player has to hit some other shot to first re-light the lock
before a ball can be locked. (In that case you'd use the event posted by the light
lock shot as one of the enable_events here.

locked_ball_counting_strategy:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: one of the following options: virtual_only, min_virtual_physical, physical_only, no_virtual. Default: ``virtual_only``

See the :doc:`general multiball lock documentation </game_logic/multiballs/multiball_locks>`
for an explanation of how each of these works.

priority:
~~~~~~~~~
Single value, type: ``integer``. Default: ``1``

Relative priority when claiming balls entering a device.
This can be used to give one :doc:`ball_hold <ball_holds>` or
:doc:`multiball_lock <multiball_locks>` preference when claiming balls.

reset_all_counts_events:
~~~~~~~~~~~~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

Event(s) which reset the locked ball counts for all players.

reset_count_for_current_player_events:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

Event(s) which reset the locked ball count for the current player.

source_playfield:
~~~~~~~~~~~~~~~~~
Single value, type: string name of a :doc:`ball_devices <ball_devices>` device. Default: ``playfield``

The name of the playfield that feeds balls to this lock. If you only
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

Name of this device in service mode.

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Defaults to empty.

Not used.


Related How To guides
---------------------

* :doc:`/game_logic/multiballs/index`
