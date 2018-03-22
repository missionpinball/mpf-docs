Sequence Logic Blocks
=====================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/sequences`                                                     |
+------------------------------------------------------------------------------+

"Sequences" are a type of :doc:`Logic Block </game_logic/logic_blocks/index>`
where you can trigger a new event based on a series of one or more other events
that are first posted in a specific order.

Sequences are almost identical to :doc:`/game_logic/logic_blocks/accruals`, the
only difference being that the steps in
an Accrual Logic Block can be completed in any order, and the steps in
a Sequence Logic Block must be completed in the specific order they're
listed.

An example might be if you have to hit four shots in a specific order to complete
a mode, like this example from the World Tour mode of *Brooks 'n Dunn*:

.. code-block:: yaml

  sequences:
      finish_world_tour:
         events:
           - shot_north_america_hit
           - shot_south_america_hit
           - shot_europe_hit
           - shot_australia_hit
        events_when_complete: wt_done

The example above has a single sequence logic block called "finish_world_tour". When
it's enabled, it starts watching for the event *shot_north_america_hit* to be posted.
Once it's posted, then it starts watching for the event *shot_south_america_hit* to
be posted. At this point, if the europe or australia event is posted, it doesn't matter
because this is a "sequence" logic block and the events have to happen in order. So this
logic block will just sit there waiting for the current event only to be posted, and
then once it is, it moves on, and any posted before or after are just ignored.

Once all four events have been posted in order, the event *wt_done* is posted which you
can use to stop the mode or add a score or play a show or whatever you want.


