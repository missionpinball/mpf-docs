
MPF's virtual platform interface is a software-only platform you can
you if you don't have a physical pinball controller attached. Note
that MPF now includes an improved virtual platform interface called
the ` *smart virtual* platform`_ which is the new default for MPF and
most likely the platform you'll want to use for testing. The
traditional virtual platform interface described here still exists,
but it's mostly used now for testing MPF itself since the smart
virtual platform is much better for game testing. When you use the
virtual interface, you can "run" your game by using keyboard keys to
simulate switches, the OSC interface to send switches from a desktop
app or mobile device, or the switch player which lets you write
scripts that automatically send switch events based on a timer. (The
switch player is great for automated testing!) Note for P-ROC and
P3-ROC users: P-ROC's pyprocgame includes a virtual P-ROC interface
called *FakePinPROC*. We don't use that in the MPF because doing so
requires that pyprocgame is installed, and it's likely that people
using MPFwon't have pyprocgame. Using MPF's virtual hardware interface
is conceptually similar to *FakePinPROC*.

.. _ platform: https://missionpinball.com/docs/mpf-core-architecture/platform-interfaces/smart-virtual/


