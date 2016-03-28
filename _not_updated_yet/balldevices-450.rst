
The *ball_devices:*config file section contains settings for the
various `Ball Devices`_ in a pinball machine. This sectioncan be used
in your machine-wide config files. This sectioncanbe used in mode-
specific config files. Here's an example:


::

    
    ball_devices:
    
        trough:
            tags: trough, home, drain
            label: Main Trough
            ball_switches: s_trough1, s_trough2, s_trough3, s_trough4, s_trough5, s_trough6, s_troughJam
            entrance_count_delay: 0.5s
            eject_coil: c_trough
            confirm_eject_type: target
            eject_targets: right_shooter_lane
            jam_switch: s_trough_jam
    
        right_shooter_lane:
            tags: ball_add_live
            label: Right Plunger Lane
            ball_switches: s_shooter_right
            entrance_count_delay: 0.3s
            eject_coil: c_shooter_right
            confirm_eject_type: target
    
        left_shooter_lane:
            label: Left Plunger Lane
            ball_switches: s_shooter_left
            entrance_count_delay: 0.3s
            eject_coil: c_shooter_left
            confirm_eject_type: count
            exit_count_delay: 0.5s






ball_capacity:
~~~~~~~~~~~~~~

Optional value for how many balls this device can hold. You only need
to specify this if your device holds more balls that it has
*ball_switches* for. (In other words, probably99% of the ball devices
in the world don't need this because they have one switch for each
ball.) Some devices, like the Dead World lock in *Judge Dredd* or the
gumball machine in *Twilight Zone* don't have a 1-to-1 mapping for
ball switches to balls held, so you would use this setting to tell MPF
how many balls that device can hold. Default will be set to the number
of *ball_switches* there are.



ball_missing_target:
~~~~~~~~~~~~~~~~~~~~

When a ball is goes missing from a device, this is the name of the
ball device that will get the ball added to it. (After all, the ball
didn't just vaporize. It went somewhere.) The default is *playfield*.
(In other words, if a ball disappears from a device, MPF assumes it's
on the playfield unless you specific a different device here.) Most
devices have ball switches which means that a ball which disappears
from a device that only has an exit to another device will be picked
up by that device. But if you have a device that leads into another
device that doesn't know how many balls it has, or if you have
multiple playfields, you can set that target here. Default is
*playfield*.



ball_missing_timeouts:
~~~~~~~~~~~~~~~~~~~~~~

A list of timeouts (in `MPF time string format`_) that correspond to
how much time after a ball goes missing passes before MPF assumes that
ball went into this device's target device. This is a list, so you can
enter multiple values to match the multiple entries in your
*eject_targets:* list. If you don't enter a value here, or if the
number of values you enter here are less than the number of eject
targets this device has, MPF use *20 seconds* as the default.



ball_switches:
~~~~~~~~~~~~~~

A list of switch names that are active when a ball is in the device.
It's assumed there is a one-to-one *ball switch* to *ball* ratio, so
if you have three switches then MPF assumes that device can hold three
balls. (Note that if your device can hold more balls than it has
switches for, like the gumball machine in *Twilight Zone*, then you
can use the *ball_capacity:*setting to specify how many balls it can
hold.) MPF uses these switches to count how many balls a device has at
any time by counting how many of them are active. Note that "active
switch" means "there is a ball here." So if you have a trough with
opto switches which "invert" their state, then you will have to
configure those switches with the "NC" (normally closed) type in the
*`switches:`_* section of your config file. Default is *None*.
(Meaning this device tracks the number of balls it has virtually based
on *entrance_switch* activations.)



captures_from:
~~~~~~~~~~~~~~

This is the name of the ball device that this device captures balls
from. In other words, if a ball randomly appears in this device, it
assumes it came from this *captures_from* device. Default is
*playfield*.



confirm_eject_event:
~~~~~~~~~~~~~~~~~~~~

This is the name of the event that will be used to confirm a
successful ball eject if you have *confirm_eject_type: event*. Default
is *None*.



confirm_eject_switch:
~~~~~~~~~~~~~~~~~~~~~

This is the name of the switch activationthat will be used to confirm
a successful ball eject if you have *confirm_eject_type: switch*.
Default is *None*.



confirm_eject_type:
~~~~~~~~~~~~~~~~~~~

Whenever the a ball device attempts to eject a ball, it needs to
verify that the ball was actually ejected properly. There are several
ways that eject verification can take place, and this option allows
you to specify which verification method you want. Note that many of
these options require further configuration settings. Options for
confirming the eject include:


+ * event * - The ball device willlook for a specific event, and when
  it sees that event, it knows the eject was successful. This can be any
  event you want, specified via the *confirm_eject_event:* setting.
+ * switch * - If your ball device has a switch which is activated
  when the ball exits, you can use this *switch*type of confirmation.
  Then when the ball device sees this switch become active (even if it's
  momentary), it knows the eject was successful. An example of this
  might be if there's a switch on the ball gateat the top of a plunger
  lane. Note that you only want to use this type of eject confirmation
  if the eject confirmation switch cannot be activated by balls on the
  playfield. Otherwise if you're trying to eject a ball when you already
  have one in play, you wouldn't know if the newly-ejected ball hit that
  switch or if an existing live ball hit it. This can be any switch you
  want, specified via the *confirm_eject_switch:*setting.
+ * target *- This device will confirm the eject via a ball
  successfully entering the "target" device it was ejecting the ball to.
  (The target device is one of the entries from your *eject_targets:*
  list and can either be a *ball device* or the *playfield*. Note that
  if the target device is a playfield and the playfield already has an
  active ball, then the eject confirmation will be changed to *count*
  since it wouldn't know if a playfield switch being hit was based on
  the newly-ejected ball or one of the existing playfield balls.
+ * count * - The device will confirm the eject when it notices that a
  ball is "missing". You can set a value for *exit_count_delay* if you
  want to wait longer than your typical switch count delay to make sure
  the ball really made it out.
+ * fake * - This is a setting that's used by other devices (such as
  the ball lock) when they do not want to use eject confirmation because
  they have another way of confirming the eject. It's not an option that
  you would use when setting up devices, but it's included here in case
  you happen to see a reference to it in the code or the log files.


Default is *count*.



eject_coil:
~~~~~~~~~~~

The coil that is fired to eject a ball from this device.This
*eject_coil* is optional, since some devices (like a manual plunger or
the playfield) don't have eject coils. Default is *None*.



eject_coil_jam_pulse:
~~~~~~~~~~~~~~~~~~~~~

This is the pulse time, in ms, that the eject coil will use if the jam
switch is active and the first eject attempt failed to eject the ball.
(In other words, if the jam switch is active, the ball device will try
to eject the ball with the regular pulse time. If that fails, then
subsequent ejects will use this pulse time instead. Default is *None*
which means the ball device will not change the pulse time after 2
attempts.



eject_coil_retry_pulse:
~~~~~~~~~~~~~~~~~~~~~~~

The new pulse time, in ms, that the eject coil will use if the eject
has failed 3 times. This pulse time is used on the 4th pulse up until
the device stops trying. Default is *None* which means the ball device
will not change the pulse time after 3 attempts.



eject_targets:
~~~~~~~~~~~~~~

A list of one or more ball devices and/or the word "playfield" which
is used to specify all the ball devices this device can directly eject
a ball to. This is a very important concept and can be somewhat
confusing, so bear with us as we try to explain it. Every time a ball
device ejects a ball, MPF needs to "confirm" that the ball was
successfully ejected. There are several different methods which can be
used to confirm the eject, and you configure which method you want to
use for each ball device via the *confirm_eject_type:* setting. In
many cases, it's possible that a single ball device can actually eject
a ball into one of several different targets. For example, in *Star
Trek: The Next Generation*, the main plunger catapult fires the ball
into the top of the playfield where there is a controlled drop target
blocking the entrance to a subway. If that drop target is up, then the
ball bounces off it and then is live on the playfield. If that drop
target is down, a ball ejected from the catapult flies past it and
into the subway. Once in the subway, there is a series of diverters
which can activate or deactivate to route the ball to either the *left
VUK*, the *leftcannon*, or the *right cannon*. In that machine, the
*left VUK*, *left cannon*, and *right cannon* are all ball devices. So
the *eject_targets:* setting looks like this:


::

    
    eject_targets: playfield, bd_leftVUK, bd_leftCannonVUK, bd_rightCannonVUK


In other words, the *eject_targets:* list is a list of *all possible
ball devices* that this device can eject a ball to. Notice that the
word *playfield* is also in that list, because if that drop target is
up, then the ball ejected from the catapult ends up on the playfield,
so *playfield* is a valid target too. (In MPF, the playfield is also a
ball device.) At this point you might be wondering what the point of
this is? The reason you specify all these target devices is because
MPF's ball controller and ball device code work hand-in-hand with
MPF's diverter code to automatically "route" balls to ball devices
that want them. So in *Star Trek*, you can use a command to say "the
left VUK should have one ball," and MPF will see the source device for
that ball (the *catapult*, in this case, since it includes
*bd_leftVUK*in its list of eject targets) and it will cause the
catapult to eject a ball. (What's happening behind the scenes is that
the catapult posts an event which says "I'm ejecting a ball with a
target destination of the *bd_leftVUK*"), and all the diverters
(including that top drop target) will see that and automatically
position themselves accordingly so the ball gets to where it needs to
go. Note that you only want to include devices in this list that are
directly accessible as targets for balls ejecting from this device. In
other wordsyour machine will probably have lots of ball locks and
other devices that the player can hit via flippers and balls from the
playfield. Those devices should not be on this list, because
technically balls enter them from the playfield, not from the
catapult. The order of your *eject_targets:* list doesn't really
matter except for the first entry. If a ball device is ever asked to
eject a ball but a target is not specified, then the first entry on
this list will be used as the target. (In practice this shouldn't
really ever happen.) The default is *playfield*.



eject_timeouts:
~~~~~~~~~~~~~~~

This is an optional list of one or more `MPF time strings`_ that
specify how long the device should wait for an ejected ball to be
confirmed before it assumes the eject failed. The order you enter them
here matches up with the order of your *eject_targets*. For example,
consider the following two lines from aball device configuration:


::

    
    eject_targets: playfield, bd_leftVUK, bd_leftCannonVUK, bd_rightCannonVUK
    eject_timeouts: 500ms, 2s, 4s, 4s


When this device is ejecting a ball to the *playfield*, the timeout
will be *500ms*. When it's ejecting to the *bd_leftVUK*, the timeout
is *2 seconds*, etc. If you don't specify a list of eject timeouts, or
if the length of the list is less than the number of eject targets,
then the default value of *10 seconds* is used.



entrance_count_delay:
~~~~~~~~~~~~~~~~~~~~~

This is the time delay (in `MPF time string format)`_ that this ball
device will wait before counting the balls after any of the
*ball_switches* changes state. This delay exists because there's often
a "settling time" when a ball first enters a device where the balls
are bouncing around and the switches change state really fast. Default
is *500ms*.



entrance_switch:
~~~~~~~~~~~~~~~~

The name of a switch that is activated when a ball enters the device.
Most devices don't have this, since they have the ball switches that
are updated and will count the balls. But some devices, like those
that do not have switches for each ball, have a switch at the entrance
that is triggered when a ball enters. This switch has no effect if
your ball device has *ball_switches*. Default is *None*.



exit_count_delay:
~~~~~~~~~~~~~~~~~

This is the time delay that the device will wait before counting the
balls after any after it attempts to eject a ball if the device is
configured to verify the eject via a count of the switches. You can
enter values here in seconds or milliseconds.See the full explanation
of the time duration formats `here`_. Default is *500ms*.



hold_coil_release_time:
~~~~~~~~~~~~~~~~~~~~~~~

This is the time (in `MPF time string format)`_ that devices with
*hold_coils* will hold their coil open to release a ball. Default is
*1 second*.



hold_coil:
~~~~~~~~~~

The name of a coil that is held in the enabled position to hold a
ball. This is used in place of an *eject_coil*, and it's for devices
that have to hold (like a post) to keep a ball in the device.
Disabling the hold coil releases a ball. Default is *None*.



hold_switches:
~~~~~~~~~~~~~~

A switch (or list of switches) that indicates a ball is in position to
be captured by a *hold_coil*. Default is *None*.



jam_switch:
~~~~~~~~~~~

Some pinball trough devices have a switch in the "exit lane" part of
the trough that can detect if a ball fell back into the trough from
the plunger lane. (The extra switch is needed because when the trough
ejects the ball, the remaining balls in the trough will all roll down,
so if the ejected ball falls back in, it ends up sitting "on top" of
the existing balls, so a normal trough ball switch won't see it.) This
switch is known by different names by different manufacturers, having
variously been called *trough jam*, *ball up* switch, or *ball
stacked* switch. If your ball device has a switch that can detect
jams, enter that switch name here. The ball device code in the MPF has
a jam switch handler which watches what happens to that switch. For
example, if there's an eject in progress and the jam switch becomes
active, it assumes the ball fell back in and will trythe eject again.
Default is *None*.



max_eject_attempts:
~~~~~~~~~~~~~~~~~~~

Defines how many times this ball device will attempt to eject a ball
before deciding that the eject permanently failed. A value of zero
Default is *0* which means there's no limit. (e.g. the device will
just keep trying to eject the ball forever.)



mechanical_eject:
~~~~~~~~~~~~~~~~~

Boolean setting which is used to specify whether this ball device has
a mechanical eject option. In MPF, a *mechanical eject* is what
happens when a player is able to eject a ball from the ball device
mechanically, without MPF knowing about it. (A traditional spring-
powered plunger is the most common use.) This setting is used because
when a mechanical eject happens, from MPF's standpoint it's like the
ball just disappeared, so this setting is used to let MPF know that
that might happen. Set this to *True* if a mechanical eject is an
option for this ball device. Note that it's entirely possible to have
devices that support both mechanical ejects as well as coil-fired
ejects (with an *eject_coil*), such as a plunger lane with a spring
plunger and a coil-fired collar which can be used in auto or manual
mode. Default is *False*. However, if this device does not have an
*eject_coil* or *hold_coil* defined, then the mechanical_eject setting
will automatically be set to *True*.



Device Control Events
---------------------

Device control events are events you can use to control devices. They
are configured in your machine-wide or mode config with settings that
end in *_events*. For example, if a device has a setting for
*enable_events:* and you add an event to that setting, then when that
event is posted, the device will enable. You can add single events or
lists of events to these settings, and you can also configure time-
delays for how much time passes between the event being posted and the
action to take place. Details are available in the `device control
event documentation`_. Ball devices make use of the following device
control events:



eject_all_events:
~~~~~~~~~~~~~~~~~

Causes this ball device to eject all its balls. Default is *None*.



eject_events:
~~~~~~~~~~~~~

Causes this ball device to eject one ball. Default is *None*.



hold_events:
~~~~~~~~~~~~

Causes this ball device to enable its hold coil. Default is *None*.



request_ball_events:
~~~~~~~~~~~~~~~~~~~~

Causes this ball device to request a ball. Default is *None*.



stop_events:
~~~~~~~~~~~~

Causes this ball device to stop all activity, including canceling any
ejects or eject confirmations that are in progress. Does not cause
this device to eject any balls. Default is *None*.



Settings that apply to all device types
---------------------------------------

There are some settings that apply to all types of devices that also
apply here.



tags:
~~~~~

A list of one or more tags that apply to this device. Tags allow you
to access groups of devices by tag name. MPF also uses tags for ball
devices for special purposes, including:


+ home - Specifies that any balls here are "home" and that the game
  can start.When MPF boots up, any balls that are in devices not tagged
  with "home" are automatically ejected.
+ ball_add_live - Used to tag the device you want to use to launch new
  balls into play. Typically this is the plunger device.
+ drain -Specifies that a ball entering this device means the ball has
  "drained" from the playfield. (i.e. it's used to indicate a player
  lost the ball, versus some other random playfield lock.)
+ trough -Specifies that this device holds the ball(s) that are not in
  play. In most cases, your "drain" and "trough" tags will be the same
  device, though older games (Williams System 11 and early WPC) actually
  have two devices under the apron, with a "drain" device receiving
  balls from the playfield which it then immediately kicks over to a
  "trough" device which holds the balls that are not in play.




label:
~~~~~~

The plain-English name for this device that will show up in operator
menus and trouble reports.



debug:
~~~~~~

Set this to *true* to add lots of logging information about this shot
to the debug log. This is helpful when you’re trying to troubleshoot
problems with this shot. Default is *False*.

.. _here: /docs/configuration-file-reference/entering-time-duration-values/
.. _switches:: https://missionpinball.com/docs/configuration-file-reference/switches/
.. _MPF time string format): https://missionpinball.com/docs/configuration-file-reference/important-config-file-concepts/entering-time-duration-values/
.. _Ball Devices: https://missionpinball.com/docs/mpf-core-architecture/devices/logical-devices/ball-device/
.. _device control event documentation: https://missionpinball.com/docs/configuration-file-reference/important-config-file-concepts/configuring-device-control-events/


