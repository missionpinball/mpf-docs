High Scores in EM Machines
==========================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/high_score`                                                    |
+------------------------------------------------------------------------------+
| :doc:`/config/player_vars`                                                   |
+------------------------------------------------------------------------------+

Electro Mechanical (EM) pinball machines usually do not have a display which
allows a player to enter initials.
To use the existing :doc:`high score mode <index>` we can preset player
initials using :doc:`/config/player_vars`.

.. code-block:: mpf-config

   player_vars:
     initials:
       value_type: str
       initial_value: AAA

After setting this in your machine config the high score mode will no longer
ask for initials.
The exact string (here ``AAA``) does not matter since you usually will not show
it anyway.
If you have another way to enter initials you can also use that and set the
initials to the ``initials`` player variable.
