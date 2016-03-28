
The Mission Pinball Framework includes an OSC pluginwhich allows you
to interface with a pinball machine via an OSC client running on a
phone or tablet. (If you've never heard of OSC, it stands for "Open
Sound Controller" and is a protocol that's similar to MIDI.) OSC
software clients for phones and tablets are typically used by DJs in
clubs to control musical devices, but as it happens the OSC protocol
is perfect for interfacing with a pinball machine too! (Frankly one of
the main reasons we chose OSC was because there are already a ton of
different OSC clients for iOS and Android, so if by building an OSC
interface to our framework we get don't have to write our own client
app.) You can see a `demo of the MPF OSC interface here`_. Controlling
a pinball machine via an OSC client is great for testing and debugging
purposes when you're not sitting next to your physical pinball
machine. You can literally "play" your game via your phone. (Though,
we have to admit, it's also fun to fire up your OSC client on your
phone when a friend of yours is playing your game and to mess with
them by hitting the flipper buttons via your phone without them
knowing about it. :) Personally we have been using an OSC client app
for iOS called "TouchOSC," but there are literally dozens of options
and you can use whatever you want. Currently our framework's OSC
interfacelets you control switches, lights, coils, and events from
your OSC client. You can also use the OSC client to view the current
status of lights and switches. Our OSC plugin allowsmultiple OSC
clients to connect at the same time, so you can connect an iPhone and
iPad at the same time and view/control lights on one and switches on
another. :)



Prerequisites
~~~~~~~~~~~~~


+ `PyOSC`_ (You should also be able to install this via `pip install
  pyosc` from the command prompt.)




Usingthis plugin
~~~~~~~~~~~~~~~~


#. Configure options for this plugin in the` `osc:`section`_of your
   Machine Configuration Files.


.. _section: /docs/configuration-file-reference/osc/
.. _PyOSC: https://pypi.python.org/pypi/pyOSC
.. _demo of the MPF OSC interface here: https://missionpinball.com/blog/2014/09/you-can-control-the-mission-pinball-framework-from-your-ipad-iphone/


