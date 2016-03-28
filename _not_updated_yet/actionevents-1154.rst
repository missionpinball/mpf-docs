
The Mission Pinball Framework has the concept of "action events" which
are normal events that can be used to perform some kind of action. (In
other words, all the event handlers for these types of events are
built into the framework.) Here's a list of the action events included
in MPF, as well as a description of each:



action_light_<light_name>_on
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Turns on a matrix light. Pass parameters as outlined `here`_.



action_light_<light_name>_off
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Turns offa matrix light. Pass parameters as outlined `here`_.



action_play_show
~~~~~~~~~~~~~~~~

Plays a `show`_. You can usethe parameterscovered in the `Playing&
Stopping Shows`_ section to specify which show you want to play and
what settings you want it to have.



action_set_volume
~~~~~~~~~~~~~~~~~

Sets the overall system volume via one of two parameters you pass. Use
`volume` to set the overall volume (float between 0 and 1, 0 is mute,
1 is max) or `change` to set an increment (positive or negative) to
change the volume. (Again, the overall volume level is 0 to 1, so send
a change value of `.1` to increase the volume by 10%, or send `-.2` to
decrease it by 20%, etc.)



action_shutdown
~~~~~~~~~~~~~~~

Causes a graceful shutdown of the MPF software. (Note this does not
actually shut down the hardware. Also note there is a built-in event
whichdoes the exact same thing for the event `sw_shutdown`, which
means you can add a tag called 'shutdown' to any switch, and pressing
that switch will cause the MPF to exit.



action_stop_show
~~~~~~~~~~~~~~~~

Stops a running `show`_ (or ensures that it is stopped). A list of
settings is available in the `Playing & Stopping Shows`_ section.



action_target_<target_name>_light
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lights the `target`_. This action can be an actual target device name
or one that's derived from it (like drop target or rollover.) Details
`here`_.



action_target_<target_name>_unlight
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Unlightsthe target.This action can be an actual target device name or
one that's derived from it (like drop target or rollover.) Details
`here`_.



action_target_<target_name>_toggle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Togglesthe target's state. (If it's lit, this action will unlight it,
if it's not lit, this action will light it.)This action can be an
actual target device name or one that's derived from it (like drop
target or rollover.) Details `here`_.



Future ActionEvents
-------------------

Action eventsare fairly new, so we haven't implemented too many yet.
But in the future we expect to add the following:


+ action_coil_pulse
+ action_coil_enable
+ action_coil_disable
+ action_coil_pwm
+ action_matrixlight_on
+ action_matrixlight_off
+ action_led_color


.. _here: http://mpf.readthedocs.org/en/latest/mpf.devices.target.html?highlight=target#module-mpf.devices.target.unlight
.. _show: https://missionpinball.com/docs/shows/
.. _target: https://missionpinball.com/docs/devices/target
.. _here: http://mpf.readthedocs.org/en/latest/mpf.devices.matrix_light.html#mpf.devices.matrix_light.MatrixLight.off
.. _here: http://mpf.readthedocs.org/en/latest/mpf.devices.target.html?highlight=target#module-mpf.devices.target.toggle
.. _here: http://mpf.readthedocs.org/en/latest/mpf.devices.matrix_light.html#mpf.devices.matrix_light.MatrixLight.on
.. _here: http://mpf.readthedocs.org/en/latest/mpf.devices.target.html?highlight=target#module-mpf.devices.target.light
.. _ Stopping Shows: https://missionpinball.com/docs/shows/playing-shows/


