---
title: Start, Tournament and Launcher Buttons
---

# Start, Tournament and Launcher Buttons


Related Config File Sections:

* [switches:](../../config/switches.md)
* [lights:](../../config/lights.md)

Probably all pinball machines have a start button which will start the
[game](../../game_design/index.md) once you press
it and there are enough
[credits](../../game_logic/credits.md).
Furthermore, machines have either a mechanical plunger or a launcher
button which will
[shoot the ball from the launcher](../plungers/coil_fired.md). Additionally, some machines have tournament buttons to
start a tournament.

## Hardware

![image](../images/button.jpg)

Those buttons usually come with a
[micro switch](mechanical_switches.md) and a
[#555 bulb](../lights/matrix_lights.md).
You can connect the switches to any direct input on your controller or
put them into your switch matrix (with an additional diode). The LED is
rated at 6.3V which works fine at either 5V or in a lamp matrix at 12V
(the latter commonly used).

## Config

To configure your start button you can use this config:

``` yaml
lights:
  l_start_button:
    number: 3           # number depends on your platform
    subtype: matrix     # depends on your platform
switches:
  s_start:
    number: 23          # number depends on your platform
    tags: start
```

The tag `start` will hook the button into your game. See
[Tutorial step 9. Add the start button](../../tutorial/9_start_button.md) for details.
You might want to integrate the button into your attract light show.

## Related How To guides:

* [Tutorial step 9. Add the start button](../../tutorial/9_start_button.md)
* [Mechanical Switches](mechanical_switches.md)
* [Matrix Lights (Bulbs)](../lights/matrix_lights.md)
