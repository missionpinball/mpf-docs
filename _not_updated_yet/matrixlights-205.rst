
The *matrix_lights:*section of the machine configuration file is used
to map`lights connected to a lamp matrix`_ (whetherincandescent lamps
or LEDs) to driver board outputs. This sectioncan be used in your
machine-wide config files. This sectioncanbe used in mode-specific
config files. Here's a snippet of the *matrix_lights:*section of the
configuration file for *Judge Dredd*:


::

    
    matrix_lights:
        l_award_sniper:
            number: L64
            label: Sniper Shot Lit
            tags: playfield, white
        l_air_raid:
            number: L65
        l_left_center_feature:
            number: L66
        l_tank_left:
            number: L67
        l_mystery:
            number: L68
        l_drop_target_j:
            number: L71
        l_drop_target_u:
            number: L72
        l_drop_target_d:
            number: L73
        l_drop_target_g:
            number: L74




<light_name>:
~~~~~~~~~~~~~

Each subsection of *matrix_lights:* is the name of the light as you'd
like to refer to it in your game code.This can really be anything you
want, but it’s obviously best to pick something that makes sense.



number: (required)
~~~~~~~~~~~~~~~~~~

The way you enter the number for a light depends on the type of
pinball controller hardware you're using and what type of pinball
machine it is. Refer to the following sections for information about
how the numbering works for those platforms:


+ `P-ROC with a lamp matrix connected to a PD-8x8`_
+ `P3-ROC with a lamp matrix connected to a PD-8x8`_
+ P-ROC or FAST WPC Controller in a WPC machine (keep reading below)


With WPC hardware, the number is simple. It's just a capital letter
"L" followed by the number of the light from the operators manual. The
Mission Pinball Framework and the platform drivers handle the hard
work of mapping these numbers to actual column and row outputs. Note
that many of the Williams operators manuals have typos here which no
one has probably noticed in 25 years. But if you find that the proper
light is not lighting up when you think it should, you might have to
experiment a bit.



Device Control Events
---------------------

Device control events are events you can use to control devices. They
are configured in your machine-wide or mode config with settings that
end in *_events*. For example, if a device has a setting for
*enable_events:* and you add an event to that setting, then when that
event is posted, the device will enable. You can add single events or
lists of events to these settings, and you can also configure time-
delays for how much time passes between the event being posted and the
action to take place. Details are available in the `device control
event documentation`_. Matrix lights make use of the following device
control events:



on_events:
~~~~~~~~~~

Turns on this light. Default is *None*.



off_events:
~~~~~~~~~~~

Turns off this light. Default is *None*.



Settings that apply to all device types
---------------------------------------

There are some settings that apply to all types of devices that also
apply here.



tags:
~~~~~

A list of one or more tags that apply to this device. Tags allow you
to access groups of devices by tag name.



label:
~~~~~~

The plain-English name for this device that will show up in operator
menus and trouble reports.



debug:
~~~~~~

Set this to *true* to add lots of logging information about this shot
to the debug log. This is helpful when you’re trying to troubleshoot
problems with this shot. Default is *False*.

.. _P-ROC with a lamp matrix connected to a PD-8x8: https://missionpinball.com/docs/howto/how-to-use-a-p-roc-with-mpf/
.. _lights connected to a lamp matrix: https://missionpinball.com/docs/mpf-core-architecture/mechs/low-level-mechs/matrix-light/
.. _P3-ROC with a lamp matrix connected to a PD-8x8: https://missionpinball.com/docs/howto/how-to-use-a-p3-roc-with-mpf/
.. _device control event documentation: https://missionpinball.com/docs/configuration-file-reference/important-config-file-concepts/configuring-device-control-events/


