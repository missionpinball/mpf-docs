Asset Pools
===========

Asset pools are groups of assets that are pooled together to create a single asset. They're used when you want some
variation or randomizing in your game.

For example, you might have a laser sound effect that plays when a slingshot is hit. But since the slingshots are hit
often, that single laser sound could get boring. So instead, you can create several variations of the laser sound which
you can then group into an asset pool which looks to MPF like a regular sound file. Then you tie that asset pool to your
slingshot, and each time the slingshot is hit, you get a different sound.

Asset pools are available for all types of assets. Also there are options to control how the individual asset is
selected (random, weighted random, round-robin, etc.).