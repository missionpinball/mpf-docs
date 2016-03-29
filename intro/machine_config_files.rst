Machine configuration files
===========================

The real magic of the Mission Pinball Framework happens with
configuration files. MPF uses a file format called `YAML <http://www.yaml.org/spec/1.2/spec.html>`_ which
istext-based and human readable. (YAML is kind of like XML, though
easier to read and write. It's kind of like INI files, though more
powerful.) We call these the * machine configuration files *(because
they specify the configuration of your pinball machine), and if you
use the MPF then you're going to get to know them *very* well! In MPF,
just about *everything* your game does can be configured via these
config files. (Seriously. Almost everything: switches, coils, lights,
light and sound shows, animations, scoring, game logic, modes, display
effects, cut scenes...)

We have a :docs:`detailed configuration file
reference </config-file-reference>` that explains all the options for all the files, but for
now we just want to explain the basic concept ofhow these files work.
When you create code for a pinball machine with MPF, you create a
folder which will hold all the settings and files that machine needs.
(This folder contains everything, and in fact will be portable. You
could drop your machine's folder into our copy of MPF and it would
work fine.) Inside your machine's folder, you'll have a subfolder
called `config`, and that folder will hold your configuration file (or
files). So then when you run MPF, you specify which machine (i.e.
which folder) you want to run, and then MPF will look for a
configuration file called ``<your machine>/config/config.yaml``. (You
can actually use the command line to specify *which* config file you
want to use for your machine, meaning you can easily test out
different things or run different configurations for the same machine
with the same folder in MPF.) In addition to holding settings for your
machine, a config file can actually point to an additional config file
(or files) that should be read in too. This means you can break up your
configuration across as many files as you want, and MPF parses all the
settings from all the files—-in the order they're listed—-to create the
actual configuration for your machine. (If you look at the *demo_man*
example from the *mpf-examples* download,
you'll see that we broke its config down in a bunch of different
files, like ``machine.yaml``, ``game.yaml``, ``devices.yaml``,
``text_strings.yaml``, etc.)

How many configuration files you have is
totally up to you. You can break the settings into fiftylittle files
if you want, or you can have one huge file that contains all your
settings. It really doesn't matter at all. (Seriously, it doesn't
matter. The game reads all the settings from all the files into a
single configurationdictionary when the game code starts up, so once
all the settings are read in it doesn't care whether they came from
100 files or one file.)

The reason we allow the machine config files
to be broken into multiple files is because it makes it easier to
share files between projects and machines. For example, at the most
basic level, the switches, coils, and lights in a *Funhouse* machine
are the same regardless of whether you're writing new game rules from
scratch or just building a new version of the classic game. (So for
*Funhouse*,the solenoid which moves Rudy's eyes to the right is Driver
#25, connected to J122 Pin 1, no matter what.) So in that case you
might put all the hardware configuration settings in a file called
`funhouse_hardware.yaml`, and then you might have `brian.yaml` which
is Brian's version of the game rules, and `gabe.yaml` which is Gabe's
version, etc.

What do you configure in these config files?
--------------------------------------------

In a word: everything. The machine config files specify what hardware
platform you use, how your coils, switches, and lights are mapped,
what options they have, and what names these use, how your playfield
devices are set up, ball search, ball save, coin and credit settings,
text strings, high scores, score values, sound and music effects, DMD
animations, game modes, game logic and game flow—the list goes on and
on. You also usethese config files also specify what your operator
settings are. You literally use them to control *which* options are
exposed via the service menu (as well as default options and
acceptable ranges of inputs), and they're used to read in stored
options that affect how the game is played and how the machine
behaves. When an operator navigates through the service menu to
configure their game, those configuration settings are written to—you
guess it—another YAML configuration file. (The YAML file holding the
operator settings is read last, meaning any settings the operator
changed overwrite whatever default settings you specified in earlier
files.) For example, you might have the following setting in a
configuration file called ``game.py``:

::

    game:
        balls_per_game: 3

And then if the operator changes this to 5, an entry might be written
in a file called `operator_settings.yaml` file like this:

::

    game:
        balls_per_game: 5

If you look in the initial `config.yaml` which is first read in that
specifies the names and order of additional files, you'll see that
`operator_settings.yaml` is the last file loaded, meaning it will
overwrite any default settings that were specified earlier. (This also
means that you can play with different sets of settings or sets of
operator settings by creating multiple initial config files which each
specify different combinations of subsequent files. Then you can just
specify different initial files via the command line when you run your
game to try out different settings.) One final note in case it's not
clear. The actual names of the YAML configuration files are totally
arbitrary. Any setting can be in any file, and which files are read
are specified in the list in the initial file. We picked default file
names and broke them into logical file groupings, but if you want to
call your files potato.yaml and hubcap.yaml, that's fine with us.
Again, you can check out the :docs:`config file reference </config-file-reference>` to see all the
settings and options for things you can configure via these files.
