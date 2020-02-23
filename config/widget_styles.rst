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

.. code-block:: mpf-mc-config

   widget_styles:
     text_default:
       font_size: 21
       color: red

Specifying widget styles
------------------------

You can also specify re-usable styles and apply them to widgets. In the following
example, the text "HELLO" will render at font size 100:

.. code-block:: mpf-mc-config

   widget_styles:
     big_style:
       font_size: 100
   slides:
     slide1:
       - type: text
         text: HELLO
         style: big_style

You can supply multiple styles to a single widget, and they will be applied in
the order given.

.. code-block:: mpf-mc-config

  widget_styles:
    warning_text:
      font_size: 12
      color: yellow
    bottom_left:
      anchor_x: left
      anchor_y: bottom
      x: 5
      y: 5
    hurryup:
      color: red
  widgets:
    timer_runout:
      - type: text
        text: Hurry!
        style: warning_text, bottom_left, hurryup

In the above example, the text "Hurry!" will be anchored in the lower-left of
the display and rendered at size 12 and color red. Notice that the color from
the *hurryup* style overwrites the color from *warning_text* style, because of
the order the styles are listed in the widget.

