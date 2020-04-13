ball_devices:
=============

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``ball_devices:`` section of your config is where you configure your :doc:`ball devices </mechs/ball_devices/index>`.

You can find examples here:

* :doc:`Troughs </mechs/troughs/index>`
* :doc:`Plungers </mechs/plungers/index>`
* :doc:`Scoops/Vertical UP Kickers (VUKs)/Saucer Holes </mechs/scoops/index>`

.. config


Optional settings
-----------------

The following sections are optional in the ``ball_devices:`` section of your config. (If you don't include them, the default will be used).

auto_fire_on_unexpected_ball:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``true``

If a ball randomly shows up in this device, should it be automatically ejected?

ball_capacity:
~~~~~~~~~~~~~~
Single value, type: ``integer``. Defaults to empty.

Optional value for how many balls this device can hold. You only need
to specify this if your device holds more balls that it has
*ball_switches* for. (In other words, probably 99% of the ball devices
in the world don't need this because they have one switch for each
ball.) Some devices, like the Dead World lock in *Judge Dredd* or the
gumball machine in *Twilight Zone* don't have a 1-to-1 mapping for
ball switches to balls held, so you would use this setting to tell MPF
how many balls that device can hold. Default will be set to the number
of *ball_switches* there are.

ball_missing_target:
~~~~~~~~~~~~~~~~~~~~
Single value, type: string name of a :doc:`playfields <playfields>` device. Default: ``playfield``

When a ball is goes missing from a device, this is the name of the
ball device that will get the ball added to it. (After all, the ball
didn't just vaporize. It went somewhere.) The default is *playfield*.
(In other words, if a ball disappears from a device, MPF assumes it's
on the playfield unless you specify a different device here.) Most
devices have ball switches which means that a ball which disappears
from a device that only has an exit to another device will be picked
up by that device. But if you have a device that leads into another
device that doesn't know how many balls it has, or if you have
multiple playfields, you can set that target here. Default is
*playfield*.

ball_missing_timeouts:
~~~~~~~~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: ``time string (ms)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`). Defaults to empty.

A list of timeouts that correspond to
how much time after a ball goes missing passes before MPF assumes that
ball went into this device's target device. This is a list, so you can
enter multiple values to match the multiple entries in your
*eject_targets:* list. If you don't enter a value here, or if the
number of values you enter here are less than the number of eject
targets this device has, MPF uses *20 seconds* as the default.

ball_search_order:
~~~~~~~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``200``

A relative value which controls the order individual devices are pulsed when ball search is running. Lower numbers are
checked first. Set to ``0`` if you do not want this device to be included in the ball search.
See the :doc:`/game_logic/ball_search/index` documentation for details.

ball_switches:
~~~~~~~~~~~~~~
List of one (or more) values, each is a type: string name of a :doc:`switches <switches>` device. Defaults to empty.

A list of switch names that are active when a ball is in the device.
It's assumed there is a one-to-one *ball switch* to *ball* ratio, so
if you have three switches then MPF assumes that device can hold three
balls. (Note that if your device can hold more balls than it has
switches for, like the gumball machine in *Twilight Zone* , then you
can use the *ball_capacity:* setting to specify how many balls it can
hold.) MPF uses these switches to count how many balls a device has at
any time by counting how many of them are active. Note that "active
switch" means "there is a ball here." So if you have a trough with
opto switches which "invert" their state, then you will have to
configure those switches with the "NC" (normally closed) type in the
``switches:`` section of your config file. Default is *None* .
(Meaning this device tracks the number of balls it has virtually based
on *entrance_switch* activations.)

captures_from:
~~~~~~~~~~~~~~
Single value, type: string name of a :doc:`playfields <playfields>` device. Default: ``playfield``

This is the name of the ball device that this device captures balls
from. In other words, if a ball randomly appears in this device, it
assumes it came from this *captures_from* device. Default is
*playfield*.

confirm_eject_event:
~~~~~~~~~~~~~~~~~~~~
Single event. The device will add an handler for this event. Defaults to empty.

This is the name of the event that will be used to confirm a
successful ball eject if you have ``confirm_eject_type: event``.

confirm_eject_switch:
~~~~~~~~~~~~~~~~~~~~~
Single value, type: string name of a :doc:`switches <switches>` device. Defaults to empty.

This is the name of the switch activation that will be used to confirm
a successful ball eject if you have ``confirm_eject_type: switch``.

confirm_eject_type:
~~~~~~~~~~~~~~~~~~~
Single value, type: one of the following options: target, switch, event, fake. Default: ``target``

Whenever the a ball device attempts to eject a ball, it needs to
verify that the ball was actually ejected properly. There are several
ways that eject verification can take place, and this option allows
you to specify which verification method you want. Note that many of
these options require further configuration settings. Options for
confirming the eject include:

+ ``target`` (default) - This device will confirm the eject via a ball
  successfully entering the "target" device it was ejecting the ball to.
  (The target device is one of the entries from your *eject_targets:*
  list and can either be a *ball device* or the *playfield*. Note that
  if the target device is a playfield and the playfield already has an
  active ball, then the eject confirmation will be changed to *count*
  since it wouldn't know if a playfield switch being hit was based on
  the newly-ejected ball or one of the existing playfield balls.
+ ``event`` - The ball device will look for a specific event, and when
  it sees that event, it knows the eject was successful. This can be any
  event you want, specified via the *confirm_eject_event:* setting.
+ ``switch`` - If your ball device has a switch which is activated
  when the ball exits, you can use this *switch*type of confirmation.
  Then when the ball device sees this switch become active (even if it's
  momentary), it knows the eject was successful. An example of this
  might be if there's a switch on the ball gate at the top of a plunger
  lane. Note that you only want to use this type of eject confirmation
  if the eject confirmation switch cannot be activated by balls on the
  playfield. Otherwise if you're trying to eject a ball when you already
  have one in play, you wouldn't know if the newly-ejected ball hit that
  switch or if an existing live ball hit it. This can be any switch you
  want, specified via the *confirm_eject_switch:* setting.
+ ``fake`` - This is a setting that's used by other devices (such as
  the ball lock) when they do not want to use eject confirmation because
  they have another way of confirming the eject. It's not an option that
  you would use when setting up devices, but it's included here in case
  you happen to see a reference to it in the code or the log files.

eject_all_events:
~~~~~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

Causes this device to eject all its balls.

eject_coil:
~~~~~~~~~~~
Single value, type: string name of a :doc:`coils <coils>` device. Defaults to empty.

The coil that is fired to eject a ball from this device.This
*eject_coil* is optional, since some devices (like a manual plunger or
the playfield) don't have eject coils. Default is *None*.

eject_coil_enable_time:
~~~~~~~~~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: ``time string (ms)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`). Defaults to empty.

When using an ``eject_coil`` and specifying ``eject_coil_enable_time`` MPF
will enable to ``eject_coil`` for ``eject_coil_enable_time`` instead of
pulsing that coil.

eject_coil_jam_pulse:
~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`). Defaults to empty.

This is the pulse time, in ms, that the eject coil will use if the jam
switch is active and the first eject attempt failed to eject the ball.
(In other words, if the jam switch is active, the ball device will try
to eject the ball with the regular pulse time. If that fails, then
subsequent ejects will use this pulse time instead. Default is *None*
which means the ball device will not change the pulse time after 2
attempts.

eject_coil_max_wait_ms:
~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`). Default: ``200ms``

MPF might delay the eject by ``eject_coil_max_wait_ms`` to ensure consistent
pulses. See :doc:`psus` for details.

eject_coil_reorder_pulse:
~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`). Defaults to empty.

Pulse duration to use to reorder balls. If the ball device assumes that the
balls are not settled properly it will pulse the ``eject_coil`` for
``eject_coil_reorder_pulse`` and recount the balls. This might happen
if multiple balls disappear or the ``jam_switch`` is active.

eject_coil_retry_pulse:
~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`). Defaults to empty.

The new pulse time, in ms, that the eject coil will use if the eject
has failed too many times. This pulse time is used up until the device stops trying.
Default is *None* which means the ball device will not change the pulse time after failed attempts.

Note that the number of times the ball device will attempt the eject before increasing
the pulse time is controlled in the ``retries_before_increasing_pulse:`` setting.

eject_events:
~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

Causes this device to eject one ball.

eject_targets:
~~~~~~~~~~~~~~
List of one (or more) values, each is a type: string name of a :doc:`ball_devices <ball_devices>` device. Default: ``playfield``

A list of one or more ball devices and/or the word "playfield" which
is used to specify all the ball devices this device can directly eject
a ball to. This is a very important concept and can be somewhat
confusing, so bear with us as we try to explain it.

Every time a ball
device ejects a ball, MPF needs to "confirm" that the ball was
successfully ejected. There are several different methods which can be
used to confirm the eject, and you configure which method you want to
use for each ball device via the *confirm_eject_type:* setting.

In many cases, it's possible that a single ball device can actually eject
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

.. code-block:: yaml

    eject_targets: playfield, bd_leftVUK, bd_leftCannonVUK, bd_rightCannonVUK

In other words, the *eject_targets:* list is a list of *all possible
ball devices* that this device can eject a ball to.

Notice that the
word *playfield* is also in that list, because if that drop target is
up, then the ball ejected from the catapult ends up on the playfield,
so *playfield* is a valid target too. (In MPF, the playfield is also a
ball device.)

At this point you might be wondering what the point of
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
go.

Note that you only want to include devices in this list that are
directly accessible as targets for balls ejecting from this device. In
other words your machine will probably have lots of ball locks and
other devices that the player can hit via flippers and balls from the
playfield. Those devices should not be on this list, because
technically balls enter them from the playfield, not from the
catapult.

The order of your *eject_targets:* list doesn't really
matter except for the first entry. If a ball device is ever asked to
eject a ball but a target is not specified, then the first entry on
this list will be used as the target. (In practice this shouldn't
really ever happen.)

eject_timeouts:
~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: ``time string (ms)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`). Defaults to empty.

This is an optional list of one or more MPF time strings that
specify how long the device should wait for an ejected ball to be
confirmed before it assumes the eject failed. The order you enter them
here matches up with the order of your *eject_targets*. For example,
consider the following two lines from a ball device configuration:

.. code-block:: yaml

    eject_targets: playfield, bd_leftVUK, bd_leftCannonVUK, bd_rightCannonVUK
    eject_timeouts: 500ms, 2s, 4s, 4s

When this device is ejecting a ball to the *playfield*, the timeout
will be *500ms*. When it's ejecting to the *bd_leftVUK*, the timeout
is *2 seconds*, etc. If you don't specify a list of eject timeouts, or
if the length of the list is less than the number of eject targets,
then the default value of *10 seconds* is used.

See :doc:`/finalization/ball_devices` for details about thouse timeouts.

ejector:
~~~~~~~~
Unknown type. See description below.

You ejector implemententation and settings.
By default MPF will select an implementation based on the settings and
configure it accordingly.

Default ejectors (you can use those via the ball device config):

* mpf.devices.ball_device.pulse_coil_ejector.PulseCoilEjector
* mpf.devices.ball_device.enable_coil_ejector.EnableCoilEjector
* mpf.devices.ball_device.hold_coil_ejector.HoldCoilEjector

Additional ejectors:

* mpf.devices.ball_device.event_ejector.EventEjector

.. code-block:: mpf-config

   #! switches:
   #!   s_ball_switch1:
   #!     number:
   #!   s_ball_switch2:
   #!     number:
   ball_devices:
     device_with_eject_event:
       ejector:
         class: mpf.devices.ball_device.event_ejector.EventEjector
         events_when_eject_try: my_ball_device_eject
       ball_switches: s_ball_switch1, s_ball_switch2

entrance_count_delay:
~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`). Default: ``500ms``

This is the time delay (in MPF time string format) that this ball
device will wait before counting the balls after any of the
*ball_switches* changes state. This delay exists because there's often
a "settling time" when a ball first enters a device where the balls
are bouncing around and the switches change state really fast. Default
is *500ms*.

entrance_event_timeout:
~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``time string (secs)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`). Default: ``5s``

How long does the ball need after an ``entrance_event`` to settle in
the ball device? This is used for some heuristics to determine if this is
a new ball or if the ball returned from a failed eject.

entrance_events:
~~~~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

:doc:`device control events </config/instructions/device_control_events>` format.

Default: ``None`` (Note that if you add an entry here, it will replace the default. So if you
also want the default value(s) to apply, add them too.)

These events tell this ball device that a ball has entered (been added to) the device.

entrance_switch:
~~~~~~~~~~~~~~~~
Single value, type: string name of a :doc:`switches <switches>` device. Defaults to empty.

The name of a switch that is activated when a ball enters the device.
Most devices don't have this, since they have the ball switches that
are updated and will count the balls. But some devices, like those
that do not have switches for each ball, have a switch at the entrance
that is triggered when a ball enters. This switch has no effect if
your ball device has *ball_switches*. Default is *None*.

entrance_switch_full_timeout:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`). Default: ``0``

When using an ``entrance_switch`` and setting this to anything except 0,
the device will be considered to be full after ``entrance_switch_full_timeout``
ms. This is used in some troughs where the last ball sits on the entrance
switch (see :doc:`/mechs/troughs/two_coil_one_switch`).

entrance_switch_ignore_window_ms:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`). Default: ``0``

How long should another entrance switch be ignored after a previous activation?

exit_count_delay:
~~~~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`). Default: ``500ms``

This is the time delay that the device will wait before counting the
balls after any after it attempts to eject a ball if the device is
configured to verify the eject via a count of the switches.

hold_coil:
~~~~~~~~~~
Single value, type: string name of a :doc:`coils <coils>` device. Defaults to empty.

The name of a coil that is held in the enabled position to hold a
ball. This is used in place of an *eject_coil*, and it's for devices
that have to hold (like a post) to keep a ball in the device.
Disabling the hold coil releases a ball. Default is *None*.
An example for such a hold coil is the lock that comes up below Magneto 
in X-Men. A further lock of this kind is in Avatar below Jake Sully 
in the transporter link.

hold_coil_release_time:
~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`). Default: ``1s``

This is the time (in MPF time string format) that devices with
*hold_coils* will hold their coil open to release a ball. Default is
*1 second*.

hold_events:
~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

These events cause this device to enable its hold coil.

hold_switches:
~~~~~~~~~~~~~~
List of one (or more) values, each is a type: string name of a :doc:`switches <switches>` device. Defaults to empty.

A switch (or list of switches) that indicates a ball is in position to
be captured by a *hold_coil*. Default is *None*.

idle_missing_ball_timeout:
~~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``time string (secs)`` (:doc:`Instructions for entering time strings </config/instructions/time_strings>`). Default: ``5s``

How long should the device wait before declaring a ball missing if it
disappeared outside of an eject? Usually balls do not disappear when the
device is not ejecting.

jam_switch:
~~~~~~~~~~~
Single value, type: string name of a :doc:`switches <switches>` device. Defaults to empty.

Some pinball trough devices have a switch in the "exit lane" part of
the trough that can detect if a ball fell back into the trough from
the plunger lane. (The extra switch is needed because when the trough
ejects the ball, the remaining balls in the trough will all roll down,
so if the ejected ball falls back in, it ends up sitting "on top" of
the existing balls, so a normal trough ball switch won't see it.)

This switch is known by different names by different manufacturers, having
variously been called *trough jam*, *ball up* switch, or *ball
stacked* switch. If your ball device has a switch that can detect
jams, enter that switch name here. The ball device code in the MPF has
a jam switch handler which watches what happens to that switch. For
example, if there's an eject in progress and the jam switch becomes
active, it assumes the ball fell back in and will try the eject again.

max_eject_attempts:
~~~~~~~~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``0``

Defines how many times this ball device will attempt to eject a ball
before deciding that the eject permanently failed. A value of zero
means there's no limit. (e.g. the device will just keep trying to eject 
the ball forever.)

mechanical_eject:
~~~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

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

player_controlled_eject_event:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Single event. The device will add an handler for this event. Defaults to empty.

When using player controlled eject wait for this event to autofire the
ball. (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`)

request_ball_events:
~~~~~~~~~~~~~~~~~~~~
List of one (or more) device control events (:doc:`Instructions for entering device control events </config/instructions/device_control_events>`). Defaults to empty.

These events cause this device to request a ball to be sent to it.

retries_before_increasing_pulse:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``4``

The number of times this ball device will attempt to eject the ball before increasing
the eject coil pulse time as specified in the ``eject_coil_retry_pulse:`` above.

Note that this number is the attempts that it will increase the pulse, so the default
setting of 4 means that it will try the original pulse value 3 times and then increase
it on the 4th.

target_on_unexpected_ball:
~~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: string name of a :doc:`ball_devices <ball_devices>` device. Defaults to empty.

Target playfield to use when capturing an unexpected ball.

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

The plain-English name for this device that will show up in operator
menus and trouble reports.

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Defaults to empty.

See the :doc:`documentation on tags </config/instructions/tags>` for details.

Special-purpose tags for ball devices include:

+ ``home`` - Specifies that any balls here are "home" and that the game
  can start. When MPF boots up, any balls that are in devices not tagged
  with "home" are automatically ejected.
+ ``drain`` - Specifies that a ball entering this device means the ball has
  "drained" from the playfield. (i.e. it's used to indicate a player
  lost the ball, versus some other random playfield lock.)
+ ``trough`` - Specifies that this device holds the ball(s) that are not in
  play. In most cases, your "drain" and "trough" tags will be the same
  device, though older games (Williams System 11 and early WPC) actually
  have two devices under the apron, with a "drain" device receiving
  balls from the playfield which it then immediately kicks over to a
  "trough" device which holds the balls that are not in play.
  + ``no-eject-on-ballsearch`` - Specifies that this device should never
  attempt to eject a ball as a result of ball search, even when idle and
  containing no balls.

The use of ``ball_add_live`` is discontinued. Use ``default_source_device`` in
your :doc:`playfield </config/playfields>` instead.


Related How To guides
---------------------

* :doc:`/mechs/ball_devices/index`
