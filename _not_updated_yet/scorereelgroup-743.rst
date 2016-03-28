
A *Score Reel Group* is a logical grouping of multiple `Score Reel
devices`_ that are used grouped together to show a multi-digit value
in an EM pinball machine. For example, there might be a Score Reel
Group called "Player1" that's a grouping of 4 Score Reel devices, one
each for the thousands, hundreds, tens, and ones digits. Score Reel
Groups have properties including which Score Reels are in which
positions in the score (thousands, hundreds, etc.), whether there are
any fake "blank" positions (like the plastic "0" inserts some machines
use to make the scores seem bigger), and howmany individual reels in
the group may be firing simultaneously. Score Reel Groups have methods
that let you do things like add to the score, and reset the reels. The
Score Reel Group functionality in the Mission Pinball Framework is
somewhat advanced. Check out `this blog post that we wrote`_ for more
information. Details for configuring Score Reel Groups can be found in
the `Score Reel Groups section of the machine configuration file
reference`_.

.. _Score Reel Groups section of the machine configuration file reference: /docs/configuration-file-reference/score-reel-groups/
.. _Score Reel devices: https://missionpinball.com/docs/devices/score-reel/
.. _this blog post that we wrote: /blog/2014/08/em-style-score-reels/


