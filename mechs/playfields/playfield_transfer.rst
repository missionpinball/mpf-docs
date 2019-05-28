Playfield transfer
==================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/playfields`                                                    |
+------------------------------------------------------------------------------+
| :doc:`/config/playfield_transfers`                                           |
+------------------------------------------------------------------------------+

*MPF Device*

If you want to track balls across multiple playfields you can use a
:doc:`playfield_transfer </config/playfield_transfers>` device to move a ball
from one playfield to another.
This is mostly useful in head2head games.
However, you can also use it to track balls on a mini-playfield.
In some cases you can also use a :doc:`ball_device </config/ball_devices>`
which captures from one playfield and ejects to another playfield to achieve
the same result.


Related Events
--------------

.. include:: /events/include_playfield_transfers.rst
