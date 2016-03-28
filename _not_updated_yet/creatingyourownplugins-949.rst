
If you want to add to, modify, or extend the core functionality of the
Mission Pinball Framework, you can create your own plugins. Plug-ins
are conceptually similar to `scriptlets`_, except plugins are designed
to be generic things that could apply to any pinball machine, whereas
scriptletsare meant to add custom code to individual games. To create
a plugin, all you do is create a python file that contains the class
for your plugin, then you add it to the /plugins folder. You can
enable your plugin for a specific machine by adding it to the `Plugins
section of that machines configuration file`_. The only thing to know
about creating a plugin is that when it's loaded, the machine
controller will pass a reference to itself as the only argument for
the `__init__()` method. So for example, you'd want to start your
plugin like this:


::

    
    class MyPlugin(object):
        def __init__(self, machine):
            self.machine = machine  # save a reference here so you can access everything else in the game


What you do with your plugin is up to you. Since plugins and
scriptletsare so similar, you can check out our `example
scriptletfile`_ for some ideas. (The biggest difference is that since
scriptletswill probably be used by beginners, they subclass
Scriptletwhich sets up the environment for them. Plugins subclass
object since if you're writing a plugin, you probably know what you're
doing. You can also check out all the existing plugins which come with
MPF in the `/plugins` folder for an idea of how they work.

.. _Plugins section of that machines configuration file: /docs/configuration-file-reference/plugins/
.. _scriptlets: /docs/programming-guide/hacklets/
.. _file: /docs/programming-guide/another-scriptlet-example/


