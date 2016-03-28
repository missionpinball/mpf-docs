
Okay, so MPF is installed and you're able to run *Demo Man*. Great!
Now it's time to create the folders and files for your own game.



(A) Make sure you're running the right version of MPF
-----------------------------------------------------

This tutorial is written for MPF version 0.21. So before we go any
further, let's make sure that you have that version of MPF.
Instructions for checking the version of MPF you have are `here`_.
Make sure you have v0.21.x.



(B) Understand the "machine folder" concept
-------------------------------------------

In MPF, we use the term *machine folder* to describe all the
configuration files, code, images, videos, sounds, audits, and
everything else you need for a pinball machine in one single folder.
These folders are portable, so you can grab a machine folder from one
computer and run it on another—even if it's a different platform.
(Windows to Linux, Mac to Windows, etc.) (Note that we call these
"machines" and not "games" because in MPF language, a "game" is an
actual game-in-progress—what you're really creating a pinball machine
config, not a pinball game config.) You can have multiple different
pinball machine projects (and multiple versions of each) all living
side-by-side on your computer. (We have dozens of them on ours!) Each
is in its own folder. Your machine folder can be anywhere you want. It
does not have to be inside the MPF folder. In fact we actually
recommend that you *do not put your machine folder inside the MPF
folder*, because that way when we update MPF you can just cleanly
delete the old MPF folder and replace it with the new one without
overwriting the files in your machine folder. That said, there is a
folder in the MPF package called */machine_files* that has some sample
machine configurations you can look at. For example, the *Demo Man*
game from the previous step is in the
*<your_mpf_root>/machine_files/demo_man* folder. But those are just
examples that are part of the MPF package and you shouldn't put your
own machine folder there. Before we dive into creating your machine,
take a few minutes tolook at all the various files and foldersin the
*machine_files/demo_man*folder. This just gives you a taste of what
you'll ultimately be creating. Note that *Demo Man*is *not* a complete
game. (Again, you can follow our progress `here`_.) In fact it's not
really a goal of ours to ever build a complete *Demo Man* game. It
just so happens that we have a *Demolition Man* machine handy, so it's
the guinea pig where we test out all the MPF functionality. But it's
still worth looking through the folder to see the types of things
we're doing. You'll see folders for configurations, modes, assets,
etc... Just poke around and see what things look like.



(C) Create your machine folder
------------------------------

Okay, so let's get started with your own game's machine folder. The
first step is to create an empty folder somewhere. (Again, do *not*
put this in your MPF folder.) Maybe something like
*c:\pinball\your_machine*. Throughout this tutorial we'll refer to
this as "your machine folder". Next create a subfolder in your new
machine folder called ` /config `. This is where your machine
configuration files will live. This folder should be inside your
machine folder, e.g. *c:\pinball\your_machine\config.* Next, create a
file called ` config.yaml ` in your *config* folder. This will be your
main configuration file which will ultimately be thousands of lines
long and which will contain all the configuration and settings for
your machine. This file should be at
*<your_machine_folder>/config/config.yaml*. Note that if you're on
Windows and you just right-click and select *New > Text Document*,
make sure that Windows Explorer is configured to show file extensions
so you actually create a file called *config.yaml* and not
*config.yaml.txt*. Now let's try running your machine! Make sure
you're in your MPF root folder (the one with *mpf.py* in it, not your
machine folder) and run the following command: (Replace
*c:\pinball\your_machine* with the path to your actual machine
folder.)


::

    
    python mpf.py c:\pinball\your_machine -v


Note that we're running Python directly to just start the MPF core
engine rather than running the batch file which launches the core
engine and the media controller. We use `-v` (lowercase) to tell it we
want verbose logging to the log file. Your result should look
something like this. (This example is from Windows, but it's similar
for Linux):


::

    
    C:\pinball\mpf>python mpf.py c:\pinball\your_machine -v
    INFO : Machine : Mission Pinball Framework v0.21.0
    INFO : Machine : Machine config file #1: z:\machine_files\your_machine\config\config
    ERROR : ConfigProcessor : Config file z:\machine_files\your_machine\config\config.yaml is version 0. MPF 0.21.0 requires version 3
    ERROR : ConfigProcessor : Use the Config File Migrator to automatically migrate your config file to the latest version.
    ERROR : ConfigProcessor : Migration tool: https://missionpinball.com/docs/tools/config-file-migrator/
    ERROR : ConfigProcessor : More info on config version 3: https://missionpinball.com/docs/configuration-file-reference/config-version-3/
    ERROR : root : Config file version mismatch: z:\machine_files\your_machine\config\config.yaml
    Traceback (most recent call last):
      File "mpf.py", line 119, in main
        machine = MachineController(options_dict)
      File "Z:\mpf\mpf\system\machine.py", line 85, in __init__
        self._load_machine_config()
      File "Z:\mpf\mpf\system\machine.py", line 221, in _load_machine_config
        Config.load_config_file(config_file))
      File "Z:\mpf\mpf\system\config.py", line 61, in load_config_file
        config = FileManager.load(filename, verify_version)
      File "Z:\mpf\mpf\system\file_manager.py", line 130, in load
        halt_on_error)
      File "Z:\mpf\mpf\file_interfaces\yaml_interface.py", line 51, in load
        format(filename))
    Exception: Config file version mismatch: z:\machine_files\your_machine\config\config.yaml
    C:\pinball\mpf>


Of course all this does is cause MPF to crash saying that there's a
"Config file version mismatch," but hey, MPF ran and found your
machine folder! (The errors are saying that your *config.yaml* is not
a valid MPF configuration file, which makes sense, because it's
totally empty. We'll add stuff to it in the next step.) MPF will
automatically look for a file called */config/config.yaml* in the
folder you pass in the command line. So running *python mpf.py
c:\pinball\your_machine* means MPF is looking for a file at
*c:\pinball\your_machine\config\config.yaml*.



What if it doesn't work?
------------------------

If you don't get an output that looks like the example above, there
could be a few reasons for this, depending on the error. If you get an
IOError: Couldn't find file , that means MPF couldn't find your
*config.yaml* file, like this:


::

    
    C:\pinball\mpf>python mpf.py c:\pinball\wrong_folder
    INFO : Machine : Mission Pinball Framework v0.21.0
    INFO : Machine : Machine config file #1: c:\pinball\wrong_folder\config\config
    ERROR : root : Could not find file c:\pinball\wrong_folder\config\config
    Traceback (most recent call last):
      File "mpf.py", line 119, in main
        machine = MachineController(options_dict)
      File "c:\pinball\mpf\system\machine.py", line 85, in __init__
        self._load_machine_config()
      File "c:\pinball\mpf\system\machine.py", line 221, in _load_machine_config
        Config.load_config_file(config_file))
      File "c:\pinball\mpf\system\config.py", line 61, in load_config_file
        config = FileManager.load(filename, verify_version, halt_on_error)
      File "c:\pinball\mpf\system\file_manager.py", line 140, in load
        raise IOError("Could not find file {}".format(filename))
    IOError: Could not find file c:\pinball\wrong_folder\config\config
    
    C:\pinball\mpf>


In that case make sure you typed the proper path to the machine root
in the command line, and make sure your config file is in the
*<machine_root>/config/config.yaml*. If you get some type oferror
about python not being a valid command , that means you either don't
have Python installed or it's not in your path. You can read the
documentation on python.org about `Python setup and usage`_ to get
that cleared up. If you get an error about mpf.py not found , make
sure you're running Python from the root folder you unzipped the MPF
package to. (There should be a file called *mpf.py*in that folder.)
You'll notice that the MPF download package has two *mpf*folders.
There's the overall package name called *mpf*, and then within there
you'll find additional folders called *machine_files*, *mpf*, *tests*,
and *tools*. (So the parent *mpf* folder is your main MPF folder, and
the child *mpf* folder holds the actual MPF python files.) You want to
be running this command from within the parent *mpf* folder. Once
you've confirmed that MPF is trying to load your config file (with the
error about the config version mismatch), then you can move on to the
next step of actually adding things into your config!

.. _here: https://missionpinball.com/blog/category/building-demo-man/
.. _Python setup and usage: https://docs.python.org/2/using/index.html
.. _here: https://missionpinball.com/docs/howto/mpf-version/


