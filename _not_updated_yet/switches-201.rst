
The *switches:* section of the config files is used to map switchnames
to controllerboard inputs. You can map both direct and matrix
switches. This section *can* be used in your machine-wide config
files. This section *cannot* be used in mode-specific config files.
Here’s an example section:


::

    
    switches:
        flipperLwR_EOS:
            number: SF1
        flipperLwR:
            number: SF6
        fireR:
            number: S12
            tags: plunger
        start:
            number: S13
            tags: start
        plumbBob:
            number: S14
            tags: tilt
        outlaneL:
            number: S16
            tags: playfield_active
            debounce: True
        inlaneL:
            number: S17
            tags: playfield_active
            debounce: True
        trough1:
            number: S81
            type: 'NC'
        shooter_lane:
            number: S82
            activation_events: ball_in
            deactivation_events: ball_out


Each subsection of `switches:` is a switch name, which is how you
refer to the switch in your game code. Then there are several
parameters for each switch:



number:
~~~~~~~

The number is the physical switch input number. The exact format if
this will vary depending on what type of pinball controller you're
using and how the switch is connected. You can refer the the how to
guides for each hardware platform for details:


+ `P-ROC switch numbering`_
+ `P3-ROC switch numbering`_
+ `FAST Pinball controller switch numbering`_
+ WPC switch numbering (keep reading below)


If you're using a Williams WPC machine (with either FAST or P-ROC,
when your *machine: driverboards* configuration is set to *wpc*), you
can use the switch numbers printed in the game's operators manual and
the P-ROC or FAST platform interface will translate them into the
actual numbers behind-the-scenes. The numbering scheme is as follows:


+ SFx - This is a switch connected to a Williams Fliptronics interface
  board, labeled *Fx* in the Williams Operators Manual. These types of
  switches would be entered into the config file like `number: SF1`.
+ SDx - This is a dedicated switch, labeled *SDx* in the
  Williamsmanual. Use them like `number: SD21`.
+ Sx - This is a matrix switch, just labeled with a switch number in
  the Williams manual. Use them like `number: S12`.




activation_events:
~~~~~~~~~~~~~~~~~~

A list of one or more names of events that MPF will post when this
switch goes active. Enter the list in the MPF `config list format`_.
These events are posted exactly as they're entered, in addition to any
events that are posted based on the switch's tags.



deactivation_events:
~~~~~~~~~~~~~~~~~~~~

A list of one or more names of events that MPF will post when this
switch goes inactive. Enter the list in the MPF `config list format`_.



type:
~~~~~

You can add *NC* as a type (like *type: NC*) to indicate that this
switch is a normally closed switch, i.e. it's closed when it's
inactive and open when it's active. This is mostly used for optos.
Switches which are type NC are automatically inverted by the Switch
Controller. In other words an NC switch is still "active" when it's
being activated, but the Switch Controller knows that activation
actually occurs when the switch opens, rather than closes. Setting the
type to NC here means that you never have to worry about this
inversion anywhere else in your game code. Note: This `type`: entry
will probably go away in the future and we'll just add a tags: option
for NC, since really there's no need for a separate `type` parameter
here.



debounce:
~~~~~~~~~

Lets you configure whether a switch should be debounced or not. Each
hardware platform handles debounce differently, so check out the how
to guides for your specific platform for details:


+ `P-ROC switch debounce settings`_
+ `P3-ROC switch debounce settings`_
+ `FAST Pinball controller switch debounce settings`_




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
event documentation`_. Switches make use of the following device
control events:



Settings that apply to all device types
---------------------------------------

There are some settings that apply to all types of devices that also
apply here.



tags:
~~~~~

You can add tags to switches to logically group them in your game code
to make it easier to do things. (Like "if all the switches tagged with
`DropTargetBank1` are active, then do something.") Tags are also used
to create MPF events which are automatically posted with an *sw_*
prefix, by tag, when a switch is activated. For example, if you have a
switch tagged with "hello", then every time that switch is activated,
it will post the event *sw_hello*. If you have a switch tagged with
"hello" and "yo", then every time that switch is activated it will
post the events *sw_hello* and *sw_yo*. MPF also makes use of several
tags on its own, including:


+ playfield_active - This tag should be used for all switches on the
  playfield that indicate a ball is loose on the playfield. This tag is
  used to validate the playfield as well as to reset the ball search
  timer. (i.e. as long as switches with the playfield_active tag are
  being activated, the ball search timer won't start.)
+ start - Used to tell the game that the player has hit the start
  button.




label:
~~~~~~

The plain-English name for this device that will show up in operator
menus and trouble reports.



debug:
~~~~~~

Set this to *true* to add lots of logging information about this shot
to the debug log. This is helpful when you’re trying to troubleshoot
problems with this shot. Default is *False*.

.. _P-ROC switch debounce settings: https://missionpinball.com/docs/howto/how-to-use-a-p-roc-with-mpf/
.. _config list format: https://missionpinball.com/docs/configuration-file-reference/adding-lists-and-lists-of-lists-to-config-files/
.. _FAST Pinball controller switch debounce settings: https://missionpinball.com/docs/howto/how-to-use-a-fast-pinball-controller-with-mpf/
.. _P3-ROC switch debounce settings: https://missionpinball.com/docs/howto/how-to-use-a-p3-roc-with-mpf/
.. _device control event documentation: https://missionpinball.com/docs/configuration-file-reference/important-config-file-concepts/configuring-device-control-events/


