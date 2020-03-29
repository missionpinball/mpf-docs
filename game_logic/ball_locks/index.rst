Ball Locks
==========

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/multiball_locks`                                               |
+------------------------------------------------------------------------------+
| :doc:`/config/ball_holds`                                                    |
+------------------------------------------------------------------------------+

.. contents::
   :local:

MPF supports ball locks which are used to hold a ball that has
entered a :doc:`/mechs/ball_devices/index`.
To separate use-cases MPF supports two cases of ball locks:

* :doc:`Multiball_locks </game_logic/multiballs/multiball_locks>` which lock
  balls for a multiball. Locked balls are no longer in play (i.e. deducted
  from ball count).
* :doc:`Ball_holds </game_logic/ball_holds/index>` which only hold balls
  temporarily. This is used to play animations or stop the ball during a
  video mode. Those balls are technically still in play.

