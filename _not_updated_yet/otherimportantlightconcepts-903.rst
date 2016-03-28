
There are a few other important concepts to understand that we haven't
covered yet.



Colors and Color Lists
----------------------

Throughout this documentation about lights, we've referenced colors as
six-digit hex strings, such as "000000", "ffffff", or "ffaa00." (In
most cases these would be 2-byte red-green-blue color values, though
technically speaking they are the values that apply to the first,
second, and element depend on your hardware and how the lightobjects
areconfigured in your machine configuration file. So if you configure
your lightin a way that doesn't have the first output to the red
element, the second to the green, and the third to the blue, then you
would have GRB or RBG or whatever else you configured your file as.
Probably easiest to fix your yaml file in that case. :) MPF has
intelligence to handle scenarios where the color length doesn't match
the number of elements that make up a light. If you have a single-
color light, then you can pass it a color of "ff" which the light
driverwill translate to 255 which will then be used to activate the
lightat full intensity. If you pass a color like "ff0000" to an
lightthat only has a single element, then MPFwill translate that color
to [255, 0, 0], but since the lightonly has a single element it will
only take the value from the first item in the dictionary and ignore
the rest. Similarly if you send a color of "ff" to a three-element RGB
LED, then MPFwill translate that to a color dictionary of [255, 0, 0],
meaning you will get the first element at full intensity and the
second and third elements will be off. (In other words a color value
of "ff" will enable an RGB LED to be red (assuming the order of the
elements in your yaml file is red-green-blue.) Again, none of this
really matters if you're using entirely RGB LEDs. But what about
single-element, single-color lights?



Understanding Single Colorlights
--------------------------------

Single color lightsonly have one element, and as far as MPF is
concerned, they don't have a "color" at all. Single color lightssimply
use the 2-byte color value as their intensity. So it can be confusing
if you have a single-color blue light, because to turn it on at full
brightness you would pass it a color of "ff" (which is internally
translated to "ff0000" and ultimately [255, 0, 0]. So it can be kind
of weird to think, "Wait, I'm sending this lightthe color "red" but
it's coming out "blue?" Again, that's because single-color lightdon't
really have color as far as MPF is concerned. They just have a single
intensity value and the color is determined by whatever colorthe
plastic insert in your playfield is. The bottom line is the word
"color" is used throughout this documentation. If you have RGB LEDs,
then "color" really is the color that the LED will be. But if you have
single-color LEDs or lamps, you just use two bytes whenever color is
used (color="ff", color="a0", etc.). "Color" in the case of single-
element lightsis really more like "brightness."



Using variables to 'save' colors
--------------------------------

Remember in python that you can use variables anywhere. You might want
to define a bunch of colors once in your game, like


::

    
    self.red = ff0000
    self.yellow = ffaa00
    self.green = 00ff00


Doing this means that you can "tune" your colors in one central
location (at least in terms of lightcommands and lightscripts, and
then whenever you need to specify a color, you can use for variable,
like this: `self.machine.light_controller.enable("LED1", priority=6,
color=self.green` This might also be nice for defining a "white" color
with RGB LEDs where the operator canspecify whether they want a "cool"
or "warm" white setting. (Note at this time you can't use color
definitions in light shows. We've added that to the todo list.)



Understanding the Concept of "Blends"
-------------------------------------

Throughout this documentation there have also been several references
to "blends." Almost all of the methods that enable lightsor play
scripts of shows have a parameter "blend" which can either be True or
False. The blend parameter is universally used to describe what
happens when an light is "off." When blend=True, that means that
whenever alightis off that any lower priority light shows, scripts, or
commands that have enabled that lightwill "show through." To
understand this, let's look at an example where you have a script
running at priority 2 that flashes an RGB LED between red and off. You
also have a lower-priority command (running at priority 1) that has
the LED set to blue. If your higher priority script has blend=True,
then when it is off the lower LED setting will show through, so you
will have the effect of the LED alternating between red and blue. If
your higher priority script has blend=False, then it will "block" the
lower priority setting and your LED will alternate between red and
off. Blends also affect what happens when an LED is fading between a
color and off. For example, in the same example scenario from above,
if your priority 2 script is slowly "pulsing" the LED between red and
off and you have blend=True, then because it's running on top of a
blue setting you'll get the effect of the LED fading between red and
blue. Again in that scenario with blend=False, then the LED will fade
between red and off. Note that blends only affect what happens when an
LED is either off, or fading to/from off to a color. There is no
support for any concept of "alpha" blends that blend full colors.
(Maybe that's a future feature?) Also note that blends are intended to
deal with lights receiving conflicting instructions at different
priorities. If you simply want to flash an RGB LED between two colors,
it would be much easier just to use a script that alternates between
the two colors you want. No need to mess with blends in that case.



Configuring Max Brightness Settings
-----------------------------------

The MPF light controllersupports the concept of a "maximum brightness"
setting for each light in a machine. Max brightness is a floating-
point multiplier value (between 0 and 1) that's applied to every
command sent to the an LED. The default multiplier is 1.0, which means
if you tell an LED output to turn on with the intensity 255, then it
will get 255. You can set the max brightness value to be less than one
to turn down the brightness. For example, if you configure an LED to
have a maximum brightness of 0.85, then sending an intensity command
of 255 will actually be sent as 216. You configure max_brightness as a
dictionary of floating-point values which is maintained by each light
deviceobject in your game. For example, if you have an lightdefined as
"shootAgain," you can configure its max_brightness via:
`self.game.leds.shootAgain.max_brightness = [0.85, 0.85, 0.85]` The
max_brightness value must always be a dictionary, even for single
element LEDs (in which case you'd use `max_brightness=[1.0]`. Note
that the max_brightness settingscan be a bit weird for LEDs and
incandescent lamps connected to traditional lamp matrixes since the
matrix timing means we can only set 12 levels of brightness instead of
255 for direct-controlled LEDs. As for what you can do with this
setting, that's up to you as the programmer. You can configure
different elements of the same LED to have different settings to
compensate for elements that are out-of-whack. You can make system-
wide brightness compensation settings accessible via the operator's
menu. Maybe you have an ambient light sensor and adjust the LEDs based
on how light or dark the room is. Really the sky's the limit. The
important thing is that you change the max_brightness setting of any
LED object at any time. (The change is instant.) And you can still
continue to pass color commands to your LEDs without worrying about
the brightness setting. (In other words you don't have to do any
complex math just to turn down your LEDs.) By the way, experiment with
different default brightness settings. On our test machines we can't
tell a difference between 0.85 and 1.0. So maybe you get longer life
with lower settings? (Though we don't know. That might not be true at
all.)



Global Fades & Defaults
-----------------------

The lightitems in MPFalso support the concept of a "default_fade"
value which is an integer which specifies the fade time (in ms) that
should be used for each lightwhen it is enabled or disabled instantly.
You can access this setting in the same way you access the
brightness_compensation setting. For example:
`self.game.leds.LED1.default_fade=50` Using a default_fade is nice
because it allows the LEDs to "feel" more like incandescent bulbs that
fade on and off instead of harshly turning on and off. This is a
matter of personal taste. Some people like the LED "look" and others
hate it. In our game we wrote code which reads these default fade
settings in via the yaml file, and we've also written an operator menu
setting that allows the operator to specify their own default fades to
suit their individual tastes. By default the default_fade is 0.
Default fades only apply to lightinstructions that instantly turn
alighton or off. If you use alightcommand to fade an lighton over
20ms, then it will fade on over 20ms regardless of what your
default_fade is set to. We can imagine incorporating default_fade
changes in your gameplay. (Perhaps you want a cool strobe effect where
you quickly flash a bunch of lights with a fade of 0 even though your
default is 20?)



Sync Locking
------------

One of the cool features of this light controller is that it sets a
"current time" variable once per update loop. This means if you have a
large update—maybe you're stopping a bunch of shows and looping
through a bunch of scripts—as long as they all happen in the same game
loop then they will all have the same "start" time. Also when light
shows and scripts are processed, the "next" action time is based on
when the last action time should have happened. This means you can
have multiple shows and scripts that all use the same timing, they
will stay in sync, and if your game loop gets bogged down then the
lightswill remain in sync.



