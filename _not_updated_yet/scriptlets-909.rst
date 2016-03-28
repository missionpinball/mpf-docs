
Ascriptlet is a standalone piece of Python code you write which
provides specific custom functionality for a specific pinball machine.
You put your scriptlet files inthe
`/machine_files/<your_machine>/scriplets` folder, and then you add a
reference to them in your machine configuration files. Then when you
run your machine code, the scriptlets are loaded. What's cool about
the scriptlets is that they can interact with the MPF in a number of
different (and deep) ways, none of which require actual hacking of the
MPF code. For example, you can use scriptlets to:


+ Post events which other MPF components (or other scriptlets will act
  on).
+ Act on events that the MPF posts. You can even use scriptlets to
  "hook" boolean and queue events, which means you can insert your
  scriptlet into the game or ball start or stop process, the player add
  process, whatever...
+ Register Tasks so your scriptlet can get control every game loop, or
  they can yield (sleep) as needed and wake up when they have more work
  to do.


The intention of scriptlets is that they're for machine-specific
stuff. If you want to write something that's more generic that you
would use across multiple games (like if you want to write your own
Match routine or coin handling module), then you would write those as
plugins instead. (Though really scriptlets and plugins are very
similar.)



Creating a scriptlet
--------------------

The easiest way to understand how to create a scriptlet is probably to
go through an example of creating one. We'll eventually post lots of
them here as examples, but for now let's start with one. This
scriptlet is for our *Demo Man*machinesample game. It turns on the GI
(general illumination) lights during attract mode, and then makes sure
that all the playfield lights are off before a game starts


::

    
    # Attract mode Scriptlet for Demo Man
    
    from mpf.system.scriptlet import Scriptlet
    
    
    class Attract(Scriptlet):
    
        def on_load(self):
            self.machine.events.add_handler('machineflow_attract_start', self.start)
            self.machine.events.add_handler('machineflow_attract_stop', self.stop)
    
        def start(self):
            for gi in self.machine.gi:
                gi.on()
    
        def stop(self):
            for light in self.machine.lights:
                light.off()


When you write a scriptlet, you put all your code in a class which you
subclass from `Scriplet`.The class name can be whatever you want, and
it doesn't matter if it you use a class name that's used anywhere else
in MPF. You can put multiple classes in a single scriptlet file or put
one class per file—it really doesn't matter. Since this scriptlet is
for the attract mode, we've named the class `Attract`. Next you create
a method called `on_load()`. This method will be run automatically
(one time only) when the scriptlet is loaded, so you use it to set up
your scriptlet. In our example, we use the `on_load()` method to
register event handlers which will cause our other methods to run when
MPF posts certain events. You'll see that we register the scriptlet's
methods `self.start` and `self.stop` for the event notification of the
attract mode stopping or starting. The actual method names are
arbitrary. We just picked `start()` and `stop()` since they make
sense. But we could have called them whatever we want. In our example,
`our start()` method will be called when MPF posts the
*machineflow_attract_start* event which will loop through all the GI
strings and turn them on. And when the Attract mode ends (either
because a player started a game or because the operator went into the
service menu), MPF will post the *machineflow_attract_stop* event
which will call our `stop()`method which will turn off any lights that
are currently on.



Saving your scriptlet
---------------------

We saved our scriptlet with a file name attract.py and put it in the
scriptlet folder withour other *Demo Man* machine files.



Adding your scriptlet to your game
----------------------------------

The final step is to "install" your scriptlet into your game. You do
this in the machine configuration files, in a section called
`scriptlets:`. Just add the file name, then a dot, then the class
name, like this:


::

    
    scriptlets:
        attract.Attract


You can add as many as you want, one per line. So that's pretty much
it! When you run your game code, MPF will automatically import your
scriptlets and then run the `on_load()`method from each one.
Everything else they do is up to you!



Another Scriptlet example
-------------------------

We include another scriptlet example in the
/machine_files/new_machine_template/scriptlets folder called
'new_scriptlet_example.py.' This example scriptlet doesn't really do
anything useful, (though it is fully functional), rather, it shows off
some different things you can do in a scriptlet in addition to playing
some light shows:


::

    
    """Example scriptlet which shows different things you can do."""
    
    from mpf.system.scriptlet import Scriptlet  # This import is required
    
    
    class YourScriptletName(Scriptlet):  # Change "YourScriptletName" to whatever you want!
        """To 'activate' your scriptlet:
            1. Copy it to your machine_files/<your_machine_name>/scriptlets/ folder
            2. Add an entry to the 'Scriptlets:' section of your machine config files
            3. That entry should be 'your_scriptlet_file_name.YourScriptletName'
        """
    
        def on_load(self):
            """Called automatically when this scriptlet is loaded."""
    
            # add code here to do whatever you want your scriptlet to do when the
            # machine boots up.
    
            # This example scriptlet has lots of different examples which show (some)
            # of the things you can do. Feel free to delete everything from here on
            # down when you create your own scriptlet.
    
            # you can access the machine object via self.machine, like this:
            print self.machine
            print self.machine.physical_hw
            # etc.
    
            # you can access this scriptlet's name (based on the class name above):
            print self.name  # will print "YourScriptletName" in this case
    
            # you can write to the log via self.log:
            # The logger will be prefaced with Scriptlet.YourScriptletName
            self.log.info("This is my scriptlet")
            self.log.debug("This is a debug-level log entry")
    
            # you can access machine configuration options via self.machine.config:
            print self.machine.config['Game']['Balls per game']
    
            # feel free to add your own entries to the machine configuration files,
            # like: self.machine.config['YourScriptlet']['Your Setting']
    
            # you can post events which other modules can pick up:
            self.machine.events.post('whatever_event_you_want')
    
            # you can register handlers to act on system events
            self.machine.events.add_handler('ball_add_live_success',
                                            self.my_handler)
    
            # you can create periodic timers that are called every so often
            from mpf.system.timing import Timer
            self.machine.timing.add(Timer(callback=self.my_timer, frequency=10))
            # (Or save a reference to the timer if you want to remove() it later.)
    
            # you can register a handler for the machine tick which will be called
            # every machine tick!
            self.machine.events.add_handler('timer_tick', self.tick)
    
            # you can create a task that can yield as needed
    
        def my_handler(self):
            # This is just an arbitrarily-named method which is the handler for
            # `ball_add_live_event` from the on_load(). Feel free to create as
            # many methods as you want in your scriptlet!
            print "A new ball was added"
    
        def my_timer(self):
            print "another 10 seconds just passed"
    
        def tick(self):
            # this will run every single machine tick!!
            pass


You can run this scriptlet as is by copying it into your
/machine_files/<your machine>/scriptlets folder and then adding
`new_scriptlet_example.YourScriptletName` to the Scriptlets section of
your machine configuration files.



New scriptlet template file
---------------------------

We also include a blank scriptlettemplate filein the
/machine_files/new_machine_template/scriptlets folder called
'new_scriptlet_template.py.'This is the file we use as the starting
point to create our own scriptlets:


::

    
    """Template file you can customize to build your own machine-specific scriptlets.
    """
    
    from mpf.system.scriptlet import Scriptlet
    
    
    class YourScriptletName(Scriptlet):  # Change "YourScriptletName" to whatever you want!
        """To 'activate' this scriptlet:
            1. Copy it to your machine_files/<your_machine_name>/scriptlets/ folder
            2. Add an entry to the 'Scriptlets:' section of your machine config files
            3. That entry should be 'your_scriptlet_file_name.YourScriptletName'
        """
    
        def on_load(self):
            """Called automatically when this scriptlet is loaded."""
            pass




