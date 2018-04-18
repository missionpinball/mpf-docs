Stationary Targets
==================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/switches`                                                      |
+------------------------------------------------------------------------------+


Mission Pinball Framework's (MPF) *stationary target* device represents a switch in a pinball machine. This might also
be know as a stand-up target. It is essentially a switch above the playfield with a scoring value
associated with it. When the ball hits it the value is scored.

.. code-block:: mpf-config

   switches:
      s_target:
         number: 5
         debounce: quick
         ignore_window_ms: 1000ms

Most platforms support debouncing of switches for a few ms.
Usually, you have to reduce debouncing to 1-2ms because a strong hit to a
target might be very short (see ``debounce`` in :doc:`/config/switches`).
However, targets sometimes start to swing after a hit and would cause multiple hits.
To prevent that you can set ``ignore_window_ms`` to prevent multiple hits
within that window.
