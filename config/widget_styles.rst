widget_styles:
==============

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+

.. overview

The ``widget_styles:`` section of your config is where you configure
styles for your widgets.

Default styles for widget types
-------------------------------

You can define defaults for certain :doc:`widget types </displays/widgets/index>`.
A widget will use the style ``(name)_default`` if no other style is specified.
For instance, a default style for all
:doc:`text widgets </displays/widgets/text/index>` would look like:

.. code-block:: mpf-config

   widget_styles:
     text_default:
       font_size: 21
       color: red

Specifying widget styles
------------------------

You can also specify a style for a certain widget.

.. code-block:: mpf-config

   widget_styles:
     big_style:
       font_size: 100

   slides:
     slide1:
       - type: text
         text: HELLO
         style: big_style
