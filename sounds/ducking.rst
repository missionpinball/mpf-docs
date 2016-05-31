Ducking
=======

*Ducking* is an audio effect that lowers the level of one audio signal based upon the level of
another audio signal (one sound "ducks" out of the way of another).  It is used to allow particular
sounds to be heard more clearly when there is other audio happening at the same time. In the context
of a pinball machine, a common use of ducking is to lower the volume of the background music while
an important callout is played (such as "Extra Ball!") and then return the volume when the callout
is finished. When done professionally, you should not really be able to notice that the music
volume is being lowered, but you'll be able to hear the callout prominently.

By default ducking is not enabled for any sounds in MPF. Ducking settings can be optionally set
for each sound asset in the machine. To best illustrate ducking and its parameters, here is a
diagram:

.. image:: ducking.png

The voice clip in the top track of the diagram illustrates a callout that we wish to add ducking
settings to.  The bottom track is playing music.  The following parameters control the ducking
behavior of the voice clip:

+ ``target`` (The track name to apply the ducking to when the sound is played. In the example
  above the `music` track is the target.).
+ ``delay`` (The duration to delay after the sound starts playing before ducking starts.  This
  value may be specified as a time string or a number of samples.).
+ ``attack`` (The duration of the period over which the ducking starts until it reaches its maximum
  attenuation (attack stage). This value may be specified as a time string or a number of samples.).
+ ``attenuation`` (The attenuation (gain) to apply to the target track while ducking.  This controls
  how quiet to make the target track while the sound is playing.).
+ ``release_point`` (The point relative to the end of the sound at which to start the returning the
  attenuation back to normal (release stage). This value may be specified as a time string or a
  number of samples. A value of 0.5 seconds means to begin to release the ducking 0.5 seconds prior
  to the end of the sound.).
+ ``release`` (The duration of the period over which the ducking goes from its maximum attenuation
  until the ducking ends (release stage). This value may be specified as a time string or a number
  of samples.).

Ducking settings are specified for each desired sound in the :doc:`sounds: </config/sounds>`
section of the configuration files.
