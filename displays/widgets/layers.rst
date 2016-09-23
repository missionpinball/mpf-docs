Controlling overlapping widget drawining order
==============================================

If you have widgets that overlap each other, you can control the order of how they're stacked.

By default, the widgets are drawn on the screen to match the order they're in the list in a widget group, slide,
slide_player, or widget_player section of your config.

For example, this config...

::

   slides:
      my_slide:
         widgets:
            - type: text
              text: HELLO
              color: white
            - type: rectangle:
              width: 200
              height: 100
              color: blue

...will produce the following results:

.. image:: /displays/images/z_order_1.png

Notice that the text widget is drawn on top of the rectangle widget since the text widget is higher up in the config.

If you switch the order in the config, like this...

::

   slides:
      my_slide:
         widgets:
            - type: rectangle:
              width: 200
              height: 100
              color: blue
            - type: text
              text: HELLO
              color: white

...then you will get the following result:

.. image:: /displays/images/z_order_2.png

In this case, the text widget is still there, but you can't see it because the rectangle is opaque. (You can change the
opacity setting of the rectangle, perhaps to ``opacity: .5`` and then the text will show through. Also if you change
the position of either widget, whichever part of the text is not covered by the rectangle will show through.)

Setting the order manually
--------------------------

The drawing order of the widgets is called the "z" order. Widgets with a higher z value will be drawn on top of widgets
with a lower z value. For example, if you add ``z:`` settings to the last example above, you can get the text widget
to draw on top of the rectangle even though it's lower down in the list:

::

   slides:
      my_slide:
         widgets:
            - type: rectangle:
              width: 200
              height: 100
              color: blue
              z: 1
            - type: text
              text: HELLO
              color: white
              z: 2

The above config will again show this:

.. image:: /displays/images/z_order_1.png

If you don't specify a z: value, then ``0`` is used. So you could also achieve the same results from the example above
by just adding a z: value to the text widget.

Note that you can mix-and-match z: values and positional order of widgets. Any time there are two widgets with the same
z-value, whichever one is higher up in the list will be shown.

No more negative z-values
-------------------------

In versions of MPF prior to 0.31.3, you could use a negative z-value to configure a widget to be added to the parent
slide frame "above" the current slide. This functionality has been changed, and now you target a parent from with the
``target:`` setting in the widget player. More details are in the :doc:`parent_frames` guide.
