How to play a sound with variations
===================================

One of the ways to make your machine more professional is to use different variations of sounds in
your machine. This will add variety and make your audio less predictable and more "alive".  This
guide explains how to play a sound with multiple variations in your machine. Sound support is
part of the MPF media controller and only available if you're using MPF-MC for your media
controller. This guide assumes you have already configured your sound system for your machine and
are familiar with the basic sound setup concepts.  If not, please start with the
:doc:`Setting up sound for your machine <basic_setup>` guide first.

1. An brief introduction to sound pools
---------------------------------------

Sound pools allow you to group multiple sounds together and treat the pool as a single sound. Each
time a sound pool is played, it selects a sound from its group of sounds.  The selection can be
configured to be random or in a particular sequence.  For more complete information, please read
the :doc:`sound_pools </config/sound_pools>` documentation.

Although sound pools can be used to play a random music track or random callout when an event
occurs, in this guide we will be using a sound pool to play variations of a sound when a slingshot
is hit.

2. Add a sound and some variations
----------------------------------

Before we can create our sound pool, we first need to configure the individual sounds that will
make up our pool. We've decided we want to have a small ding (like a triangle hit) play whenever
the slingshot is hit.  Let's start by adding our basic sound to our sound assets. The hardest part
of this process is to either generate or find the sound you want (we won't go into that process
here). Once you have your sound file, put it in the appropriate sound asset folder.  I found a
simple triangle sound on `www.freesound.org <http://www.freesound.org/>`_ that we'll use here,
*13147__looppool__triangle1.wav*.  Place the file in your sound effects track folder
(``<machine_folder>/sounds/sfx``).  Now we'll add it to your machine configuration file, but give
it an easier name to remember (``triangle_01``) using the ``file:`` setting (or you could simply
rename the file to *triangle_01.wav* and omit the *file:* setting):

::

   sounds:
      triangle_01:
         file: 13147__looppool__triangle1.wav
         volume: 0.7

Now add a few variations of the sound. I used my favorite sound editor to slightly adjust the
pitch and frequency content of the triangle sound file, creating three variations. You can also
just find some other similar sounds on the internet. After you have your variations, place them in
the same directory as your first sound file.  We are now ready to add them to the ``sounds:``
section in the machine configuration file (I named the sound variations *triangle_02*,
*triangle_03*, and *triangle_04*:

::

   sounds:
      triangle_01:
         file: 13147__looppool__triangle1.wav
         volume: 0.7
      triangle_02:
         volume: 0.7
      triangle_03:
         volume: 0.7
      triangle_04:
         volume: 0.7

3. Configure the sound pool
---------------------------

We now have 4 variations of the same basic triangle sound.  It's time to put them all into a single
sound pool object so we can treat them as a single sound.  To do so, we need to add a
``sound_pools:`` section to our machine configuration file as follows:

::

   sound_pools:
      triangle:
         type: random
         sounds:
            - triangle_01
            - triangle_02
            - triangle_03
            - triangle_04

We now have a sound pool asset called ``triangle`` that acts just like a sound asset, except that
each time ``triangle`` is played, one of the 4 sound variations contained in the sound pool will
randomly be selected to be played.  Want to add more variations or take one out? It's just as
simple as modifying the list of sounds in the sound pool.

This is great, but let's adjust the sound pool settings a bit to fine tune its behavior.  We
really want the main sound (``triangle_01``) to be played more often than the other sounds. How
can we make that happen? It's very easy to do. We can add weights to each sound in the pool that
specify the probability of each sound being selected.  Let's look at our ``sound_pools:`` section
again:

::

   sound_pools:
      triangle:
         type: random
         sounds:
            - triangle_01|5
            - triangle_02|2
            - triangle_03|2
            - triangle_04|1

Notice we've added a pipe character (``|``) to the end of each sound followed by a numeric value.
These values assign a relative weight to each sound that will be used in the random selection
process.  ``triangle_01`` has a relative weight of ``5`` out of a total weighting of ``10``
(simply add all the weight values), therefore its probability of being selected is ``50%``. The
``|1`` appended to ``triangle_04`` is unnecessary because a relative weight of ``1`` is the default
value for all sounds in the pool that do not have explicit weight values assigned.

Sometimes you may want to have sounds included based on conditional events. You can add a condition
to any sound and the sound pool will only include that sound if the condition evaluates to true at
playback time. If the selection is random, excluded events will not be weighted in the distribution.
If the selection is sequential, excluded events will simply be skipped.

::

   sound_pools:
      triangle:
         type: random
         sounds:
            - triangle_01
            - triangle_02{current_player.triangles_found>1}|2
            - triangle_03{current_player.triangles_found>2}
            - triangle_04{device.achievements.supertriangle.state=="complete"}|5

Sound conditions are formatted the same as all :doc:`conditional events </events/overview/conditional>`.
Any sound in a pool can have a weight, a condition, both, or neither.

For additional sound pool setting options, take a look at the :doc:`sound_pools </config/sound_pools>`
documentation.

4. Configuring the sound player
-------------------------------

We have our sounds and sound pool configured.  To trigger the sounds with MPF events, the sound
player can be used. The sound player was covered in the previous tutorial and will not be covered
again here.  You can also read the :doc:`sound_player </config_players/sound_player>`
documentation.
