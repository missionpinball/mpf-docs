
The `triggers:` section of a config file is used to send BCP trigger
commands based on MPF events. This sectioncan be used in your machine-
wide config files. This sectioncan be used in your mode-specific
config files. The BCP specification dictates that triggers are sent in
the format `trigger?name=foo`. They can optionally include additional
parameters, such as `trigger?name=foo&some_param=whatever`. To
configure triggers, create a triggers: section in your config file.
Then create a sub-section with a name that matches an MPF event,
specify the name that you want to be passed via BCP as well as
(optionally) any additionalparameters. For example:


::

    
    triggers:
      sw_plunger:
        bcp_name: plunged
        params:
          how_many: 1
          this_many: 2
      shot_ramp:
        bcp_name: ramp_made


In the above example, the BCP command
`trigger?name=plunged&how_many=1&this_many=2` will be sent when the
MPF event *sw_plunger* is posted and the BCP command
`trigger?name=ramp_made` when the MPF event *shot_ramp* is posted. You
can optionally use % signs like with text display elements of the
`Slide Player`_ to substitute event parameter text with player
variables and/or parameters attached to MPF events.

.. _Slide Player: https://missionpinball.com/docs/configuration-file-reference/slideplayer/


