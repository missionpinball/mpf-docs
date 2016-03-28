
A show"script" lets you attach a simple script to a single light which
does something more than just turning it on. A script is usually
pretty simple, like "turn red for 500ms, then off for 500ms, then
repeat." But you can also make more complex scripts with multiple
steps, like cycling through all the colors of the rainbow. More
features of scripts:


+ Set as many steps as you want, including how long each step is and
  whether the lightfades to that step or switches instantly.
+ Assign variables to scripts for easy reuse. So you can have a script
  called self.flash_red which you can play at any time. You can specify
  which lightthat script is played for when you play it. So you can end
  up with a library of scripts you can reuse through your game.
+ Use the blend setting to specify whether the lightblends with lower
  priority stuff when it is off in the script.
+ Specify how many times a script repeats, or whether it repeats
  forever.
+ Set the priority of the script. This is the same priority system of
  the light shows which means it handles how multiple things setting
  this LED at the same time work.


From a technical standpoint, a light script is a Python list of
dictionaries. Each list item is one step in the script, and each
dictionary contains key/value pairs which specify the color and (if
you want the script to fade to the next color) the fade time (in ms).
The key with scripts is they are *not* tied to a specific lightwhen
you create them. (That happens when you run them.)



Creating and Playing Scripts
----------------------------

Creating a script is easy. Here's a script called "flash_red" that
will flash an LED between red and off:


::

    
    self.flash_red = []
    self.flash_red.append({"color": "ff0000", "time": 100})
    self.flash_red.append({"color": "000000", "time": 100})


To run the script, use the show controller's `run_script()` method,
like this: `self.machine.show_controller.run_script("LED1",
self.flash_red, "4", blend=True)` Most likely you would define your
scripts once when the game loads and then call them as needed. You can
also make more complex scripts. For example, here's a script which
smoothly cycles an RGB LED through all colors of the rainbow:


::

    
    self.rainbow = []
    self.rainbow.append({'color': 'ff0000', 'time': 400, 'fade': True})
    self.rainbow.append({'color': 'ff7700', 'time': 400, 'fade': True})
    self.rainbow.append({'color': 'ffcc00', 'time': 400, 'fade': True})
    self.rainbow.append({'color': '00ff00', 'time': 400, 'fade': True})
    self.rainbow.append({'color': '0000ff', 'time': 400, 'fade': True})
    self.rainbow.append({'color': 'ff00ff', 'time': 400, 'fade': True})


Playing a script causes the show controllerto dynamically create a
light showwhich is played just like any other light show. If you want
to save a reference to the light showthat's created when a script is
played, you can call it like this: `self.blah =
self.machine.show_controller.run_script("LED2", self.flash_red, "4")`
Then you can use that reference to stop the show, change the playback
speed, change the priority, etc.



Stopping a Script
-----------------

You can use show controller's `stop_script()` method to stop a script.
In a practical sense there are several ways you can use this.


+ Specify `lightname` only to stop (and remove) all active light shows
  created from scripts for that light name, regardless of priority.
+ Specify `priority` only to stop (and remove) all active light shows
  based on scripts running at that priority for all lights.
+ Specify `lightname` and `priority` to stop (and remove) all active
  light scriptsfor that light name at the specific priority you passed.
+ Specify a `show` object to stop and remove that specific show.


If you call `stop_script()` without passing it anything, it will
remove all the light showsstarted from all scripts. This is useful for
things like end of ball or tilt where you just want to kill
everything. Some examples: To stop every running script, use the
following: (Technically this stops all the shows that were started
from scripts versus started from show yaml files)
`self.machine.show_controller.stop_script()` To stop every script
attached to the LED called "LED1":
`self.machine.show_controller.stop_script(lightname="LED1")` To stop
every script that's running at priority 10:
`self.machine.show_controller.stop_script(priority=10)`



