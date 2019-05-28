text_strings:
=============

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+

.. overview

The ``text_strings:`` section of your config is where you define text strings
which can be used in slides or widgets.

This is an example:

.. code-block:: mpf-config

   text_strings:
     greeting: HELLO PLAYER. THIS IS YOUR BALL (ball)

   slides:
     slides_with_text:
       - type: text
         text: $greeting
