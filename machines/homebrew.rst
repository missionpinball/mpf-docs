Controlling a custom "home brew" machine with MPF
=================================================

Details for how to build custom machine hardware are covered on the
`PinballMakers.com Wiki <http://pinballmakers.com>`_.
We cover some general areas here and suggest that you investigate those on
your own.
Contributions to the guide (and the rest of the documentation are
:doc:`welcome </about/contributing_to_mpf_docs>`).

Control System
--------------

If you are "just" retheaming a machine have a look at the
:doc:`existing` section.
If you want to use MPF to power a new *custom* pinball machine that you build
yourself, you should buy new custom driver boards.
There are a few common choices:

* :doc:`Multimorphic P3-Roc </hardware/multimorphic/index>`
* :doc:`FAST Pinball </hardware/fast/index>`
* :doc:`Open Pinball Project (OPP) </hardware/opp/index>`
* :doc:`LISY Home (custom pinball version of LISY) </hardware/lisy/index>`
* :doc:`Arduino Pinball Controller </hardware/apc/index>`

P3-Roc and FAST are both commercial systems at a similar price point but
features vary slightly so compare them wisely.
OPP is an open source/open hardware project and much cheaper but expect to
invest some more time into the hardware itself.

You might also want to some more control boards for servos, steppers and light.
Common choices are:

* :doc:`Fadecandy </hardware/fadecandy/index>` for WS2812 lights
  (FAST and P3-Roc offer this too)
* :doc:`Pololu Maestro </hardware/pololu_maestro/index>` for servos

See the :doc:`Hardware Section </hardware/index>` for all hardware supported by
MPF.


Power and Wiring
-----------------

You should invest some time into at the beginning of your custom pinball
journey into your power supply and wiring.

* :doc:`/hardware/voltages_and_power/voltages_and_power`
* :doc:`/hardware/voltages_and_power/wiring_and_connectors`

Parts and Assemblies
--------------------

MPF supports a :doc:`varity of pinball mechs </mechs/index>`.
You can have a look at manuals of existing machines to find numbers of mechs.
For homebrew machines it is wise to buy assemblies of mechs.
Mostly, because mechs consist of a lot of parts and you will likely fail
to order all of them at once.
Additionally, assemblies are often cheaper.

There are a few shops such as `Pinballlife <https://www.pinballlife.com/>`_
which offer assemblies.
They also have a homebrew section which is worth checking out.
Other shops such as
`Marcos Specialities <https://www.marcospecialties.com/>`_ offer more parts
but are less focused on homebrew.
