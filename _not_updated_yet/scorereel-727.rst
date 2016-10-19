
A *Score Reel* in the Mission Pinball Framework is an
electromechanical (EM) score reelunit from an EM pinball machine. This
device represents a single reel, and multiple Score Reels can be
groups together (into a `Score Reel Group`_) to make up a complete
grouping that might represent a player's score. The credit unit in an
EM machine is also a score reel device. Maybe we should take a step
back. Did you know you can use this framework to control EM pinball
machines? It's very cool, but also a lot of work because you have to
strip out the EM guts of the machine and completely rewire the machine
from scratch for your modern digital control environment. We did this
for a 1974 Gottlieb Big Shot machine, and we estimate the effort to be
about 100 hours. (`Details of thatproject arehere`_.) Individual score
reels have properties like the number of digits they have, the name of
the coil that advances them, positional switches that let the machine
know what position the reel is in, and (optionally) whether there is
also a coil to decrement the reel (like with a credit reel) and
whether or not the reel can "roll over." (So a typical reel in a score
unit can roll over from 9 to 0, while a credit reel cannot.) More
details about score reels are available in the `Score Reel section of
our machine configuration file reference`_.

.. _Score Reel Group: /docs/mechs/score-reel-group/
.. _here: /blog/category/big-shot-em-conversion/
.. _Score Reel section of our machine configuration file reference: /docs/configuration-file-reference/score-reels/


