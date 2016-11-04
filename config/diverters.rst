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

::

    diverters:
        top_diverter:
            activation_coil: c_top_divertor # WMS uses the -tor spelling
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
            activation_switches: s_underTopHole, s_underLeftHole, s_underBorgHole
            targets_when_active: bd_rightCannonVUK
            targets_when_inactive: bd_leftVUK
            feeder_devices: bd_catapult
        subway_bottom_diverter:
            activation_coil: c_underDivertorBottom
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

Understanding the difference between "enabling" and "activating" diverters
--------------------------------------------------------------------------

When talking about diverters in MPF, we use the terms *activate* and
*enable* (as well as *deactivate* and *disable*). Even though these
words sound like they're the same thing, they're actually different,
so it's important to understand them.

When a diverter is *active*, that
means it's physically activated in its active position. A diverter
that is *enabled* means that it's ready to be activated, but it's not
necessarily active at this time. To understand this, let's step
through an example.

Imagine a typical ramp in a pinball machine which
has one entrance and two exits. These kinds of ramps usually have a
diverter at the top of them that can send the ball down one of the two
paths. When the diverter is *inactive* (its default state), the ball
goes down one path, and when the diverter is *active*, the ball is
sent down the other path (perhaps towards a ball lock).

There is
typically an entrance switch on the ramp which lets the game know that
a ball is potentially headed towards that diverter, so when the game
wants to route the ball to the "other" ramp exit, rather than turning
on that diverter and holding it on forever, the game just watches for
that ramp entry switch and then quickly fires the diverter to route
the ball to the other exit. Then once the ball passes by the diverter,
it hits a second switch which turns off the diverter. (Typically the
diverter activation also has a timeout which is used when a weak shot
is made where the ball trips the ramp entrance switch but doesn't
actually make it all the way up the ramp to the diverter.)

So in MPF
parlance, we say that the diverter is *enabled* whenever it's ready to
be fired, but it's not actually *active* until the coil is physically
on.

Again using our example, let's say we have a ramp with a diverter,
and when that diverter is *active* it sends a ball into a lock. When
the game starts, the diverter is *disabled* and *inactive*. Ramp shots
just go up the ramp and come out the default path, and the diverter
ignores the ramp entrance switch.

Then when the player does whatever
they need to do to light the lock, the diverter is *enabled*. At this
point the diverter is *not* active since it's not actually firing, but
it's *enabled* (which means it's ready to fire) and the diverter is
watching that ramp entrance switch. (So the diverter is *enabled* but
*inactive*.) Then when the player shoots the ball up that ramp, the
diverter sees the ramp entrance switch hit and the diverter activates.
(So now the diverter is *enabled* and *active*.)

Then once the ball
passes by the diverter, the diverter deactivates. At this point
whether the diverter is disabled or enabled depends on the game logic.
If the lock should stay lit, then the diverter remains enabled even
though it's not *active*, and if the player has to do something else
to re-light the lock, then the diverter is *disabled* and *inactive*.

Hopefully that makes sense? :)

<diverter name>
~~~~~~~~~~~~~~~

Create a subentry in your *diverters:* section for each diverter you
want to create. (Remember that you should create anything that's
activated to change the path of the ball as a diverter, including
traditional diverters, up/down posts, coil-controlled gates, playfield
trap doors, and controlled drop targets which block entrances to
devices.)

Optional settings
-----------------

The following sections are optional in the ``diverters:`` section of your config. (If you don't include them, the default will be used).

activate_events:
~~~~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``ms``. Default: ``None``

Causes this diverter to activate.

activation_coil:
~~~~~~~~~~~~~~~~
Single value, type: string name of a ``coils:`` device. Default: ``None``

The name of the coil that is used to activate your diverter.

activation_switches:
~~~~~~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: string name of a ``switches:`` device. Default: ``None``

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
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings) </config/instructions/time_strings>` . Default: ``0``

This is how long the diverter stays active once it's been activated.
A value of zero (or omitting
this setting) means this diverter does not timeout, and it will stay
active until it's disabled or you manually deactivate it.

deactivate_events:
~~~~~~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``ms``. Default: ``None``

Causes this diverter to deactivate.

deactivation_coil:
~~~~~~~~~~~~~~~~~~
Single value, type: string name of a ``coils:`` device. Default: ``None``

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
List of one (or more) values, each is a type: string name of a ``switches:`` device. Default: ``None``

A list of one or more switches that will deactivate a diverter. (For
example, this might be a switch that's "after" the diverter in a
subway, so once this switch is activated then MPF knows the ball made
it through the diverter and it can deactivate it.)

debug:
~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

.. todo::
   Add description.

disable_events:
~~~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``ms``. Default: ``None``

Disables this diverter. Typically it's *ball_ending* (which is posted
when a ball is in the process of ending), meaning this diverter will
not be enabled when the next ball is started. You might also set a
disable event to occur based on the event posted from a mode ending.

disable_switches:
~~~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: string name of a ``switches:`` device. Default: ``None``

A list of one more more switches that will automatically disable this
diverter. It's optional, since the diverter will also be disabled
based on one of your *disable_events* being posted.

enable_events:
~~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``ms``. Default: ``None``

Enables this diverter. (Remember that enabling a diverter is not the
same as activating it.)

feeder_devices:
~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: string name of a ``ball_devices:`` device. Default: ``playfield``

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

label:
~~~~~~
Single value, type: ``string``. Default: ``%``

.. todo::
   Add description.

reset_events:
~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``ms``. Default: ``machine_reset_phase_3``

.. todo::
   Add description.

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

.. todo::
   Add description.

targets_when_active:
~~~~~~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: string name of a ``ball_devices:`` device. Default: ``playfield``

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
List of one (or more) values, each is a type: string name of a ``ball_devices:`` device. Default: ``playfield``

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
  with a *hold_power*, then it will use that pwm pattern to hold the
  coil on. If no *hold_power* is configured, then MPF will use a
  continuous enable to hold the coil. (In this case you would need to
  add *allow_enable: true* to that coil's configuration in the *coils:*
  section of your machine configuration file.)


