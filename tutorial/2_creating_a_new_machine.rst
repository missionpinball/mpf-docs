Tutorial step 2: Creating your machine folder
=============================================

Okay, so MPF |version| is installed and you're able to run *Demo Man*. Great!
Now it's time to create the folders and files for your own game.


1. Understand the "machine folder" concept
------------------------------------------

In MPF, we use the term *machine folder* to describe the folder that contains all the
configuration files, code, images, videos, sounds, audits, and
everything else you need for a pinball machine.
Machine folders are portable, so you can grab a machine folder from one
computer and run it on another—-even if it's a different platform.
(Windows to Linux, Mac to Windows, etc.)

Note that we call these "machine" folders and not "game" folders because in MPF, a "game" is an
actual game-in-progress running on a machine. So you're really creating a pinball machine
config, not a pinball game config.

2. Create your machine folders
------------------------------

Okay, so let's get started with your own game's machine folder. The
first step is to create an empty folder somewhere. (Anywhere you want.)
You can name this folder whatever you want too.

Let's use the name "your_machine", and we'll assume you're on Windows,
so you might put it in your ``C:\pinball`` folder, like this:

::

   C:\pinball\your_machine

Throughout this tutorial we'll refer to this as "your machine folder".

Next create a subfolder in your new machine folder called ``/config``. This is where your machine
configuration files will live. This folder should be inside your
machine folder, like this:

::

   C:\pinball\your_machine\config\


3. Create your machine config file
----------------------------------

Now let's actually create your machine config file. To do that, create a file called ``config.yaml`` in your */config*
folder. This will be your main config file which will ultimately be hundreds of lines long and which will contain all
the config and settings for your machine. This file should be here:

::

   C:\pinball\your_machine\config\config.yaml


Note that if you're on Windows and you just right-click and select *New > Text Document*,
make sure that Windows Explorer is configured to show file extensions
so you actually create a file called ``config.yaml`` and not ``config.yaml.txt``. (That's in the "View" menu of Explorer.)

4. Add #config_version=4 to the top of your config file
-------------------------------------------------------

The first thing you need to do when you create any new config file for MPF is to add an entry on the very top line that
tells MPF what “version” of the MPF config spec you’re using for the file you’re creating. For MPF |version|, that
should look like this:

::

   #config_version=4

So just open the file (with a text editor or a free tool like `Atom <http://atom.io>`_ or `Sublime <https://www.sublimetext.com/>`_)
and then add that to the top of the file and save it.

The reason we do this is because one of the challenges we had with all the frequent updates to MPF is that sometimes new
versions of MPF change certain settings in the config files. So we need a way to track which set of config file settings
a particular YAML file uses. That way when MPF loads the config, it can make sure the actual contents of the config file
match up with what MPF is expecting.

That said, not every new version of MPF has changes to the YAML file, so that’s why the YAML file config_version and the
MPF version aren't the same.

Adding versioning to YAML files also means it’s easy us to migrate config files from older versions to newer versions.
(We have a config migration tool that does this, so when we change MPF, you don't have to change your configs.)

The current version of the config files is 4 which is what’s used with MPF 0.30 and newer, so that’s what we’re adding
here.

5. Run your game!
-----------------

Believe it your not, it's time to run your game! Simply open a console window and change to your machine
folder, and run ``mpf -b``, like this:

::

   C:\pinball\your_machine>mpf -b

(The ``-b`` option tells MPF not to try to connect to a media controller for display and sound since we haven't set that
up yet.)

You should get results that look something like this:

::

   C:\pinball\your_machine>mpf -b
   INFO : Machine : Mission Pinball Framework Core Engine v0.30.0
   INFO : Machine : Machine path: C:\pinball\your_machine
   INFO : Machine : Loading cached config: C:\Users\BRIANM~1\AppData\Local\Temp\235c13dee169bec54dce4d06c2665fe9config
   INFO : Machine : Starting clock at 30.0Hz
   INFO : Mode.attract : Mode Starting. Priority: 10

You might notice that it seems like the command is hung because you didn't get the command line back. Actually what's
happening is MPF is running! Your machine is live and sitting in the attract mode!!

At this point since we are running a completely blank config, the only way to stop MPF is to hit ``CTRL+C`` (or ``CMD+C``
on the Mac). When you do that, you should see a few more lines appear, like this:

::

   INFO : Machine : Actual MPF loop rate: 32.04 Hz
   INFO : root : MPF run loop ended.

   C:\pinball\your_machine>

At this point you're all set! You're all set. Move on to the next step. However if you got something else on your
display or some kind of error or crash, read on below...

What if it didn't work?
-----------------------

If you don't get an output that shows the attract mode running like the example above, there could be a few reasons for
this, depending on the error.

If you get a crash with a message about a "Config file version mismatch", like this:

::

   Traceback (most recent call last):
     File "z:\git\mpf\mpf\commands\game.py", line 130, in __init__
       MachineController(mpf_path, machine_path, vars(args)).run()
     File "z:\git\mpf\mpf\core\machine.py", line 98, in __init__
       self._load_config()
     File "z:\git\mpf\mpf\core\machine.py", line 290, in _load_config
       self._load_config_from_files()
     File "z:\git\mpf\mpf\core\machine.py", line 309, in _load_config_from_files
       config_type='machine'))
     File "z:\git\mpf\mpf\core\config_processor.py", line 99, in load_config_file
       config = FileManager.load(filename, verify_version, halt_on_error)
     File "z:\git\mpf\mpf\core\file_manager.py", line 155, in load
       round_trip)
     File "z:\git\mpf\mpf\file_interfaces\yaml_interface.py", line 295, in load
       raise ValueError("Config file version mismatch: {}".format(filename))
   ValueError: Config file version mismatch: C:\pinball\your_machine\config\config.yaml

This means you don't have ``#config_version=4`` in the top line of your config file. (Make sure you include the hash
mark as part of that.)

If you get an error that says ``Could not find machine folder: 'None'``, that means that you ran MPF from the
wrong folder. For example:

::

   C:\pinball\your_machine\config>mpf
   Error. Could not find machine folder: 'None'.

This happens because the command prompt is in the child "config" folder, rather than the base machine folder. So ``cd ..``
up one level and try again.

::

   C:\>mpf
   Error. Could not find machine folder: 'None'.

Again, same thing here. The example above is in the root of C: which is not a valid machine folder. (It is possible to
run a machine from another folder via command line options which is why this error says it couldn't find the machine "None"
(since no command line options were passed), but for now just know that you need to run MPF from the root of your
machine folder.

It's possible you might also get an error about "mpf" not being recognized. For example, on Windows:

::

   C:\pinball\your_machine>mpf
   'mpf' is not recognized as an internal or external command,
   operable program or batch file.

Or on Mac or Linux:

::

   $ mpf
   -bash: mpf: command not found

In this case you probably don't have MPF installed right, so jump back to the installation part of the docs and
follow that again.
