sound_pools:
============

*Config file section*

.. include:: _machine_config_yes.rst
.. include:: _mode_config_yes.rst

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
             drain_01
             drain_02
             drain_03
             drain_04
       slingshot:
          load: preload
          type: random
          sounds:
             slingshot_01|5
             slingshot_02|3
             slingshot_03|2
       target_completion:
          load: on_demand
          type: sequence
          sounds:
             target_completion_01
             target_completion_02
             target_completion_03



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
be contained in the sound pool.  Optionally, a number may be appended to the sound asset name
delimited by a pipe (``|``) character.  This optional number controls the relative weighting for
random item selection, or the number of times to repeat the sound before moving to the next sound
in the pool with a sequence pool.  In the example above, the `slingshot:` random sound pool
contains relative weighting values.  The weights sum to 10 for the three sounds so the
`slingshot_01` sound has a probability of being randomly selected of 5 out of 10 (50%),
`slingshot_02` 3/10 (30%), and `slingshot_03` 2/10 (20%).

Optional settings
-----------------

The following sections are optional for each named sound pool in your config. (If you don't
include them, the default will be used).

load:
~~~~~
Single value, type: one of the following options: preload, on_demand. Default: ``on_demand``

This controls the timing of when the sound assets in the sound pool will be loaded into memory
(see the documentation on (:doc:`Managing Assets </assets/index>` . for an explanation of what
loading is.) Options for ``load:`` are:

+ ``preload`` (The asset is loaded when MPF boots and stays in memory as long as MPF is running.).
+ ``on_demand`` (The asset is loaded "on demand" when it's first called for. (At this point,
  assets loaded on demand stay in memory forever, but at some point we'll change that so they get
  unloaded on demand too.).

type:
~~~~~
Single value, type: one of the following options: sequence, random, random_force_next, random_force_all. Default: ``sequence``

The ``type:`` of sound pool dictates how the next sound in the pool will be selected when the sound
pool is referenced for playback. Options for ``type:`` are:

+ ``sequence`` (Sounds are selected in the order in which they appear in the ``sounds:`` section of
  the sound pool. An optional number/weight appended after each sound controls how many times
  the sound will repeat before the next one in the list is selected.  The sequence of sounds will
  repeat once all sounds have been played.).
+ ``random`` (Sounds are randomly selected from the list of sounds in the ``sounds:`` section of
  the sound pool. The probability of selecting each sound in the list can be controlled by an
  optional numeric weight value appended after each sound.  This weight value is relative to all
  other sounds in the list.).
+ ``random_force_next`` (Sounds are randomly selected from the list of sounds in the ``sounds:``
  section of the sound pool. This sound pool type ensures that the next sound selected will not
  be the same as the previously selected sound (no back-to-back repeats of a single sound). The
  probability of selecting each sound in the list can be controlled by an optional numeric weight
  value appended after each sound.  This weight value is relative to all other sounds in the list.).
+ ``random_force_all`` (Sounds are randomly selected from the list of sounds in the ``sounds:``
  section of the sound pool. This sound pool type ensures that all sounds in the list will be
  played once before any sound will be repeated. The probability of selecting each sound in the
  list can be controlled by an optional numeric weight value appended after each sound.  This
  weight value is relative to all other sounds in the list.).

