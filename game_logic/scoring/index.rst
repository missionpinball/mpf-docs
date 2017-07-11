Scoring
=======

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/scoring`                                                       |
+------------------------------------------------------------------------------+

Scoring is commonly used to score points for the current player when a certain event is posted.
This event could be a switch hit (i.e. for `s_your_switch` use the event `s_your_switch_active`).

.. code-block:: yaml

  scoring:
    s_your_switch_active:
      score: 100

Furthermore, you can add or set any other player or machine variable.
Placeholders are available as well.
See the :doc:`example config </examples/scoring/index.html>` for working examples.
