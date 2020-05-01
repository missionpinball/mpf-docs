Ending the Current Game by Long-pressing Start
----------------------------------------------

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/timed_switches`                                                |
+------------------------------------------------------------------------------+

The following snippet will end a running game by long-pressing the start
button:

.. code-block:: mpf-config

   timed_switches:
     game_cancel:
       switch_tags: start
       time: 5s
       events_when_active: end_game


Please note that this will also work on ball one and will not inhibit bonus
nor high_score mode.
Let us know in the forum if you need this.
