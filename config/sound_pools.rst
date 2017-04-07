sound_pools:
============

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+

.. overview

The ``sound_pools:`` section of your config is where you specify pools (or groupings) of sound
assets in your machine.

Creating a sounds pool allows you to reference a group of sound variations as if it were a single
sound. A sound pool name may be used anywhere a sound asset name may appear. Pools can be used for
random differences in a sound (such as slight variations of a slingshot sound) or for an ordered
sequence of sounds that will repeat.  Another common use for sound pools is to play a random
callout from a defined list when triggered. (Sound pools are part of the MPF media controller and
only available if you're using MPF-MC for your media controller.)

Here's an example of a typical sound_pool configuration.

::

    sound_pools:
       drain_callout:
          type: random_force_all
          sounds:
             - drain_01
             - drain_02
             - drain_03
             - drain_04
       slingshot:
          load: preload
          type: random
          sounds:
             - slingshot_01|5
             - slingshot_02|3
             - slingshot_03|2
       target_completion:
          load: on_demand
          type: sequence
          sounds:
             - target_completion_01
             - target_completion_02
             - target_completion_03

To create a sound pool, add a sub entry to the  ``sound_pools:`` section of your config which will
be the name of that sound pool. The name must be unique among all sound pools *and* sound assets.
In the above example `drain_callout:`, `slingshot:` and `target_completion:` are each a sound pool
name.  Then create one or more of the following settings for each sound pool:

Required settings
-----------------

The following sections are required for each named sound pool in your config:

sounds:
~~~~~~~

The ``sounds:`` section contains an indented list of existing sound assets (one per line) that will
be contained in the sound pool.  It is suggested you use block sequence notation for this list (begin
each line with a dash followed by a space ``- ``). Optionally, a number may be appended to the sound asset
name delimited by a pipe (``|``) character.  This optional number controls the relative weighting for
random item selection, or the number of times to play the sound before moving to the next sound
in the pool with a sequence pool. If no weight value is provided, a default value of ``1`` will be
applied. In the example above, the `slingshot:` random sound pool contains relative weighting
values.  The weights sum to 10 for the three sounds so the `slingshot_01` sound has a probability
of being randomly selected of 5 out of 10 (50%), `slingshot_02` 3/10 (30%), and `slingshot_03`
2/10 (20%).

.. note:: If you want to use a sound that has spaces in its name, the name of the sound must be
   in quotes:
   ::

       sound_pools:
       drain_callout:
          type: random_force_all
          sounds:
             - drain_01
             - drain_02
             - "drain 03" # example of a sound with a space in its name using quotes
             - drain_04


Optional settings
-----------------

The following sections are optional for each named sound pool in your config. (If you don't
include them, the default will be used).

load:
~~~~~
Single value, type: one of the following options: preload, on_demand. Default: ``on_demand``

This controls the timing of when the sound assets in the sound pool will be loaded into memory
(see the documentation on (:doc:`Managing Assets </assets/index>` for an explanation of what
loading is). Options for ``load:`` are:

+ ``preload`` - The asset is loaded when MPF boots and stays in memory as long as MPF is running.
+ ``on_demand`` - The asset is loaded "on demand" when it's first called for. At this point,
  assets loaded on demand stay in memory forever, but at some point we'll change that so they can
  be unloaded on demand too.

type:
~~~~~
Single value, type: one of the following options: sequence, random, random_force_next,
random_force_all. Default: ``sequence``

The ``type:`` of sound pool dictates how the next sound in the pool will be selected when the sound
pool is referenced for playback. Options for ``type:`` are:

+ ``sequence`` - Sounds are selected in the order in which they appear in the ``sounds:`` section.
  An optional number/weight appended after each sound controls how many times the sound will be
  played before the next one in the list is selected.  The sequence of sounds will repeat once all
  sounds have been played.
+ ``random`` - Sounds are randomly selected from the list of sounds in the ``sounds:`` section of
  the sound pool. The probability of selecting each sound in the list can be controlled by an
  optional numeric weight value appended after each sound.  This weight value is relative to all
  other sounds in the list.
+ ``random_force_next`` - Sounds are randomly selected from the list of sounds in the ``sounds:``
  section of the sound pool. This sound pool type ensures that the next sound selected will not
  be the same as the previously selected sound (no back-to-back repeats of a single sound). The
  probability of selecting each sound in the list can be controlled by an optional numeric weight
  value appended after each sound.  This weight value is relative to all other sounds in the list.
+ ``random_force_all`` - Sounds are randomly selected from the list of sounds in the ``sounds:``
  section of the sound pool. This sound pool type ensures that all sounds in the list will be
  played once before any sound will be repeated. The probability of selecting each sound in the
  list can be controlled by an optional numeric weight value appended after each sound.  This
  weight value is relative to all other sounds in the list.

simultaneous_limit:
~~~~~~~~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``None``

The numeric value indicating the maximum number of instances of this sound pool that may be
played at the same time (up to the limit of the track).  Once the maximum number of instances has
been reached, the ``stealing_method`` setting determines the how additional requests to play
the sound pool will be managed.  This setting is useful for sounds that can be triggered in rapid
succession (such as spinners and pop bumpers).  Setting a limit will ensure a reasonable number
of instances will be played simultaneously and not overwhelm the audio mix.  The default value of
``None`` indicates no limits will be placed on the number of instances of the sound pool that may be
played at once up to the limit of the track.

.. note::

  The sounds contained in a sound pool can also have their own ``simultaneous_limit``
  setting which can lead to some unexpected behavior when interacting with the
  ``simultaneous_limit`` setting in the sound pool.

stealing_method:
~~~~~~~~~~~~~~~~
Single value, type: one of the following options: oldest, newest, skip. Default: ``oldest``

The ``stealing_method:`` of a sound pool determines the behavior of additional requests to play the
sound pool once the number of simultaneous instances of the sound has reached its
``simultaneous_limit`` limit. This setting is ignored when ``simultaneous_limit`` is set to ``None``.
Options for ``stealing_method:`` are:

+ ``oldest`` - Steal/stop the oldest playing instance of the sound and replace it with a new
  instance (essentially restarts the oldest playing instance).
+ ``newest`` - Steal/stop the newest playing instance of the sound and replace it with a new
  instance (essentially restarts the newest playing instance).
+ ``skip`` - Do not steal/stop any currently running instances of the sound. Simply skip playback
  of the newly requested instance.
