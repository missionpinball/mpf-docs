Dynamically Updating Text
=========================

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`text widgets </displays/widgets/text/index>`                           |
+------------------------------------------------------------------------------+
| :doc:`segment displays </segment_displays/index>`                            |
+------------------------------------------------------------------------------+

Your text can contain placeholders which will be replaced and updated when the text is shown.
Use `(param)` to replace the parameters of the event which triggers the text (usually you do not want to use this).
Player vars from the current player can be accessed using `(player|var)` (e.g. `(player|score)` or `(player|ball)`).
Furthermore, you can target a specific player using `(playerX|var)` where X is the player number starting at 1.
To display machine variables use `(machine|var)` (e.g. `(machine|credit_string)`).
