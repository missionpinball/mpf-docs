---
title: Autofire Coils
---

# Autofire Coils


Related Config File Sections:

* [autofire_coils:](../config/autofire_coils.md)

An autofire coil in MPF is used for "instant response" type devices
(like pop bumpers and slingshots) where you want a switch activation to
trigger a coil as close to instantaneous as possible.

## First, some background...

The Mission Pinball Framework is based on Python. Running a "real"
pinball machine means you have some kind of computer-like board running
Python (Mini ITX x86 computer, Raspberry Pi 3, etc.) which runs your
game, controls the display, and plays your sounds. That computer
connects to your hardware controller (P-ROC, FAST, etc.) to interface
with your actual pinball machine components (switches, coils, lights,
motors, LEDs...).

There are several types of devices in a pinball machine that you want to
react "instantly." For example, when a switch in a slingshot or pop
bumper is activated, you want the coil to fire as fast as possible. When
the player pushes a flipper button, you want that flipper to fire
instantly, and when the player releases the flipper button, you want the
machine to cut power to that flipper coil instantly. Unfortunately if
you think about what the flow chart of activity looks like for that to
happen, there are a lot of steps. (And it's certainly not instant.) For
example, imagine what happens when a ball hits a slingshot:

1.  The slingshot switch is activated.
2.  The hardware controller debounces that switch.
3.  The hardware controller sends a notification that the slingshot
    switch changed state to your Python game code via USB.
4.  Something in your code says, "if the slingshot switch is activated,
    fire the slingshot coil."
5.  The Python game code sends the "fire the slingshot coil" command
    to the hardware controller via USB.
6.  That command is queued on the USB bus and transmitted.
7.  The hardware controller fires the slingshot coil.

Wow! That's a lot of steps just to fire a coil when a switch is hit!
Unfortunately the entire process of all this going from the hardware to
the computer to the game code to the hardware to the coil takes some
time----maybe 10ms or so. But with a fast moving pinball you might find
that it's not fast enough. (What if your game code was in the middle of
updating a bunch of lights and that delayed it another 5ms?) You might
find that by the time your game code gets around to firing the coil
it's too late. In effect your slingshot firing has lag and might miss
the ball altogether. Not good!

Fortunately the people who designed the hardware controllers know this,
so they have options where "autofire" or "trigger" rules can be
written into the hardware controller which the hardware controller can
handle on its own. In the Mission Pinball Framework, we call these types
of rules "Autofire" rules, because we specify that a coil fires
automatically based on some switch event without any involvement of our
host computer or the Python game code.

To use an autofire rule, you specify the name of a switch, the state of
the switch (whether it goes active or inactive), the name of a coil or
driver, and what you want that coil to do. (Turn on, turn off, pulse for
a certain number of milliseconds, receive a pwm pulse pattern, etc.)

So for example, if you want to configure a slingshot, you might use a
rule on your hardware controller which says, "when switch
*left_slingshot* goes active, fire coil *left_slingshot_coil* for
30ms." Or you might have a rule which says, "When switch
*right_flipper* becomes inactive, cut power to the coil called
*right_flipper_hold*.

You can set any combination of rules you want onto a hardware
controller. In fact, MPF will use several individual rules on the same
set of switches and coils to do what might seem like simple things. For
example, think about what rules you'd need for a dual-wound (power and
hold windings) flipper coil:

* When the flipper button becomes active, enable the power coil.
* When the flipper button becomes active, enable the hold coil.
* When the EOS switch becomes active, disable the power coil.
* When the flipper button becomes inactive, disable the hold coil.
* When the flipper button becomes inactive, disable the power coil.
    (We need this one to "cancel" the flip action if the player
    releases the flipper button before the flipper hits the EOS switch
    at the top of its stroke.)
* If the flipper button is active *and* the EOS switch becomes
    inactive, enable the power coil. (This causes the flipper to go back
    to the "up" position if for some reason it comes down when the
    player is holding the flipper button.)

Now look at that above list. That's six rules just for one flipper! If
you have four flippers in your game, you'll have 24 autofire rules just
to get your flippers set up!

Fortunately MPF makes this easy and hides the complexity from you. :)

## How MPF interacts with autofire rules

The hardware controllers in your pinball machine have no concept of what
your game code is doing at any given time. (Actually they don't even
know what a "game" is, or really what a "pinball machine" is.) They
just know that they have rules programmed into them, and those rules
specify what instantaneous actions they should take based on certain
switches changing state. So your game code can overwrite rules at any
time (and as often as you want) to overwrite existing rules with new
actions. For example, if your player tilts the machine, then you need to
disable the flippers. To do so you would overwrite the above six rules
with the following:

* When the flipper button becomes active, do nothing.
* When the flipper button becomes inactive, do nothing.
* When the EOS switch becomes active, do nothing.
* When the EOS switch becomes inactive, do nothing.

And just like that, your flippers are disabled! You can also see how you
can use these autofire rules to do all sorts of fun things, like
reversing the flippers (so the right button controls the left flipper
and vice versa), or making "no hold" flippers, or inverting the
flipper buttons so pushing them in disables the flippers and letting go
enables them. :)

The final thing that's important to know about these autofire rules you
program into your hardware controller is that they do not prevent the
hardware controller from doing everything else it might do. For example,
if you have a pop bumper then you will probably install an autofire onto
your hardware controller that causes the pop bumper coil to fire
instantly to knock the ball away.

When that rule is installed, the hardware controller will do two things
when the pop bumper switch is activated. First, it will fire the coil,
but second, it will also notify MPF that the pop bumper switch was hit
(since it notifies your game of any switch that was hit). Then your game
code can respond how you want, perhaps by scoring some points and
playing a sound effect. When this happens, *technically speaking* they
won't happen at the same time. The hardware controller will probably
fire the coil in under 1ms, and it might take your game code 5 or 10ms
to add the score and play the sound. But that's fine. 10ms is still
1/100th of a second and no human player is going to notice that delay.
(Heck, the speed of sound is so slow it takes another 1/100th of a sound
for the sound wave to travel from your machine's speaker in the back
box to the player's ear!)

The point is that just because you install autofire rules doesn't mean
you can't also service those switches in your game code. It's just
that you end up dividing the duties----the hardware controller handles
the coil responses on its own, and you handle audio and scoring in your
game code.

Oh, by the way, it's not like you need to use these autofire rules for
*all* your coil activity. Most things like ejecting balls, resetting
drop targets, and firing your plunger can all be handled in your game
code because in those cases you don't care about the extra 1/100th of a
second delay. You only need autofire rules for things you want to happen
instantly, which is usually only pop bumpers, slingshots, and flippers.

## How MPF handles autofire rules

Now that you just read 1500 words on how autofire rules work, the good
news is that you don't really have to worry about these details of them
when using the Mission Pinball Framework. In MPF, you use the
configuration files to setup devices like pop bumpers, slingshots, and
flippers, and the framework handles all the autofire hardware rule
programming based on the switches and coils you specify in your config
files.

In fact the framework automatically creates lists of your devices and
gives them enable() and disable() methods, so rather than having to know
all the intricacies of all those different rules, enabling your flippers
is as simple as self.flippers.enable(). Nice! (But if you dig through
the source code you'll see that the framework uses all these rules
behind the scenes.)

You can also configure autofire coils manually for simpler things like
pop bumpers and slingshots. See the
[autofire_coils](../config/autofire_coils.md)
section of the configuration file reference for details.

## Debounce and Recycle in Autofire Coils

In MPF you can
[configure debounce for each switch](switches/debounce.md) and
[recycle for each coil](coils/recycle.md). If you do that MPF will respect that configuration for
autofire hardware rules. However, if you do not configure it (or set
debounce to `auto`) MPF will try to select a reasonable default. For
autofire coils it selects debounce `quick` if you either did not specify
debounce or set it to `auto`. Recycle will be set to `true` if you do
not specify it.

In some platforms MPF might reconfigure your switch debounce settings
when activating the hardware rules (if the platform does not allow
separate settings). This happens when debounce is set to `auto` (or
unspecified) as switches are then automatically configured as debounce
`normal` and then reconfigured as `quick` when the rule is send to the
hardware (if the platform only supports one configuration at a time).

You can overwrite both settings using `switch_overwrite` and/or
`coil_overwrite` in your `autofire_coils` section.

## Monitorable Properties

For
[dynamic values](../config/instructions/dynamic_values.md) and
[conditional events](../events/overview/conditional.md), the prefix for autofire coils is `device.autofires.(name)`.

### *enabled*:

Boolean (true/false) which shows whether this autofire coil is enabled.

## Fully working basic example

Let's learn by example. Though the following example is a fully working
minimal set for the Cobra controller, it is as well helpful to
understand the concept more if you use a different set of hardware. For
this example to work physically, the Cobra board needs to have the micro
controllers powered up only. No need for a high voltage power supply,
neither for any coil. The `config.yaml` below is the only configuration
file you need in your project. The config file is fully valid for the
Cobra board connected to a Linux PC running MPF. If you have a Cobra
board but run Windows or macOS you have to change the `ports`. If you
run a completely different hardware you have to adapt the `hardware`
section.

``` yaml
#config_version=5

hardware:
   platform: opp
   driverboards: gen2

opp:
   ports: /dev/ttyACM0, /dev/ttyACM1

playfields:
playfield:    #playfield must exist for autofire coils
   tags: default
   default_source_device: bd_plunger   #value must be set, default "none" not allowed when having autofire coils

ball_devices:
bd_plunger:
   ball_capacity: 1
   mechanical_eject: true

coils:
c_my_coil:
   number: 0-0-11

switches:
s_my_switch:
   number: 0-0-16

autofire_coils:
my_autofire_1:
   coil: c_my_coil
   switch: s_my_switch
   enable_events: simulate_start
   disable_events: simulate_stop

keyboard:
1:
   event: simulate_start
2:
   event: simulate_stop
```

Now run `mpf both` to start above example. The Cobra board has a little
LED next the coil output which will light up yellow when the coil is
activated, see the [Cobra board](../hardware/opp/cobrapin/index.md)
documentation for details. Now press the connected switch,
you will see that the LED will not light up since the coil has not been
activated. Press key 1 and afterwards press again the switch, this time
you will see the LED light up for a short time. After you pressed the
key 2, the LED won't light up anymore when the switch is activated,
because you deactivated the coil.

A few comments on the above example:

* The playfield is needed even in this basic example, in a real setup
    you have it anyways.
* Coils are enabled by MPF upon the `ball_started` event and disabled
    by the events `ball_will_end`, `service_mode_entered`. In our basic
    example we don't have these events, thus added our own events when
    the keys are pressed. In a real pinball most likely you won't have
    these additional events.
* Both, coil and switch, need to be controlled by the same micro
    controller for autofire coils, as you can see both `number` value
    starts with 0. If you would use different values MPF will throw an
    exception once the coil is being enabled, but not directly at
    startup. The error message is
    `Config File Error in OPP: Invalid switch being configured for driver. Driver = 1-0-1 Switch = 0-0-16. Driver and switch have to be on the same board.`
* The auto fire rules are stored in the micro controller. If you
    execute the above example, then change the coil to another coil (on
    micro controller 0) and run it again. Now the switch will then
    trigger both coils. If you do these kind of changes you want to
    power down the micro controllers to have a fresh start and avoid
    strange behavior.

## Related How To guides

* [Tutorial step 13: Add slingshots, pop bumpers, and other](../tutorial/13_add_autofires.md)

## Related Events

### *None*:

The autofire coils can be configured to enable or disable based on other events.
