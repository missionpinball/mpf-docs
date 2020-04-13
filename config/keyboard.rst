keyboard:
=========

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``keyboard:`` section of your config is used to configure
options for how you map computer keyboard keys to pinball machine
switches and events. This is useful for testing your game from your
computer when you're not around your physical machine.

You might also want to implement some virtual switches in your machine which
can be only used via a keyboard for debugging.

Options for each key & key combination
--------------------------------------

Once you enter the key and/or key combination, then you need to create a
subsection which defines what this key or key combination does when
it's hit. There are several options:

.. config


Optional settings
-----------------

The following sections are optional in the ``keyboard:`` section of your config. (If you don't include them, the default will be used).

debug:
~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

.. todo:: :doc:`/about/help_us_to_write_it`

event:
~~~~~~
Single event. This device will be posted by the device. Defaults to empty.

You can specify an event name to be posted when this key is pressed.
This is useful for testing when you want to test some part of your
game code based on an event. For example, you could map a keyboard key
to *clockwise_orbit_hit* event instead of having to hit the
*left_orbit_enter* key quickly followed by the *right_orbit_enter*
key. Events entered here are transmitted posted by the MPF core engine
process.

invert:
~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

If True, then this key is inverted, meaning the associated switch is
active when you're not pushing the key down, and it's inactive when
you're holding the key.

mc_event:
~~~~~~~~~
Single event. This device will be posted by the device. Defaults to empty.

This is similar to the *event:* entry, except an *mc_event* is posted
as events in the media controller process, rather than in the MPF
process.

params:
~~~~~~~
One or more sub-entries. Each in the format of ``string`` : ``string``

This section contains subsections which are a list of parameters that
are posted along with the *event* or *mc_event* specified above. Using
the following configuration file snippet as an example:

.. code-block:: mpf-mc-config

    keyboard:
      4:
        event: advance_reel_test
        params:
          reel_name: score_1p_10
          direction: 1

This keyboard entry will post the event *advance_reel_test* when the
*4* key is pressed, and it will pass the parameters
*reel_name=score_1p_10* and *direction=1*.

switch:
~~~~~~~
Single value, type: string name of a :doc:`switches <switches>` device. Defaults to empty.

The switch name of the pinball machine switch you want this key (or
key combination) to control.

toggle:
~~~~~~~
Single value, type: ``boolean`` (``true``/``false``). Default: ``false``

If True, then the key acts like a "push on / push off" key, where you
just have to tap it once to hold the switch active. This is useful for
switches in ball devices, since you don't want to have to hold down
the keys on your keyboard forever whenever a ball is locked in a
device. Default is *False*. You might want to create multiple entries
for the same switch for different key combinations. For example:

.. code-block:: mpf-mc-config

   #! keyboard:
     1:
       switch: trough1
     shift+1:
       switch: trough1
       toggle: true

In the above code, you can momentarily "tap" the *trough1* switch by
hitting the *1* key, but if you want to lock that switch on, then you
can push *Shift+1*.


Related How To guides
---------------------

* :doc:`/hardware/virtual/keyboard`
