
In MPF, you can add custom code to specific game modes. This code is
conceptually similar to scriptlets, except that it's mode-specific. In
other words, the code in a scriptlet runs and is active always,
whereas mode-specific code is only active when that particular game
mode is active. To add mode-specific code:


#. Create a `code`subfolder in your that mode's `mode` folder.
#. Create a file in the code folder to hold your game code called
   `<mode_name>.py`.
#. Create an empty file called `__init__.py` in your code folder.
   (That's two underscores, then "init", then two more underscores, then
   ".py".)
#. In your mode config file (in your
   `<mode_folder>/config/<mode_name>.yaml` file, add a setting in the
   `mode:` section for your mode. For example `code:
   skillshot.SkillShot`.


For example, here's what the folder structure would look like to
create some custom code for the skillshot mode: ` `_ And here's what
the `skillshot.yaml` mode config file would look like:


::

    
    mode:
        start_events: ball_starting
        stop_events: timer_mode_timer_complete 
        code: skillshot.SkillShot
        priority: 300


To actually start writing code, you need tosubclass MPF's `Mode`
class. Here's an example of the bare minimum in need in your
`skillshot.py` file using the skillshot mode example from above:


::

    
    from mpf.system.modes import Mode
    
    class SkillShot(Mode):
        pass


Note that the name of your subclass here matches the name of the class
you specified in the `code:` section inthe mode's config file. From
there, you can addwhatever methodsyou want. The Mode super class
contains three methods which are designed to be overwritten in your
own mode-specific code:


+ `mode_init()` - runs on MPF boot when the mode is read in and set
  up.
+ `mode_start()` - runs when the mode starts
+ `mode_stop()` - runs when the mode stops


There's also another helper method in the parent class called `
`add_mode_event_handler()``_. This method is used exactly like the
regular event modules ` `add_handler()``_ with one addition: Any event
handlers you register here will automatically be removed when the mode
stops. Using this method (instead of the regular one) in your mode
code is completely optional, but it makes things a bit cleaner since
you don't have to track and remove mode-specific event handlers on
your own.

.. _add_mode_event_handler(): http://mpf.readthedocs.org/en/latest/mpf.system.modes.html?highlight=add_mode_event_handler#mpf.system.modes.Mode.add_mode_event_handler
.. _add_handler(): http://mpf.readthedocs.org/en/latest/mpf.system.events.html?highlight=add_handler#mpf.system.events.EventManager.add_handler


