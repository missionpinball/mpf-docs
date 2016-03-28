
If you haven't done so already,it's probably not a bad idea to readthe
`Overview`_ section of this documentation, including the parts about
`understanding the MPF download package`_and`the file & folder
structure`_. ` `_ Once you look at that, there are a few things you
need to know about MPF: The MPF software runs on a host computer
plugged into a pinball hardware controller . MPF iswritten in Python
2.7, so anythingthat can run Python 2.7 should be ableto run MPF.
(Windows and Linux are both fine today. Mac kind of works with some
caveats and should be fully fixed in the next release of MPF in early
2016.) MPF will not run on Python 3. The MPF software is self-
contained . MPF is literally just a folder full of Python code and
configuration files. Of course if you want to control a real pinball
machine, you'll need a`pinball hardware controller`_. Today we support
both the `Multimorphic P-ROC/P3-ROC`_and the `FAST Pinball`_
controllers, each of which has itsown drivers and Python interfaces.
The good news is you don't need to have a pinball hardware controller
to get started . We also include a `"virtual" (software only)
interface`_ which you can use to run MPF without any real hardware
attached. In fact you can (theoretically) build an entire game without
ever connecting it to a real machine. (Though that's not as fun.)

.. _Multimorphic P-ROC/P3-ROC: https://missionpinball.com/docs/mpf-core-architecture/platform-interfaces/p-roc/
.. _FAST Pinball: https://missionpinball.com/docs/mpf-core-architecture/platform-interfaces/fast-pinball/
.. _"virtual" (software only) interface: https://missionpinball.com/docs/mpf-core-architecture/platform-interfaces/virtual/
.. _understanding the MPF download package: https://missionpinball.com/docs/overview/understanding-the-mpf-package/
.. _pinball hardware controller: https://missionpinball.com/docs/overview/hardware-controllers/
.. _Overview: https://missionpinball.com/docs/overview/
.. _ folder structure: https://missionpinball.com/docs/overview/understanding-the-mpf-package/file-folder-structure/


