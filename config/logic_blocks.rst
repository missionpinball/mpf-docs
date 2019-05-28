logic_blocks:
=============

Logic blocks moved one level up in MPF 0.50. Instead of

.. code-block:: yaml

    logic_blocks:
      counters:
        your_counter:
          count_events: count_it_up

just use:

.. code-block:: mpf-config

    counters:
      your_counter:
        count_events: count_it_up


There are three type of logic blocks:

* :doc:`accruals: </game_logic/logic_blocks/accruals>`
* :doc:`counters: </game_logic/logic_blocks/counters>`
* :doc:`sequences: </game_logic/logic_blocks/sequences>`

Click each of the links above for details and settings for each type of logic block.
