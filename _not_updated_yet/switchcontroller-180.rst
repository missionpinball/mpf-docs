
The Mission Pinball Framework includes a core system component called
the *Switch Controller* which is responsible for receiving all
hardware switch state changesand translating them into MPF events
which are broadcast out to all the other game modules. In other words,
the switch controller is the only part of the game that actually
receives notification of the physical switches—it's the only thing
that "talks to" the switch hardware. Everything else in the game just
waits for the switch controller to tell them that a switch action
happened, rather than all different parts of the game all talking to
hardware. MPF's switch controller is based on the SwitchController
class located in the `/mpf/system/switch_controller.py`module. Why do
we force everything to talk to the switch controller instead of
letting individual modules talk to the switches directly? Lots
ofreasons:


+ The switch controller has the intelligence to know whether a switch
  is normally open (NO) or normally closed (NC), based on how each
  switch is configured in the machine configuration files. This means
  that all the game modules only have to listen for the ` *switch
  active*and *switch inactive*events`_, rather than each module
  needingthe intelligence to transpose the switch states as needed.
+ The switch controller can "hide" physical switch activities from the
  game. This is most useful for broken switches that are firing like
  crazy. If the switch controller notices that a switch is going nuts,
  it can suppress those events, slow them down, or just ignore them
  altogether. That way you can just write your game code to say
  something like "when this switch is active, assign these points" and
  you don't have to worry about a bad switch giving all your players
  high scores! (This functionality is not yet complete)
+ The switch controller can also reprogram the game logic around
  broken switches. So if it knows that a switch is broken, it can send
  the game switch events for the broken switch when some alternate
  switch is hit. This means that each of your game modules can
  automatically get the benefit of this intelligent switch substitution
  without you having to write anything special. (Again, how this
  substitution takes place and which switches can be substituted for
  others is all configurable in your config files.)
+ Since the switch controller is the only interface into the game for
  switches, it can "inject" switch events fromany source. For example,
  MPF includes functionality to simulate switch events with a computer
  keyboard (for testing and debugging), as well as switch events from a
  mobile phone or tablet (via theOSC plug-in). Wealso havea plug-in to
  read and playback switch events from log files fromgames that already
  ran, as well as the ability to write scripts that simulate games. All
  this is done by interfacing to the switch controller—your actual game
  code doesn't know (or care) where the original switch events came
  from.


.. _events: /docs/system-components/events/built-in-events/


