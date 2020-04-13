diverters:
==========

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

You create and configure your diverters in the *diverters:* section of
your machine configuration file. Here's an example from *Star Trek: The Next Generation*:

.. code-block:: mpf-config

   #! switches:
   #!   s_ball1:
   #!     number:
   #!   s_ball2:
   #!     number:
   #!   s_ball3:
   #!     number:
   #!   s_ball4:
   #!     number:
   #!   s_ball5:
   #!     number:
   #!   s_under_ueft_hole:
   #!     number:
   #!   s_under_borg_hole:
   #!     number:
   #!   s_under_top_hole:
   #!     number:
   #!   s_under_left_hole:
   #!     number:
   #!   s_enter_left_ramp:
   #!     number:
   #! coils:
   #!   c_eject1:
   #!     number:
   #!   c_eject2:
   #!     number:
   #!   c_eject3:
   #!     number:
   #!   c_eject4:
   #!     number:
   #!   c_eject5:
   #!     number:
   #!   c_top_divertor:
   #!     number:
   #!   c_under_divertor_top:
   #!     number:
   #!   c_under_divertor_bottom:
   #!     number:
   #!   c_top_drop_down:
   #!     number:
   #!   c_top_drop_up:
   #!     number:
   #! ball_devices:
   #!   bd_borg_ship:
   #!     eject_coil: c_eject1
   #!     ball_switches: s_ball1
   #!   bd_catapult:
   #!     eject_coil: c_eject2
   #!     ball_switches: s_ball2
   #!   bd_left_vuk:
   #!     eject_coil: c_eject3
   #!     ball_switches: s_ball3
   #!   bd_left_cannon_vuk:
   #!     eject_coil: c_eject4
   #!     ball_switches: s_ball4
   #!   bd_right_cannon_vuk:
   #!     eject_coil: c_eject5
   #!     ball_switches: s_ball5
   diverters:
     top_diverter:
       activation_coil: c_top_divertor      # WMS uses the -tor spelling
       type: hold
       activation_time: 3s
       activation_switches: s_enter_left_ramp
       enable_events: ball_started
       disable_events: ball_ended, borg_lock_Lit
       targets_when_active: playfield
       targets_when_inactive: bd_borg_ship
     subway_top_diverter:
       activation_coil: c_under_divertor_top
       type: hold
       activation_time: 3s
       activation_switches: s_under_top_hole, s_under_left_hole, s_under_borg_hole
       targets_when_active: bd_left_cannon_vuk
       targets_when_inactive: bd_left_vuk
       feeder_devices: bd_catapult
     subway_bottom_diverter:
       activation_coil: c_under_divertor_bottom
       type: hold
       activation_time: 3s
       activation_switches: s_under_top_hole, s_under_ueft_hole, s_under_borg_hole
       targets_when_active: bd_left_cannon_vuk
       targets_when_inactive: bd_left_vuk
       feeder_devices: bd_catapult
     drop_target:
       activation_coil: c_top_drop_down
       deactivation_coil: c_top_drop_up
       type: pulse
       targets_when_active: bd_left_cannon_vuk, bd_right_cannon_vuk, bd_left_vuk
       targets_when_inactive: playfield
       feeder_devices: bd_catapult

.. config


Optional settings
-----------------

The following sections are optional in the ``diverters:`` section of your config. (If you don't include them, the default will be used).

activate_events:
~~~~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

Default: ``None``

Events in this list, when posted, cause this diverter to activate.

activation_coil:
~~~~~~~~~~~~~~~~
Single value, type: string name of a :doc:`coils <coils>` device. Defaults to empty.

The name of the coil that is used to activate your diverter.

activation_switches:
~~~~~~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: string name of a :doc:`switches <switches>` device. Defaults to empty.

A list of one or more switches that trigger the diverter to activate.
This switch only activates the diverter if the diverter has been
enabled (either manually or via one of the *enable_events*. If you
have an activation switch, MPF writes a hardware autofire coil rule to
the pinball controller which fires the diverter automatically when the
*activation_switch* is hit. This is done so the diverter will have
instantaneous response time, needed to get the diverter to fire in
time to catch a fast-moving ball.

activation_time:
~~~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`). Default: ``0``

This is how long the diverter stays active once it's been activated.
A value of zero (or omitting
this setting) means this diverter does not timeout, and it will stay
active until it's disabled or you manually deactivate it.

allow_multiple_concurrent_ejects_to_same_side:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``true``

.. todo:: :doc:`/about/help_us_to_write_it`

ball_search_hold_time:
~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`). Default: ``1s``

How long this diverter will be activated for when it is activated during ball search.

ball_search_order:
~~~~~~~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``100``

A relative value which controls the order individual devices are pulsed when ball search is running. Lower numbers are
checked first. Set to ``0`` if you do not want this device to be included in the ball search.
See the :doc:`/game_logic/ball_search/index` documentation for details.

cool_down_time:
~~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`). Default: ``0``

How long does the diverter need to cool down until the next eject can happen
into the diverter?

deactivate_events:
~~~~~~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

Events in this list, when posted, cause this diverter to deactivate.

deactivation_coil:
~~~~~~~~~~~~~~~~~~
Single value, type: string name of a :doc:`coils <coils>` device. Defaults to empty.

The name of the coil that's used to deactivate your diverter. You only
need to specify this coil if it's a different coil from from
*activation_coil*. (In other words this is only used with diverters
that have two coils.)

An example of this is when a drop target is used
to block the entrance of a ball device. (For example, the drop target
under the saucer in *Attack from Mars*, the drop target to the left of
the upper lanes in *Star Trek: The Next Generation*, or the middle
letter "D" drop target in *Judge Dredd*.) Each of these has one coil
to "knock down" the drop target and a second coil to "reset" the drop
target.

By the way, if you have two coils to control a diverter, it
doesn't really matter which one is the *activation_coil* and which is
the *deactivation_coil*. Just know that after the *activation_coil* is
fired, MPF will consider that diverter to be in the active state, and
once the *deactivation_coil* is fired, MPF will consider that diverter
to be in the inactive state, and set up your targets accordingly.

deactivation_switches:
~~~~~~~~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: string name of a :doc:`switches <switches>` device. Defaults to empty.

A list of one or more switches that will deactivate a diverter. (For
example, this might be a switch that's "after" the diverter in a
subway, so once this switch is activated then MPF knows the ball made
it through the diverter and it can deactivate it.)

disable_events:
~~~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

Events in this list, when posted, disable this diverter. Typically it's *ball_ending* (which is posted
when a ball is in the process of ending), meaning this diverter will
not be enabled when the next ball is started. You might also set a
disable event to occur based on the event posted from a mode ending.

disable_switches:
~~~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: string name of a :doc:`switches <switches>` device. Defaults to empty.

A list of one more more switches that will automatically disable this
diverter. It's optional, since the diverter will also be disabled
based on one of your *disable_events* being posted.

enable_events:
~~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

Events in this list, when posted, enable this diverter. (Remember that enabling a diverter is not the
same as activating it.)

feeder_devices:
~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: string name of a :doc:`ball_devices <ball_devices>` device. Default: ``playfield``

This is a list of one or more ball devices that can eject balls which
have the option of being sent to this diverter. This is an important
part of the diverter's ability to automatically route balls to the
devices they go to.

When you configure a *feeder_device:* setting for
a diverter, it causes the diverter to watch for balls ejecting from
that device. Every ball that's ejected in MPF has a "target" (either a
ball device or the playfield), so when a diverter's feeder device
ejects a ball, the diverter will see what the eject target is, and if
that target is included in the diverter's list of
*targets_when_active* or *targets_when_inactive*, then the diverter
will activate or deactivate itself to make sure the balls gets to
where it needs to go.

playfield:
~~~~~~~~~~
Single value, type: string name of a :doc:`playfields <playfields>` device. Default: ``playfield``

The name of the playfield that this diverter is on. The default setting is "playfield", so you only have to
change this value if you have more than one playfield and you're managing them separately.

reset_events:
~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Default: ``machine_reset_phase_3``

Reset will disable the diverter.

targets_when_active:
~~~~~~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: string name of a :doc:`ball_devices <ball_devices>` device. Default: ``playfield``

This is a list of *all* ball devices that can be reached by a ball
passing through this diverter when it's active. Valid options include
the names of ball devices and the word "playfield."

This setting
exists because diverters in MPF can be configured so that they
automatically activate or deactivate when one of their target devices
wants a ball. For example, if you have a diverter on a ramp that will
route a ball to a lock when its active, you can add the name of that
ball device here. Then if that device ever needs a ball, the diverter
will automatically activate to send a ball there. This greatly
simplifies programming, because all you have to do is essentially say,
"I want this device to have a ball," and MPF will make sure the
diverter sets itself appropriately to get a ball to that device.

Let's
look at the diverter configuration from *Star Trek: The Next
Generation* included at the top of this section for an example. In the
settings for the *dropTarget* diverter, notice that there are three
items in the *targets_when_active:* list: *bd_leftCannonVUK*,
*bd_rightCannonVUK*, and *bd_leftVUK*. This means that when this
diverter is active, balls passing through it are able to reach any one
of those three ball devices. Note that this particular diverter
doesn't exactly know how the ball gets to any of those devices—that's
actually handled via additional downstream diverters (
*subwayTopDiverter* and *subwayBottomDiverter*). All the *dropTarget*
diverter needs to know is, "If a ball needs to go to one of these
three diverters, then I better be active."

targets_when_inactive:
~~~~~~~~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: string name of a :doc:`ball_devices <ball_devices>` device. Default: ``playfield``

This is exactly like the *target_when_active:*above, except it
represents the target devices that a ball can reach when this diverter
is disabled. Looking at the same *dropTarget* diverter example from
above, we see that when the *dropTarget* is inactive, the ball is
routed to the playfield.

type:
~~~~~
Single value, type: one of the following options: hold, pulse. Default: ``hold``

Specifies how the *activation_coil* should be activated. You have two
options here:

+ ``pulse`` - MPF will pulse the coil to activate the diverter.
+ ``hold`` - MPF should hold the diverter coil in a constant state of
  "on" when the diverter is active. Note that if the coil is configured
  with a *default_hold_power*, then it will use that pwm pattern to hold the
  coil on. If no *default_hold_power* is configured, then MPF will use a
  continuous enable to hold the coil. (In this case you would need to
  add *allow_enable: true* or *max_hold_power* to that coil's configuration in the *coils:*
  section of your machine configuration file.)

console_log:
~~~~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``basic``

Log level for the console log for this device.

debug:
~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

Set this to ``True`` to see more debug output.

file_log:
~~~~~~~~~
Single value, type: one of the following options: none, basic, full. Default: ``basic``

Log level for the file log for this device.

label:
~~~~~~
Single value, type: ``string``. Default: ``%``

Name in service mode.

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Defaults to empty.

Tags are currently unused.


Related How To guides
---------------------

* :doc:`/mechs/diverters/index`
