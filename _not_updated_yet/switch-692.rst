
A switch in a pinball machine is like any switch you'd expect. It's
used for all switches, including cabinet buttons, rollovers, targets,
optos, trough switches, DIP switches, etc. MPF supportsmatrix
switches, direct switches, and Fliptronics switches. They only have
two properties:active or inactive. (Note we don't say "open" or
"closed" because sometimes switches are normally-closed which mean
they're actually active when they're open.) In the MPF, you `specify
your switches in your machine configuration file`_, as well as whether
each switch is normally open or normally closed. (Then the framework
translates those into "active" and "inactive" events for the machine.)
You can also configure debounce settings for each switch, which
controls how MPF responds to switch events. Saying that a switch has
to be "debounced" means that the pinball controller makes sure the
switch is actually in its current state for a few milliseconds before
it send the switch event to MPF. This can be useful to filter out
unwanted or phantom switch events which might happen due to electrical
interference or other little weird things. Most switches in pinball
machines are debounced except for the ones that you absolutely want to
fire instantly, like flipper switches and the switches attached to
automatically fired coils like slingshots and pop bumpers.



MPF Events posted by Switches
-----------------------------
Event Type Description sw_ *tagname* Standard When a switch moves from
the "inactive" to "active" state, the Switch Controller will post one
event for each tag the switch is configured for. The event name starts
with "sw_" followed by the tag name.


Configuring your Switches
-------------------------

Switches are configured in the ` `switches:` section`_of the machine
configuration file.



Tutorial for step-by-step switch setup
--------------------------------------

The step-by-step tutorial covers switch setup in the following
sections: `Step 4. Get flipping!`_

.. _ section: https://missionpinball.com/docs/configuration-file-reference/switches/
.. _specify your switches in your machine configuration file: /docs/configuration-file-reference/switches/
.. _Step 4. Get flipping!: https://missionpinball.com/docs/tutorial/get-flipping/


