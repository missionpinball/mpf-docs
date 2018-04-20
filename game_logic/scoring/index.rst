Scoring
=======

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/variable_player`                                               |
+------------------------------------------------------------------------------+

The variable_player is commonly used to score points for the current player when a certain event is posted.
This event could be a switch hit (i.e. for `s_your_switch` use the event `s_your_switch_active`).

.. code-block:: mpf-config

  ##! config: mode1
  variable_player:
    s_your_switch_active:
      score: 100

Furthermore, you can add or set any other player or machine variable.
Placeholders are available as well.
