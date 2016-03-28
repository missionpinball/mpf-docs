
The MPF media controllerincludes a keyboard interfacewhich allows you
to interact with your running machine via a computer keyboard. In most
cases you'd use this to simulate pinball switch events via keys on
your keyboard, but you can also post MPF events via keyboard presses.
You can map single key presses or combinations of keys, and you can
use the keyboard module with or without a physical pinball machine
connected to your computer. (You can also simulate switch eventsvia a
phone or tablet with our OSC interface.) To use the keyboard
interface, you add a `keyboard:` section to your machine configuration
file and then create a list which maps keyboard keys to pinball
machine switch names or MPF events. Then when you press a key on the
keyboard, the switch controller receives that event and sends it to
the game. The keyboard module tracks both key-down and key-up events,
so you can hold down a key to represent a ball sitting on a switch.
You can also set several options for each key, including:


+ Specify that a key is a "toggle" key, meaning the switch stays in
  the state even after you let go of the key. (In other words, tap the
  key once to activate the switch. Tap it again to deactivate it.) This
  is helpful for things like your trough or ball locks where you want to
  simulate a ball sitting on a switch but you don't want to play a crazy
  game of keyboard Twister where you're trying to hold down all these
  keys at once.
+ Specify that a key is inverted, so pressing (or holding) the
  keyboard key deactivates the switch, and releasing it activates the
  switch. (Note this is *not* needed to compensate for normally-closed
  switches, as the switch controller handles that automatically. This is
  just is you want to invert the computer's keyboard action.)
+ Specify combo keys, so you can set up one switch action for the
  `S`key, a different one for `CTRL+S`, another one for `SHIFT+S`, etc.


If you want to use the keyboard interface, details of the keyboard
mapping configuration can be found in the ` `keyboard:` section of
theconfiguration file reference`_.

.. _configuration file reference: /docs/configuration-file-reference/keyboard/


