
MPF's hardware show controller is responsible for playing hardware
shows. It lives in the *mpf/system/hw_show_controller.py* module. A
hardware a scripted series of actions that happen at certain times.
These used to be called "light shows" though we changed the name to
"hardware shows" since they can also include LEDs, flashers, and
coil/driver actions. Shows can be played, paused, stopped, sped up, or
slowed down. Each show plays at a certain priority, and lights or LEDs
in higher priority shows will take precedence over those in lower
priority shows. The hardware show controller is responsible for
managing all of this.



